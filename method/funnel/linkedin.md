# linkedin

The profile is a search surface first and a document second. Treating it as a document is what produces a beautifully written page nobody ever opens.

## The premise

Recruiters find people by searching. They type a boolean string full of titles and technologies, they get a list, and they work down it. A term that appears nowhere in the profile makes the person invisible to every search containing that term, however strong the profile is on everything else.

So the scenario that gets neglected is the one with no feedback in it. The recruiter who opens the profile and moves on at least leaves a trace. The recruiter who searches and never sees the profile leaves nothing, and the person concludes that the market is quiet.

Write for the search first. The page still has to read well for the human who arrives after it.

## Read these first

`profile/PROFILE.md` for the target titles, the seniority band, the geographies and the work arrangement. Those are the inputs to every search a recruiter would run.

`profile/masters/linkedin.md` for the live text. That file is the canonical copy of what is published, and it is what any proposal is diffed against.

The masters change only with the person's approval. This stage proposes blocks, shows them, and waits. Publishing is always their decision, and so is the wording that reaches the public page.

## Decide which of the two jobs this is

**An audit.** The ask is to fix the profile, or to understand why nobody is finding them. Run the whole checklist and the reverse boolean test.

**An increment.** There is one new fact to place: a shipped project, a new responsibility, a public repository, a title change, a course. Run the placement table and nothing else.

Ask if it is genuinely unclear. Running a full audit when the person wanted one line added burns an hour of their attention and buries the line.

## The audit

Run the checklist item by item and report each one as pass or fail. A summarised verdict hides the two failures that matter.

| Item | Passes when |
|---|---|
| `Headline` | It carries the target title, the strongest specialism and the terms a recruiter would type, inside the character limit |
| `About` | It opens with what the person does now, carries at least one measured number, and ends with what they are looking for |
| `Experience` titles | Each one uses the title the market searches for, with the internal title kept beside it where they differ |
| `Experience` bodies | Each role carries bullets that pass `method/funnel/_refs/xyz.md`, with numbers from `profile/experience/locks.md` |
| `Skills` | The target stack is present, ordered so the endorsable ones lead |
| Location and work arrangement | They match what `profile/PROFILE.md` declares the person is eligible for |
| `Open to work` | Configured the way the person chose, visible to recruiters or not, and that choice is recorded |
| The public address of the profile | Customised rather than the generated string, since it goes on the resume |
| Photograph and banner | Present. An absent photograph measurably suppresses profile views |
| Featured items | The two or three artifacts worth opening, with the strongest first |

Deliver the corrections ordered by impact, not in the order of the table. The headline and the titles move more searches than everything below them combined, and a person reading a list in checklist order fixes the cheap items and stops.

## The reverse boolean test

This is the gate that turns opinions into corrections. Run it on every audit.

Assemble the searches a recruiter would actually run for the person's target roles. Build them from `profile/PROFILE.md` the same way `tools/scan.py` builds a sourcing query, with title variants, the seniority band, the stack and the geography. Three to five searches is enough, and they should differ from each other, because a recruiter hiring for the same seat at two companies will type two different strings.

Then go term by term. For each term in each search, check whether the profile contains it, in the exact spelling a recruiter would type. A term missing from the profile is a profile that is absent from that search, and no amount of quality elsewhere compensates.

The output is a list of missing terms with a placement for each, using this mapping:

| Kind of term | Where it has to appear |
|---|---|
| A target job title | `Headline`, and at least one `Experience` title |
| A core technology | `Skills`, and the body of the role where it was used |
| A secondary technology | `Skills`, and the trailing technology list |
| A domain or industry word | `About`, and the body of the relevant role |
| A seniority or scope word | `Headline` and `About` |
| A method or practice | The body of the role where it was practised |

A term that cannot be placed honestly does not get placed. The profile is a claim the person has to defend in the first call, and a keyword stuffed into a role where the work never happened is a claim that collapses on the first question.

## The increment

A new fact rarely belongs in one place. Walk the table and decide each row explicitly, including the rows where the answer is no.

| Section | The fact enters when |
|---|---|
| `Headline` | It changes what the person is, rather than adding to what they have done |
| `About` | It changes the story of what they do now, or it adds the first measured number for a claim already there |
| `Experience` | It happened inside a role on the profile. This is the default and it is where most facts land |
| `Skills` | It introduces a technology or a practice that is not already listed |
| `Featured` | It is something a reader can open: a repository, a talk, a published piece |
| Education and certifications | It is a completed course or a credential with an issuer |

## The voice gate, with one exception

Every proposed block runs `method/voice.md` before it is shown to the person. A profile is text a reader attributes to the person, and machine prose is as visible there as it is in a cover letter.

The exception is the trailing technology list. It is a search device, it exists to be matched by a string comparison, and the rhythm rules do not apply to it. A list of technologies is allowed to read as a list of technologies. Everything above it is prose and gets the full gate.

## The fact goes back to the bank

Anything new that surfaces while working on the profile goes into `profile/experience/` under ZERO-B, in the same turn, with its measured number into `profile/experience/locks.md`.

This happens constantly on this stage, because writing a profile makes a person remember work they never recorded. A fact that reaches the public page and never reaches the bank is a claim the resume cannot use and the interview preparation cannot find.

## The follow-up metric

A week after the person publishes a change, look at `Search appearances`: how many searches surfaced the profile, and under which job titles.

The count on its own says little. The titles are the measurement. When the titles the profile is surfacing under match the titles in `profile/PROFILE.md`, the change worked. When they describe a job the person is trying to leave behind, the headline and the role titles are still selling the previous seat, and that is the next correction.
