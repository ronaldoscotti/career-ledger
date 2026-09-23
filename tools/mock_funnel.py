#!/usr/bin/env python3
"""Builds a realistically shaped funnel for the README screenshot.

Thirty applications and seventy-odd triage lines, because the ratio is the
point: most of a search is deciding not to apply. Every company is invented.
"""
import json
import random
from datetime import date, timedelta

random.seed(1729)

APPS = [
    # (company, site, role, status, level, comp, fit, situation, next)
    ("Arboreta", "arboreta.io", "Senior Data Platform Engineer", "offer", "strong",
     "EUR 118k base, offered", "Read 02/09. Glove fit. Event ingestion at their volume is the exact problem she solved twice.",
     "Offer in writing, counter sent 19/09.", "Their answer by 24/09."),
    ("Solvenn", "solvenn.com", "Staff Backend Engineer", "process", "strong",
     "EUR 105-125k published", "Read 28/08. Strong. Pipelines that must finish before the morning, which is her sentence.",
     "Passed the technical. System design on 25/09.", "Prep the design stage."),
    ("Kestrel Data", "kesdata.dev", "Platform Engineer", "process", "good",
     "GBP 90-110k published", "Read 01/09. Good. Smaller team, wider surface, less depth on the ingestion side.",
     "Hiring manager call done. Take-home received 20/09.", "Take-home due 27/09."),
    ("Brannock Labs", "brannock.dev", "Senior Software Engineer, Data", "process", "good",
     "EUR 95-115k published", "Read 05/09. Good. Batch-heavy, which is the half of her work she shows less.",
     "Two stages done. Founder call pending.", "Chase the scheduler on 23/09."),
    ("Nodefall", "nodefall.io", "Data Infrastructure Engineer", "process", "stretch",
     "USD 130-160k, band unclear outside the US", "Read 08/09. Stretch. Bigger scale than she has run, and they say so in the posting.",
     "Recruiter screen passed. Technical on 26/09.", "Confirm the format with the recruiter."),
    ("Hollowmere", "hollowmere.co", "Senior Engineer, Ingestion", "sent", "strong",
     "EUR 110k asked", "Read 12/09. Strong. The posting describes her Lomvik work almost line for line.",
     "Applied 15/09 with a tailored resume and a letter.", "Follow up 25/09 if silent."),
    ("Vantable", "vantable.com", "Backend Engineer, Data Products", "sent", "good",
     "EUR 100k asked", "Read 11/09. Good. Product-facing, less infrastructure than she wants.",
     "Applied 14/09.", "Follow up 24/09."),
    ("Puliza", "puliza.eu", "Senior Platform Engineer", "sent", "good",
     "EUR 98-112k published", "Read 13/09. Good. Strong on-call culture, worth asking about early.",
     "Applied 16/09.", "Follow up 26/09."),
    ("Draycott Systems", "draycott.io", "Staff Engineer, Data", "sent", "strong",
     "EUR 120k asked", "Read 14/09. Strong. They name the exact failure mode she fixed at Lomvik.",
     "Applied 17/09 through a referral.", "The referral pings them on 23/09."),
    ("Merrowfield", "merrowfield.com", "Senior Data Engineer", "sent", "good",
     "EUR 95-110k published", "Read 15/09. Good. Consultancy shape, several clients at once.",
     "Applied 18/09.", "Follow up 28/09."),
    ("Ostrer", "ostrer.dev", "Backend Engineer", "sent", "stretch",
     "EUR 90-105k published", "Read 16/09. Stretch. Band starts below the floor, kept for the product.",
     "Applied 18/09 with the floor stated.", "Follow up 30/09."),
    ("Calderwood", "calderwood.io", "Senior Engineer, Reliability", "sent", "stretch",
     "EUR 92k published", "Read 17/09. Stretch. Reliability rather than data, adjacent and defensible.",
     "Applied 19/09.", "Follow up 29/09."),
    ("Tulvane", "tulvane.co", "Data Platform Lead", "sent", "good",
     "EUR 115k asked", "Read 18/09. Good, with framing friction. Lead in the title, builder in the body.",
     "Applied 20/09, resume ordered to lead with what she builds.", "Follow up 30/09."),
    ("Lindquist Health", "lindquist.health", "Senior Backend Engineer", "limbo", "good",
     "EUR 100-118k published", "Read 20/08. Good. Health data, which she has done once and not loved.",
     "Applied 22/08. Silence past the stated two weeks.", "One more follow-up, then close it."),
    ("Ferrowyn", "ferrowyn.com", "Platform Engineer, Pipelines", "limbo", "good",
     "EUR 105k asked", "Read 18/08. Good. Small team, clear ownership.",
     "Applied 21/08. Two follow-ups, no answer.", "Close it on 26/09."),
    ("Ashgrove Retail", "ashgrove.shop", "Senior Data Engineer", "limbo", "stretch",
     "EUR 88-104k published", "Read 25/08. Stretch. Band opens under the floor.",
     "Applied 27/08. Recruiter went quiet after one exchange.", "Close it."),
    ("Wrenholt", "wrenholt.io", "Backend Engineer, Platform", "limbo", "good",
     "EUR 97k published", "Read 29/08. Good. Reasonable fit, nothing exceptional either way.",
     "Applied 01/09. Nothing since the automated receipt.", "Follow up once on 24/09."),
    ("Pelagic Labs", "pelagiclabs.com", "Senior Engineer, Data", "ready", "strong",
     "EUR 112-130k published", "Read 21/09. Strong. Streaming ingestion, and their engineering posts are specific.",
     "Resume derived and reviewed. Not sent.", "Send by 23/09."),
    ("Tamsin Analytics", "tamsin.io", "Staff Data Engineer", "ready", "good",
     "EUR 108k published", "Read 21/09. Good. Analytics rather than platform, adjacent.",
     "Triaged. Material not written.", "Write the resume."),
    ("Groveport", "groveport.dev", "Senior Platform Engineer", "ready", "stretch",
     "Not published", "Read 22/09. Stretch. No band published, which is a question for the screen.",
     "Triaged. Material not written.", "Ask the recruiter for the band first."),
    ("Bexley Freight", "bexleyfreight.com", "Data Engineer", "rejected", "good",
     "EUR 95k published", "Read 04/08. Good. Logistics telematics, which she has actually done.",
     "Rejected 12/08, no interview, no reason given.", "Nothing. Interval before reapplying."),
    ("Novara Systems", "novarasys.io", "Senior Backend Engineer", "rejected", "good",
     "EUR 100-115k published", "Read 06/08. Good. Generic backend, her stack.",
     "Rejected 14/08 at the automated screen.", "Nothing."),
    ("Halvard", "halvard.co", "Platform Engineer", "rejected", "stretch",
     "EUR 90k published", "Read 09/08. Stretch. Below the floor and she knew it.",
     "Rejected 15/08.", "Nothing."),
    ("Quill & Rowe", "quillrowe.com", "Senior Data Engineer", "rejected", "good",
     "GBP 85-100k published", "Read 11/08. Good. Publishing, interesting domain.",
     "Rejected 20/08, position filled internally.", "Nothing."),
    ("Standfast", "standfast.dev", "Backend Engineer, Data", "rejected", "stretch",
     "EUR 92-108k published", "Read 13/08. Stretch. Vague posting, lots of everything.",
     "Rejected 21/08.", "Nothing."),
    ("Threnody Media", "threnody.media", "Senior Engineer", "failed", "good",
     "EUR 102k published", "Read 22/07. Good. Media pipelines at real volume.",
     "Reached the system design stage and did not pass. Feedback said the design was sound and the trade-offs went unstated.",
     "Nothing. The feedback went into the bank."),
    ("Corrance", "corrance.io", "Staff Engineer, Platform", "failed", "strong",
     "EUR 125k published", "Read 28/07. Strong on paper. The best-paying posting of the batch.",
     "Four stages, then no. They hired someone with more time at scale.",
     "Nothing. Their objection answer reshaped the next two preps."),
    ("Ivelet", "ivelet.com", "Senior Backend Engineer", "failed", "good",
     "EUR 98-112k published", "Read 02/08. Good. Fintech, tight on-call.",
     "Failed the behavioral stage. Conflict story did not hold up under follow-ups.",
     "Nothing. That story got rewritten."),
    ("Marchmont", "marchmont.co", "Data Platform Engineer", "paused", "good",
     "EUR 104k published", "Read 19/08. Good. Solid team, slow process by their own admission.",
     "She paused it herself while the offer conversation runs.", "Revisit after 24/09."),
    ("Sidderly", "sidderly.io", "Senior Engineer, Ingestion", "withdrew", "good",
     "EUR 100k published", "Read 15/08. Good. Ingestion work, right shape.",
     "Withdrew after the second stage. Convergent pattern in the reviews about leadership turnover.",
     "Nothing."),
]

