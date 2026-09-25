"""
Decode a "Bundled Page" export from Claude Design back into readable source.

When you export an artboard from Claude Design, the downloaded HTML is a
self-contained runtime "bundle": all fonts/images inlined as base64, plus a
loader script that unpacks everything at page-load time. The actual .dc.html
source you authored is buried inside that bundle as a single JSON-escaped
string (the runtime needs the original markup text to render it) — which is
why the file is huge (often ~1MB, mostly font data) and unreadable as-is.

This script finds that embedded string, decodes it back into plain HTML, and
writes it out as a separate file you can actually read.

Usage:
    python3 decode_claude_design_export.py "Settings Screen.html"

Writes: "Settings Screen.decoded.html" next to the input file.
"""

import sys
import json
import html
from pathlib import Path


def decode_bundle(input_path: str) -> str:
    content = Path(input_path).read_text(encoding="utf-8")

    # The embedded source is a JSON string literal starting with the doctype
    # (escaped as / for slashes, \n for newlines, \" for quotes) and
    # ending at the matching </html> (also escaped: </html>).
    start_marker = '<!DOCTYPE html>\\n<html>'
    end_marker = '<\\u002Fhtml>'

    start = content.find(start_marker)
    if start == -1:
        raise ValueError(
            "Couldn't find the embedded source marker. This may not be a "
            "Claude Design 'Bundled Page' export, or the format has changed."
        )
    end = content.find(end_marker, start)
    if end == -1:
        raise ValueError("Found the start of the embedded source but not its end.")
    end += len(end_marker)

    raw = content[start:end]

    # It's JSON-escaped (backslash escapes), so wrapping it in quotes and
    # running it through json.loads is the correct way to unescape it —
    # far safer than hand-rolling replace() calls, which breaks on edge
    # cases like literal backslashes inside the source.
    decoded = json.loads('"' + raw + '"')

    # On top of the JSON escaping, HTML entities (&quot; etc.) are also
    # present from an extra layer of attribute-encoding — unescape those too.
    decoded = html.unescape(decoded)

    return decoded


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 decode_claude_design_export.py <exported_file.html>")
        sys.exit(1)

    input_path = sys.argv[1]
    decoded = decode_bundle(input_path)

    out_path = Path(input_path).with_suffix("")
    out_path = out_path.with_name(out_path.name + ".decoded.html")
    out_path.write_text(decoded, encoding="utf-8")

    print(f"Decoded source written to: {out_path}")
    print(f"({len(decoded):,} characters, {decoded.count(chr(10)) + 1:,} lines)")


if __name__ == "__main__":
    main()
