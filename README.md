# career-ledger

**Keep your repository private.** A repository created from this template is private by default, and it should stay that way. `profile/` and `applications/` hold your salary floor, your employment history, your interview notes and the state of every application you have open. That data is meant to be committed, so that your own history is diffable and yours. It is not meant to be public.

## What this is

A job search run as a system, with an AI agent doing the work alongside you: find openings, judge them, write the application material, review it before it is sent, prepare each interview stage, negotiate the offer, and keep a funnel that never lies about its own state.

The unit of value is the evidence bank. Every claim that reaches a resume, a cover letter or an interview answer traces back to a recorded fact with a measured number and a person who can confirm it. A claim without one does not ship.

## The four layers

- `method/` is the method: the funnel stages, the setup steps, the voice gate, the reference files. It carries no personal data and needs no editing.
- `profile/` is yours: who you are, what you have done, the numbers that are attested, the master resume and the master LinkedIn text.
- `applications/` is state: the funnel as one JSON file, a directory per company, and a running log of what happened.
- `tools/` is stdlib Python with no dependencies: the tracker that validates every funnel write, the resume build, the search assembly, and the gate that keeps personal data out of `method/`.

## Getting started

Create your own private repository from this template, clone it, and run `/setup`. The orchestrator asks where you are, and dispatches the next step. Setup is resumable, because the long step does not fit in one sitting: profile, then the career walk, then voice, then the master resume, then LinkedIn. The first pass takes a little over two hours, and the career walk keeps deepening for as long as the search runs.

If your agent has no skill mechanism, read `AGENTS.md` instead. It says the same thing in prose: which file to open, and when.

## The example candidate

`example/` is a fictional, finished tree: a filled profile, an evidence bank, a funnel with cards in several states. Read it to see what a working repository looks like, then delete it.

```bash
rm -rf example/
```
