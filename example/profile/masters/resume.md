# Ada Wrzesinska

Senior Data Platform Engineer · Kraków, Poland · Remote across Europe
ada.wrzesinska@example.com · +48 000 000 000 · linkedin.com/in/example-ada · github.com/example-ada

---

## Summary

Data platform engineer, nine years, all of it in Python. I build event ingestion that does not lose events and nightly pipelines that finish before the people who read them wake up. At Lomvik I took the nightly aggregation from just over six hours to just over two and cut its failures from nine a month to one in six months. I have run an on-call rota, and the standing monitor I built for client event loss is still the thing that catches a bad release.

## Experience

### Lomvik, Berlin. Senior Data Engineer, Platform. February 2022 to August 2026

Subscription commerce across the German-speaking market and the Nordics. Remote from Kraków. Platform team of three growing to six, owning event ingestion, the warehouse and the nightly aggregation the whole company read every morning.

- Cut the nightly aggregation from just over six hours to just over two by replacing a full re-aggregation of all order history with an incremental merge on a fourteen-day watermark, after six weeks of instrumentation showed one task holding seventy percent of the runtime.
- Took pipeline run failures from nine a month to one over the following six months, measured on the on-call log, and moved the median finish time from after eleven in the morning to before five.
- Cut the compute cost of the nightly run by thirty-one percent, thirty-eight percent including storage.
- Found and closed a three percent silent loss in client events that had been attributed to mobile networks for a year, by adding a sequence number to the client envelope and building a gap detector. Loss fell to zero point two percent and the detector is still the standing monitor on client releases.
- Ran the on-call rota from 2023 and took two engineers through their first rotation.

### Merivo Health, Helsinki. Data Engineer. March 2020 to May 2021

Telehealth across Finland and Estonia, seventy people, eight months past a Series A. Second data engineer, hired to build the reporting platform. Remote from Kraków.

- Built the clinical reporting platform to production in four months, replacing a weekly utilisation figure that clinical operations had been assembling by hand every Friday.
- Owned the delivery guarantees on an event stream where bookings could be amended after the fact, and the weekly reconciliation against the manual figure for eight months.

### Trakvia, Kraków. Backend Engineer, 2018 to 2020. Quality Automation Engineer, 2017 to 2018

Fleet telematics for regional road carriers, forty-five people, family-owned.

- Cut the integration suite from fifty-two minutes to a nine-minute fast path and took main branch failures from about fourteen a week to under two, by tagging failures by cause for a week before fixing any of them.
- Moved to the backend team in 2018 and owned the route optimisation service through 2019.

## Between roles

June 2021 to January 2022, out of full-time work. Family illness, and two days a week on contract for the Kraków municipal museum group, consolidating a decade of ticketing exports into a queryable finance dataset.

## Skills

Python, Apache Airflow, Kafka, dbt, PostgreSQL, Snowflake, Terraform, Docker, Kubernetes, Prometheus, Grafana, SQL, Spark, Debezium, Great Expectations, Amazon Web Services

## Languages

Polish, native. English, fluent, working language for six years. German, conversational.