TRIAGE_REASONS = [
    ("US-only, no employer of record", 14),
    ("management seat, not a builder seat", 9),
    ("below the declared floor with nothing else on offer", 11),
    ("onsite required", 7),
    ("advertisement older than the declared limit", 8),
    ("seniority below the target band", 6),
    ("excluded domain", 3),
    ("no overlap with the working hours declared in the profile", 5),
    ("rejected there recently, interval not elapsed", 2),
    ("contract through an intermediary at a rate that does not clear the floor", 4),
]
TRIAGE_COMPANIES = [
    "Ravenscroft", "Beltane Group", "Corvid Logistics", "Ashmount", "Pellworth",
    "Tindall", "Verrick", "Oakhanger", "Dunmore Health", "Swanscombe",
    "Fenwick Rail", "Harroway", "Lyddington", "Marrick", "Norbury Tech",
    "Oldbury", "Penhale", "Quarrendon", "Rossington", "Scaldwell",
    "Tattershall", "Uffington", "Vexley", "Wadborough", "Yarnton",
    "Zennor", "Ablington", "Bramshill", "Cropredy", "Dinnington",
    "Everleigh", "Fordington", "Garsington", "Hanbury", "Ickleton",
    "Jevington", "Kilnwick", "Langrish", "Mickleover", "Newnham",
    "Ossington", "Padworth", "Quenington", "Rampisham", "Sturminster",
    "Thrupp", "Ulceby", "Vernham", "Wootton", "Yardley",
    "Alconbury", "Bishopstone", "Chettisham", "Doddington", "Elmswell",
    "Fingringhoe", "Gedling", "Hollesley", "Ingoldsby", "Kelvedon",
    "Lavenham", "Mundford", "Nayland", "Orwell", "Papworth",
    "Ridlington", "Snettisham", "Thelnetham", "Wickhambrook",
]
ROLES = [
    "Senior Backend Engineer", "Data Engineer", "Platform Engineer",
    "Staff Software Engineer", "Engineering Manager", "Senior Data Engineer",
    "Backend Engineer", "Site Reliability Engineer", "Head of Platform",
    "Software Engineer II", "Principal Engineer", "Data Platform Lead",
]

