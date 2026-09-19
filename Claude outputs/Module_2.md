# Tasks - Module 2

*Discovery and Problem Definition — mirrors the Task Tracker in narrative Question/Solution form, same as the Module 1 doc.*

---

## Task 2.1 — Learn: The design thinking process, end to end

### Task 2.1 — Step 1
**Question:** Read both, then draw the five stages on paper with an arrow between each — including the loops backwards.

**Solution:** Completed on paper — read the IxDF articles and sketched the five stages (Empathise, Define, Ideate, Prototype, Test) with forward arrows and the backward loops between them.

### Task 2.1 — Step 2
**Question:** For each stage write: its purpose, its output, and what typically gets missed when it's rushed.

**Solution:**

| Stage | Purpose | Typical Output | What Gets Missed When Rushed |
|---|---|---|---|
| **Empathize** | Understand users' real needs, setting aside assumptions. | Deep user research and insights. | Teams assume instead of observing real users. |
| **Define** | Turn research into a human-centered problem statement. | A clear "How might we..." problem statement. | Problem gets framed around business goals, not user needs. |
| **Ideate** | Generate diverse solution ideas by challenging assumptions. | A shortlist of promising solution concepts. | Skipping brainstorming leads to settling for the first idea. |
| **Prototype** | Build cheap, quick versions of solutions to test feasibility. | Multiple low-cost prototypes. | Testing begins without knowing if the solution even works. |
| **Test** | Try solutions with real users to validate them. | Validated insights, often looping back to earlier stages. | Treated as final, so real usability issues go undiscovered. |

### Task 2.1 — Step 3
**Question:** Ask Claude: *"I'm learning design thinking. Here's my one-line summary of each stage. Give me a real example of a product that clearly skipped one of these stages, and what went wrong as a result."*

**Solution:** **Juicero** — a clean example of skipping (or badly compressing) **Define**. The team had real research (people wanted fresh juice with minimal effort and cleanup), but instead of turning that into an honest problem statement, the problem got reframed around the business model: a machine that only worked with proprietary juice packets, to sell a subscription. Bloomberg reporters found you could squeeze the same packets by hand just as fast, with no machine at all — the press coverage was brutal, investor confidence collapsed, and the company shut down about eight months later. The failure wasn't the engineering; it was that the problem statement being solved was the business's preferred problem, not the user's actual one.

### Task 2.1 — Step 4
**Question:** Pick one app you use daily and guess which stage its team invested most in.

**Solution:** **Instagram — Ideate.** To ensure the successful execution of the app's functions and to attract millions of users, the team clearly put a lot of effort into the thinking process — iterating on the Empathize and Define work while shaping each feature (e.g. purpose-built formats for stories/reels/reactions instead of copying WhatsApp's text-first chat, the bio and private-account options, and a UI designed to appeal across age groups).

### Task 2.1 — Step 5
**Question:** *Journal: which stage do you think you'll personally be tempted to skip, and why?*

**Solution:** **Define.** Not from time pressure directly, but from the illusion of having already defined the problem clearly when I haven't actually brainstormed the problem statement enough — I might not even notice I've skipped it.

---

## Task 2.2 — Practise: Empathise — talking to users

### Task 2.2 — Step 1
**Question:** Read both NN/g articles, noting the difference between asking about past behaviour and asking about hypothetical future behaviour.

**Solution:** Completed — read both articles, noting that past-behavior questions ("tell me about the last time you...") produce reliable, concrete answers, while hypothetical questions ("would you ever...") tend to get people's aspirational self-image rather than how they'd actually behave.

### Task 2.2 — Step 2
**Question:** Read Brief A (PawPal) in Appendix A.

**Solution:** Completed. Brief A · PawPal (used in Module 2), as the client wrote it:

> We're a small team in Ahmedabad and we want to build an app for pet sitting. The idea is that pet owners can find someone nearby to look after their pet when they travel. There are a lot of these apps abroad but nothing good for the Indian market.
>
> Our main worry is trust — people are nervous about handing their dog to a stranger. We want it to feel safe. We're thinking about reviews and maybe some kind of verification.
>
> We'd want owners to be able to book someone quickly, see who's available, and message them. Sitters should be able to set their availability and rates. Payments through UPI.
>
> We have a small budget and want something in the market within four months.

