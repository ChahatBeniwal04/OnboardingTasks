# Task 1.4 — Debugging a Prompt That Isn't Working
Reference material for the **Brief Work** Claude Project — a worked example of raw output being pushed, round by round, into something sendable.

## Step 1 — The hard ask
**Prompt:** "Write onboarding copy for a pet-sitting app aimed at anxious first-time users."

Ran the prompt as-is. Output was generic onboarding copy for "PawCare" — reassuring in tone but with no concrete trust signal and some negatively-framed language (e.g. the word "stressful").

## Step 2 — Judging criteria (set before reading further)
1. Easy language.
2. Content must be comfortable for a first-time anxious user.
3. The app's purpose must be clear.

## Step 3 — Biggest gap, first fix
Biggest gap: not enough assurance/trust data for the user — just claiming background-verification of the sitter wasn't enough reassurance for an anxious first-timer. Needed something like concrete numbers ("trusted by millions/lakhs of users").

Fix: added an instruction to include a concrete trust signal ("Trusted by millions of pet owners"). Reran — new output included the trust stat.

## Step 4 — Five rounds, one change at a time
- **Round 1:** Added a concrete trust signal ("Trusted by millions of pet owners").
- **Round 2:** Replaced negative/stressful words with positive, calming language throughout.
- **Round 3:** Removed anxiety-triggering opening phrases ("leaving your pet," "first time," "big step"); opened with warmth instead.
- **Round 4:** Added a line conveying the brand's core values/mission.
- **Round 5:** Opened with a use-case question ("Going on a vacation and wondering who'll look after your pet while you're away?") instead of a statement.

**Final (round 5) output:**
> "Going on a vacation and wondering who'll look after your pet while you're away? Meet PawCare — trusted by millions of pet owners to care for the ones they love most. We started PawCare on a simple belief: every pet deserves the same love and attention they get at home, even when their family can't be there. Every sitter is carefully background-checked and verified, so you can relax knowing your pet is safe. You'll get photo updates, real-time check-ins, and a friendly support team available around the clock — so you're always just a tap away from your pet's day. Your pet deserves a sitter who feels like family. Let's find the perfect match together."

## Step 5 — Diagnosis per round
- Round 1 (trust signal) — Missing constraints
- Round 2 (positive language) — Missing constraints
- Round 3 (remove anxiety-triggering phrases) — Missing constraints
- Round 4 (brand values line) — Missing context
- Round 5 (open with a question) — Wrong format

**Note:** most fixes across the five rounds were missing-constraints issues — the underlying task and available context were largely fine from the start; the original bare prompt just didn't specify the rules to follow. When an output feels "off" but not wrong in kind, the fix is usually a missing rule, not a missing fact.

---

*Source: Task 1.4 ("Practise: Debugging a prompt that isn't working"), completed 2026-09-10. Pulled from the "Tasks - 10th Sept 2026" running log. Useful for Brief Work as a model of tone (warm, concrete, no corporate hedging) and of how to push a rough draft toward sendable through targeted, one-change-at-a-time edits.*
