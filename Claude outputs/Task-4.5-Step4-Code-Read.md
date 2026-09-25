# Task 4.5, Step 4 — Reading the Settings prototype's code
*"Open any Claude Design prototype's code and read it. Identify the structure, the tokens, and where the states are handled."*

Source: `Settings Screen.html`, exported from Claude Design (project `3e9a349b-165f-4df0-9ab6-446c1617388c`). The download is a self-contained runtime "bundle" — all fonts/images inlined as base64, plus a loader script — not the raw authored source. The actual `.dc.html` markup is embedded inside it as a JSON-escaped string; decoded with `decode_claude_design_export.py` to get readable source.

## Structure

One HTML file, no separate CSS/JS files. Layout, top to bottom: header ("Settings"), Account group (Profile, Password), a divider, Preferences group (Notifications, Dark mode toggles), a divider, Support group (Help center), a 56px gap, then the Log-out block. Every group is a plain flex-column `<div>` — no layout classes, everything is inline `style="display:flex; ..."`.

## Tokens

Partial adoption of a real design system. The log-out icon is a mounted component — `<x-import component-from-global-scope="OstrichAIDesignSystem_6d2749.Icon" name="log-out" ...>` — a real system component, not hand-drawn markup. Everything else on the screen (row gradients, `#E5484D` red, the `#0090FF`/`#46A758` toggle colors) is literal hex values inline, not referencing that system's own CSS variables. So the screen is "themed" in exactly one place and hardcoded everywhere else — a concrete example of partial, not full, design-system usage.

## State handling

`class Component extends DCLogic` in the script tag. The constructor seeds three state fields from props: `notifications`, `darkMode`, `confirming` (all default false). `renderVals()` derives what's shown from that state — track color per toggle (`#46A758` when on, `#0090FF` when off) and knob position — and returns the click handlers: `toggleNotifications`/`toggleDarkMode` flip their booleans, `requestLogout` sets `confirming: true` (gated by a `confirmBeforeLogout` prop, default true), `cancelLogout` resets it to false.

## The bug found by reading the code

The confirmation panel that appears when `confirming` is true has two buttons: Cancel and a red "Log out". Both call `cancelLogout`. The actual confirm action never fires — clicking either button just closes the dialog. This isn't visible from looking at the rendered screen or clicking around casually; it only shows up by reading `renderVals()` and matching each button's `sc-camel-on-click` binding against the handler it points to.