*What's deliberately missing: who the sitters are and how they're recruited, what "verification" means, what happens when something goes wrong, whether this is boarding or home visits, and how the two sides of the marketplace get seeded.*

### Task 2.2 — Step 3
**Question:** Write ten interview questions for a prospective PawPal user. At least seven must ask about something they actually did.

**Solution (as originally written):**

1. Tell me approximate number of times you travel out of town in a year
2. Tell me about the last time you left your pet at someone's place
3. Tell me about your pet's requirements in your absence
4. Tell me about the kind of pet you have
5. What is the reason for your trust issues regarding your pet at pet care
6. What is the health status of your pet?
7. How has been your journey with your pet
8. How much are you willing to pay for the pet care service?
9. Describe your pet's name and the story behind keeping this name
10. What kind of food supplements does your pet require?

### Task 2.2 — Step 4
**Question:** Ask Claude to critique them: *"Here are ten user-interview questions. Mark each as leading, hypothetical, double-barrelled, or good — and rewrite the weak ones."*

**Solution:**

| # | Original | Verdict | Final (Revised) |
|---|---|---|---|
| 1 | Tell me approximate number of times you travel out of town in a year | Good | *(no change)* Tell me approximate number of times you travel out of town in a year |
| 2 | Tell me about the last time you left your pet at someone's place | Good | *(no change)* Tell me about the last time you left your pet at someone's place |
| 3 | Tell me about your pet's requirements in your absence | Good (not behavioral) | Tell me about the last time someone else looked after your pet — what did you have to explain to them beforehand? |
| 4 | Tell me about the kind of pet you have | Good (not behavioral) | Tell me about how you ended up with this particular pet. |
| 5 | What is the reason for your trust issues regarding your pet at pet care | **Leading** — assumes "trust issues" exist before the person has said so | Tell me about a time you looked into a pet-sitting or boarding option — what made you go ahead with it, or decide against it? |
| 6 | What is the health status of your pet? | Good (not behavioral) | Tell me about a time your pet's health affected a decision about travel or care. |
| 7 | How has been your journey with your pet | Good (not behavioral, too vague) | Tell me about the hardest moment you've had arranging care for your pet. |
| 8 | How much are you willing to pay for the pet care service? | **Hypothetical** — stated willingness-to-pay, not actual spend | Tell me about the last time you paid someone for pet care, a vet visit, or grooming — what did it cost, and did the price ever change your decision? |
| 9 | Describe your pet's name and the story behind keeping this name | Good (not behavioral, off-topic, kept as rapport-builder) | *(no change)* Describe your pet's name and the story behind keeping this name |
| 10 | What kind of food supplements does your pet require? | Good (not behavioral) | Tell me about the last time you had to arrange feeding or medication for your pet while you were away. |

