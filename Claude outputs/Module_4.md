# Tasks - Module 4

*From Idea to Screen — mirrors the Task Tracker in narrative Question/Solution form, same as the Module 1, 2, and 3 docs.*

---

## Task 4.1 — Learn: Wireframing fundamentals

### Task 4.1 — Step 1
**Question:** Read the IxDF wireframing guide and the NN/g wireframing article.

**Solution:** Completed — read IxDF's *What is Wireframing — The Complete Guide* and NN/g's *Wireframing*.

### Task 4.1 — Step 2
**Question:** Write down what a wireframe should contain (structure, hierarchy, content priority, key interactions) and what it must not (final colour, real imagery, polished type).

**Solution:** First attempt restated the given must-include/must-not-include labels rather than defining them — corrected after realizing the exercise asked for working definitions of each term, not a repeat of the vocabulary already provided. Final seven working definitions covered what each term means in practice — for example, *structure* as the answer to "what sections exist and in what order," not just "the sections on a screen" — and named final colour, real imagery, and polished type as the three things a wireframe must deliberately withhold so a review stays about structure rather than aesthetics.

### Task 4.1 — Step 3
**Question:** Take three screens from your reference library and wireframe them backwards — reduce each finished screen to its wireframe.

**Solution:** Completed with three real screens: Zomato's home screen, an Alarm app screen, and Splitwise's Activity page. Each was reduced to its structural skeleton — sections, hierarchy, and key interactions only, with colour and imagery stripped out.

### Task 4.1 — Step 4
**Question:** Have Claude critique: *"Here's my description of a wireframe reduced from a finished screen. Did I keep anything that's a visual decision rather than a structural one?"*

**Solution:** Completed — submitted all three reduced wireframes for critique. Noted explicitly that none of the three carried colour forward ("there is no colour in these"), confirming the reduction held to the structural-only rule from Step 2.

### Task 4.1 — Step 5
**Question:** Add your three reduced wireframes to your board, next to the finished screens they came from.

**Solution:** Completed — all three reduced wireframes (Zomato, Alarm app, Splitwise) added to the board alongside their source screens.

---

## Task 4.2 — Practise: Sketching by hand

### Task 4.2 — Step 1
**Question:** Read the paper prototyping article and print a few browser-frame templates.

**Solution:** Completed — read NN/g's *Paper Prototyping* article and located printable browser-frame templates (sneakpeekit.com).

### Task 4.2 — Step 2
**Question:** Set a timer for eight minutes and sketch eight different layouts for one screen: a claims list with filters and a detail panel.

**Solution:** Initially **Blocked** — no physical drawing pad or paper set up for hand-sketching. Marked Blocked rather than skipped or faked digitally, since the exercise's value is specifically in paper's speed and disposability, which a mouse-drawn substitute wouldn't test. Unblocked once a way to sketch by hand was available; ran the timed eight-minute/eight-sketch round for the claims-list screen.

### Task 4.2 — Step 3
**Question:** Do it again for a different screen — a settings page.

**Solution:** Completed — same eight-minute/eight-sketch exercise, this time for a generic settings page.

### Task 4.2 — Step 4
**Question:** Pick your best from each set and redraw it larger with annotations.

**Solution:** Picked one favorite from each set of eight and redrew both larger with annotated reasoning:

**Claims screen** — filter rail kept narrow and stacked rather than wide, since filters are a supporting tool, not the main content, for someone who spends most of their time scanning the list and reading detail. The selected row is marked with a left border plus shaded background rather than colour alone, so it survives quick or greyscale scanning. Rows are kept to two fields (claim ID, status) with everything else one click away in the detail panel, which goes full-width below the list rather than beside it — the deliberate trade-off being that detail content (multiple fields, tabs) needs the width more than a side-by-side layout would allow.

**Settings screen** — section labels sit above their group in lighter, smaller text with no border, since they're dividers, not settings themselves. Navigational rows end in a chevron and toggle rows end in a switch, so the row signals what tapping it does before it's tapped. This variant needs no navigation model at all (no tabs, no sidebar), which is both the simplest structure for a modest option count and the most familiar pattern (mirrors mobile OS settings). Log out is placed last, separated from routine settings, since it's a destructive one-way action and shouldn't be reachable by accident while scanning.

Two threads from these annotations were left open rather than resolved on the spot: what the claims screen's detail panel shows before any row is selected, and whether "Support" (where Log out was hedgingly placed) is a real third settings section or Log out is really sitting alone with no group around it.

### Task 4.2 — Step 5
**Question:** Photograph everything into your `02-Module-Work` folder.

**Solution:** Completed — all sixteen quick sketches plus the two annotated redraws photographed and saved into `02-Module-Work`.

---

## Task 4.3 — Learn: Information architecture and user flows

### Task 4.3 — Step 1
**Question:** Read all three (NN/g *Information Architecture*, NN/g *Card Sorting*, IxDF *User Flows*).

**Solution:** Completed — read all three resources.

