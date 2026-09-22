# sourcing

This stage produces volume and a cheap filter over it. Nothing here judges fit. The expensive pass belongs to `method/funnel/triage.md`, and the whole point of sourcing is that triage gets spent only on survivors.

## Check the bottleneck before generating any volume

Read `applications/applications.json` first, before opening a single board.

Two states mean the search is not short of postings:

- A card sitting at `ready` with material written and never sent. The work is done and the application is still in the repository.
- A card at `process` with a stage on the calendar and no preparation written for it.

Either one is the bottleneck, and two hundred fresh postings poured into a blocked funnel make the real problem harder to see. Say which card is blocking, say what it needs, and ask the person whether they want sourcing anyway. They may well say yes, and that is their call. What is not acceptable is running the volume stage while the funnel is jammed and not mentioning it.

A funnel with nothing stuck in it is the green light. Go.

## Where to look

`method/funnel/_refs/sources.md` holds the three tiers, organised by what an automated client can actually open. Follow it rather than improvising a list of boards, because the improvised list rediscovers the login walls every time.

Assemble the boolean strings with `tools/scan.py`, which reads the target titles, the seniority band, the work arrangement and the eligible geographies out of `profile/PROFILE.md`. Build title variants rather than one title. The same seat gets advertised under three or four names depending on who wrote the posting.

For the blocked sources, send the ready-made request from `method/funnel/_refs/sources.md` and wait. Name the exact filters and the four fields to copy back, ask for one page, and write the message as one paragraph per line with no hard wrap. See the pasteable-text rule in `method/voice.md`. A request the person has to reformat before reading is a request that does not get run.

## The cheap pre-filter

Every criterion here is read from `profile/PROFILE.md`. None of them is a judgment, and none of them needs the posting read in full. That is what makes the pass cheap enough to run over a hundred rows.

| Criterion | Discard when |
|---|---|
| Geography and work authorization | The seat cannot legally be filled by the person, or the location requirement rules them out |
| Individual contributor or management | The posting is for the track the person is not pursuing |
| Seniority | The band sits below the person's floor of scope, or so far above it that the posting is describing a different job |
| Published range against the floor | The top of the published range sits under the floor declared in `profile/PROFILE.md` |
| Working-hours overlap | The required overlap with the team is wider than what the profile declares as workable |

Apply them in that order, cheapest first. Work authorization kills more rows than anything else and costs one glance per posting.

Discard in bulk and record in bulk. A hundred-row paste produces one grouped write, not a hundred deliberations. Group the rejections by the criterion that closed them, so the record reads as four lines rather than forty.

## This stage never gives a fit verdict

A survivor is a posting nobody has ruled out yet. It is not a recommendation, it does not get a level, and it does not get a card.

The temptation is to write a sentence of judgment beside each row, because the rows are already open and it feels like a saving. It is not one. A fit judgment made while skimming a list is a judgment made without the posting read in full, without the company researched, and without the three gates in `method/funnel/triage.md` having run. Survivors go to triage one at a time.

## The output

One ranked list, most interesting first, with the ranking explained in a sentence at the top so the person can disagree with it.

Each row carries five things:

- Company.
- Role, in the posted title verbatim.
- The link to the original posting, never to an aggregator that republished it.
- The published range, when there is one, and an explicit blank when there is not.
- Why it survived, in a clause. The requirement that looked like the person, or the stack that matched, or the range that cleared the floor.

Ten strong rows beat sixty unranked ones. The person reads this list to decide where the next hour goes, and an unranked list hands that decision back to them unmade.

## The discards get written down

ZERO-A applies here as it does everywhere. Each discarded posting becomes a line in the `triage` array through `tools/tracker.py`, carrying the company, the role, the reason and the date.

This is what stops the same posting reappearing in the next sourcing run and consuming a second decision. Over a long search the discard log grows several times larger than the funnel itself, and that ratio is the normal shape of a search rather than a sign that something went wrong.

Write the real reason. A discard recorded as "not a match" gets reopened and re-judged. A discard recorded as the criterion that closed it gets skipped on sight.

## Handing off

Take the top of the ranked list into `method/funnel/triage.md`, one posting at a time. A company with a strong signal and nothing currently open goes on the watchlist in `profile/PROFILE.md` instead of into the discards.
