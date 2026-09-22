# Screening dossier, Arboreta

Stage: recruiter screening, 2026-09-08, thirty minutes, video. Recruiter: Femke Boonstra, talent partner.
Written 2026-09-06. Post-call capture appended 2026-09-08.

## The ruler

She already passed the competence bar. They read the resume and scheduled the call, so the question of whether she can do the work is answered. This stage measures eligibility, the compensation range, motivation, and whether she is coherent about why this seat.

Her declared risk is that she takes the smaller title when she is nervous. The first stage is where underselling does the most damage, because every later stage inherits the level set here. If Femke asks what level she sees herself at, the answer is senior, without a qualifier attached to it.

## The company

Arboreta builds a climate data platform for agricultural insurers. Amsterdam, founded 2019, about ninety people, Series B in March 2026. They ingest satellite imagery, ground sensor networks and public weather feeds, and they sell risk models off it.

What changed recently: the Series B in March, and an engineering post in July describing a migration off their current warehouse. That post is the reason the stack question in the posting reads differently than it looks.

What they sell and to whom: parametric crop insurance pricing, sold to insurers and reinsurers in the European Union and Australia.

The four questions from `method/funnel/_refs/reputation.md` are answered in full at the bottom of this file. Nothing convergent in the reviews. Two mentions of a slow hiring process and nothing else that repeats.

## The map of the posting

Requirements in their words, weighted by the room each one got.

| The requirement | The story | The number | Verdict |
|---|---|---|---|
| "Ingestion pipelines that are correct in the presence of late-arriving data" | Lomvik, the watermark | 99.4 percent of amendments within nine days; run from just over six hours to just over two | Matched |
| "Data you can trust enough to price on" | Lomvik, the dropped events | 3.1 percent to 0.2 percent | Matched |
| "Own the platform end to end, including the pager" | Lomvik, on-call rota from 2023 | None | Matched, unmeasured |
| "Python, Airflow, dbt" | All three, four years | Not applicable | Matched |
| "Experience with Iceberg or a comparable table format" | None | None | Gap |
| "Comfortable telling a stakeholder team no" | None in the bank | None | Gap, and it is a real one |
| "You have seen a platform team get it wrong and know what that costs" | Merivo, the streaming platform | 11 of 41 reports reissued | Matched, and it is the strongest thing she has for this row |
| Bonus: "reading a scientific paper and turning it into a pipeline" | Trakvia route optimisation, thinly | None | Framing friction |

**The friction row.** She describes the route optimisation work as "maintaining a service". She built two of the heuristics in it off a published paper. Lead with what she built.

**The gap row that matters.** Telling a stakeholder team no is asked about in most hiring manager stages and she has no story for it. It goes into `profile/experience/` before the 2026-09-24 call, not into this dossier as an improvisation.

## Three selling points

1. She has run an ingestion platform where the data arrived late, arrived twice and sometimes never arrived, and she has the numbers for all three.
2. She has shipped a platform design that was wrong, watched what it cost the people downstream, and can say exactly what she would do differently.
3. She measures before she changes anything. Six weeks of instrumentation is the story, not the merge.

## The warehouse answer, prepared

Asked in the screening, and it was asked. The prepared version:

"I have not run it in production. I read your July post about the migration, and the thing I would want to know first is how you are handling schema evolution on the sensor tables during the cutover, because that is where I would expect the late-arriving readings to break. The closest thing I have done is a warehouse migration at Lomvik in 2023 where we ran both for five months."

No apology in front of it and no hedge behind it. The question was asked, so the limitation is named because the question named it first.

## Compensation

Published range is 105,000 to 125,000 euros. Floor is 95,000 and target is 120,000, from `profile/PROFILE.md`.

If the number is asked for, the answer is the target, stated once, with no range and no softening. The published band reaches it, so there is nothing to negotiate around at this stage.

## The two questions she asks

**The objection question.** "Having read the application and talked to me, is there anything in my background that gives you pause?"

**The high-performer question.** "What separates somebody excellent in this seat from somebody who is just doing the job well?"

## The spoken gate

Run over every prepared answer, `method/funnel/_refs/spoken-gate.md`.

| # | Check | Yes or no |
|---|---|---|
| 1 | Every sentence is sayable in one breath. | Yes, after splitting the warehouse answer into three |
| 2 | No clause nested inside another clause. | Yes |
| 3 | Every number is written the way it would be spoken. | Yes. "Just over six hours to just over two", never a decimal |
| 4 | No opening takes more than two sentences to reach the point. | Yes |
| 5 | No word the person would not use in conversation. | Yes. Cut "instrumentation" from the spoken version and said "I measured it for six weeks" |

## The voice gate on the form answers

Run 2026-08-26 over the four answers in `applications/arboreta/form-answers.md`. Eleven rows, all pass. Row 11 needed a fix: the second answer had been wrapped at seventy-two columns in the draft and was rewritten as one paragraph per line before it went in the field.

## The four company questions

- **What do they sell and to whom.** Parametric crop insurance pricing, to insurers and reinsurers.
- **What changed recently.** Series B in March 2026, a warehouse migration under way since July.
- **What does the team look like.** Data platform team of four inside an engineering group of about thirty. The head of data platform, Tomas Lindgren, has been there since 2021 and writes most of the engineering posts.
- **What do people who left say.** Eleven reviews across two sites. Two mention a slow hiring process. Nothing else repeats, and no pattern worth cancelling for.

---

# Post-call, 2026-09-08

Captured the same day, before the result.

**What was asked that was not predicted.** Whether she would consider a contract for the first six months. She said she wanted permanent and asked why the question. Femke said it was standard and dropped it. Worth raising again at the offer.

**What was answered badly.** The question about what she is looking for next. She said "something like what I was doing" and then corrected herself thirty seconds later. The prepared version of that answer did not exist, because the dossier treated motivation as covered by the three selling points and it is not.

**What the objection question extracted.** Femke said the only thing flagged in the review was the table format, and that Tomas had written "she has done the hard version of this problem, the format is a month" on the scorecard. That goes straight into the hiring manager dossier.

**What the high-performer question extracted.** "The people who do well here argue with the model, not just with the pipeline." Re-anchor the selling points for the 2026-09-24 call against that.

**What was learned about them.** They are mid-migration and the posting does not say so. The Iceberg requirement is aspirational for them too.

**New career facts.** None. Nothing came up that is not already in `profile/experience/`.

**Card.** Moved to `process` on 2026-09-18 when the next call was confirmed, with `situation` and `next` rewritten and `fit` untouched.
