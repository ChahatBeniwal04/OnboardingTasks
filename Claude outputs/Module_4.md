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

## Task 4.5 — Learn: Reading the front end

### Task 4.5 — Step 1
**Question:** Work through the W3Schools HTML tutorial as far as forms. Aim to recognise elements, not to memorise them.

**Solution:** Completed.

### Task 4.5 — Step 2
**Question:** Skim the CSS tutorial through the box model, then play Flexbox Froggy — it takes half an hour and makes layout conversations make sense.

**Solution:** Completed.

### Task 4.5 — Step 3
**Question:** Learn what semantic HTML means and why a `<button>` is not a styled `<div>`. This one has real accessibility consequences you'll be asked about.

**Solution:** Completed.

### Task 4.5 — Step 4
**Question:** Open any Claude Design prototype's code and read it. Identify the structure, the tokens, and where the states are handled.

**Solution:** Read the real source of the Task 4.6 Settings prototype (`Settings.dc.html`, exported from Claude Design). The first export downloaded was a "Bundled Page" — a self-contained runtime with fonts inlined as base64, not raw source — so the actual markup had to be extracted from a JSON-escaped string embedded in the bundle (a reusable decode script was written for this). A later, direct export (`Settings.dc.html` + `CHANGELOG.md` from the project's own export folder) confirmed the decoded content was accurate.

**Structure:** one self-contained HTML file, no separate CSS/JS. Header, Account group (Profile, Password), a divider, Preferences group (two toggles), a divider, Support group (Help center), a 56px gap, then the Log-out block. Every group is a plain flex-column `<div>` with inline styles — no layout classes.

**Tokens:** partial design-system adoption. The log-out icon is a real mounted component (`<x-import component-from-global-scope="OstrichAIDesignSystem_6d2749.Icon" ...>`), but every color, gradient, and radius elsewhere on the screen is a literal hardcoded hex value, not a system token reference.

**States:** `class Component extends DCLogic`. Constructor seeds `notifications`, `darkMode`, `confirming` from props. `renderVals()` derives toggle track color/knob position from state and returns the click handlers (`toggleNotifications`, `toggleDarkMode`, `requestLogout`, `cancelLogout`).

**Bug found by reading the code:** the Log-out confirmation panel's two buttons — Cancel and the red "Log out" — both call `cancelLogout`. The actual confirm action never fires; there's no sign-out logic implemented anywhere. Not visible from the rendered screen — only found by matching each button's `onClick` binding against the handler it points to.

### Task 4.5 — Step 5
**Question:** Ask Claude: *"Explain which CSS and layout changes are cheap for a developer and which imply restructuring — I want to know which of my requests are expensive before I make them."* Write down the five that surprised you.

**Solution:** Asked the literal question, answered with reference to the real `Settings.dc.html` source rather than generic examples.

**Cheap:** toggle track colors (one-line hex swap); section label styling (size/tracking/case); divider color/spacing; row background gradient or shadow (cheap per instance, but duplicated identically across five rows with nothing shared — cheap in isolation, tedious in practice); the hand-drawn CSS-triangle chevron.

**Expensive:** the confirm-panel bug itself — looks like a one-word fix (swap `cancelLogout` for a real handler on the second button) but the actual sign-out logic doesn't exist anywhere yet, so the "cheap-looking" fix has no real implementation behind it; turning the inline confirm panel into a real modal/dialog; the hand-built toggle switch vs. the mounted design-system icon — reverting the toggle to a real system component is an architecture decision (does the system's Switch even support per-state color control?), not a style tweak; collapsing the five duplicated row-style blocks into one shared token; adding any new screen state (loading, error) that doesn't exist yet, since each needs a new `state` field and a new `sc-if` branch.

**The five that surprised me:**

1. The row background gradient/shadow — cheap per instance, but five near-identical copies of that exact style block exist with nothing shared between them. Technically simple, still tedious in practice: a real example of "cheap" not meaning "fast."
2. The confirm-panel bug — both buttons call `cancelLogout`. Looks like a one-word fix, but the real "Log out" button has nothing to call; there's no sign-out logic anywhere in `renderVals()`. Writing the actual destructive action is new logic, not a template edit — the fix that's visible in one line isn't the fix that actually exists.
3. Turning the confirm panel into a real modal/dialog instead of an inline `sc-if` block — new state shape, probably a portal, possibly a design-system dialog component. Not CSS.
4. The hand-built toggle switch vs. the mounted design-system icon — the round log shows the system's own Switch component got swapped out for a hand-built one specifically so both on/off colors could be controlled. Reverting to the real component means checking whether it even supports that, and possibly losing the custom behavior. An architecture decision, not a style tweak.
5. Collapsing the five duplicated row-style blocks into one shared style/token — makes future color changes cheap, but doing it is real refactoring now.

