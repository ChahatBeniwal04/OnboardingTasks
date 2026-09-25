# Tasks - Module 5

*Delivery — mirrors the Task Tracker in narrative Question/Solution form, same as the Module 1, 2, 3, and 4 docs.*

---

## Task 5.1 — Learn: The basics of good project management

### Task 5.1 — Step 1
**Question:** Watch the video and take structured notes.

**Solution:** Completed — watched *The Basics of Good Project Management* and took structured notes.

### Task 5.1 — Step 2
**Question:** Draw the iron triangle — scope, time, cost — and write one sentence on what happens when a client wants to change each.

**Solution:** Sketched the iron triangle, then wrote one sentence per side: changing scope forces time or cost to give, since the same fixed time and budget can't absorb more work without something else moving; changing time (wanting it faster) forces scope to shrink or cost to rise, since the work itself doesn't shrink just because the deadline did; changing cost (wanting to spend less) forces scope to shrink or the timeline to stretch, since a fixed amount of work still takes a fixed amount of effort regardless of budget.

### Task 5.1 — Step 3
**Question:** Define in your own words: milestone, dependency, critical path, stakeholder, risk register.

**Solution:** First pass conflated a few terms with related-but-different ideas — milestone as "a goal to achieve in a given time" (rather than a zero-duration marker of progress), dependency as general reliance on stakeholders/factors (rather than specifically an ordering relationship between two tasks), and — the one that mattered most — critical path as "the path that completes fastest with maximum efficiency," which has the definition backwards. Revised all three, plus tightened risk register from "an action you take" to "the artifact itself": **Milestone** — a specific point in time marking progress, zero duration, no work of its own (e.g., "requirements signed off," "beta ships"); a marker, not a chunk of work. **Dependency** — a relationship between two tasks where one can't start or finish until another does; about task ordering specifically, not general reliance on people or factors. **Critical path** — the longest chain of dependent tasks in the whole project, which sets the minimum possible duration for everything; nothing on it has slack, so any slip on it slips the whole project, while tasks off it can usually absorb some slip without moving the end date. **Stakeholder** — every person involved in, or affected by, the project. **Risk register** — a running log of identified risks, each recorded with its likelihood, impact, and an owner or mitigation plan; reporting it up to leadership is one use of it, not what it actually is.

### Task 5.1 — Step 4
**Question:** Ask Claude: *"I'm a junior product manager. For each of these project management concepts, tell me specifically how it affects my day-to-day work rather than just what it means."*