### Task 4.3 — Step 2
**Question:** For Brief B (Harvest Hub, Appendix A), list every piece of content and function the product needs — aim for at least thirty items.

**Solution:** Built a 42-item content/function inventory covering orders (incoming queue, manual entry, order detail, assign-to-driver, stock check), inventory (stock levels, update on receipt/dispatch, item history), deliveries (driver workload by route/city, late tracking), and the owner's business-summary view. Removed item #42 after review flagged it as not conforming to the content/function format, finishing at 41 items.

### Task 4.3 — Step 3
**Question:** Group them into a navigation structure and draw the sitemap.

**Solution:** Grouped the inventory by role — Ops, Warehouse, Owner — rather than by feature area, each branching from a shared Login node. Revised across three rounds based on critique:

- **Round 1 → 2:** added a missing order-creation entry point under Ops (New order/manual entry), added a Driver workload node (full load by route/city) since it wasn't otherwise reachable, and added an explicit annotation that drivers deliberately have no login — "off-system by decision, not by omission" — after the first round left that ambiguous.
- **Round 2 → 3:** removed a separate "Inventory (read-only)" node that had been sitting under the Ops branch, once it became clear that stock-checking was already covered as a function inside Order Detail — a cleaner fix than relocating the node, which is what had been suggested.

**Final structure:** Login → {Ops team home, Warehouse home, Owner home}. Ops team home → Orders and deliveries (late count always visible) → {New order/manual entry, Order detail (includes stock check), Driver workload}. Warehouse home → Inventory (primary) → Stock item detail (history as a tab) → Orders (read-only). Owner home → Business summary (orders, late-rate, trend) → optional drill-down links. Persistent header on every role: notifications icon, account/settings menu.

### Task 4.3 — Step 4
**Question:** Draw the user flow for the single most important task, including every decision point and error path.

**Solution:** Chose the order-to-delivery flow, given the brief's own emphasis that a late order is "often worthless" and "the thing that costs us the most." Drew four sequential decision points — stock availability, driver availability, order-edited-after-dispatch, and delivered-on-time — with the happy path running New order received → Reserve stock → Order dispatched → In transit → Mark delivered, and "Flag on owner dashboard" wired specifically off a late delivery, tying the flow's output back to what the owner needs to see.

Revised once after critique flagged two dead-end error paths (a stock-out and a no-driver case that simply stopped, with no stated outcome) and an unresolved loop (what happens if re-verification fails after an order is edited post-dispatch). The revision replaced both dead ends with concrete branches — Cancel or Hold (timer) for a stock-out; Reassign or Hold (timer) for no driver — and added an explicit "Re-verify result?" decision after the edited-after-dispatch loop, resolving to Continue or Recheck rather than assuming re-verification always succeeds.

### Task 4.3 — Step 5
**Question:** Ask Claude: *"Here's my sitemap and main user flow for a produce distributor's admin dashboard. What's missing, and where have I organised things by internal logic instead of user logic?"*

**Solution:** Completed — asked the literal prompt against the final sitemap and flow. Claude's answer:

- **Missing:** the flow starts at "New order received" as if it appears on its own, with no step showing an ops person actually transcribing a WhatsApp order into the system — arguably the highest-risk moment in the whole process. The owner's "Business summary" screen has nothing in the flow feeding it (what exactly rolls up into "how the business is doing" is still undefined). The warehouse manager's inventory-update action — the thing that actually determines whether "Stock available?" says yes — isn't shown as an event anywhere in the flow, only as a value that gets checked.
- **Internal logic vs. user logic:** the "reassign or wait" decision assumes the ops person can judge driver load in the moment, but the Driver workload screen is a separate destination a click away in the sitemap rather than surfaced at the point of decision — organizing screens as separate concerns (system logic) over what the person actually needs visible right then (user logic). Similarly, auto-logging a late reason the moment a delivery misses its window is clean to compute but may deny the ops person a chance to confirm or edit the reason before it's recorded.

---

## Task 4.4 — Learn: Dashboards and internal tools

### Task 4.4 — Step 1
**Question:** Watch the guide and read the NN/g article.

**Solution:** Completed — watched the dashboard-design video guide and read NN/g's *Dashboard Design* article.

### Task 4.4 — Step 2
**Question:** Write down the anatomy of a dashboard: navigation, filters, KPIs, primary data view, detail panel, actions.

**Solution (after two rounds of revision):**

- **Navigation** — switches between different sets of information; the screen itself changes.
- **Filters** — narrows to a subset of the current data; the screen stays the same, which is the explicit distinction drawn from Navigation.
- **KPIs** — Key Performance Indicators, the progress metrics tied to business goals. The first draft reached for generic consumer-app examples (user retention, MAU, AOV); revised to Harvest-Hub-appropriate ones instead — late order rate, low-stock items, unassigned orders — since an internal ops tool is measured on operational health, not growth metrics.
- **Primary data view** — the main chart or table the dashboard exists to show.
- **Detail panel** — revised from "more information about a feature" to more information about a *selected record* in the primary data view, since a detail panel is triggered by picking an item, not a dashboard feature.
- **Actions** — let the user change something from the dashboard, covering both data-mutating actions (update) and non-mutating ones (export).

