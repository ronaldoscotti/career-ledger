# Master profile text

Written 2026-08-22 from the bank. This file is the canonical copy of what should be published. The live profile was updated from it on 2026-08-23, except where a block is marked below.

## Headline

Senior Data Platform Engineer · Python, Airflow, Kafka, dbt · Event ingestion and pipeline reliability · Remote, Europe

## About

I build data platforms that people trust enough to make decisions from before lunch.

Nine years, all of it in Python. Most recently four and a half years at Lomvik, where I owned the event ingestion and the nightly aggregation that the whole company read every morning. I took that pipeline from just over six hours to just over two, cut its failures from nine a month to one over the following six months, and closed a three percent silent loss in client events that had been written off as mobile networks for a year.

What I am good at is the unglamorous half: knowing which events never arrived, knowing which number is wrong before the person reading it does, and getting a pipeline to finish at a time that matches when somebody needs it.

I am looking for a senior or staff data platform seat, remote, anywhere that overlaps Central European Time by five hours or more. Polish citizen with EU right to work, no sponsorship needed.

## Experience

### Senior Data Engineer, Platform. Lomvik. February 2022 to August 2026

Internal title: Data Engineer II, then Data Engineer III.

- Cut the nightly aggregation from just over six hours to just over two with an incremental merge on a fourteen-day watermark, after six weeks of instrumentation showed one task holding seventy percent of the runtime.
- Took pipeline run failures from nine a month to one over the following six months.
- Closed a three percent silent loss in client events by adding a sequence number to the client envelope and building a gap detector, taking loss to zero point two percent. The detector is still the standing monitor on client releases.
- Ran the on-call rota from 2023, and took two engineers through their first rotation.

### Data Engineer. Merivo Health. March 2020 to May 2021

- Built the clinical reporting platform to production in four months, replacing a weekly utilisation figure assembled by hand.
- Owned delivery guarantees on an event stream with retroactive amendments, and the weekly reconciliation against the manual figure.

### Backend Engineer, then Quality Automation Engineer. Trakvia. March 2017 to February 2020

- Cut the integration suite from fifty-two minutes to a nine-minute fast path and took main branch failures from about fourteen a week to under two.
- Owned the route optimisation service through 2019.

### Data Consultant, contract. Kraków municipal museum group. October 2021 to January 2022

Two days a week. Consolidated a decade of ticketing exports into a queryable finance dataset.

## Skills

Python · Apache Airflow · Kafka · dbt · PostgreSQL · Snowflake · Terraform · SQL · Data Engineering · Data Pipelines · Distributed Systems · Kubernetes

## Trailing technology list

Docker, Kubernetes, Prometheus, Grafana, Spark, Debezium, Great Expectations, Amazon Web Services, Redshift, Looker, Metabase, Pandas, Polars, Pytest, GitHub Actions, Linux, Bash

## The reverse boolean test, run 2026-08-22

Five searches assembled from `profile/PROFILE.md`, checked term by term.

1. `("senior data engineer" OR "data platform engineer") AND python AND airflow AND remote`
2. `("staff data engineer" OR "principal data engineer") AND (kafka OR streaming) AND europe`
3. `"analytics engineer" AND dbt AND snowflake AND (poland OR remote)`
4. `("data infrastructure" OR "data platform") AND terraform AND kubernetes`
5. `"data engineer" AND ("event driven" OR "event streaming") AND (emea OR "remote europe")`

| Term | Present | Placement |
|---|---|---|
| senior data engineer | Yes | Headline and the Lomvik title |
| data platform engineer | Yes | Headline |
| staff data engineer | No | Not placed. See absences below |
| principal data engineer | No | Not placed. See absences below |
| analytics engineer | No | Not placed. See absences below |
| python, airflow, kafka, dbt, snowflake, terraform, kubernetes | Yes | Skills, and the role bodies where each was used |
| event driven, event streaming | Placed 2026-08-22 | Added "event streaming" to the trailing list and "event ingestion" to the headline |
| remote, europe, emea, poland | Yes | Headline, About, and the location field |
| data infrastructure | Placed 2026-08-22 | Added to the Skills block |

## Known absences

- **Staff and principal.** She has never held either title and the profile does not claim one. `profile/PROFILE.md` lists both as target roles, so searches on them will miss her. This is a known cost and it is not a mistake to fix by placing the word.
- **Analytics engineer.** She has done the work and does not want the seat. Left out on purpose so the inbound matches the target.
- **The museum contract.** On the profile, because the gap reads worse unexplained than explained.

## Not yet published

The trailing technology list was extended on 2026-08-22 and has not been copied to the live profile. Until it is, searches on Debezium and Polars return nothing.
