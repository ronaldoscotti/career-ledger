# materials

This stage derives single-use material for one application: a tailored resume, the answers to a form, and a cover letter when there is a reason for one. The source is `profile/masters/` for the shape and `profile/experience/` for the facts.

Adapting means reordering, promoting, cutting and detailing. It never means fabricating. Every sentence that reaches the derived file traces back to something already recorded, and a fact that is not in the bank gets collected under ZERO-B in `method/rules.md` before it can be used.

## Read these before writing any number

Open `profile/experience/locks.md` and `profile/experience/conflicts.md` first, and keep both in view while writing.

The locks file is the only place a number is attested. The conflicts file is where two sources of the person's own history disagree, and a number sitting in there is a number that cannot be written down as settled. Writing first and checking after produces a draft the person has to re-litigate line by line, and the numbers are the lines they will be asked about in the room.

## The masters are never edited by an application

`profile/masters/` holds the canonical resume and the canonical profile text. An application reads them and writes nothing back.

The derived file lives under `applications/<company>/`, named for the application it belongs to, and it exists for this one posting. Changing a master is the person's decision and goes through them, as ZERO-B requires. When work on an application turns up something that clearly belongs in the master, note it and carry on. Do not edit it in passing.

## The six levers

Every adaptation is one of these. A change that is none of them is a change to justify out loud before making it.

**The title and the tagline.** Name the stack the posting names, in the words the posting used. Open at the person's level rather than closing below it. A tagline that hedges the seniority does the screening work for the reader, and it does it in the wrong direction.

**The centre of gravity.** Whatever the posting spends the most words on gets its own section in the derived file, with real detail under it. The ranking of requirements produced in `method/funnel/triage.md` is the input. A resume whose longest section is the person's favourite project and not the posting's central requirement is a resume answering a different advertisement.

**The rare requirement.** Find the thing the posting asks for that almost nobody else applying will have, and promote it. Common requirements are how an application avoids being cut. The rare one is how it gets chosen, and it is frequently buried three bullets deep in the master because it never mattered before.

**The order of the stack.** Put the technologies the posting names first, in the posting's own spelling. This is a search surface as much as a reading surface, and the rules in `method/funnel/_refs/ats.md` govern how it is laid out.

**Cutting.** Cut without mercy. Anything that does not serve this posting is stealing room from something that does, and the reader's attention runs out long before the page does. A strong project that has nothing to do with this seat comes out.

**Not listing a gap.** Neither the resume nor the letter names a requirement the person does not meet. This reverses an older instinct, so the reason gets written down. Naming a gap hands an objection to a reader who had not formed one, phrased in the person's own weakest words, and it leaves them holding that version instead of the answer. The gap stays recorded in `profile/experience/` and on the card, and the answer gets prepared in `method/funnel/interview.md` for the moment somebody asks.

The same rule has a second edge worth knowing before writing a form answer: outgoing material never opens by naming a limitation of the person, however good the story that follows it. The subject of the paragraph a reader remembers is the thing that lands. The weakness question in `method/funnel/_refs/basics.md` carries the incident behind this and the test that comes out of it.

## Four gates, all mandatory, all reported

Run them and report each one item by item as pass or fail. A gate is a checklist with an output, and an unreported gate did not run.

| Gate | Runs over | When |
|---|---|---|
| `method/funnel/_refs/xyz.md` | Every resume bullet and every claim carrying a number | Always |
| `method/funnel/_refs/ats.md` | The layout and the formatting of the resume | Always |
| `method/funnel/_refs/cover-letter.md` | The letter, its structure and its opening | When a letter exists |
| `method/voice.md` | Every block of prose the reader will attribute to the person | Always, and last |

The voice gate runs last, after the bullet gate. The order is not arbitrary. The bullet gate demands the measurement, and it is while writing the sentence around a number that the text acquires the ornament the voice gate exists to strip. Running the voice gate first means running it over prose that is about to change.

## The header of the derived file

Every derived file opens with a block listing what changed against the master and why, one bullet per decision. It is the auditable difference.

Three weeks later, somebody looks at this file and asks why the strongest project is missing. The header answers in one line, and without it the answer is a reconstruction. The block also catches the adaptation nobody meant to make, because a decision that cannot be stated in a line is usually a decision that happened by accident.

## When two sources disagree

Resolve to the smaller number, and write a note to reconcile the master.

The smaller number is the one the person can defend if both are somehow in play, and the cost of understating a result is smaller than the cost of a claim that collapses under one question. The note matters as much as the resolution, because a conflict resolved silently in one application is a conflict that will be resolved differently in the next one.

## You write the markdown only

The build belongs to `tools/build/build.sh`, which renders the markdown, produces the file to send and runs the checks over it. Pass the application directory, the basename and the output, and the posting when there is one, so the keyword coverage gets measured.

Do not hand-copy a stylesheet into the application directory. Do not call a browser directly. Both have been tried and both produce a file that looks right and fails the parser rules the build script is there to enforce.

## Over the page budget

Cut, then merge, then compress, in that order.

Cutting removes a whole item that does not serve this posting. Merging folds two related bullets into one that keeps both numbers. Compressing tightens the wording of what is left. Going straight to compression produces a dense page carrying everything at once, which reads as a wall and hides the thing the posting was asking for.

## Closing the stage

List what is missing, explicitly, as markers in the file:

- `[CONFIRM: x]` for a fact or a number the person has to verify before this goes anywhere.
- `[ACTION: x]` for something only the person can do, such as pulling a figure from a system you cannot reach.

Never invent to fill a hole. A plausible number with no measurement behind it is invention whatever hedge sits in front of it, and the room finds out by asking one question. See the measured-number test in `method/funnel/_refs/xyz.md`.

Update the card through `tools/tracker.py` in the same turn, attaching every file produced with its label. Then say plainly that `method/funnel/review.md` runs before anything leaves the repository, and that the markers above have to be closed first.
