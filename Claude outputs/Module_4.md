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

**Solution:** **Blocked.** No physical drawing pad or paper set up for hand-sketching at the moment. Marked Blocked rather than skipped or faked digitally, since the exercise's value is specifically in paper's speed and disposability — a mouse-drawn substitute wouldn't test the same thing.

### Task 4.2 — Steps 3–5
**Status:** To do — blocked behind Step 2 (sketch a settings page eight ways; pick the best of each set and redraw larger with annotations; photograph everything into `02-Module-Work`). Not started; will resume once a drawing pad/paper setup is available.

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
