# Setup step 02, the career walk

The expensive step, and the one the rest of the method lives off. Everything downstream draws its facts from what this step records, and a claim with no entry behind it cannot be shipped.

Around forty-five minutes for a whole career on the first pass. Then it never really ends.

## Two modes, one protocol

**The walk.** A single pass over the whole career, most recent job first, one story each. This is what setup runs today.

**Continuous capture.** One fact at a time, forever after, whenever any stage meets something the bank does not hold. ZERO-B in `method/rules.md` points here for the questions, so they are defined once, below, and nowhere else.

The protocol is identical. What changes is how many facts arrive at once.

## The shallow pass is the target

One story per job, carrying one measured number, then move on. That is a finished first pass and it is what the budget above assumes.

Depth arrives later, driven by a posting that needs it. A person who goes deep on job one spends their whole evening there, and the bank ends up rich about the job that matters least and empty about the one they were hired to talk about.

## Never block

A job that cannot produce a measured number yields an entry marked `[UNVERIFIED]` and the walk continues to the next job.

Ask once. If the number is not there, write what is there, mark it, and move. An agent that keeps pushing until a figure appears has built the exact failure this step exists to prevent, and the person quits somewhere around job three. An `[UNVERIFIED]` entry cannot reach outgoing material, and that is the only thing the marker costs.

## The walk itself

Chronological, most recent first. Per job, ask these and write the answers down as they come.

- What the company did, and what stage it was at when they joined.
- What they were hired to do.
- What they actually owned, which is frequently a different list.
- The hardest decision they made there, and what they chose.
- The measurable result, with who measured it.
- Who they reported to, and how many people reported to them.
- What they would do differently.

Each job yields at least one story in the shape `method/funnel/_refs/star.md` defines: a short situation, a long first-person account of what they did, a result carrying the number, and one optional line of reflection.

The hardest decision is the question that produces the story. The others produce the frame around it. When time runs short, ask that one and the result.

## The four collection questions

These are the whole of ZERO-B, and they run on every fact that enters the bank from any stage at any time.

1. What was the situation, and what was at stake.
2. What the person did, in the first person singular.
3. The measured number, and who measured it.
4. When it happened, and who can confirm it.

Question two is where most answers arrive as "we". Push back every time. A story told in the plural gives a room no way to score the person in front of it.

## Three files, and what separates them

**The period files**, one per job or per stretch of self-employment, under `profile/experience/`. They hold the stories, in prose, with their context.

**`profile/experience/locks.md`** holds attested numbers and nothing else. One line per number: the figure, what it measures, who measured it, and when. A number that is not in this file is not a number, and `method/funnel/_refs/xyz.md` treats the lookup as mechanical rather than as a judgment.

**`profile/experience/conflicts.md`** holds the places where two sources of the person's own history disagree, left unresolved on purpose.

## Why the conflicts file exists

The same project gets reported with three different figures across three documents, each written by hand months apart, none of them obviously wrong. A reconciliation done quietly in the moment picks one and destroys the only evidence that there was ever a disagreement. Six weeks later the person is asked about the figure in a room and cannot remember which of the three they committed to.

So write both numbers, both sources, and the date each came from. `method/funnel/materials.md` reads this file before it writes any number, and it resolves to the smaller one with a note.

## The completeness record

`profile/experience/README.md` lists every job, marks it shallow or deep, and carries the open questions per job.

Keep it current in the same turn as any write to a period file. It is how anyone answers whether the bank is ready for a given posting without reading every file in the directory, and `method/funnel/interview.md` reads it when it decides whether to ask for depth.

## Careers that do not fit the shape

- **Contracting.** Walk the engagements, not the years. The client is the context and the engagement is the job.
- **A company they founded.** Ask what they did that was not founding it. The room already knows they ran the thing, and what it wants is the decision they made inside it.
- **A gap.** Record it as a period with what happened in it. A gap with a recorded reason is a question answered before it gets asked.
- **A career change.** Walk the earlier career too, and ask what transferred. The story that carries the change is usually in the old career and not the new one.
- **Academia.** The project is the job, the supervisor is the reporting line, and the number is the one in the paper.

## Closing the pass

Report the board: every job walked, which ones produced a measured number, which ones carry `[UNVERIFIED]` entries, and what is still open.

Write `02-experience` into `.setup-state.json` as `partial` with its per-job list, not as `done`, unless every job is deep and every number is locked. Then return to `method/setup/00-orchestrator.md`.