### Task 4.4 — Step 3
**Question:** List the specific problems dense interfaces face — scanning, data density, filter state, bulk actions, pagination versus infinite scroll, keyboard use.

**Solution:**

- **Scanning** — a dense screen forces the eye to read every row when nothing carries deliberate visual weight; without hierarchy, a user can't skip what's irrelevant, which defeats the point of showing a lot at once.
- **Data density** — more fields packed in makes it harder to tell which few actually drive a decision; the failure mode is treating "the data has this field" as "the user needs to see it always," rather than allowing show/hide or reprioritization per task.
- **Filter state** — as active filters accumulate, a user can lose track of what's narrowing the view, leading either to an unexplained empty/odd result set, or to misreading a partial view as the complete picture. Active filters need to be visible and removable at a glance.
- **Bulk actions** — dense tables exist so someone can act on many rows at once, which risks selecting more or fewer rows than intended — including the sharp distinction between "all visible" and "all matching this filter." Needs clear selection state and a confirmation step scaled to the size of the action.
- **Pagination vs. infinite scroll** — pagination gives a sense of total scope and a stable position to return to at the cost of a per-page click; infinite scroll removes that friction but costs the sense of total size, a bookmarkable position, and often a real footer/summary.
- **Keyboard use** — dense interfaces are exactly where keyboard navigation matters most for repetitive, many-row tasks, yet it's where it's most often neglected; unpredictable tab order and invisible focus states force keyboard-benefiting users back onto a mouse.

**Harvest Hub connection:** the brief states the ops team is "much faster on the spreadsheet than they'd be on a new system" — and what spreadsheets are fast at is exactly keyboard-driven range selection for bulk operations. If Harvest Hub's order table only supports bulk-selecting rows by mouse click, it isn't just a weaker keyboard experience — it's slower than the spreadsheet it's meant to replace, for the specific people the brief already warns are reluctant to give it up. Keyboard use and bulk actions are the same problem from two angles here, not two independent items.

### Task 4.4 — Step 4
**Question:** For each problem, find a solution in your reference library and note it.

**Solution:** Built `Dense-Interface-Analysis.docx` (saved to `05-Reference-Library`), cross-checking all six problems against five real reference screens (Splitwise Activity, Amazon Alexa's More menu, the default Calculator, Google Classroom's home dashboard, Rapido's rating screen) — noting honestly where a problem didn't apply to a screen rather than inventing a solution for it. Concrete solutions found: colour/weight-coding Splitwise rows by amount so high-stakes entries stand out; a "Settle selected" bulk action with a selected-count indicator; a "Today / Earlier" divider in place of full pagination for the infinite-scroll activity feed; collapsing the Calculator's history by default to free up primary-task space; a "Clear history" control kept separate from AC to avoid confusing the two.

**Gap surfaced:** every one of the five reference screens is a touch-only mobile app, so **Keyboard use scored "No" on all five** — not because it doesn't matter, but because nothing in the existing reference library could show a real example solution for it. This is the one problem with zero example behind it, and — per the Harvest Hub connection above — the one most likely to matter for the actual product, since ops runs it on laptops, not phones. Flagged as worth adding a desktop, keyboard-driven reference screen (even something as ordinary as Gmail or Google Sheets) rather than leaving it a diagnosed-but-unsolved gap.

### Task 4.4 — Step 5
**Question:** Ask Claude: *"What do teams coming from consumer apps consistently get wrong when they first specify enterprise dashboards?"* Compare against your list.

**Solution:** Claude's answer named five patterns: under-specifying bulk actions/multi-select (consumer apps rarely need to act on many records at once); carrying over infinite-scroll/feed patterns without registering the cost of losing "how many total" and "where was I"; neglecting keyboard and hardware-input paths entirely, coming from mobile-first design habits; not designing for persistent, visible filter state, since consumer flows are usually short and linear; and treating "clean/simple" as the goal itself, when a dense interface's actual goal is "fast to parse" — two things that can directly conflict.

Compared against the Step 3 list: the first four map cleanly onto bulk actions, pagination-vs-infinite-scroll, keyboard use, and filter state respectively. The fifth — "clean mistaken for the goal" — doesn't map onto any existing item. Scanning and data-density problems (as actually diagnosed across the five reference screens in Step 4) only ever ran in the direction of *too much* stimulus; this fifth point runs the opposite direction — a consumer-style minimalist redesign actively stripping out metadata or status a power user needs. Verdict: a real gap, not a relabeling — and arguably not a coequal seventh item either, since it's the design instinct that produces the wrong version of scanning and data density in the first place, sitting upstream of both rather than beside them. Kept as a flat sixth-plus-one note rather than restructuring the list, per instruction not to add an extra item.

---
