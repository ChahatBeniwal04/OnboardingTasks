# PawPal — Discovery Process (Brief A)

*Revised write-up, Task 2.7 Step 5. Covers Tasks 2.2–2.6: Empathize, Define, Ideate, Prototype, Test. Revision 1 of the Task 2.7 Step 1 compilation, incorporating the critique from Step 4.*

---

## Summary

Interview and usability-test evidence (n=1 throughout — see **Known Limitations**) points to one core problem: PawPal's trust barrier does not dissolve through vetting or payment alone. A colleague who paid for a dog walker still needed to stay physically nearby before the dog would settle — proof that "trust" in this brief means something more specific than a verified badge or a good rating. That finding shaped the POV statement, three of five HMW questions, and the three ideation directions carried forward.

What the process did **not** do is carry that finding all the way to a prototype. The wireframe actually built and tested (Task 2.6) is a generic PawPal booking flow — search, profile, messaging, booking, sitter-availability — not a build of any of the three specific directions (Recreate the Owner's Presence / Gradual Trust-Building Protocols / Caregiver Vetting & Matching) chosen in Task 2.5. The one concrete usability finding that came out of testing (a missing day/time element on the sitter-availability screen) is a real, valuable catch, but it is a build-completeness bug, not a validated or invalidated learning about the trust hypothesis itself. That gap is documented below rather than papered over.

## Feasibility check against Brief A's constraints

Brief A specifies: a small team in Ahmedabad, a small budget, four months to market, UPI-only payments, Indian market. Checked against that, before committing further design time to any one direction:

| Direction | Feasibility within Brief A's constraints |
|---|---|
| Recreate the Owner's Presence | Weakest fit. Live video or voice-during-visit features add real-time infrastructure cost and complexity that competes for scarce engineering time in a four-month window built around a small team. Worth validating the underlying assumption cheaply (paper sketch, per Task 2.5) before committing build time either way. |
| Gradual Trust-Building Protocols | Best fit. This is mostly booking/scheduling logic and policy sequencing (visit 1 → visit 2 → longer visit), not new infrastructure — closer to configuration of the core booking flow than to a separate feature. |
| Caregiver Vetting & Matching for Calming Ability | Moderate fit. A calming-specific trust score or certification field is a data-model and profile-UI addition, not a new subsystem — feasible, but scoping which signals actually get collected (self-reported vs. verified) matters for a small team's four-month budget. |

This check was not run at the time the three directions were chosen (Task 2.4) or fidelity was picked (Task 2.5); it's added here because a direction that can't ship inside Brief A's stated budget and timeline isn't a real option regardless of how well it answers the HMW.

---

## 1. Empathize

**What was done:** Ten interview questions were drafted, reviewed for leading/hypothetical/double-barrelled phrasing, and revised until nine of ten asked about actual past behavior. A fifteen-minute interview was run with one colleague (a real pet owner), notes taken live, then written up.

**Key finding:** Across five and a half years of pet ownership, this colleague never once left his dog with anyone outside his immediate family — not for lack of trying: during a family medical emergency he actively searched for a trustworthy boarding option and found none good enough to use. When he did hire a paid dog walker during a genuine gap in family availability, the dog would only walk when the owner stayed visibly nearby. Payment and vetting bought access to a helper, not the dog's actual settledness.

**Sample size:** One interview. See Known Limitations.

## 2. Define

**What was done:** Interview notes were clustered by theme (first pass missed the two richest observations; a revised pass created a dedicated "Trust Barrier" cluster). A point-of-view statement was drafted through three iterations — the first two named a solution mechanism ("dog walker," "an entity," "automated technology") instead of staying at the level of the need; the third stayed outcome-focused and anchored to the actual hybrid-trust finding:

> A needs confidence that his pet will feel genuinely secure with a caregiver even when A isn't physically present, because even after paying for a trusted walker, the dog would only settle into the walk when A was nearby — showing that vetting and payment alone don't transfer the trust A relies on, and after 5.5 years and multiple real occasions requiring it, A still hasn't found a solution that closes that gap.

Five How Might We questions were generated from the POV, then pressure-tested. Two were flagged: HMW #3 ("gradually reduce a dog's need for its owner's physical presence") bakes in a strategy — desensitization — rather than leaving the approach open; HMW #5 was judged too broad to be actionable. Both were noted but, by deliberate choice at the time, left unrevised and carried forward as written.

**Note on process documentation:** Task 2.1's stage-purpose table describes Define's output as "a clear How might we... problem statement." The work actually done in Task 2.3 treats the POV statement as Define's real output, with the HMW set functioning as a bridge into Ideate rather than Define's own deliverable. That's the more accurate description of what happened here and is the version this write-up uses; the Task 2.1 table is a simplified summary written before Define was actually practiced, not a correction of the later work.

## 3. Ideate

**What was done:** Eight sketches (Crazy Eights, eight minutes) against HMW #1, followed by 25 Claude-generated directions (including five deliberately impractical ones) against the same HMW. The combined 33 ideas were clustered into seven themes and narrowed to three directions to carry forward: Recreate the Owner's Presence, Gradual Trust-Building Protocols, and Caregiver Vetting & Matching for Calming Ability. A fourth candidate, Monitoring & Safety Net, was dropped after checking it against the HMW directly — its own stated logic reduces the owner's risk rather than building the dog's felt security, so it didn't actually answer the question being asked.

**Unresolved flag carried forward:** HMW #3 was flagged in Task 2.3 Step 5 as a solution in disguise (it assumes "gradual reduction" is the right strategy) and left unrevised. "Gradual Trust-Building Protocols" — one of the three directions ultimately chosen — is a direct, literal instance of that same strategy. The flagged assumption was never revisited before it became a real, resourced ideation direction; it should have been re-examined at the point of selecting directions, not left as a Define-stage footnote.

## 4. Prototype

**What was done:** A fidelity-selection framework was built (what question each fidelity answers / what it costs / what feedback it attracts) and applied per direction, selecting the fidelity by naming each direction's riskiest unproven assumption rather than by convenience:

| Direction | Fidelity chosen | Riskiest assumption it targets |
|---|---|---|
| Recreate the Owner's Presence | Paper sketch | Whether sensory substitutes (scent, voice, video) calm the dog at all — a concept-validity question, not a layout one. |
| Gradual Trust-Building Protocols | Paper sketch | Whether the visit-escalation sequence itself makes behavioral sense — testable by writing down the sequence, not by app navigation. |
| Caregiver Vetting & Matching | Wireframe | Whether the information architecture (what shows on a profile, how a trust signal is positioned) is sensible — a layout question. |

Claude then argued against each choice (Task 2.5 Step 4); all three challenges were judged sound, but the original choices were kept rather than revised.

## 5. Test

**What was done:** A five-task usability script was written, phrased as goals rather than instructions, and revised through several rounds — dropping unconfirmed features ("packages," a satisfaction-review system) and a UPI/credit-card mismatch, and adding a concrete day/time constraint to Task 4 so it had a checkable completion state. Claude reviewed the script for leaked interface vocabulary and vagueness; four of five tasks passed cleanly, one (Task 4) was tightened.

A five-screen wireframe (Browse/Search Sitters, Sitter Profile, Messaging, Booking/Confirmation + Payment, Sitter-Side Availability Setup) was built to a literal, no-additions specification, then tested on one real colleague against the five tasks.

**What broke, structurally:** the wireframe has no ratings/reviews element anywhere, despite trust being Brief A's stated #1 concern since Task 2.2 — an omission caused by literal compliance with a fixed element list rather than by judgment. The colleague also got genuinely stuck on Task 4: the Sitter-Side Availability Setup screen has no day/time-setting element at all, only name, pet-ownership questions, and an animal-type checklist.

**How this finding should be read:** the Task 4 breakdown is a real, useful usability catch — it shows the build doesn't yet support a task the product needs to support. It is **not**, however, a validated or invalidated learning about the underlying trust hypothesis from Empathize/Define, because the wireframe tested was never built as an instance of any of the three chosen ideation directions. Testing this wireframe answers "does this specific screen set support the five tasks" — it does not answer "does recreating the owner's presence, gradual trust-building, or calming-specific vetting actually address the trust barrier." Both are legitimate questions; only the first was actually tested here.

---

## What I Learned

*(Task 2.7 Step 3, written in full by me based on the actual work above — reproduced here as part of the compiled record.)*

What I learned — Module 2, running the whole loop on PawPal.

Where the process helped: The five-stage structure caught mistakes I wouldn't have caught working freeform. In Empathize, my first pass at clustering my own interview notes dropped the two richest insights entirely (that the family never found a boarding option they trusted, and that the dog only walked with the hired sitter when I was nearby) — the discipline of one observation per line, then group, is what surfaced that gap, not instinct. In Define, my first two POV drafts both named a solution ("dog walker," "an entity," "automated technology") instead of staying at the level of the actual need, and the second one claimed a "days/months" timeframe the research never supported — the POV format's rigidity is what made those errors visible enough to fix before they became load-bearing. The pressure-test step caught two more real problems in my five HMW questions — one baked in a strategy ("gradually reduce"), one was too generic to be anchored to my actual research — and both would have quietly warped whatever I designed downstream if I hadn't run that specific check.

Ideate is where the process helped the most, and in the way I expected least. Left alone, five of my eight Crazy Eights sketches drifted into a different, more comfortable problem ("what should a pet-care app include") rather than the actual HMW I was supposed to answer. Claude's 25 divergent ideas gave me directions I genuinely wouldn't have generated myself, and the real value showed up at selection, not generation: I picked "Monitoring & Safety Net" as a final direction because it sounded solid, and only caught that its own stated logic didn't answer the actual question when it was checked against the HMW itself, not against my gut feeling.

Prototype and Test are where the loop proved itself hardest, because they're the two stages I'm least naturally rigorous about. The fidelity framework — name the riskiest unproven assumption, then pick the cheapest thing that actually tests it — stopped me from jumping straight to a wireframe for equipment layout and straight to hi-fi for a matching concept that wasn't validated yet. And the usability test genuinely delivered: a real colleague got stuck on Task 4 because the sitter-availability screen has no day/time element at all — a concrete failure I hadn't caught in two separate reviews of my own wireframe.

Where it felt like overhead: Some of the sequence felt like re-proving something I already half-knew. The core "trust isn't transferred by vetting and payment alone" insight was visible from the very first interview, and I re-derived versions of it through clustering, the POV statement, and the HMW set — useful for precision, but by the third pass it felt more like reformatting the same insight than discovering anything new.

The literal-instruction wireframe build is where the overhead was most costly, and it was self-inflicted: because I built to a strict "only what's on the list" constraint, ratings and reviews — the brief's number one stated concern — never made it onto any screen, even though I'd known about that concern since Task 2.2. That wasn't the process failing; it was me treating literal compliance as a substitute for judgment.

And deciding fidelity for all three ideation directions, one at a time, with a full "riskiest assumption" writeup for each, was arguably more deliberation than two of those decisions (both landed on paper sketch) actually needed — at that fidelity level the whole point is that the decision should be cheap and fast, and the analysis around it started to cost more than the sketch itself would have.

---

## Known Limitations

These are gaps the critique in Task 2.7 Step 4 surfaced that this revision does not fix, because fixing them would require new research or a new build rather than better writing:

1. **n = 1 throughout.** Both the Empathize interview (Task 2.2) and the Test usability session (Task 2.6) draw on a single colleague. Every finding in this document — the hybrid-trust behavior, the Task 4 breakdown — is a single, real, worth-taking-seriously data point, not a validated pattern. Before committing build resources to any direction, this needs more than one interview and more than one usability session.
2. **The prototype-to-ideation loop doesn't close.** The wireframe tested in Task 2.6 is a generic PawPal booking flow, not a build of Recreate the Owner's Presence, Gradual Trust-Building Protocols, or Caregiver Vetting & Matching — the three directions Task 2.4 and 2.5 spent real effort choosing and fidelity-matching. None of those three specific directions has actually been prototyped or tested yet. This write-up documents that break rather than backfilling a prototype that wasn't built.
3. **HMW #3's "solution in disguise" flag was never resolved before Gradual Trust-Building Protocols was selected and fidelity-matched.** Re-examining or re-writing that HMW now, after the direction has already been chosen, would retroactively justify a decision rather than genuinely revisit it — noted here as an open question for whoever picks this direction up next, not resolved by this document.

---

*Revision history: this is the first and only revision of the Task 2.7 Step 1 compilation, incorporating gaps flagged in the Step 4 critique (missing synthesis, unflagged sample size, no feasibility check, the unresolved HMW #3 flag, and the conflation of a build bug with a validated learning). Unfixable gaps are recorded above under Known Limitations rather than resolved.*
