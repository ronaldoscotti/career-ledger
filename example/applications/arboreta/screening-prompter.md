# Screening prompter, Arboreta

2026-09-08, thirty minutes, Femke Boonstra. On screen during the call. No tables here on purpose.

## Opening

### Tell me about yourself

Nine years of data platforms, all of it in Python. The last four and a half at Lomvik, where I owned the event ingestion and the nightly aggregation the whole company read in the morning.

Two things I am known for there. I took the nightly run from just over six hours to just over two. And I found a three percent loss in client events that had been blamed on mobile networks for a year.

I am here because your first two paragraphs describe late-arriving data, and that is the problem I have spent four years on.

### Why Arboreta

Because the data has to be right before anybody prices on it, and the readings arrive late from places with bad connectivity.

At Lomvik the late thing was an order amendment. Here it is a sensor that went quiet for three days. Same shape, harder inputs.

I also want the platform to be the product. I have done the version where it is a service function inside somebody else's roadmap.

## Motivation and fit

### What are you looking for in your next role

A senior data platform seat where I own ingestion end to end, including the pager.

I want to be on the team that owns the numbers rather than the team that answers questions about them. And I want to work somewhere the platform is the thing being sold.

### Why did you leave Lomvik

The platform team was cut from six to two in August. Four of us went, including my manager.

He has agreed to be a reference and I can give you his details now.

### Tell me about the gap in 2021

I left Merivo Health in May 2021 after a project that did not work out. My mother was ill that summer and I was at home.

From October I did two days a week for a museum group in Kraków, cleaning up ten years of ticketing exports. I came back full time in January 2022.

## The technical questions

### Have you worked with Iceberg

I have not run it in production.

I read your July post about the migration. The first thing I would want to know is how you are handling schema evolution on the sensor tables during the cutover, because that is where I would expect late readings to break.

The closest thing I have done is a warehouse migration at Lomvik in 2023 where we ran both sides for five months.

### Tell me about a pipeline you fixed

The nightly aggregation at Lomvik finished at ten past eleven in the morning. The retention team met at nine, so Monday decisions ran on Friday's numbers.

I measured it for six weeks before I changed anything. One task was seventy percent of the runtime, because it rebuilt the entire order history every night. I checked how late amendments actually arrive: ninety-nine point four percent inside nine days.

I moved it to an incremental merge on a fourteen-day window with a full rebuild once a month. It runs in just over two hours now and it finishes before five in the morning. Failures went from nine a month to one over the next six months.

### Tell me about something that went wrong

At Merivo I built a streaming reporting platform when a nightly batch would have done the job.

I designed for a roadmap that promised real-time dashboards in two quarters. They never came. Bookings could be amended after the fact, so my aggregate and the booking service disagreed whenever an amendment landed out of order, and the clinical operations lead had to reissue eleven of forty-one weekly reports.

I knew at month six and I said so at month fourteen. Now the first question I ask about any design is who is asking for this in the next quarter, and I ask the person who would be asking.

## Logistics

### What are your compensation expectations

A hundred and twenty thousand euros base.

### When could you start

Now. I have been available since the end of August.

### Where are you based and do you need sponsorship

Kraków. Polish citizen, so no sponsorship anywhere in the European Union. Your hours are my hours.

## My questions

### The objection

Having read my application and talked to me, is there anything in my background that gives you pause?

### The bar

What separates somebody excellent in this seat from somebody who is just doing the job well?

### The process

What are the remaining stages, and who runs each one?
