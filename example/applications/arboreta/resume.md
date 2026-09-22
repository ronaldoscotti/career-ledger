# Ada Wrzesinska

Data Platform Engineer, event ingestion and late-arriving data · Kraków, Poland · Remote across Europe
ada.wrzesinska@example.com · +48 000 000 000 · linkedin.com/in/example-ada · github.com/example-ada

---

## Ingestion and late-arriving data

Four years owning an event pipeline where amendments arrived after the fact and clients dropped events silently.

- Replaced a nightly full re-aggregation of all order history with an incremental merge on a fourteen-day watermark plus a monthly rebuild, after measuring that ninety-nine point four percent of amendments landed within nine days. The run went from just over six hours to just over two, and the median finish time moved from after eleven in the morning to before five.
- Closed a three percent silent loss in client events that had been attributed to mobile networks for a year. Added a sequence number to the client envelope, built a gap detector over the stream, and took the loss to zero point two percent. The detector is still the standing monitor on client releases.
- Took pipeline run failures from nine a month to one over the following six months, measured on the on-call log.
- Handled the volume at around forty-one million events a day at peak.

## Experience

### Lomvik, Berlin. Senior Data Engineer, Platform. February 2022 to August 2026

Subscription commerce across the German-speaking market and the Nordics. Remote from Kraków. Platform team of three growing to six, owning event ingestion, the warehouse and the nightly aggregation the whole company read every morning. The work above is from this role.

- Cut the compute cost of the nightly run by thirty-one percent, thirty-eight percent including storage.
- Ran the on-call rota from 2023 and took two engineers through their first rotation.

### Merivo Health, Helsinki. Data Engineer. March 2020 to May 2021

Telehealth across Finland and Estonia, seventy people. Second data engineer. Remote from Kraków.

- Built the clinical reporting platform to production in four months, replacing a weekly utilisation figure assembled by hand.
- Owned the delivery guarantees on an event stream where bookings could be amended after the fact, and the weekly reconciliation against the manual figure for eight months.

### Trakvia, Kraków. Backend Engineer, 2018 to 2020. Quality Automation Engineer, 2017 to 2018

Fleet telematics for regional road carriers, forty-five people.

- Cut the integration suite from fifty-two minutes to a nine-minute fast path and took main branch failures from about fourteen a week to under two.

## Between roles

June 2021 to January 2022, out of full-time work. Family illness, and two days a week on contract for the Kraków municipal museum group, consolidating a decade of ticketing exports into a queryable finance dataset.

## Skills

Python, Airflow, Kafka, dbt, Postgres, Terraform, Kubernetes, Docker, Prometheus, Grafana, SQL, Spark, Debezium, Great Expectations, Amazon Web Services

## Languages

Polish, native. English, fluent, working language for six years. German, conversational.
