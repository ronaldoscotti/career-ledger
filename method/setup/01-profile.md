# Setup step 01, the profile

Around twenty minutes. One file out: `profile/PROFILE.md`. Every funnel stage reads it on every run, so a wrong answer here is a wrong answer in fifty places later.

Ask the questions in the order below and write the file at the end, in one pass. Do not write a partial file and come back, because the front matter is read by a tool that has no tolerance for a half-filled one.

## The front matter is a machine contract

`tools/scan.py` opens this file, and it raises on a file with no front matter. It indexes `target_market` directly, so an unexpected value is a crash. Worse, it **silently drops** `roles`, `stack` or `location_terms` when any of them is spelled differently. Sourcing and the reverse boolean test keep running and quietly return less.

Delimit the front matter with `---` and use these keys, spelled exactly like this.

| Key | Type | Read by |
|---|---|---|
| `language_conversation` | `pt-BR` or `en` | every stage, for how it talks to the person |
| `language_artifacts` | `pt-BR` or `en` | every stage that writes something that gets sent. `method/funnel/_refs/scripts.md` conditions on this one, because a negotiation message goes to a recruiter |
| `target_market` | `international`, `domestic` or `both` | `tools/scan.py`, which raises on anything else |
| `roles` | list | `tools/scan.py` |
| `stack` | list, ordered by what the person wants to be hired for rather than by what they know best | `tools/scan.py` |
| `location_terms` | list | `tools/scan.py` |
| `work_arrangement` | `remote`, `hybrid` or `onsite` | `method/funnel/linkedin.md`, `method/funnel/sourcing.md` and `method/funnel/triage.md` |
| `work_authorization` | free text | triage, for eligibility |
| `overlap_hours` | free text, where the market makes it matter | triage and sourcing |
| `comp_floor`, `comp_target`, `currency` | free text | triage and negotiation |
| `posting_age_limit` | free text | the triage age gate |
| `domains_excluded` | list | the triage domain gate |

**Two language fields, and both are needed.** Somebody hunting abroad may want to be talked to in their own language while every artifact ships in the market's. One field cannot carry that, and `method/funnel/_refs/scripts.md` is already written against the artifact one.

**Order the stack by ambition.** Ask what they want to be hired for, then ask what they know best, and write the first list. The two lists differ more often than people expect, and sourcing searches on whichever one you wrote down.

## What goes in the body

Three things sit below the front matter: the non-negotiables, the risk to watch, and an empty `## Watchlist` heading.

Leave the watchlist heading in place even though it is empty. `method/funnel/sourcing.md` and `method/funnel/_refs/sources.md` both write companies into that section, and without the heading the first write lands wherever the agent guesses.

## The risk to watch

One line, in the person's own words, naming the thing they want the method to catch them doing. Undervaluing themselves. Chasing a title. Applying to everything. Going silent after a rejection.

Ask it plainly and wait. Every funnel stage reads this line and acts on it, so a vague answer produces a method that watches nothing. If they give you a shrug, give them the four above and ask which one they recognise.

## Compensation, asked in the order that does not anchor them low

Ask for the number that would make them leave their current situation. Then ask what they would accept if everything else were right.

Those are the target and the floor, in that order, and the order is the whole point. Asking for the floor first gives you a number shaped by what they think they can get, and every later conversation is then negotiated down from it.

The floor is where a conversation starts. Record it as the number below which a posting becomes a declared question in triage, and say so to the person while you write it. It closes nothing on its own.

## The age of a posting

Ask how old an advertisement can be before they stop bothering with it.

`method/funnel/triage.md` reads this as a gate. Where it is empty, the stage falls back to naming the posted date and asking, every single time, which is a worse experience for everybody. The field exists because the incident behind that gate names no number, and a number invented here would be candidate data living in the method.

## Domains the person will not work in

Ask directly and write the list. It becomes a triage gate, and it fires as a refusal with no weighing against anything else. A gate the person never declared is a gate that arrives as a surprise on the one posting they liked.

## What the finished file looks like

Placeholders below are written with angle brackets on purpose. Substitute the person's own answers.

```markdown
---
language_conversation: en
language_artifacts: en
target_market: international
roles:
  - <target title>
  - <title variant>
stack:
  - <what they want to be hired for>
  - <next>
location_terms:
  - <region term>
work_arrangement: remote
work_authorization: <what they hold, and for where>
overlap_hours: <required overlap, and with which zone>
comp_floor: <floor> <currency>
comp_target: <target> <currency>
currency: <currency>
posting_age_limit: <how old is too old>
domains_excluded:
  - <domain>
---

# Profile

## Non-negotiables

- <a refusal, stated as a refusal>

## The risk to watch

<one line, their words>

## Watchlist
```

## Closing the step

Read the front matter back to the person, key by key, and ask them to correct it. Then run `tools/scan.py` once. It prints the boolean searches it assembles, and a search that comes back missing a term the person cares about is a key you spelled wrong.

Mark the step `done` in `.setup-state.json` and return to `method/setup/00-orchestrator.md`.
