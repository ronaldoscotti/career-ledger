# Setup, the orchestrator

This file dispatches and nothing else. Read `.setup-state.json`, tell the person where they stopped, open one step and follow it.

Every step runs on its own. A person coming back after a week starts here and loses nothing, which is the whole reason the state file exists.

## The state file

`.setup-state.json` ships seeded with every step `pending`. Six entries, one per step, each carrying a status of `pending`, `partial` or `done` and a free-text note for what remains. Step 02 also carries a per-job list, because it is the one step that stays legitimately partial for weeks.

```json
{
  "updated": "<date>",
  "steps": {
    "01-profile":      {"status": "done",    "note": ""},
    "02-experience":   {"status": "partial", "note": "two jobs still shallow",
                        "jobs": [{"job": "<employer>", "depth": "deep",    "open": ""},
                                 {"job": "<employer>", "depth": "shallow", "open": "no number yet"}]},
    "03-voice":        {"status": "done",    "note": ""},
    "04-resume":       {"status": "pending", "note": ""},
    "05-linkedin":     {"status": "pending", "note": ""},
    "06-first-triage": {"status": "pending", "note": ""}
  }
}
```

Rewrite the file whenever a step changes status, and set `updated` in the same write. Nothing else records where setup is.

## Reconcile against the filesystem, every run

The state file is never missing, so a guard that checks for a missing file protects against the one case that cannot happen. What always happens is drift. The seeded answer is wrong the moment the person writes a line by hand, and people do.

So look at what exists before reporting anything.

| Step | Done on disk looks like |
|---|---|
| 01 | `profile/PROFILE.md` exists and its front matter carries every key the step defines |
| 02 | `profile/experience/` holds at least one period file, and `profile/experience/README.md` lists every job |
| 03 | `profile/voice.md` exists |
| 04 | `profile/masters/resume.md` exists, with a built file beside it |
| 05 | `profile/masters/linkedin.md` exists |
| 06 | `applications/applications.json` carries at least one card or one line in its `triage` array |

Where the two disagree, the filesystem wins. Correct the state file, then say which entries you changed and what you read to decide. An inference the person cannot see is an inference they cannot argue with.

## The order, and which parts of it are load-bearing

01 runs before everything. Every later step and every funnel stage reads `profile/PROFILE.md`, and a wrong answer there is wrong in fifty places afterwards.

02 runs before 04 and 05, because both draw their content from the bank rather than from the conversation.

03 runs before 04, because the master resume runs `method/voice.md` and that gate reads `profile/voice.md` for what the person actually sounds like.

06 runs last and is optional on day one. 05 and 04 have no order between them.

## The report

Print the whole board before dispatching. One line per step: the number, what it produces, its status, and for anything `partial` what is still missing in the words the note uses. Then one line naming the step you are about to open and what it will ask the person for.

A person returning after a week needs to see the board, not just the next task. They are deciding how much of their evening this costs.

## The budget, honestly

| Step | First pass |
|---|---|
| 01 | Twenty minutes |
| 02 | Forty-five minutes for a whole career, shallow |
| 03 | Fifteen minutes, plus whatever it takes them to find three samples |
| 04 | Thirty minutes |
| 05 | Twenty minutes |
| 06 | Twenty minutes, on a posting they already have |

A little over two hours for 01 through 05. Say that number out loud before starting, and say the other one too: 02 keeps deepening for as long as the search runs, one fact at a time under ZERO-B in `method/rules.md`. That is the design and not a shortfall.

## When the person wants to skip a step

Say what breaks, then do as they ask. Mark the step `partial` with the reason in the note. A setup that refuses to proceed is a setup that gets abandoned at the first friction, and an abandoned setup produces nothing at all.

| Skipped | What breaks |
|---|---|
| 01 | Triage has no floor, no gates and no risk to watch, so every verdict is measured against nothing |
| 02 | Every claim downstream is improvised, and `method/funnel/materials.md` has no attested number to draw on |
| 03 | `method/voice.md` still strips machine prose, and what survives reads correct and anonymous |
| 04 | No master to derive from, so each application starts from a blank page |
| 05 | The profile stays invisible to the searches recruiters actually run |
| 06 | Setup ends with an empty funnel, which is a tool and not a search |

## Handing off

Open the step file and follow it. Do not summarise it back to the person first.

| Step | File |
|---|---|
| 01 | `method/setup/01-profile.md` |
| 02 | `method/setup/02-experience.md` |
| 03 | `method/setup/03-voice.md` |
| 04 | `method/setup/04-resume.md` |
| 05 | `method/setup/05-linkedin.md` |
| 06 | `method/setup/06-first-triage.md` |

When a step ends, come back here, write the new status, and report the board again before opening the next one.
