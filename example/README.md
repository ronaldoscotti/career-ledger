# The example candidate

**Everything in this directory is invented.** Ada Wrzesinska does not exist, and neither do Trakvia, Merivo Health, Lomvik, Arboreta, Pelagic Labs or Mira Freight. The numbers, the colleagues and the interview notes were written to show a shape, not to record a life. Nothing here is advice about the companies named, because none of them are companies.

Read it to see what a finished tree looks like, then delete it.

```bash
rm -rf example/
```

## The path convention inside this tree

Every path written inside these files is written as it would be in a real repository: `profile/experience/locks.md`, `applications/arboreta/resume.md`. That is the shape you want in your own tree. To open one of them here, put `example/` in front of it.

## Who she is

Ada Wrzesinska, thirty-four, in Kraków. Nine and a half years of building data platforms, all of it in Python, none of it in a company larger than three hundred people. She started in quality automation at a logistics software house, moved into backend in her second year, and has been a data platform engineer ever since. One specialism, stated plainly: event ingestion that does not lose events, and nightly pipelines that finish before the people who need them wake up.

She has a gap. Eight months out of full-time work between June 2021 and January 2022, after fourteen months at a telehealth company that went badly and a family illness that needed her at home. She did two days a week of contract work for a museum in the back half of it. She does not hide the gap and she does not apologise for it.

The telehealth job is the one that went badly, and it went badly partly because of her. She chose a streaming architecture for a reporting platform that needed a nightly batch, because the roadmap promised real-time dashboards in six months. The dashboards never came. The platform produced two numbers that disagreed, the clinical operations team reissued eleven of forty-one weekly reports, and they eventually went back to exporting a spreadsheet by hand. She left in May 2021. The platform was switched off five months later and replaced by a batch job one engineer wrote in three weeks. She heard that from a former colleague, which is why it sits in `profile/experience/locks.md` marked `[UNVERIFIED]`.

Then four and a half good years at a subscription commerce company in Berlin, remote from Kraków, where both of her strongest stories live. The platform team was cut in August 2026. She has been searching since.

## What to look at first

- `profile/experience/2022-2026-lomvik.md` for what a finished story looks like. Three of them, one of them ending badly.
- `profile/experience/conflicts.md` for two sources of her own history that disagree, left unresolved on purpose.
- `applications/applications.json` for a funnel with seven postings judged and three pursued, which is the normal ratio.
- `applications/arboreta/` for one application carried all the way to a scheduled call.

Only the Arboreta directory is shipped. The Pelagic Labs card names files under `applications/pelagic-labs/`, which is what a real tree would hold and what this one leaves out.
