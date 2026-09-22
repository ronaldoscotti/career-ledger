# voice

Run this gate over any text a person will read as if the person wrote it: a resume, a cover letter, a form answer, a message to a recruiter. It is subtractive, and the only thing it does is remove what is not the person; `profile/voice.md` holds what is.

The reason it matters is the reader. Somebody on the other side has worked through four hundred applications this month, and machine prose is the cheapest thing for that person to reject. A text that sounds assembled gets filtered before anyone weighs what it claims.

## The banned constructions

Each row is a construction to remove on sight. The sample that fails is real output; the repair is the same fact without the tell.

| Construction | Sample that fails | Repaired |
|---|---|---|
| The em dash | `The rollout was slow — three weeks slow.` | `The rollout took three weeks.` |
| `not X, it is Y` | `This was not a side project, it was a product.` | `Four teams ran on it in production.` |
| Label and colon | `Impact: cut the review queue in half.` | `The review queue halved in the first month.` |
| Bridge sentence | `There are three things worth saying about this.` | Delete the sentence and say the three things. |
| Jargon stack | `Passionate about leveraging data at scale.` | `I rebuilt the reporting pipeline that six analysts query daily.` |
| Praise with no measure | `A robust and elegant solution.` | `It has run for two years with no rollback.` |
| Closing restatement | `In short, I bring exactly what you described above.` | Delete the paragraph. The last real sentence is the close. |
| Apologetic hedging | `I know I lack formal experience with your stack, but...` | Delete the clause. Answer the question that was asked. |

The em dash sits at the top because it is the single most reliable tell, and because a person who never typed one has no reason to start now. The bridge sentence and the closing restatement come from the same habit of announcing structure, which a reader experiences as delay. Apologetic hedging is worse than a tell: it hands the reader a reason to stop, and the reader had not asked for one.

Where the text names a weakness at all, it is because the question named it first.

## The length rule

Cut until every sentence carries a fact, a number or a decision. A paragraph that carries none of the three gets deleted, not shortened. Shortening a hollow paragraph produces a shorter hollow paragraph, and the reader still pays to walk past it.

## The pasteable-text rule

Any block the person will paste into a form field, an email client or a message box goes out as one paragraph per line, however long that line runs, with a blank line between paragraphs. Hard wrapping at any column is the failure. A textarea rewraps the text it receives, so a line break in the middle of a paragraph survives into what the reader sees.

On 2026-08-14, a form answer wrapped at eighty columns went into an application textarea and arrived as a ragged column of fragments. The answer was good. It read as broken, and that is the only thing the reader could judge.

This rule is mechanical, and it is not a matter of taste.

## The register rule

A cover letter and a form answer are different objects. A cover letter has an arc and the structure set out in `method/funnel/_refs/cover-letter.md`. A form field is somebody typing.

Write a form answer at a cover letter's standard and it comes out composed, which is the easiest machine tell there is. Half the volume, no opening flourish, no sentence that exists to set up the next one. If it reads as drafted, it failed.

## The self-check table

Every writing stage runs these eleven rows over its own output and reports the table filled in. A skipped row counts as a failure, and so does a row answered from memory instead of from the text.

| # | Check | Yes or no |
|---|---|---|
| 1 | Sentence length varies. No run of three sentences at the same length. | |
| 2 | No banned vocabulary. Nothing from the jargon stack survived. | |
| 3 | Zero em dashes, and zero `not X, it is Y`. | |
| 4 | Every section carries at least one concrete detail: a number, a name or a place. | |
| 5 | A position is taken wherever the subject allows one. | |
| 6 | Nothing ends by summarizing itself. | |
| 7 | No adjective of praise without a measurement beside it. | |
| 8 | Bullet opening verbs vary. | |
| 9 | No paragraph opens with a label and a colon. | |
| 10 | No planning scaffolding survived: no table row name, no heading lifted from a spec, no checklist item. | |
| 11 | Pasteable text has no line break inside a paragraph. | |

Row 10 catches the failure that embarrasses hardest. An outline written to organise the work leaks into the sent text as a heading nobody asked for, or as a bullet whose first word is the name of a column in a planning table.

## What this gate does not do

It does not judge whether the argument is good, whether the claim is true, or whether the angle fits the posting. Those belong to `method/funnel/review.md`, which runs with clean context and reads the text as an adversary. A text can pass all eleven rows here and still be wrong about the company.

<!-- lang:pt-BR -->
## Tells in the person's first language

Instructions in this section stay in English. Only the samples are translated, because a tell is a property of the language it appears in and does not survive translation.

Three failures show up in Portuguese output that the rows above will not catch.

1. **The literal translation of an English construction.** The sentence is grammatical and nobody speaks that way. Fails: `Eu sou apaixonado por resolver problemas complexos.` Repaired: `Passei dois anos consertando a fila de pagamentos, e ela parou de cair.`

2. **The over-long subordinate clause.** Portuguese tolerates a clause that buries the verb, so the sentence arrives with the point at the end and the reader has already stopped. Fails: `Foi nesse contexto que, a partir da necessidade de reduzir o tempo de resposta do serviço, eu decidi reescrever o processamento.` Repaired: `Reescrevi o processamento. O tempo de resposta caiu pela metade.`

3. **The bureaucratic register.** Formal Portuguese has a register that reads as a document filed with an office, and it makes a candidate sound like a form. Fails: `Venho por meio desta manifestar meu interesse na oportunidade em questão.` Repaired: `Quero trabalhar nesse time, e o motivo é o problema que vocês descreveram.`

A fourth habit is worth naming even though it has no clean sample. Portuguese lets a writer soften a claim with a diminutive or a conditional, and a claim softened that way stops being a claim. Write the verb in the past and leave it there.
<!-- /lang -->
