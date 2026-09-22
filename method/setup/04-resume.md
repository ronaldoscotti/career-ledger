# Setup step 04, the master resume

Around thirty minutes. Two things out: `profile/masters/resume.md`, written by hand, and a built file beside it that nobody edits.

Run it after step 02 and step 03. The content comes from the bank, and the last gate reads `profile/voice.md`.

## This is the master, and no application ever edits it

`method/funnel/materials.md` derives a single-use version per posting, into the company directory, and writes nothing back here. The master stays general.

So resist tailoring while writing it. A master aimed at one posting is a master that has to be un-aimed for the next one, and the derivation step is where aiming belongs.

## Selecting from the bank

The bank is the reservoir. The master is one draw from it.

Take the strongest story per job, not every story. Strongest means the one carrying an attested number from `profile/experience/locks.md` and the widest scope the person can defend in three questions. Two bullets per recent role and one for the older ones is a normal shape.

Everything left behind is still in the bank and still available to `method/funnel/materials.md`. Nothing is lost by leaving it out, and a master carrying every story is a master nobody finishes reading.

Where `profile/experience/conflicts.md` holds two figures for the same result, use the smaller one and say so to the person.

## Three gates, reported item by item

Run them in this order and report each one as pass or fail per item. A summarised verdict hides the two items that matter.

| Gate | Runs over |
|---|---|
| `method/funnel/_refs/xyz.md` | Every bullet, and every claim carrying a number |
| `method/funnel/_refs/ats.md` | The layout and the formatting |
| `method/voice.md` | Every block of prose, last |

The voice gate runs last for the reason `method/funnel/materials.md` gives: the ornament it strips is acquired while writing the sentence around a number, so running it first means running it over prose that is about to change.

## The build

You write the markdown. That is the only thing written by hand.

```bash
tools/build/build.sh profile/masters resume resume.pdf
```

Do not hand-copy a stylesheet, do not call a browser yourself, and do not edit the generated file. All three produce something that looks right and breaks the parser rules the build exists to enforce. When the output is wrong, the fix is in the markdown.

The build needs a browser binary on the machine. Where it reports none, tell the person the file is finished and the render is pending, and mark the step `partial` rather than blocking the setup on an installation.

## Reading the summary line

The build prints one line and then stops talking.

```
pages 2 · em-dashes 0 · ats ok · keywords n/a
```

| Field | Wrong when | What to do |
|---|---|---|
| `pages` | Over two for most careers, over one for a short one | Cut, then merge, then compress, in that order |
| `em-dashes` | Anything above zero | Find them in the markdown and rewrite the sentences. The character is the single most reliable machine tell |
| `ats` | It names a rule instead of reporting ok | It names what broke. Fix the markdown and build again, never the generated file |
| `keywords` | Low, and only when a posting was passed | The master takes no posting, so this reads as unavailable here. It becomes a measurement in `method/funnel/materials.md` |

## When the bank is too shallow to fill a page

Say so plainly. Then go back to `method/setup/02-experience.md` for the jobs closest to the target role, and go deep on those only.

Do not pad. A resume filled out with responsibilities nobody measured fails the two-how test in `method/funnel/_refs/xyz.md`, and the place it fails is the first call rather than this step. A short honest page is a worse-looking document and a better outcome.

## Closing the step

Show the person the markdown, not the rendered file, because the markdown is what they will be asked to change. Read the summary line back to them with what each field means.

Mark `04-resume` in `.setup-state.json` and return to `method/setup/00-orchestrator.md`.
