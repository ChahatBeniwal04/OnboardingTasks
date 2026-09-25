# Task 4.7, Step 4 — Copy review across the eight states
*"Write the actual copy for each — no placeholder text. Error messages must say what happened and what to do next."*

Source: `Settings Screen States.html`, exported from Claude Design (same project as the Task 4.6 prototype). Decoded with `decode_claude_design_export.py`. All eight boards use real, specific copy — no "Lorem ipsum," no "Error message goes here." Below is what each state actually says, and whether it clears the "what happened + what to do next" bar.

## The eight states

**1 · Loading** — No text copy by design. A skeleton screen (pulsing grey blocks at the exact row geometry) doesn't need words; the shape itself communicates "still coming." Not applicable to the copy rule.

**2 · Partial Load** — "Support options unavailable" + a local **Retry** button, scoped to just the Support section while Account/Preferences finish loading normally.
Clears the bar: says what happened (this one section failed) and what to do (Retry).

**3 · Error** — "Couldn't Load Settings" / "Your settings didn't load. Nothing has changed on your account." / "Error 503 · 14:22" / **Try Again** button.
Clears the bar cleanly: states the failure, reassures nothing was lost, gives a support-usable error code, and one clear action.

**4 · Offline** — Banner: "You're offline. Showing your last saved settings." Account rows dim with "Account changes need a connection." Dark mode toggle shows a "Will sync" badge.
**Gap found:** the banner says what happened but never tells the user what to do about it — there's no "reconnect to make changes" or similar, just a passive disabled state. A user skimming the banner alone wouldn't know a connection would fix anything; they'd have to notice the smaller grey caption under Account to infer it.

**5 · Permission Denied** — Banner: "Managed by HSBC Bank. Your admin controls these settings." Locked Password row. A **Contact Your Admin** button below.
Clears the bar: the button supplies the "what to do next" that the banner text alone doesn't state.

**6 · One Item** — "This is the only setting available on your plan. Account and support options appear once your workspace is verified."
**Gap found:** same shape as Offline — it names the condition (unverified workspace) and the eventual resolution (verification unlocks more), but gives no button or link to start verifying. It's the one locked-content state without a paired action control.

**7 · One Thousand Items** — No user-facing message text; this is a density/layout state (dense list, sticky counted headers, search promoted to the top), not an error or empty state. Not applicable to the copy rule.

**8 · No Results After Filtering** — "No Settings Match 'biometric login'" / "Searched 1,284 settings across 9 sections." / **Clear Search** button + three "Try Instead" suggestion chips (Two-Factor Auth, Password, Device Access).
Clears the bar comprehensively: repeats the query, states the scope searched, and offers two different ways forward.

## What this shows

Of the five states where copy is doing real work (Partial Load, Error, Offline, Permission Denied, One Item, No Results — six, since I'm counting Permission Denied), four fully pair "what happened" with a concrete "what to do next" action (Partial Load, Error, Permission Denied, No Results). Two state the problem but leave the resolution path implicit rather than actionable — Offline and One Item both describe a condition without a control that lets the user act on it in that same moment.

The fix in both cases is cheap and consistent with the pattern the other four states already use: Offline could add a *lightweight* "Retry connection" or simply rely on the OS reconnecting (no control needed, but the copy should say "changes will sync automatically once you're back online" instead of leaving it to the badge alone), and One Item could turn "once your workspace is verified" into a clickable link or button, the same way Permission Denied turned "your admin controls these" into a Contact Your Admin button.
