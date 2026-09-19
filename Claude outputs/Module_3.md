# Tasks - Module 3

*Working with Designers — mirrors the Task Tracker in narrative Question/Solution form, same as the Module 1 and Module 2 docs.*

---

## Task 3.1 — Learn: Visual literacy — enough to give useful feedback

### Task 3.1 — Step 1
**Question:** Read the Toptal piece and the whitespace article, and skim Laws of UX. You're building vocabulary, not craft.

**Solution:** Completed — read NN/g's *Whitespace in Design*, Toptal's *The Principles of Design and Their Importance*, and skimmed Laws of UX.

### Task 3.1 — Step 2
**Question:** Write down the five things you'll check on any screen: hierarchy, spacing, alignment, contrast, and whether the primary action is obvious.

**Solution:** The five checks — hierarchy, spacing, alignment, contrast, and whether the primary action is obvious.

### Task 3.1 — Step 3
**Question:** Ask Claude to describe a deliberately bad settings page: *"Describe a settings page for a project management tool that violates hierarchy, spacing, alignment and contrast. Be specific — I'm going to critique it."*

**Solution:** Completed — asked Claude the literal prompt. Claude produced a deliberately bad settings page for a project-management tool, built specifically to violate all four principles so it could be critiqued. Details that came up during the critique in Step 4 confirm the page included: field labels ("Display name," "Email," etc.) in medium grey (`#555`) on a near-white (`#F5F5F5`) background; a Save button in white text on pale grey; a required-field asterisk in a lighter grey than its label; a Company Name label sitting to the right of its input while Email's label sits to the left; a Delete Workspace button that is bolder, bigger, and more saturated than Save Changes; input fields with inconsistent widths (180px, 320px, 90px) for similarly short fields; and a disabled "Plan" field styled identically to the editable ones.

