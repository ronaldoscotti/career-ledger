# ats

A parser opens the file, pulls a single stream of text out of it, and throws the layout away. It then walks that stream looking for shapes it knows: a name, contact details, headings it recognises, dates, employers, and blocks of skill words. Anything it cannot place is dropped, or filed under whichever heading it happened to land beneath. Every rule below exists to keep that stream in the order a human would read it.

## The eight common failures

| Failure | The rule | What it costs |
|---|---|---|
| Multi-column layout | One column, top to bottom. | The parser reads straight across and interleaves two jobs into one unreadable entry. |
| A table used for layout | No tables. Headings and bullets carry the structure. | Cells arrive in storage order, so dates detach from the roles they belong to. |
| Text inside an image or a logo | No text in images. Delete decorative logos. | That text is absent from the stream. A skill shown only in a graphic is invisible to every search for it. |
| Contact details in the page header or footer | Contact details in the body, in the first block. | Many parsers skip the header and footer outright, and the application lands with no way to reply to it. |
| A non-standard bullet glyph | A plain round bullet or a hyphen. | Exotic glyphs extract as a stray character or as nothing, and the bullets run together into one paragraph. |
| A font with letter-spacing applied | No tracking, no letter-spacing, anywhere. | Spacing is inserted between letters in the extracted text, turning the word into a string no keyword search will match. |
| A heading style rendering as small caps | Type the heading in the case it should have and apply no transform. | Small caps extract inconsistently, and the section heading stops being recognised as a heading. |
| A file format other than the one requested | When the posting asks for a document in the portable format, send that, named plainly. | Some systems reject the upload without telling anyone, and some accept it and index nothing. |

## The header

Name on the first line. One line of contact details beneath it, with the e-mail, the phone and the location the posting cares about. Links written out as plain text, because a parser keeps the text and discards the anchor behind a word.

Nothing else belongs there. No photo, no date of birth, no marital status, no decorative rule. Each of them costs space at the top of the page, which is the most expensive space in the document.

## Over the page budget

Cut in this order, and do not reorder it.

1. Cut content that does not serve this posting. A role from twelve years ago, a bullet about a system nobody asked about, a skill block listing everything ever touched.
2. Merge related bullets. Two lines about the same project usually become one stronger line with both numbers in it.
3. Only then compress the layout. Margins, leading, type size.

Compressing first keeps the dead weight on the page and shrinks the type around it, so the document ends up harder to read and no shorter in substance. The person then has to cut anyway, and now the layout has to be undone too.

## What the build already checks

`tools/build/` reports the page count, any em dash that survived, three of the parser rules above and the keyword coverage against the posting. Run it rather than eyeballing the output, and read the report before sending anything.

It cannot see whether a bullet is a disguised job description, whether the section headings mean anything to a human reader, or whether the cut kept the content this posting was actually asking for. Those go through `method/funnel/_refs/xyz.md` and through a person.
