# Setup step 06, the first triage

Around twenty minutes, on a posting the person already has.

Optional on day one, and worth doing anyway. Everything before this built a tool. This is the step that proves the tool runs and puts the first thing in the funnel.

## Why it belongs to setup

A person who finishes setup with an empty tracker has spent two hours and started nothing. The next day, opening the repository means choosing to begin, and beginning is the part people postpone.

There is a second reason, and it is the one that makes this a step rather than a habit. Five earlier steps wrote files that nothing has read yet. Running one real posting end to end is the only way to find out whether they answer the questions the funnel actually asks, while the person is still here to correct them.

## How to run it

Ask for a posting they already have in hand. Not the best one they can find, and not one you went looking for. Anything real will do, including one they expect to discard.

Then open `method/funnel/triage.md` and follow it unchanged. Do not simplify it because this is the first run, do not skip the gates, and do not explain the stage while running it. A first run that skipped three things is not proof of anything.

## What to watch, since this is the first time anything reads the profile

Run the triage normally and keep a note of these three. Report them at the end, after the verdict.

**Whether `profile/PROFILE.md` answered every question the stage asked.** The stage reads the floor, the market, the authorization, the arrangement, the age limit, the excluded domains, the non-negotiables and the risk to watch. Any one of them arriving empty means a gate fell back to asking the person, which is a gap in `method/setup/01-profile.md` and takes two minutes to close now.

**Whether the bank had a story for the requirements that mattered.** The verdict lists three or four proofs from `profile/experience/`. Coming up short on the requirements the posting spends the most words on means the walk went shallow in the wrong place, and the fix is `method/setup/02-experience.md` for those jobs specifically rather than for the whole career again.

**Whether the write to the funnel succeeded.** Every triage ends with a write through `tools/tracker.py` under ZERO-A, either a card or a line in the `triage` array. Run `tools/tracker.py check` afterwards and read the exit code. A failure here is a malformed write and not a setup gap, and it gets fixed before the turn ends.

## Closing setup

Mark every step in `.setup-state.json`, including the ones still `partial`, and set `updated`.

Then say what happens next, and name a stage rather than a step. A verdict of pursue goes to `method/funnel/materials.md` for this posting. A no means the funnel is open and empty of cards, and the next move is `method/funnel/sourcing.md` to fill it.

Say one more thing before ending. The career walk is `partial` on purpose and stays that way, and every stage from here feeds it one fact at a time under ZERO-B in `method/rules.md`. Nobody comes back to `method/setup/00-orchestrator.md` for that.
