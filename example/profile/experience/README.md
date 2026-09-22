# Completeness

Every job, how deep the walk went, and what is still open. Keep this current in the same turn as any write to a period file. `method/funnel/interview.md` reads it before asking the person for depth, so a request names the job instead of sending them looking.

Last updated 2026-09-21.

| Period | What | Depth | File | Open |
|---|---|---|---|---|
| 2017-03 to 2020-02 | Trakvia, Kraków. Quality automation, then backend | Shallow | `profile/experience/2017-2020-trakvia.md` | The route optimisation service she owned in 2019 has no measurement and may never have had one |
| 2020-03 to 2021-05 | Merivo Health, Helsinki, remote. Data engineer | Deep | `profile/experience/2020-2022-merivo.md` | Nothing is documented from inside the company. One figure is `[UNVERIFIED]` |
| 2021-06 to 2022-01 | Eight months out of full-time work | Recorded | `profile/experience/2020-2022-merivo.md` | Nothing open. The reason is written down and the museum contract is in the same file |
| 2022-02 to 2026-08 | Lomvik, Berlin, remote. Data engineer, then senior | Deep | `profile/experience/2022-2026-lomvik.md` | No number for the mentoring or the on-call rota. The 2025 runtime regression was never measured |

## Coverage against the ten themes

From the table in `method/funnel/_refs/star.md`. A theme with no story behind it is a gap in the bank and it gets collected before an interview, not improvised in one.

| Theme | Covered by |
|---|---|
| Shipping under ambiguity | Thin. The Merivo story is ambiguity handled badly, which is a different answer |
| A decision that turned out wrong | Merivo, the streaming platform |
| Influence without authority | Lomvik, the dropped events |
| Conflict with a peer | Thin. The watermark argument with Jonas is the closest thing and it resolved in one conversation |
| A system that broke in production | Lomvik, the nine failures a month, told from the on-call side |
| A trade-off deliberately accepted | Lomvik, the fourteen-day watermark and the expensive monthly rebuild |
| Mentoring or raising the bar | Lomvik, two engineers through their first on-call rotation. Counted, with no outcome measured behind it |
| Saying no to scope | Missing |
| A project owned end to end | Lomvik, the nightly pipeline |
| The largest thing ever owned | Lomvik, the ingestion platform at forty-one million events a day |

Two gaps are worth closing before a hiring manager stage: saying no to scope, and a real conflict with a peer. Both are likely to exist in the Lomvik years and neither has been walked.
