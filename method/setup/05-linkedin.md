# Setup step 05, the master profile text

Around twenty minutes. One file out: `profile/masters/linkedin.md`.

Read `method/funnel/linkedin.md` first. The premise lives there and is not repeated here: a profile is a search surface before it is a document, and a term that appears nowhere in it makes the person invisible to every search containing that term.

## What this step does that the funnel stage does not

The funnel stage works on a profile that already exists. It audits one, or it places one new fact into one.

This step writes the first version, from the bank, into a file. There is nothing to audit yet and nothing to diff against, so the placement table and the increment path in that file do not apply here.

What does carry over is the reverse boolean test, and it runs as the acceptance criterion for this step rather than as a review at the end.

## What to write

Draw from `profile/experience/` for the content and from `profile/PROFILE.md` for the target. The file mirrors the sections of the live profile so that a later audit can diff against it.

| Block | Built from |
|---|---|
| `Headline` | The target title in `profile/PROFILE.md`, the strongest specialism, and the terms a recruiter would type |
| `About` | What the person does now, at least one number from `profile/experience/locks.md`, and what they are looking for |
| `Experience` titles | The title the market searches for, with the internal title beside it where they differ |
| `Experience` bodies | The same bullets the master resume drew, through `method/funnel/_refs/xyz.md` |
| `Skills` | The stack from `profile/PROFILE.md`, ordered so the endorsable ones lead |
| The trailing technology list | Everything else, as a list |

Every block except the last one runs `method/voice.md` before the person sees it. The trailing list is a search device matched by string comparison, and the rhythm rules do not reach it.

## The reverse boolean test

This is the gate, and the step does not finish without it.

Assemble three to five searches a recruiter would run for the target roles, built from `profile/PROFILE.md` the way `tools/scan.py` builds a sourcing query: title variants, the seniority band, the stack, the geography. Make them differ from each other. Two companies hiring for the same seat produce two different strings.

Then go term by term, for every term in every search, and check whether the file contains it in the exact spelling a recruiter would type. Report the result as a list, with a placement for each term that is missing, using the mapping in `method/funnel/linkedin.md`.

A term the person cannot honestly claim does not get placed. Record it as a known absence in the file, with one line saying why, so the next audit does not rediscover it and place it by accident.

Finishing this step with a missing term unrecorded is the one failure mode that matters here. The profile then looks complete and is absent from a search nobody will ever tell the person about.

## This step publishes nothing

The file is a draft of what the live profile should say. Publishing is the person's decision, every time, including the wording that reaches the public page.

Say that out loud when handing the file over, and say what it costs to publish nothing: the searches keep returning the old profile until somebody copies the text across.

## Closing the step

Show the person the blocks, the missing-term list, and the absences you recorded. Ask which of the blocks they want changed before they take any of it to the live profile.

Mark `05-linkedin` in `.setup-state.json` and return to `method/setup/00-orchestrator.md`.