---

## Task 4.6 — Build: Your first Claude Design prototype

### Task 4.6 — Step 1
**Question:** Read the getting-started guide fully.

**Solution:** Completed.

### Task 4.6 — Step 2
**Question:** Build the settings page you sketched in Task 4.2, starting from a detailed prompt that specifies structure, hierarchy and what matters most on the screen.

**Solution:** Before writing the prompt, checked the Task 4.2 settings-page wireframe against the Task 4.2 journal entry and found a gap: the annotation said Log out should be "separated from routine settings so it can't be tapped by accident," but the wireframe itself placed Log out as the third row inside Support, same box style and chevron as Help center — not actually isolated, and left as one of the two open questions from that entry's own annotations. Decided (with a check back before building) to resolve it in the prompt rather than reproduce the ambiguity: the prompt specifies Log out as its own section below Support, with extra spacing, no chevron, and a distinct warning treatment, framed explicitly as "different in kind, not just position."

Built the first prototype from that prompt via Claude Design.

### Task 4.6 — Step 3
**Question:** Refine it through at least eight rounds — some via chat, some via inline comments on the canvas.

**Solution:** Ten rounds run directly in Claude Design (inline canvas comments), logged in the project's own `CHANGELOG.md`. Summary: rounds 2, 4, 6 were net improvements (fixed broken icon loading and row alignment, increased font sizes for legibility, added dividers between sections). Rounds 3, 5, 9 were reversions from spec (blue/green toggle colors instead of the design system's brand teal; filled CSS triangles instead of the system's line-icon chevrons; a gradient added to one row that read as a stray selected state). Round 10 fixed round 9's inconsistency by applying the gradient to all five rows — but combined with round 7 (which had dropped the divider above Log out to fix an unrelated text-wrap issue), this left Log out as the only *flat* row on a screen of raised ones, the reverse of round 1's intent.

### Task 4.6 — Step 4
**Question:** Log every round: what you asked, what changed, whether it improved.

**Solution:** Full ten-round table saved as `Settings-Screen-Round-Log.md`, plus an added analysis of what happened to the Log-out requirement specifically: it was originally differentiated three independent ways (spacing, a divider, color/border); by round 10 two of the three were gone, not because any single round targeted it, but because two separately-reasonable fixes (a text-wrap fix, a gradient-consistency fix) combined to erode it. Fix identified: restore the divider, and deliberately leave Log out flat while the other rows carry the raised treatment, rather than matching its style to them.

### Task 4.6 — Step 5
**Question:** Compare your first prompt with what you'd write now, and add the better version to your prompt library.

**Solution:** The first prompt stated the Log-out requirement once, as descriptive prose in the initial build instructions — sufficient for round 1, but nothing carried it forward through later, unrelated rounds. Wrote a generalized replacement, "Iterative Prototype Build — Protect the Core Requirement," which turns a must-keep requirement into a standing check applied to every future round: before applying any requested change, check whether it would weaken the requirement (even indirectly), apply the change but flag the tradeoff if it would, and state at the end of every round whether the requirement still holds. Added to both `My_Prompt_Library.md` and the workbook's actual Prompt Library tab (row 31) — the two are separate documents that had drifted apart; reconciled during this task.

---

## Task 4.7 — Build: States, edges and the unhappy path

### Task 4.7 — Step 1
**Question:** Read both NN/g articles.

**Solution:** Completed.

### Task 4.7 — Step 2
**Question:** List every state a data-heavy screen can be in: first-use empty, user-cleared empty, loading, partial load, error, no results after filtering, permission denied, offline, too much data, one item, one thousand items.

**Solution:** Listed all eleven states as given — a naming/definition exercise, not a design one; the design pass comes in Step 3.

### Task 4.7 — Step 3
**Question:** Take your Task 4.6 prototype and design at least six of those states in Claude Design.

**Solution:** Built eight of the eleven states (more than the six required) as a multi-artboard board in Claude Design, exported as `Settings Screen States.html` — another "Bundled Page" export, this time a static board of eight side-by-side artboards sharing one `showNotes` toggle rather than eight instances of one stateful component. Decoded with the same script used for Task 4.5. States built: Loading (skeleton pulse holding exact row geometry), Partial Load (one section fails while others load normally, scoped Retry), Error (full-screen failure with a support-usable error code), Offline (banner + dimmed server-bound rows + a "will sync" pending state), Permission Denied (locked rows + a Contact Your Admin action), One Item (single-setting plan state), One Thousand Items (dense list with sticky counted headers and search promoted to the top), and No Results After Filtering (query restated, scope searched stated, two recovery paths offered).

