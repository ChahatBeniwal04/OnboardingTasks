# Task 4.10, Step 4 — Gap analysis: PawPal Sitter Verification Queue
*"Put what you got next to what you meant, and find the gaps. For each gap, work out which words caused it."*

Compared the cold Claude Design build (`PawPal User Management.html`) line-by-line against the eight bullets of the Step 2 description.

## Confirmed gap — no bulk action anywhere

**What's missing:** there is no bulk action in the build at all — not just an absent toolbar, but no selection mechanism of any kind. Each row is one large click target that opens the detail panel (`u.onClick`); there is no checkbox, no "select all," and no `selectedIds`-type state anywhere in the file. Every status change happens one user at a time, through the detail panel.

**Which words caused it:** Task 4.10 Step 1 itself defined the screen type as "a user management table with roles, filters and **a bulk action**" — so a bulk action was a real requirement one step before this one. But none of Step 2's eight lines mention it. Structure says "a filterable table of users... with a per-user detail panel," Hierarchy talks about verification status, Tokens lists the four badges, four bullets cover the four states, one bullet covers not hardcoding a verification method, and the closing bullet is the "one thing that matters most." Nowhere in the compression to ten lines did "bulk action" survive. Claude Design only ever saw Step 2 — it built exactly what Step 2 asked for, and Step 2 quietly dropped a requirement that Step 1 had explicitly named. That's the mechanism this exercise is testing: a requirement that's true doesn't get built if it doesn't survive the compression into the actual working description.

## Strong matches — not gaps

- **Hierarchy:** the table's column order is "Verification status, Name, Role, City, Joined" — status is literally the first, leftmost column, an exact literal read of "verification status is the single most prominent thing on both the row and the detail panel."
- **Tokens:** the four status definitions match exactly — `Pending` (blue, clock), `Verified` (success, circle-check), `Flagged` (warning, flag), `Rejected` (danger, circle-x) — same four states, same order implied by the description, reused identically between the table pills and the detail panel badge.
- **Both user types:** sample data includes both `role: 'Sitter'` and `role: 'Owner'` records with realistic, role-appropriate fields (rate/availability/pets for sitters, ownerPets/bookings for owners) — even though "both user types" is Step 1's wording rather than Step 2's, the "role" column named in Step 2's Structure bullet was enough of a signal for Claude Design to build it correctly.
- **Rejected requires a reason:** `FORM.Rejected.noteLabel` is `'Reason for rejection (required)'` — an exact match to "requires a reason field."
- **No hardcoded verification method:** no "ID check," "background check," or "document upload" string anywhere in the file — the build correctly leaves the verification method undefined, matching the explicit "deliberately doesn't hardcode" instruction.
- **Filters:** a status-pill filter (with live per-status counts) and a city dropdown filter both exist — a fair, if generous, reading of "a filterable table of users" in the Structure bullet, even though the word "filters" itself doesn't appear until Step 1.

## Minor, unprompted over-build — worth noting, not a real problem

`FORM` also requires a reason for **Flagged** (`'Reason for flag (required)'`) and for **reopening a Rejected user back to Pending** (`'Reason for reopening (required)'`). Step 2 only asked for a reason on Rejected. Claude Design generalized "explain yourself when you move someone's trust status in a way that could hurt them" to two more transitions that weren't in the ten lines. It's a reasonable, consistent extension — not a bug — but it is something the description didn't ask for, so it's worth knowing it came from the model's own judgment rather than your spec.

## A nice, on-target invention

The detail panel includes a "Review criteria" line reading *"Not yet defined. Decisions are recorded as reviewer judgement with a note."* This turns your "deliberately doesn't hardcode a verification method... leaving the actual criteria as a decision the client still owes an answer to" bullet into a real, visible piece of UI copy — the screen honestly tells the person using it that the criteria are unresolved, instead of silently omitting the question or inventing a fake method. That's the ten-line description doing exactly what it was supposed to do: communicating a "don't build this part yet" instruction clearly enough that it became a deliberate design decision, not an accidental gap.

## Summary

One real, confirmed gap — no bulk action, anywhere — traced directly to Step 1's requirement not surviving the compression into Step 2's ten lines. Every one of Step 2's eight explicit bullets was matched correctly, including the subtle one (not hardcoding a verification method, which the build turned into actual honest UI copy). One minor unprompted over-build (reason fields on two transitions beyond the one you specified) is worth knowing about but isn't a defect. The lesson for Step 5: the words that don't make the ten lines don't get built, even when they were true requirements a moment earlier — so a bulk action needs its own explicit line next time, not an assumption that it carries over from the screen type.