**Solution:** Asked the literal question against the five Step 3 concepts. Milestone: it's what you report progress against, so day-to-day work is constantly working backward from milestone dates and flagging risk early rather than at the deadline. Dependency: it's what turns the day into sequencing work — chasing upstream blockers (another team's API, a design sign-off) before they quietly turn a green status red. Critical path: it's what tells you where urgency actually belongs — chase critical-path blockers hard, don't spend the same energy on tasks that have slack. Stakeholder: it's translation work — the same underlying truth gets repackaged differently for engineering, the client, and a manager, and knowing who needs looping in before a decision (not after) is the actual skill. Risk register: it's a habit, not a document — write the worry down the moment it occurs, with a likelihood and an owner, so a known risk never lands as a surprise.

### Task 5.1 — Step 5
**Question:** Note in your journal the one concept here you expect to matter most in your first project.

**Solution:** Dependency — tracking what work is actually waiting on what, and chasing the upstream blocker before it quietly turns a status from green to red.

---

## Task 5.2 — Learn: Agile and Scrum

### Task 5.2 — Step 1
**Question:** Watch the video, then read the Atlassian Scrum guide.

**Solution:** Completed — watched *What is Agile?* and read Atlassian's Scrum guide.

### Task 5.2 — Step 2
**Question:** Write down each ceremony — sprint planning, daily standup, review, retrospective, backlog refinement — with its purpose, who attends, and how long it should take.

**Solution:** Sprint Planning — decides what to pull into the sprint and roughly how; whole Scrum team; time-boxed to 8 hours max for a one-month sprint (scaled down for shorter sprints). Daily Standup — Developers check progress and plan the next 24 hours, surfacing blockers rather than solving them live; Developers attend (Scrum Master may facilitate, Product Owner optional); 15 minutes flat, regardless of sprint length — the one ceremony whose time-box doesn't scale. Sprint Review — demonstrates what was actually completed and gathers feedback that can reshape the backlog; Scrum team plus stakeholders, a working session not a presentation; 4 hours max for a one-month sprint. Sprint Retrospective — the team inspects its own way of working and picks concrete improvements; Scrum team only, no outside stakeholders; 3 hours max for a one-month sprint. Backlog Refinement — ongoing clarifying, sizing, and prioritizing so items are ready for a future planning session; mainly Product Owner and Developers, Scrum Master often facilitates; not one of the five official Scrum events and not formally time-boxed, but commonly guided at no more than ~10% of the team's capacity per sprint.

### Task 5.2 — Step 3
**Question:** Define the roles and the artefacts (product backlog, sprint backlog, increment).

**Solution:** **Product Owner** — owns the "what" and "why," maximizes product value, manages and prioritizes the Product Backlog; one accountable person, not a committee. **Scrum Master** — owns how well the team works with Scrum (not the product itself); coaches, removes impediments, facilitates events; a servant-leader role, not an authority over what gets built. **Developers** — do the hands-on work of turning backlog items into a Done increment each sprint; self-manage how they'll accomplish the sprint goal; "Developer" isn't limited to people who write code. **Product Backlog** — the single ordered list of everything that might be needed in the product, owned by the Product Owner, never finished; its commitment is the Product Goal. **Sprint Backlog** — the subset of Product Backlog items selected for the current sprint plus the plan to deliver them, owned by the Developers and updated throughout the sprint; its commitment is the Sprint Goal. **Increment** — the sum of everything completed this sprint plus all prior increments, a concrete step toward the Product Goal; only counts as an Increment if it meets the Definition of Done, regardless of whether it's actually released; its commitment is the Definition of Done itself.

### Task 5.2 — Step 4
**Question:** Write down what you own in each ceremony, and what you should be asking. Be specific.

**Solution:** Written from all three role perspectives (Product Owner, Scrum Master, Developer) across all five ceremonies, each with a specific "what I own" and a pointed question rather than a generic one — for example, Product Owner at Sprint Review owns framing the increment against the Product Goal and asks "does this feedback actually change our priorities, and what falls off the backlog to make room?"; Developer at Daily Standup owns their own progress and re-planning and asks "is what I'm doing today still moving toward the sprint goal, or have I quietly drifted?"; Scrum Master at Retrospective owns facilitation and psychological safety and asks whether last retro's action item actually happened.

### Task 5.2 — Step 5
**Question:** Ask Claude: *"What does a product manager actually do during sprint planning and backlog refinement? Give me the questions I should be asking in each."*

**Solution:** Sprint Planning — a PM's job is making sure the sprint is worth doing: backlog already ordered by value, a proposed sprint goal in one sentence, answering the "why/what" questions while leaving "how" to the developers. Key questions: does this set of items add up to one coherent goal; do we actually agree on "done" for each item; is there real pushback or just nodding along; is anything blocked on a decision only I can make right now. Backlog Refinement — where most of a PM's actual weekly effort goes: writing/rewriting acceptance criteria, splitting oversized items, cutting or reordering stale ones. Key questions: is this item actually ready to size; what's the smallest version that still delivers real value; does this still matter given what we've learned since it was written; are the acceptance criteria specific enough that everyone would independently agree it's done.

---

## Task 5.3 — Learn: The software development lifecycle

### Task 5.3 — Step 1
**Question:** Watch the video.

**Solution:** Completed — watched the SDLC overview video.

### Task 5.3 — Step 2
**Question:** Draw the SDLC phases and mark exactly where product work happens — you'll find it's more places than you expected.

**Solution:** Product work runs across every one of the seven phases, not just the start: Planning & Requirements (setting vision, prioritizing scope), Requirement Analysis (turning scope into testable acceptance criteria), Design (reviewing/validating the UX actually solves the intended problem), Implementation (staying available to resolve scope ambiguity mid-build), Testing (running UAT to confirm intent, not just function), Deployment (coordinating release notes, rollout timing, go-to-market), and Maintenance (gathering usage feedback that loops directly back into the next Planning phase).

### Task 5.3 — Step 3
**Question:** Write one line per phase on what a product manager contributes or needs from it.

**Solution:** One specific line per phase, matching Step 2's mapping: Planning & Requirements — sets vision and scope based on real business/user need; Requirement Analysis — converts scope into detailed, buildable acceptance criteria; Design — validates the UX solves the defined problem, not just that it looks good; Implementation — resolves scope ambiguity and edge cases in real time so engineers aren't left guessing; Testing — runs/oversees UAT to confirm the built product meets original intent; Deployment — coordinates release notes, rollout timing, and go-to-market alignment; Maintenance — gathers real usage feedback that becomes direct input for the next cycle's Planning phase.

### Task 5.3 — Step 4
**Question:** Compare waterfall and Agile SDLC in a short table, noting when each makes sense.

**Solution:** Seven-row comparison across structure (sequential vs. iterative), requirements (upfront vs. continuously refined), change tolerance (low vs. high), visibility of progress (limited until late vs. frequent), documentation (heavy/upfront vs. lightweight/evolving), risk profile (discovered late and expensive vs. discovered early and cheap to fix), and best fit (Waterfall: stable requirements, strict regulatory sign-off, low tolerance for rework — e.g. safety-critical or heavily contracted work; Agile: evolving requirements, unclear market/user needs, fast feedback and the ability to pivot matter more than a fixed upfront plan).

### Task 5.3 — Step 5
**Question:** Ask Claude: *"Which SDLC phases do product managers typically stop paying attention to, and what goes wrong as a result?"*

**Solution:** Testing and Deployment/Release — the two phases right after handoff to engineering, where attention naturally drops because it starts to feel like execution rather than decision-making. In Testing, PMs who step back let UAT become a rubber stamp against the ticket as written rather than a real check against the original user need, so bugs of interpretation slip through. In Deployment, disappearing right after "it's built" misses rollout sequencing, whether support/sales know what shipped and why, and watching the first hours after release — so a technically successful deploy can still land as a confusing or poorly-supported launch. The underlying pattern: PMs stay engaged as long as their own decisions are being made, and check out once work becomes "execution" — but testing and release are exactly where you find out whether those decisions were right.

---