FIELDS = ["id", "company", "site", "role", "status", "level", "triaged_on",
          "sent_on", "moved_on", "comp", "resume", "fit", "situation", "next", "files"]


def slug(name):
    return name.lower().replace(" ", "-").replace("&", "and").replace(".", "")


def build():
    today = date(2026, 9, 22)
    apps = []
    for i, (company, site, role, status, level, comp, fit, situation, nxt) in enumerate(APPS):
        triaged = today - timedelta(days=random.randint(2, 62))
        sent = "" if status == "ready" else (triaged + timedelta(days=random.randint(1, 5))).isoformat()
        moved = today - timedelta(days=random.randint(0, 20))
        if sent and moved.isoformat() < sent:
            moved = date.fromisoformat(sent) + timedelta(days=2)
        files = {}
        if status != "ready" or company == "Pelagic Labs":
            files = {"resume md": f"applications/{slug(company)}/resume.md",
                     "resume pdf": f"applications/{slug(company)}/resume.pdf"}
            if status in ("process", "offer", "failed"):
                files["screening dossier"] = f"applications/{slug(company)}/screening-dossier.md"
        apps.append(dict(zip(FIELDS, [
            slug(company), company, site, role, status, level,
            triaged.isoformat(), sent, moved.isoformat(), comp,
            "resume", fit, situation, nxt, files])))

    triage, used = [], set()
    pool = TRIAGE_COMPANIES[:]
    random.shuffle(pool)
    reasons = [r for r, n in TRIAGE_REASONS for _ in range(n)]
    random.shuffle(reasons)
    for company, reason in zip(pool, reasons):
        if company in used:
            continue
        used.add(company)
        triage.append({"company": company, "role": random.choice(ROLES),
                       "reason": reason,
                       "date": (today - timedelta(days=random.randint(1, 70))).isoformat()})
    triage.sort(key=lambda t: t["date"], reverse=True)
    return {"updated": today.isoformat(), "applications": apps, "triage": triage}


if __name__ == "__main__":
    data = build()
    print(json.dumps(data, ensure_ascii=False, indent=2))