With the revisions, nine of the ten (all except #9, kept as an icebreaker) ask about something the person actually did — well past the "at least seven" bar the task set.

### Task 2.2 — Step 5
**Question:** Run a fifteen-minute interview with your mentor or a colleague playing a pet owner. Take notes without interrupting, then write up the three most surprising things you heard.

**Solution:** Ran the interview with a real pet-owner colleague, using the revised ten-question set from Step 4. Notes below are cleaned up from the raw transcript, mapped to each question:

1. **Pet's name and story:** Golden retriever named Bodhi — his wife suggested the name. There's a deliberate irony in it: "Bodhi" carries spiritual/meditative connotations, but Bodhi doesn't let him sit still to meditate — he wants to climb into his lap despite being 35–36 kg, or runs around bumping into things nearby.
2. **Last time left pet at someone's place:** Never happened in the roughly five and a half years they've had him.
3. **Approximate travel frequency per year:** A minimum of 2 times a year on average as a family. This year has been an exception, with more travel than usual.
4. **Last time someone else looked after the pet:** When his wife recently traveled to the US for ~15 days for work, and around the same time he had a plastered leg, he hired a pet walker rather than leave Bodhi with a stranger unsupervised. Surprisingly, Bodhi would only walk with the hired walker when the owner was still visible/nearby — a hybrid trust arrangement rather than full delegation to a stranger.
5. **How he ended up with this pet:** Same as Q1 — his wife's recommendation.
6. **Looking into pet-sitting/boarding options:** When his father was diagnosed with cancer, he had to travel frequently between Ahmedabad and Kutch (where he's from) during his father's final stage of treatment. During that period they looked into boarding options for emergencies, but never found anything they trusted enough to actually use.
7. **Pet's health affecting a travel/care decision:** When Bodhi was about six or seven months old, they took him to the beach for the first time and let him off-leash. He drank seawater; the salt content made him sick and he started vomiting, requiring an emergency vet visit the same afternoon. They learned dogs can't process salt the way humans can.
8. **Hardest moment arranging care:** Not distinctly captured — likely overlaps with the beach incident (Q7) or the plastered-leg period (Q4).
9. **Paying for pet care/vet/grooming:** The most they spend on pet care is grooming. A golden retriever's coat takes ~15 minutes to wash but ~2.5 hours to fully dry — a 3-hour activity total — and improper drying risks skin infections from trapped moisture. They use a professional grooming service because of this.
10. **Arranging feeding/medication while away:** Low-confidence — references an issue roughly 6–7 months ago involving ordering food via Amazon, but not clear enough to state definitively.

**Three most surprising things:**

1. Bodhi has never actually been left with anyone outside the immediate family (wife and owner) in five and a half years — the family has consistently structured their own travel around personally staying with him rather than delegating his care.
2. Even with a hired, paid dog walker during a period when the owner had a plastered leg and his wife was away, Bodhi would only walk with the stranger when the owner was still nearby/visible — trust wasn't a binary hire-or-don't-hire decision, it was a hybrid arrangement requiring the owner's physical presence even after paying for help.
3. During a genuinely high-stakes period (his father's cancer treatment), they actively searched for a boarding/sitting option for emergencies and came up empty — not because they didn't look, but because nothing met their bar for trust, directly validating the PawPal brief's core "trust" concern from a real, high-pressure scenario.

---

## Task 2.3 — Practise: Define — turning research into a problem statement

### Task 2.3 — Step 1
**Question:** Read all three resources: IxDF *Define the Problem*, NN/g *Affinity Diagramming*, and IDEO/d.school *How Might We*.

**Solution:** Completed.

### Task 2.3 — Step 2
**Question:** Take your PawPal interview notes and cluster them into themes on paper or in a document — one observation per line, grouped.

**Solution (first pass):**

**Family**
- Never left pet with anyone outside immediate family in 5.5 years
- Family travels a minimum of 2x/year on average, more this year
- Pet's name (Bodhi) has an ironic spiritual connotation given his high-energy behavior

**Need for Paid Service**
- When wife was away for 15 days and he had a plastered leg, hired a paid dog walker rather than leave the dog unsupervised with a stranger
- During father's cancer treatment, actively searched for a boarding/sitting option for emergencies

**Dog health**
- Dog got sick from drinking seawater off-leash at the beach around 6–7 months old
- Required an emergency vet visit the same afternoon
- Learned dogs can't process salt the way humans can

**Dog Care**
- Grooming is the single biggest pet-care expense
- Full wash + dry for a golden retriever takes ~3 hours total (15 min wash, 2.5 hr dry)
- Improper drying risks skin infections from trapped moisture
- Uses a professional grooming service because of the time/skill required

*Flagged before revising:* two of the richest notes from the interview weren't placed anywhere in this first pass — that the family never found a boarding/sitting option they trusted enough to actually use, and that the hired walker could only get the dog to walk when the owner was still nearby. Both are direct evidence of the actual trust barrier, not background color.

**Solution (revised):**

**Trust Barrier** *(new cluster — the core one)*
- Never left pet with anyone outside immediate family in 5.5 years
- When wife was away for 15 days and he had a plastered leg, hired a paid dog walker rather than leave the dog unsupervised with a stranger
- During father's cancer treatment, actively searched for a boarding/sitting option for emergencies
- Never found a boarding/sitting option they trusted enough to use
- Dog would only walk with the hired walker when the owner was nearby

**Dog Health** *(unchanged)*
- Dog got sick from drinking seawater off-leash at the beach around 6–7 months old
- Required an emergency vet visit the same afternoon
- Learned dogs can't process salt the way humans can

**Dog Care** *(unchanged)*
- Grooming is the single biggest pet-care expense
- Full wash + dry for a golden retriever takes ~3 hours total (15 min wash, 2.5 hr dry)
- Improper drying risks skin infections from trapped moisture
- Uses a professional grooming service because of the time/skill required

**Not clustered** *(background/color, not thematic)*
- Family travels a minimum of 2x/year on average, more this year — context for why the trust problem recurs, but not itself an insight about trust, care, or behavior.
- Pet's name (Bodhi) has an ironic spiritual connotation given his high-energy behavior — a personality detail with no bearing on PawPal's problem space.

### Task 2.3 — Step 3
**Question:** Write a point-of-view statement in the form: *[user] needs [need] because [insight]*.

**Solution (draft 1):**
> A needs a reliable person who is an experienced dog walker because of his unavailability in emergencies.
> A needs a trusted body who excels in pet sitting because he has never trusted anyone enough to leave Bodhi with them in case of their unavailability.

*Issue:* both name the solution mechanism ("dog walker," "trusted body") rather than staying at the level of the need, and the "because" clauses are circular rather than pointing to a specific research insight.

**Solution (draft 2):**
> A needs an automated technology which connects them to an entity assisting him in keeping his pet under their care in his long-term absence (days/months) because the technology will save his time in looking for the entities and emergencies come unannounced.

*Issue:* still names a solution mechanism ("automated technology," "an entity"), and introduces a "days/months" timeframe the research doesn't actually support — the real evidence was a 15-day trip and "the final stage" of a family medical emergency, not an open-ended long-term absence.

**Solution (final, accepted):**
> A needs confidence that his pet will feel genuinely secure with a caregiver even when A isn't physically present, because even after paying for a trusted walker, the dog would only settle into the walk when A was nearby — showing that vetting and payment alone don't transfer the trust A relies on, and after 5.5 years and multiple real occasions requiring it (a 15-day trip, a family medical emergency), A still hasn't found a solution that closes that gap.

This version stays outcome-focused (no solution named), is anchored to the actual hybrid-trust finding from the interview, and doesn't overreach on timeframe.

### Task 2.3 — Step 4
**Question:** Generate five "How Might We" questions from the POV statement.

**Solution:**

1. How might we help a dog feel safe and settled with a caregiver even when its owner isn't there at all?
2. How might we build trust between a dog and a new caregiver through something beyond credentials and payment?
3. How might we gradually reduce a dog's need for its owner's physical presence when being cared for by someone new?
4. How might we make an owner feel prepared for a sudden, urgent absence they can't plan for in advance?
5. How might we earn the trust of an owner who has never found a solution good enough to actually use?

### Task 2.3 — Step 5
**Question:** Pressure-test with Claude: *"Here's my POV statement and five HMW questions from user research on a pet-sitting app. Which of these are actually solutions in disguise? Which are too broad to act on?"* Revise accordingly.

**Solution — pressure-test results:**

- **POV statement** — holds up well. Outcome-focused, appropriately scoped, no issues.
- **HMW #1, #2, #4** — clean. None names a solution; each is broad enough to invite multiple directions without being meaningless.
- **HMW #3** ("gradually reduce a dog's need for its owner's physical presence") — flagged as a **solution in disguise**. "Gradually reduce" already picks a strategy (desensitization/habituation) rather than leaving the approach open — it assumes the answer is "wean the dog off needing the owner" rather than, say, replicating the owner's presence some other way.
- **HMW #5** ("earn the trust of an owner who has never found a solution good enough to actually use") — flagged as **too broad**. It could apply to almost any startup winning over a skeptical customer in any market; it overlaps with #2 but loses the specificity of the actual research finding (that vetting and payment alone didn't transfer trust).

Verdict: 3 of 5 pass cleanly; #3 and #5 were flagged for revision. Decision: leave the set as-is and proceed — the two flagged questions were noted rather than rewritten.

---

## Task 2.4 — Practise: Ideate — quantity before quality

### Task 2.4 — Step 1
**Question:** Read about ideation methods, focusing on Crazy Eights and SCAMPER.

**Solution:** Completed.

### Task 2.4 — Step 2
**Question:** Do a genuine Crazy Eights on paper for your best HMW question (#1 — *how might we help a dog feel safe and settled with a caregiver even when its owner isn't there at all*): eight sketches, eight minutes, no editing.

**Solution:**

1. Providing nutritional food to the dog so it doesn't starve.
2. Making the dog's fixed outing schedule by also considering the input of the owner, so regular exercise is ensured.
3. Attach a smart dog collar so both caregiver and owner know the movement, sleeping time, and essential dog vitals.
4. Ensure each dog gets a personalized sleeping schedule based on their breed and regular sleeping schedule.
5. Timely dog bathing with proper tools and measures customized to their breed, for proper hygiene.
6. In-house vet setup so the dog gets immediate care in case of emergency.
7. Building a personalized dog schedule and activity tracker.
8. Regular face time with the owner on a big screen, for building a calm environment as the dog misses its owner.

*Flagged against the specific HMW:* only #8 (face time with the owner) and, more loosely, #4 (personalized routine reducing anxiety) actually answer *this* HMW's emotional-security question. #1, #3, #5, #6 solve real but different pet-care problems (nutrition, monitoring, hygiene, medical risk) rather than "feeling settled with a caregiver." #2, #4, and #7 are really three versions of the same underlying idea — a personalized schedule — so the eight sketches collapse into roughly six distinct ideas, only one or two of which target the actual question.

### Task 2.4 — Step 3
**Question:** Use Claude as a divergence partner: *"Here's my problem statement. Give me 25 distinct solution directions, including at least 5 that are deliberately impractical. Don't evaluate them."*

**Solution:**

1. A "scent transfer" object — something worn by the owner, handed to the caregiver, so the dog has a familiar smell during the visit.
2. A required multi-visit "meet and greet" protocol before any real booking, each visit slightly longer than the last.
3. A brief live video-call feature so the owner can appear on a screen during the caregiver's visit.
4. A caregiver certification track specifically in calming/settling anxious dogs, separate from general pet-care certification.
5. A calm, trained resident companion dog present during visits to help the new dog settle through pack behavior.
6. A small speaker playing a pre-recorded clip of the owner's voice during caregiver visits.
7. A weighted blanket or anxiety wrap included as standard equipment for first-time sittings.
8. A "trust levels" system where a specific caregiver earns longer, less-supervised visits with a specific dog over repeated short ones.
9. A matching algorithm based on the dog's individual temperament traits, not just breed or generic sitter ratings.
10. A "shadow visit" — the owner stays home but out of sight while the caregiver interacts with the pet, before eventually leaving for real.
11. A GPS + camera collar so the owner can passively check in without needing to interact.
12. A neighborhood-first caregiver network, prioritizing someone the dog has already met in person over a stranger from an app.
13. Calming pheromone diffusers installed at the caregiving location.
14. A "settling score" the caregiver logs each visit, giving the owner a visible trend of behavioral comfort over time.
15. An insurance/guarantee product that lowers the owner's financial risk, making it easier to justify trying an unfamiliar caregiver.
16. A subscription model that reassigns the same caregiver repeatedly, building a real relationship over months instead of random matching.
17. AI video monitoring that only alerts the owner on genuine distress signals, rather than requiring constant live watching.
18. A "buddy system" pairing two caregivers, so at least one familiar face is always present even as trust builds.
19. A community trust score built specifically from other owners' reports on a caregiver's ability to calm anxious pets, not general reliability.
20. Shipping the dog's own bedding/crate/toys to the caregiver's location to recreate a familiar environment.
21. *(deliberately impractical)* A holographic projection of the owner that periodically "interacts" with the dog throughout the day.
22. *(deliberately impractical)* A professional animal communicator who "explains" to the dog that the owner is coming back.
23. *(deliberately impractical)* A robotic surrogate that mimics the owner's scent, voice, and movement patterns to keep the dog company.
24. *(deliberately impractical)* A government-mandated national licensing exam for all pet caregivers, similar to a driving test.
25. *(deliberately impractical)* A dog-to-dog "buddy exchange" — two families periodically co-habitate their dogs in supervised swaps, so every dog grows up with an extended "pack" of already-trusted humans and animals.

### Task 2.4 — Step 4
**Question:** Merge your eight and Claude's twenty-five. Cluster into themes and pick three directions to carry forward.

**Solution — seven themes from the merged 33 ideas:**

1. **Recreate the Owner's Presence** *(sensory substitutes)* — robotic surrogate mimicking scent/voice/movement, video face-time, scent-transfer object, live video-call during visits, recorded-voice speaker, holographic projection. *Common thread: none of these change the caregiver — they make the owner's absence feel less absolute, through sight, sound, or scent.*
2. **Gradual Trust-Building Protocols** — multi-visit "meet and greet," "trust levels" system, subscription reassigning the same caregiver, "shadow visit." *Common thread: trust built incrementally through repeated, structured exposure rather than granted upfront.*
3. **Caregiver Vetting & Matching for Calming Ability** — calming-specific community trust score, neighborhood-first network, national licensing exam, calming-specific certification, temperament-based matching, buddy system, professional animal communicator. *Common thread: solve the problem upstream by selecting or credentialing the right caregiver, specifically for the calming/anxiety dimension.*
4. **Canine Companionship Substitutes** — resident companion dog, dog-to-dog buddy exchange. *Common thread: use another dog, not a human intervention, to provide the felt security.*
5. **Monitoring & Safety Net** — in-house vet setup, smart collar, "settling score," insurance/guarantee product, GPS + camera collar, AI distress-only video monitoring. *Common thread: doesn't build trust directly — reduces the owner's risk/anxiety by making problems visible or covered if they occur.*
6. **Anxiety-Reduction Environment & Comfort Objects** — weighted blanket/anxiety wrap, shipped bedding/crate/toys, calming pheromone diffusers. *Common thread: physical/environmental objects that lower anxiety independent of who's providing care.*
7. **Routine & Care Consistency** — personalized sleep schedule, nutritional feeding, fixed outing schedule, breed-customized bathing, personalized activity tracker. *Common thread: general pet-care quality-of-life items, not specific to the trust/settling problem. Not carried forward.*

**Three directions chosen to carry forward (first pass):** Recreate the Owner's Presence · Monitoring & Safety Net · Caregiver Vetting & Matching for Calming Ability.

*Flagged:* "Monitoring & Safety Net" doesn't actually answer the HMW — its own stated logic is that it "reduces the owner's risk" rather than building the dog's felt security, which is what the HMW asks for.

**Three final directions (revised):** Recreate the Owner's Presence · **Gradual Trust-Building Protocols** (swapped in) · Caregiver Vetting & Matching for Calming Ability.

*Two items dropped as deliberately impractical, at the user's choice:* #22 (professional animal communicator) and #24 in the merged numbering / the national licensing exam — noted but not forced into the final clustering.

### Task 2.4 — Step 5
**Question:** *Journal: which came from you, which from Claude, and which came from combining the two?*

**Solution:** From me: all eight Crazy Eights sketches, but five of them (nutrition, outing schedule, sleep schedule, bathing, activity tracker) clustered into "Routine & Care Consistency," which I recognized as off-target for this HMW and didn't carry forward — only my video-facetime sketch survived into a final direction. From Claude: all three of my final chosen directions are populated almost entirely by Claude's 25 divergent ideas — "Caregiver Vetting & Matching" and "Gradual Trust-Building Protocols" are entirely Claude-originated, and "Recreate the Owner's Presence" is five-sixths Claude ideas plus my one sketch. From combining the two: the real value was in selection, not generation — I initially picked "Monitoring & Safety Net" as my third direction, but Claude pointed out that theme's own stated logic ("reduces the owner's risk, doesn't build trust directly") didn't actually answer the HMW question, so I swapped it for "Gradual Trust-Building Protocols" instead — a better fit neither of us would have landed on alone.

---
