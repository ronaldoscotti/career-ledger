# xyz

Every resume bullet states what was done, how it was measured, and what it produced. A bullet missing the measurement stops being a bullet and turns into a job description, which is the thing every other applicant also submitted.

The shape is one sentence: a verb the person owns, the thing they built or changed, the number that proves it, and the consequence the number had. The order is free. The three parts are not.

| Fails | Works |
|---|---|
| Responsible for the payments integration. | Rebuilt the payments integration and cut failed charges from 9 percent to under 1 percent over four months. |
| Improved database performance. | Added the index behind the slowest report in the admin, taking it from 40 seconds to 300 milliseconds. |
| Worked with product and design on onboarding. | Ran the onboarding rewrite with product and design, moving completion from 31 percent to 52 percent. |

## The measured-number test

A number is measured if it is attested in `profile/experience/locks.md`, or in the period file under `profile/experience/` it came from. That is a lookup and not a judgment. Open the file, find the number, or do not use the number.

Anything else becomes a `[CONFIRM]` marker carrying what the number should be, and it stays a marker until the person closes it. It never becomes an approximation. A tilde does not turn invention into measurement, and neither does "roughly" or "over".

An order of magnitude drawn from a measurement that actually happened is legitimate. If the lock records 4,312 events a day, "thousands of events a day" is the same fact at lower resolution and the person can produce the exact figure when asked. A plausible number nobody ever measured is invention, and the room finds out by asking one question.

## Altitude

Restating a fact at a wider altitude is legitimate. Inflating it is not. The difference is whether the wider word is still true once somebody asks for the detail underneath it.

| Honest | Inflated | What moved |
|---|---|---|
| Owned the migration of one service onto the new queue. | Led the company's move to event-driven architecture. | One service became the whole company. |
| Mentored two engineers through their first on-call rotation. | Built the engineering mentorship program. | A repeated act became an institution. |
| Proposed the retry policy the team adopted. | Designed the platform's resilience strategy. | A decision became a strategy, and a team became a platform. |

Each inflated version survives exactly one question. The honest version survives the whole conversation, and the honest version is also more specific, which is what makes a reader stop.

## The two-how test

Every claim survives two consecutive questions of "how". Ask them out loud while writing the bullet.

Take a bullet claiming failed charges fell by eight points. How? The client stopped failing the charge on the provider's transient errors and retried instead. How did the person know which errors were transient? They read three months of provider responses and grouped them by code.

That claim holds. A claim that thins out on the second question is a claim the person cannot defend in a room, and the room is exactly where it gets asked. Cut it, or go back to `profile/experience/` and find the detail that makes it hold.

## Confidentiality without lying

When the real figure belongs to the person's employer and cannot leave it, the answer is proportion. Dropping the number costs the bullet its measurement. A ratio keeps the measurement and discloses nothing.

The lock records an absolute volume the person may not publish. The bullet reads: cut the queue's failure rate by two thirds and held it there for a year. No absolute figure appears, the claim is still measured, and the person can walk a room through it without breaching anything.

Record the real number in `profile/experience/locks.md` anyway, with a note that it is not publishable. The lock is the person's own file, and the material built from it is where the restriction applies.