*(The full page description as originally generated isn't reproduced verbatim here — only the specific elements that came up while critiquing it in Step 4. Paste the original text if you want it added in full.)*

### Task 3.1 — Step 4
**Question:** Write a numbered critique of it, naming the principle behind each problem.

**Solution:** Wrote a seven-item numbered critique. Claude's review of it:

- **Held up as accurate and well-labeled:** #1, #3, #4.
- **#5 — the sharpest catch:** input values (`#333`, darker) outweigh the page's own header (`#555`, same grey as the labels) in visual weight — the least visually assertive thing on the page is the one announcing what page you're on. A genuine, non-obvious hierarchy problem.
- **#2 — needed correcting:** originally aimed at the field labels' contrast against the background, but labels at `#555` on `#F5F5F5` are actually reasonable contrast. The real contrast problem on the page lives in the Save button (white text on pale grey) and the required-field asterisk instead.
- **#6 — needed correcting:** the alignment-inconsistency observation was right (labels really do land in three different positions across the form), but the specific example named was backwards — it's Company Name's label that sits to the right, and Email's that sits to the left, not the reverse.
- **#7 — needed correcting:** the asterisk isn't the *same* color as the surrounding label text, it's a lighter grey than it — arguably a worse problem (a required-field marker dimmer than the text it's marking), but a different mechanism than originally described.
- **Real violations missed entirely:** the Delete Workspace button visually outranking Save Changes (a hierarchy problem — the destructive, rarely-used action shouldn't outrank the primary one); the inconsistent input widths (180px/320px/90px) with no functional reason; and the disabled "Plan" field being styled identically to editable fields, with no visual way to tell it's disabled without clicking it.

Decision: treated as good enough to move on rather than revising the list against these corrections.

*(The original seven-item critique as written isn't reproduced verbatim here — only Claude's assessment of each item. Paste the original text if you want it added in full.)*

### Task 3.1 — Step 5
**Question:** Now do the same for a real screen from a product you use, and check your critique with Claude: *"Where am I stating personal preference as if it were an established principle?"*

**Solution:** Chose the Notion login page (`app.notion.com/login`) and wrote a five-item critique:

1. "Sign up" link's font color is too light, matching the background — violates contrast.
2. "Login to your Notion account" appears in the third row despite serving the page's primary purpose — violates alignment.
3. Everything is centrally aligned, which might read as monotone — violates alignment.
4. The email input's border is very light, which could cause problems for visually impaired or older users — violates contrast.
5. Given the available space, more room should exist between the header and the "Email" sub-header — violates spacing.

Claude opened the actual page in browser to check the critique against it, then walked through where it held up and where it was preference dressed as principle:

- **#4 holds up well** — the email input's border really is very light grey, a legitimate, commonly-cited accessibility/contrast concern on minimalist forms like this one.
- **#1 doesn't hold up** — "Sign up" is a grey, underlined link, clearly readable against the white page; the underline gives it enough affordance to read as clickable. Overstated the case as "matching the background."
- **#2 is mislabeled, not wrong** — the actual issue (the login instruction sitting below the marketing tagline) is a *hierarchy* question (what's most visually prominent, in what order), not an *alignment* one (how elements relate to a shared axis/grid).
- **#3 is the real lesson** — full-page centering is *consistent* alignment around one vertical axis, which is what the principle actually asks for, not a violation of it. Reading it as "monotonous" is a legitimate aesthetic reaction, but it's preference, not a broken principle — exactly the trap Step 5 is designed to expose.
- **#5 is likely the same trap** — "more space should have gone here" is a personal judgment about how the whitespace should be spent, not a spacing principle actually being broken; the current gap is a fairly standard amount for a login form like this.

**Final tally:** one solid principle-based catch (#4), two real observations mislabeled under the wrong principle (#1, #2), and two cases of personal preference dressed up as a violated principle (#3, #5).

Accepted this as the record of "catching yourself" doing exactly what the task predicted, rather than revising the critique — the value was in seeing the pattern, not in producing a clean five-for-five list. Directly relevant to Task 3.2's ten-screen critique ritual coming next: telling taste from principle is the whole point of that exercise.

---

## Task 3.2 — Practise: The daily critique ritual

### Task 3.2 — Step 1
**Question:** Read the ten heuristics and skim Laws of UX — these give you a second vocabulary alongside the visual fundamentals.

**Solution:** Completed — reviewed Nielsen's ten usability heuristics (visibility of system status, match between system and the real world, user control and freedom, consistency and standards, error prevention, recognition rather than recall, flexibility and efficiency of use, aesthetic and minimalist design, help users recognize/diagnose/recover from errors, help and documentation) and skimmed Laws of UX.

### Task 3.2 — Step 2
**Question:** Pick ten screens from apps you use — five you like, five you don't.

**Solution:**

**Dislikes:** Splitwise (Activity page), Rapido (post-ride rating screen), the default Calculator app, Google Classroom, Amazon Alexa (home screen).

**Likes:** YouTube Music (home screen), Settings page, Alarm app, Zomato (home screen), Savana (home screen).

### Task 3.2 — Step 3
**Question:** For each, write a structured critique: what's the user's goal, does the hierarchy support it, what's the type doing, what's the colour doing, what's the spacing doing, which heuristics are violated.

**Solution:** Wrote a full six-field critique for all ten screens. Highlights:

- **Splitwise:** every row carries identical visual weight regardless of amount owed or urgency; colour (avatar/icon) is decorative repetition rather than a signal. Violates *Recognition rather than recall* and *Aesthetic and minimalist design*.
- **Rapido:** the rating screen surfaces fare-paid info and a "Need Help" prompt that compete with the one action (rating) the screen exists for; the Done button stays disabled until a star is picked. Violates *Aesthetic and minimalist design* and *Flexibility and efficiency of use*.
- **Calculator:** history occupies the top half of the screen, ahead of the keypad; orange is used consistently and functionally for operator keys.
- **Google Classroom:** the layout's priority order is fine — the real problem is the system not retaining a preferred account across sessions. Violates *User control and freedom* and *Recognition rather than recall*.
- **Amazon Alexa:** all eight home-screen icons share identical size and weight, so the high-frequency "Communicate" action isn't surfaced any faster than a rarely-used one. Violates *Flexibility and efficiency of use* and *Match between system and the real world*.
- **YouTube Music:** the gradient-to-black background behind each album tile is functional (increases contrast so art pops), not decorative — a legitimate use of colour tied to a real task.
- **Settings:** consistent icon→label→status→chevron row pattern, and colour-coded icons that work as a genuine recognition aid across repeated use.
- **Alarm app:** time in large numerals with am/pm in small caps beside it; restrained, mostly greyscale palette reserved for state/navigation only.
- **Zomato:** the veg/non-veg green-dot toggle borrows a real-world Indian labeling convention directly — a clean case of *Match between system and the real world*.
- **Savana:** flagged one own weakness even on a liked screen — the cart-count indicator is small and easy to miss, a genuine *Visibility of system status* gap.

### Task 3.2 — Step 4
**Question:** Paste each critique to Claude with: *"Here's my critique of a screen. What did I miss, and where am I stating preference as if it were principle?"*

**Solution:** Claude's review found nine of ten critiques held up as genuine, principle-based observations. The Calculator entry was flagged twice: framing "history above the keypad" as a hierarchy violation assumes a single use case (one quick calculation) rather than an equally valid one (reviewing past results); and citing "User control and freedom" to justify wanting a dark-mode toggle stretches a heuristic that's actually about undo/escape routes, not display preferences. A few additional misses were also noted (e.g. Rapido's disabled Done button is also a *User control and freedom* issue, not just *Flexibility and efficiency*).

### Task 3.2 — Step 5
**Question:** Track across all ten how often you confused taste with principle. Note the pattern.

**Solution:** Went back through all ten checking each "heuristics violated/respected" claim against the heuristic's actual definition. Found two clear conflations:

- **Calculator ("no dark mode"):** cited *User control and freedom* and *Flexibility and efficiency of use* — neither heuristic is actually about display themes; the nearest official-sounding label was borrowed and loosened to fit.
- **Savana (colour palette):** the palette's "functional job" was described as "reinforcing brand tone" — but that redefines what "functional" means in this framework (signals state/groups/draws attention to something actionable) broadly enough to let a personal aesthetic preference qualify as a usability principle.
- **YouTube Music** flagged as a softer, borderline case rather than a full conflation, since the colour claim was tied to a real function (contrast/legibility).

**The pattern:** both real conflations happen at the same structural moment — when the six-field format demands a heuristic answer, but the actual observation doesn't cleanly map onto any of the ten. Two different moves covered that gap: borrowing an existing heuristic and loosening its definition (Calculator), and redefining a key term in the framework itself to smuggle taste through (Savana). The direction was symmetric — once defending a dislike, once defending a like — so the real lesson wasn't "I only stretch principles against things I dislike," but that a settled aesthetic reaction, positive or negative, will get manufactured a principled justification unless the heuristic's original definition is checked *before* the sentence is written, not after.

---

## Task 3.3 — Learn: What a design system buys you

### Task 3.3 — Step 1
**Question:** Spend forty minutes navigating Material 3 — foundations, styles, components. You're getting oriented, not memorising.

**Solution:** Completed — navigated Material 3's Foundations (design tokens, accessible design), Styles (colour, typography, shape, elevation), and Components sections, including a close look at how the Button component is documented (variants × states).

### Task 3.3 — Step 2
**Question:** Skim the Apple HIG foundations to see how a second system makes different choices for different reasons.

**Solution:** Completed — skimmed Accessibility, Layout, Color, Typography, Materials, Motion, and SF Symbols under Apple's Human Interface Guidelines Foundations section.

### Task 3.3 — Step 3
**Question:** Pick one component — the button — and note how many variants and states each system specifies. That count is the answer to "why does this take longer than you'd think".

**Solution:** The finding wasn't a number — it was that the two systems aren't comparable on these terms at all. Material treats "variant × state" as the entire organizing structure of its Button page, built literally as a spec sheet. Apple treats button design as a set of context-dependent decisions (which role fits this action, which platform convention applies) rather than a catalog to select from, and only rigorously enumerates states where the visual feedback is genuinely non-obvious — visionOS, a platform with no touch or cursor. Forcing Apple's page into a Material-style grid would invent structure that isn't actually there, and that mismatch is itself the real finding.

### Task 3.3 — Step 4
**Question:** Write three sentences on what a design system buys a delivery team, and what it costs to depart from one.

**Solution (final, after two revisions):**

> What a design system buys you differs by how much the platform is doing for you already. Material has to spell out everything — every button variant crossed with every state — because a Material app has no default look; without that full spec, two Material apps might not feel related at all. Apple's teams get something cheaper: because iOS already has a strong default appearance, an app inherits most of that just by existing on the platform, so Apple only needs to document the exceptions (like visionOS, where no convention exists yet) rather than spec a hundred button states from scratch.
>
> Departing from the system costs you exactly what it was buying — and the size of that cost also tracks the same platform-convention idea. Leave Material's system and you lose the full spec entirely: you now have to invent and document your own variant, test your own states, and maintain it forever, with none of it inherited from anywhere. Leave Apple's conventions and the cost is smaller but still real — a custom button on iOS still forfeits the states, accessibility behavior, and future OS-level updates that a system button gets for free, so it becomes a small permanent liability rather than a one-time design choice — smaller than Material's exit cost only because Apple was quietly supplying less of the spec to begin with.

*Revision history:* the first draft gave a correct but generic "shared toolbox" answer (faster work, consistent product; a custom piece costs ongoing maintenance) without drawing on the Step 3 finding. Revised once to work in the Material/Apple mechanism for the "buys" half; revised again to restore the "cost to depart" half using the same mechanism, since the first revision had dropped it.

### Task 3.3 — Step 5
**Question:** Ask Claude: *"I'm a product manager. When a designer tells me a request is off-pattern for our design system, what are they actually protecting, and when is it reasonable to push back?"*

**Solution:** Claude's answer named four things a designer is typically protecting — the token/spec system itself (an off-pattern request either invents a new token or hardcodes a value that drifts from the system), cross-screen consistency the user relies on, the designer's own future maintenance workload, and sometimes an already-settled decision from an earlier debate. Reasonable grounds to push back: a real, evidenced user need rather than stakeholder taste; a request that recurs often enough to be a case for evolving the system itself rather than a one-off exception; and being willing to explicitly own the tradeoff being asked for rather than treating the exception as free. Flagged "can we just make this bigger" as the exact phrase this task's own note warned about.

---
