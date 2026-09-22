# sources

Organised by what an agent can actually open. That is the distinction that decides how a sourcing run is spent, and it is the one nobody writes down, so every run rediscovers it by wasting forty minutes on a login wall.

## Tier one, open directly

- **Company career pages.** The highest signal-to-noise of anything here. An opening appears here first and is often gone from the boards by the time it spreads.
- **Applicant tracking systems with public listings.** Greenhouse, Lever and Ashby host boards that are readable without a session. Many of them expose a search across every company using them, which is the cheapest volume available.
- **A boolean query on a general web search engine.** Slower per result, but it reaches postings the aggregators missed and pages the boards never indexed.
- **Public job boards without a login wall.** Niche boards for a specialism, remote-only boards, boards run by a community. Read what `profile/PROFILE.md` declares about the target market before picking which ones are worth the pass.

## Tier two, blocked

Several of the highest-value sources return an error or demand a session for an automated client. The method does not guess what is behind them and does not come back empty. It hands the person a ready-made request naming the exact filter and the exact thing to paste back. After the paste, the filtering and the ranking are the agent's work again.

**The job search on LinkedIn.** Blocked outright for an automated client. The path the person follows is `Jobs`, then `All filters`, then `Date posted` set to `Past week`, then `Sort by` set to `Most recent`. Quote those labels exactly, because a filter described in other words is a filter the person hunts for and then skips.

Send this, one paragraph per line:

```
Run this search with the filters below, then paste the first page back.
Keywords: the boolean string above. Location and work arrangement: what
your profile file declares. Date posted: past week. Sort by: most recent.
Copy four fields per row, title, company, location and link. One page is
enough. Thirty rows rank fine and a hundred rows do not get pasted.
```

**The reviews and salary site.** Blocked, and it is also where `method/funnel/_refs/reputation.md` needs its data. Handle it there rather than twice.

**Any board that requires an account to see the listing.** Same shape. Name the filters, name the four fields to copy, ask for one page and not ten. A paste of thirty rows is enough to rank, and asking for more means it does not get done.

Write the request as one paragraph per line, with no hard wrap, because the person is going to read it out of a terminal or paste it into a note. See the pasteable-text rule in `method/voice.md`.

## Tier three, the watchlist

The career pages of the specific companies the person follows, checked on a schedule. This is where an opening appears before it reaches any board, sometimes by a week, and a week is most of the pipeline.

Keep the list in `profile/PROFILE.md`. When a triage returns a strong verdict on a company with nothing open, the company goes on the watchlist rather than into the discard pile.

## The boolean templates

Assembled by `tools/scan.py`, parameterised on `profile/PROFILE.md`. Every term comes from the profile: the titles the person is targeting, the seniority band, the work arrangement, the eligible geographies. Nothing is hard-coded to a stack, because a template with a stack in it is a template that belongs to one person and expires when they learn something new.

Build title variants rather than a single title. The same seat is advertised under three or four names depending on who wrote the posting, and a search matching only one of them silently drops most of the market.

## What this method leaves out, deliberately

- **Scraping anything behind a login.** It breaks, it gets the account restricted, and the person loses the source permanently. The paste-back request costs two minutes and keeps the source.
- **Recruiter inbound as a channel to optimise.** It arrives on its own schedule and cannot be run as a stage. `method/funnel/triage.md` handles whatever shows up.
- **Aggregators that republish without linking to the original posting.** The posting text is what triage reads, and a republished summary is a different document with the requirements sanded off.

Somebody rediscovers each of these about once a quarter. The reasons are written here so the rediscovery costs a paragraph instead of a week.
