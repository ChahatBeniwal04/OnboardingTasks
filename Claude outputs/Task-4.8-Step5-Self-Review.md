# Task 4.8, Step 5 — Self-review against the Task 3.1 checks
*"Self-review against your five checks from Task 3.1 — hierarchy, spacing, alignment, contrast, and whether the primary action is obvious — then fix everything you flagged."*

Reviewed against the Order Management Screen wireframe (Order Queue table, filters, detail panel with Stock Check + Assign Driver, and the Resolve Stock Shortfall modal).

## Spacing — pass
Row heights and column gutters are consistent across the whole table; the filter pills and the two detail sub-panels sit on a visibly even grid. No fix needed.

## Alignment — pass
Columns line up cleanly top to bottom, and both halves of the detail panel (Order Summary/Stock Check on the left, Assign Driver/Timeline on the right) align to the same baseline as the table above them. No fix needed.

## Contrast — pass
Late orders get two independent signals, not color alone: a colored left-edge border on the row *and* a bordered "LATE" tag with its own label text. That's the same lesson from your Task 4.2 sketch annotation (never rely on color alone) carried through correctly here.

## Hierarchy — flagged, fix below
**Problem:** the **Resolve shortfall** button inside the Stock Check panel is rendered in the heaviest, largest button text on the entire screen — heavier than **+ New Order**, which is the page's actual top-level primary action (creating a new order is the thing this whole screen exists to let ops do quickly). Right now the screen has two buttons visually competing to be "the" primary action, and the more important one (+ New Order) loses.
**Fix:** drop Resolve shortfall to the same button weight as Assign to [Driver] and the other row/panel actions. Keep it visually flagged as urgent through the red border it already has (tied to the stock problem it's resolving) — urgency and page-level primacy are two different signals and shouldn't be expressed with the same visual weight.

## Primary action — flagged, fix below
**Problem:** every row in the table has exactly one row action except #10230 (Greenleaf Grocers), which has two — an **Assign** button *and* a kebab (⋮) menu. That breaks the "one obvious primary action per row" pattern every other row follows, and it's not clear what's behind the kebab or why this row alone needs it.
**Fix:** either fold whatever's in the kebab menu into Assign's own dropdown/flow so the row keeps one action like its neighbors, or — if there's a genuine second action every row secretly needs (e.g. "view full order," "cancel") — add the kebab consistently to all four rows instead of singling one out.

**Problem (label, not a button, but the same "what's the one clear thing here" issue):** the Assign Driver panel's header reads "ASSIGN DRIVER — WORKLOAD VISIBLE HERE." Its sibling labels are plain: "ORDER SUMMARY — #10230" pairs a label with real order data, and "STOCK CHECK" is just a label — both are copy a user would actually read. "WORKLOAD VISIBLE HERE" isn't order data or a real instruction; it reads like a note left for the designer (i.e., for me, reviewing this) rather than copy for the ops person using the screen.
**Fix:** rename the panel header to just "Assign Driver" and let the workload numbers next to each driver's name (which are already on screen and already doing the job) speak for themselves — the panel doesn't need to announce its own feature.

## Summary
Three real flags, all specific and fixable: a hierarchy inversion (Resolve shortfall out-weighing +New Order), an inconsistent row action (the lone kebab menu on #10230), and one line of leftover design-annotation copy in the Assign Driver header. Spacing, alignment, and contrast all hold up as built.
