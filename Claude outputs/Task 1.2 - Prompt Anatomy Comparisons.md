# Task 1.2 — Prompt Anatomy Comparisons
Reference material for the **Product Learning** Claude Project.

## Default skeleton
Every crafted prompt below follows the same five-part skeleton:
**Role · Context · Task · Format · Constraints**
(Also saved in the workbook's Prompt Library as "Default skeleton.")

---

## Comparison 1 — "Write about design systems"

**Lazy prompt:** "Write about design systems"

**Crafted prompt (five components):**
- **Role:** You are a product manager explaining design systems to engineers.
- **Context:** These engineers are about to start building a new product and need to understand why a design system matters before they touch code.
- **Task:** Explain what a design system is and why it matters, making a persuasive case for adopting one before coding starts. Focus specifically on AI design systems.
- **Format:** A structured document with headers, using a slide-style bulleted breakdown under each section.
- **Constraints:** Fit in two pages. Avoid jargon. Avoid marketing fluff.

**What happened when both were run:**
Output A (lazy prompt) was a generic, unstructured five-paragraph essay about design systems in general, with no AI focus and no length control. Output B (five-component prompt) was a structured, headed, bulleted two-page doc specifically about AI design systems (confidence scores, streaming, wrong answers), aimed at engineers about to build, ending in a concrete ask.

**Five concrete differences:**
1. Audience framing — generic vs. speaking directly to engineers with an ask.
2. AI-specific vs. generic content.
3. Structured headers/bullets vs. plain paragraphs.
4. Bounded two-page length vs. no length control.
5. Plain and specific language vs. vague industry language like "essential tool" and "maintainable codebases."

---

## Comparison 2 — "What is automation?"

**Lazy prompt:** "What is automation?"

**Crafted prompt (five components):**
- **Role:** A PM introducing automation concepts to new hires.
- **Context:** For someone who's never worked with automation tools and needs a foundational understanding.
- **Task:** Define automation clearly and give 2-3 concrete real-world examples.
- **Format:** A definition followed by a bulleted list of examples.
- **Constraints:** Under 200 words, no jargon, keep it general (not AI/ML-specific).

**Five concrete differences:**
1. Lazy version drifts into fluff ("transforming how businesses operate") with no concrete payoff; crafted stays concrete.
2. Lazy examples are abstract; crafted examples are scenario-based with before/after.
3. Lazy has no structure; crafted follows definition + bullets as asked.
4. Lazy runs long and hedges; crafted stays under 200 words.
5. Lazy stays generic in tone; crafted is aimed at someone brand-new with no assumed background.

---

## Comparison 3 — "What are tickets?"

**Lazy prompt:** "What are tickets?"

**Crafted prompt (five components):**
- **Role:** A PM explaining support/task-tracking tickets to a new engineer.
- **Context:** For someone who's never used a ticketing system like Jira before.
- **Task:** Define what a ticket is and walk through its lifecycle (created, assigned, in progress, closed).
- **Format:** A short definition followed by a step-by-step breakdown of the lifecycle.
- **Constraints:** Under 200 words, no jargon, must use a concrete example ticket walked through all four stages.

**Five concrete differences:**
1. Lazy lists ticket fields instead of the lifecycle that was actually asked for.
2. Lazy names specific tools (Jira, Zendesk, ServiceNow) unprompted; crafted stays tool-agnostic.
3. Lazy never uses an example; crafted walks one fictional ticket through all four stages.
4. Lazy is a flat paragraph; crafted has the definition-then-steps structure.
5. Lazy ends on a vague benefit line; crafted stays literal and example-driven throughout.

---

*Source: Task 1.2 ("Learn: The anatomy of a prompt"), completed 2026-09-10. Pulled from the "Tasks - 10th Sept 2026" running log.*