### Task 4.7 — Step 4
**Question:** Write the actual copy for each — no placeholder text. Error messages must say what happened and what to do next.

**Solution:** All eight boards already carried real, specific copy (no lorem ipsum). Audited each against the "what happened + what to do next" rule: four states fully pair the two (Partial Load's Retry, Error's Try Again, Permission Denied's Contact Your Admin, No Results' Clear Search plus suggestion chips). Two states name the problem but leave the resolution implicit rather than actionable — the Offline banner never tells the user what would fix it, and the One Item locked-plan message names an unverified workspace with no link to start verifying it. Full write-up: `Task-4.7-Step4-Copy-Review.md`.

### Task 4.7 — Step 5
**Question:** Ask Claude: *"Review these six state designs and their copy. Which messages tell the user what went wrong but not what to do?"*

**Solution:** Asked the literal question against all eight states. Answer: Offline and One Item are the two that name the problem without giving the user an action to take, while Partial Load, Error, Permission Denied, and No Results each pair the problem with a concrete next step.

---

## Task 4.8 — Build: A real screen from your own flow

### Task 4.8 — Step 1
**Question:** Pick the most important screen from your Harvest Hub flow — the order management view.

**Solution:** Confirmed the order management view as the target screen — this was already the natural choice from Task 4.3, where the order-to-delivery flow was identified as the single most important task in Harvest Hub, given the brief's own emphasis that a late order is often worthless.

### Task 4.8 — Step 2
**Question:** Wireframe it on paper first. Do not skip this.

**Solution:** Produced a wireframe of the Order Management screen: navigation (Orders/Inventory/Driver Workload/Dashboard tabs), an Order Queue table with filters (Late, Needs stock check, Unassigned, City) and sortable columns (Order ID, Restaurant/Grocer, Due), row actions contextual to each order's status, a detail panel (Order Summary, Stock Check, Assign Driver with driver workload visible at the point of the assignment decision — directly fixing the internal-logic-vs-user-logic gap Claude flagged back in Task 4.3 Step 5 — plus Timeline/Edit history), and a Resolve Stock Shortfall modal tied to the flow's stock-out decision point (Cancel order / Hold — set deadline timer).

### Task 4.8 — Step 3
**Question:** Build it in Claude Design, giving it a clear written description of structure, hierarchy and every state.

**Solution:** Built from the wireframe above.

### Task 4.8 — Step 4
**Question:** Include at least: navigation, filters, a data table with sortable columns, row actions, a detail panel, and one modal.

**Solution:** All six elements present, as described in Step 2/3 above.

### Task 4.8 — Step 5
**Question:** Self-review against your five checks from Task 3.1 — hierarchy, spacing, alignment, contrast, primary action — then fix everything you flagged.

**Solution:** Spacing, alignment, and contrast all passed as built (late orders signal through both a colored border and a text tag, not color alone — consistent with the Task 4.2 sketch annotation). Three real issues flagged and fixed: (1) hierarchy — the "Resolve shortfall" button was rendered heavier than the page's actual primary action (+ New Order), creating two competing primary actions; fixed by dropping it to standard button weight while keeping its urgency signaled through its red border instead of raw text weight. (2) primary action — order #10230 alone had two row actions (Assign + a kebab menu) where every other row had one; fixed by either folding the kebab's contents into Assign or extending the kebab consistently to all rows. (3) the Assign Driver panel header read "ASSIGN DRIVER — WORKLOAD VISIBLE HERE," design-annotation phrasing rather than real UI copy, inconsistent with its sibling labels ("ORDER SUMMARY — #10230," "STOCK CHECK"); fixed by renaming it to just "Assign Driver." Full write-up: `Task-4.8-Step5-Self-Review.md`.

---

## Task 4.9 — Learn: Accessibility fundamentals

### Task 4.9 — Step 1
**Question:** Read the W3C introduction and skim the A11Y checklist.

**Solution:** Completed — read the W3C *Introduction to Web Accessibility* and skimmed the A11Y Project checklist.

### Task 4.9 — Step 2
**Question:** Write down the design-time responsibilities: colour contrast, target size, focus order, focus visibility, not using colour alone to convey meaning, label clarity, text alternatives.

