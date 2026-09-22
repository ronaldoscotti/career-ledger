# Form answers, Arboreta

Four fields from the application form, written 2026-08-26. Each answer below is what goes in the field, one paragraph per line, no line break inside a paragraph. Copy the block under the field name and nothing else.

Gates run: `method/funnel/_refs/cover-letter.md` not applicable, no letter requested. `method/voice.md` run over all four, table in `applications/arboreta/screening-dossier.md`.

---

## Why do you want to work at Arboreta?

Because the problem in your first two paragraphs is the one I spent four years on. Late-arriving data that quietly changes a number somebody already acted on. At Lomvik that was order amendments landing after the nightly run. Here it is sensor readings arriving days late from places with bad connectivity, which is harder.

I also want the data platform to be the product rather than a service function inside one. I have done the second version and I would rather not do it again.

---

## Describe a data pipeline you are proud of.

The nightly aggregation at Lomvik finished at 11:10 in the morning. The retention team met at nine, so every Monday decision ran on Friday's numbers.

I spent six weeks instrumenting it before changing anything. One task held seventy percent of the runtime, re-aggregating the entire order history every night because nobody could say how late an amendment could arrive. I measured it: ninety-nine point four percent landed within nine days. I moved to an incremental merge on a fourteen-day watermark with a monthly full rebuild to catch the rest.

The run went from just over six hours to just over two, and it started finishing before five in the morning. Failures went from nine a month to one over the next six months. The part I would do again is the six weeks of measuring, and the part I would do differently is shipping the instrumentation as a notebook instead of a dashboard, because the runtime crept back up in 2025 and nobody noticed for a month.

---

## What is your notice period and when could you start?

I am available now. I was made redundant in August 2026 when the platform team was cut from six to two.

---

## Anything else we should know?

I am in Kraków, so your hours are my hours, and my right to work is EU-wide with no sponsorship needed.

One thing on the resume worth a sentence. I was out of full-time work between June 2021 and January 2022. My mother was ill and I was at home for most of that autumn, then I did two days a week on contract for a museum group until January.

---

## What is deliberately absent

The warehouse she has never run in production appears in none of the four answers. It is a requirement she does not meet, and `method/funnel/materials.md` says outgoing material does not hand a reader an objection they had not formed, phrased in the person's own weakest words. The answer is prepared in `applications/arboreta/screening-dossier.md` for the moment somebody asks. Somebody did, in the screening, and the prepared version is what she said.
