# negotiation

This stage runs from the first time money is mentioned through to a signed offer. That includes the recruiter asking for expectations in the first call, which is the moment most people lose the negotiation without noticing it happened.

## The premise

The company expects a negotiation. The first offer is constructed with room in it, by people who negotiate for a living and do it several times a month.

A person who does not negotiate is a person the company is happy to pay less. Nothing about that is personal and nothing about it is a judgment of the work. It is the shape of the transaction, and the only question is whether the person participates in it.

## Read before saying anything

`profile/PROFILE.md` holds the floor and the target. Read both, and read the definition of the floor carefully, because a floor is where a conversation starts and not a number to announce.

Read the card in `applications/applications.json` for what was already asked. The `comp` field carries the number named earlier in the process, and the number named in a screening three weeks ago may already sit below the floor. Finding that out now is uncomfortable. Finding it out after the counter is sent is worse, because the company has both numbers and the gap between them is the whole conversation.

## Research before speaking, across five sources

Cross all five. One source is an anecdote, and a number backed by one anecdote falls apart the moment somebody asks where it came from.

1. **The posting's published range**, where the posting published one. It is the band, and it is often not the ceiling.
2. **A levels and compensation database**, for the scope rather than the title, since titles mean different things at different companies.
3. **An employee review site**, which is also the source `method/funnel/_refs/reputation.md` reads and blocks automated clients the same way. Ask the person for the paste once and use it for both.
4. **A professional network's salary data**, which skews by who self-reports and is worth having anyway as a check on the others.
5. **The person's own network.** The best of the five by a distance. One conversation with somebody who works there beats every database, and it is the only source that knows what the band actually pays this year.

Record three numbers on the card: the floor, a realistic middle, and a realistic ceiling. Three numbers written down before the conversation are what stop the person doing arithmetic while somebody waits on the line.

## Never the first number

Whoever names a figure first gives up the room between that figure and what the other side was prepared to pay.

Asked for expectations before an offer exists, use the first script in `method/funnel/_refs/scripts.md`. Deflect once. A second deflection reads as evasion and costs more than the anchor would have.

The research is internal. It exists so the person knows whether an offer makes sense while they are hearing it, and announcing it converts a position into a request.

## When to negotiate, and when to think twice

Negotiate when any of these is true:

- The offer sits below the target, at or above the floor.
- The scope described in the process is wider than the scope the posting advertised.
- The research puts comparable roles above the offer, and the sources agree with each other.
- Something other than base is missing: no signing bonus, a standard vacation allocation, no equipment budget.
- Another offer is on the table. This is the strongest position available, and it is the one that needs no argument.

Think twice when:

- The offer already clears the target and the process was fast and respectful.
- The company published a transparent band and the offer sits at the top of it.
- The person has already negotiated twice on the same offer. A third pass reads as a person who will never be finished.
- The gap is small enough that the relationship costs more than the difference.

## The fear of losing the offer

Almost no company withdraws an offer because somebody negotiated. Recruiters negotiate constantly, and a counter is the expected next message rather than a surprise.

What does withdraw an offer is rudeness, arrogance, or an ultimatum delivered before it was true. Polite and reasoned, the worst realistic outcome is that the answer is no and the original offer is still there.

Say this out loud to the person when the hesitation shows up, because the hesitation is what the company is counting on.

## How the message is built

The three-part structure in `method/funnel/_refs/scripts.md` governs every message: thank them specifically, present the data rather than the want, and make one concrete request with a specific number in it. The person substitutes the number. The method carries placeholders and never a rendered figure.

Negotiation happens in writing. Writing gives the person time to think, gives the recruiter something to forward to the person who actually approves it, and leaves a record that both sides can read back.

When it happens on a call anyway, which it will, write down what was said the moment the call ends and confirm it by message the same day. An agreement that exists only in two memories is an agreement that changes shape before the contract arrives.

## What they say back, and what to do with it

| Their response | What it means | What to do |
|---|---|---|
| The counter is accepted | The band had room, and it may still have more | Accept, confirm in writing, stop |
| A number between the offer and the counter | The normal outcome of a reasoned counter | Take it, unless it sits under the floor |
| The base is fixed by a band | Frequently true, and everything around it is usually not | Move to the third script and ask for the signing bonus or the written six-month review |
| The offer is declared final | Sometimes true | Accept the finality, then ask for the cheapest thing left, which is often the title |
| Silence for several days | An approval is moving through somebody else, or it is not | One polite follow-up, then wait. Two follow-ups in a week reads as anxiety |
| A question about other processes | They are measuring urgency | Answer honestly. Never claim an offer that does not exist |
| The offer is below the floor and will not move | The conversation is over and the relationship does not have to be | Use the graceful decline. The market is small and the same people reappear |

## Every message runs the voice gate

`method/voice.md`, over every message sent to the company, with no exception for the short ones.

A negotiation message is the worst possible place to sound like a machine. The reader is assessing judgment while they read it, and courtesy assembled out of templates reads as absence of conviction at exactly the moment the person is asking for money.

## A request below the floor is the person's decision

When the person chooses to ask for a number under their own floor and names the reason, write that number, record the reason on the card beside it, and move on.

They have information the method does not: what they are willing to trade for, how long they want to stay, what the seat opens later. Arguing a decision they have already explained costs the trust that makes the rest of this stage work. Record it and do not reopen it.

## Closing

Update the card through `tools/tracker.py` in the same turn, with the agreed figure in `comp` and the reason beside it when it sits below the floor. Put anything learned about what the market pays into `profile/experience/` under ZERO-B, since it is the input to the next search.

When it closes, stop negotiating. The person says yes, and the stage is over. Continuing to optimise after an acceptance costs goodwill on the first day of the job, which is the most expensive currency available and the hardest to earn back.