**Solution:**
- **Colour contrast** — every piece of text and meaningful icon needs enough contrast to be read by someone with low vision or in poor lighting, not just enough to look fine on a bright, calibrated monitor. Check actual contrast ratios at design time (WCAG's 4.5:1 for normal text), not "does this look readable to me right now."
- **Target size** — every clickable/tappable control needs to be large enough to hit reliably for anyone with limited motor precision. A small icon-only button crammed next to others isn't just a density choice, it's a real barrier — spacing and minimum tap-target size are design-time decisions, not something a developer can fix after the fact.
- **Focus order** — when someone navigates by keyboard or switch device, Tab order needs to match the logical, visual order a sighted mouse-user would follow. A mismatch means a keyboard user experiences the page in an order that makes no sense.
- **Focus visibility** — wherever keyboard focus currently sits needs to be visibly obvious, not just present in the code. Removing the focus outline (a common minimalist instinct) makes the interface unusable for anyone not using a mouse.
- **Not using colour alone to convey meaning** — any distinction that matters (error vs. success, late vs. on-time, required vs. optional) needs a second signal beyond colour, because colour alone is invisible or ambiguous to colour-blind users. A red row meaning "late" needs a word or icon saying so too, not just the red.
- **Label clarity** — every input, button, and control needs a label that says what it actually does, not a placeholder-only field or an icon with no accessible name. A search icon with no visible or programmatic label leaves a screen-reader user with no idea what that control is for.
- **Text alternatives** — every non-text element that conveys information needs an equivalent in text, written as a real content decision at design time, not a technical afterthought. A decorative image gets an empty alt; a status icon or a chart needs a text description that actually conveys what the visual shows.

### Task 4.9 — Step 3
**Question:** Audit your Task 4.8 screen against every one of them and list everything that needs attention.

**Solution:** One clean pass — colour is never the only signal (late orders and stock shortfalls both state the problem in words, not just red). Five items flagged: contrast ratios unconfirmed at wireframe fidelity (the LATE tag, stock-shortfall text, and muted secondary text all needed real hex values checked against 4.5:1); three small icon-only targets (row "more actions" kebab, notification bell, account icon) needing confirmed minimum tap size; focus order undefined across the two-column detail panel and the modal; no focus-visible treatment specified anywhere; and five icon-only controls (search, header options, bell, account, kebab, plus the sort-direction arrows) with no accessible name defined. Full write-up: `Task-4.9-Step3-Accessibility-Audit.md`.

### Task 4.9 — Step 4
**Question:** Fix them in Claude Design.

**Solution:** All five flagged items resolved in the rebuilt prototype (`Harvest Hub Order Management.html`): the LATE tag now uses white text on a dark red (#B42318) and error text uses a darker red (#A3161B) than the wireframe's, both clearing WCAG AA; every icon-only control (bell, account, queue options, row "more actions," modal close) is sized 44–48px; the Resolve Stock Shortfall modal is a real `role="dialog" aria-modal="true"` that makes the background `inert`, autofocuses the first field, and restores focus to the trigger on close; a global `:focus-visible` style gives a 3px visible outline; and every icon-only control has a real `aria-label` (the row menu's label is generated per order — "More actions for order #10230" — rather than singled out on one row), sortable headers use `aria-sort`, and empty table cells pair an `aria-hidden` dash with real hidden text for screen readers ("No driver assigned," "On time"). The two Task 4.8 self-review fixes came through in the same build: Resolve shortfall is now secondary-weight (New Order alone is primary), and the "more actions" menu is generated consistently for every row instead of appearing on just one.

### Task 4.9 — Step 5
**Question:** Ask Claude: *"What accessibility problems are invisible in a static design but appear as soon as someone uses a keyboard or screen reader?"*

**Solution:** Focus order and focus visibility don't exist as a concept in a static wireframe — there's no way to see tab order or a missing focus ring in a picture; they only become real problems the moment someone tries to navigate without a mouse. Icon-only controls carry the same trap: they look complete and self-explanatory visually, but a screen reader only has whatever accessible name was actually programmed in — if none was set, it announces as "button" with no indication of what it does. Contrast and target size are at least partially visible in a static mock; focus and icon-labeling are the two categories completely invisible until someone actually uses the interaction mode the design wasn't tested in.

---

## Task 4.10 — Practise: Say it precisely enough to build it

### Task 4.10 — Step 1
**Question:** Pick a screen you haven't built yet — a user management table with roles, filters and a bulk action.

**Solution:** Chose PawPal's Sitter Verification Queue — an internal admin screen (not owner- or sitter-facing) reviewing and managing both user types. This fills a real gap the brief itself left open: the client mentioned "maybe some kind of verification" without defining what it means, and the sitter-side application screen built in Task 2.6 already implied a review screen existed on the other end of it — this is that screen.

### Task 4.10 — Step 2
**Question:** Describe it in about ten lines: structure, hierarchy, which tokens, key states, and the one thing that matters most. Ten lines, not a document.

**Solution:**
- **Structure:** a filterable table of users (name, role, city, join date, verification status) with a per-user detail panel — the same list-plus-detail pattern as the Task 2.6 sitter-side application screen.
- **Hierarchy:** verification status is the single most prominent thing on both the row and the detail panel; everything else is supporting context, since trust is the entire reason this screen exists.
- **Tokens:** a small, fixed set of status badges — Pending, Verified, Flagged, Rejected — reused identically between the table and the detail panel.
- **Key state — Pending:** a new sitter application awaiting review.
- **Key state — Verified:** the trust signal eventually reflected back into the booking flow for both owners and other sitters.
- **Key state — Flagged:** a user reported or under review post-verification — distinct from Pending because it implies something went wrong *after* trust was granted, not before.
- **Key state — Rejected:** requires a reason field, since silently rejecting someone with no explanation recreates the trust problem from the other direction.
- Deliberately doesn't hardcode a specific verification method (ID check, background check) into the structure — it manages the *status* of verification, leaving the actual criteria as a decision the client still owes an answer to.
- **The one thing that matters most:** this screen is the missing other half of "some kind of verification" — everywhere else in PawPal, trust is a promise made to the user; here it has to become an operational decision someone on the team actually makes.

### Task 4.10 — Step 3
**Question:** Generate it cold in Claude Design. Don't refine it.

**Solution:** Generated once from the ten-line Step 2 description with no follow-up refinement prompts, producing the Sitter Verification Queue table with detail panel, exactly as described.

### Task 4.10 — Step 4
**Question:** Put what you got next to what you meant, and find the gaps. For each gap, work out which words caused it.

**Solution:** One real gap: no bulk action anywhere in the build — not just an absent toolbar, but no selection mechanism at all (no checkboxes, no "select all," every row a single click target into the detail panel). Traced to Step 1's own screen-type definition naming "a bulk action" as a requirement, which then didn't survive the compression into Step 2's ten lines — none of the eight bullets mention it, so Claude Design, working only from Step 2, never built one. Every one of Step 2's eight explicit bullets was otherwise matched correctly: verification-status-first column order (Hierarchy), the four status tokens with exact colors/icons (Tokens), both Sitter and Owner records in the sample data, a required reason field on Rejected, filters on status and city, and — the most notable hit — the "deliberately doesn't hardcode a verification method" instruction became a real, visible line of UI copy in the detail panel ("Not yet defined. Decisions are recorded as reviewer judgement with a note.") rather than a silent omission. One minor, unprompted over-build: the same required-reason treatment was also applied to Flagged and to reopening a Rejected user, which Step 2 didn't ask for. Lesson for Step 5: a requirement has to survive into the actual ten lines to get built — naming it a step earlier isn't enough.

### Task 4.10 — Step 5
**Question:** Rewrite those lines — still about ten — and regenerate from scratch. Do this three times, keeping all three screens.

**Solution:** Three screens kept in total, counting the original Step 3 cold build as the first: original (v1), rewrite 1 (v2), rewrite 2 (v2.1) — each one a direct, traceable response to the gap the previous round surfaced.
- **v1 → v2:** rewrite 1 named the bulk-action mechanism explicitly for the first time (checkbox per row, "select all," a bulk-action bar for Approve/Flag/Reject) — the one thing Step 4 found missing. The build closed the gap completely, and went further unprompted: it disables bulk actions that don't apply to a mixed selection and states plainly which selected users get skipped and why.
- **v2 → v2.1:** rewrite 1 had also written the reason-required rule for Flagged and for reopening Rejected→Pending directly into the description (turning what were unprompted over-builds in v1 into confirmed, intentional requirements). Comparing v2 against its own description surfaced one small remaining tension: "checkbox per row" (implying checkbox first) sat next to "verification status is the leftmost column" — two true instructions quietly pulling in different directions. Rewrite 2 resolved it explicitly ("second only to the selection checkbox itself, which exists purely as a mechanism, not a piece of information"). Diffing v2.1 against v2's source showed the build changed *exactly* that one thing — a visible divider and a darker label color separating the checkbox from the first real data column — and nothing else. A rewrite that named one precise thing got exactly that one precise thing back.
- **Overall lesson:** each rewrite fixed only what its own words changed, and only what its own words changed — no more, no less. That is the exercise's whole point: precision in the description shows up as precision in the build, and vagueness shows up as a gap that traces back to a specific missing or ambiguous word every time.

---
