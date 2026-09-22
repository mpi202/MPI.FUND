# Critique: Expanded fund card (Investment Funds page)

The expanded card is where a prospective investor decides whether a fund deserves a closer look. It has to answer what the fund does, how it has performed and where the documents are. On a regulated fund manager's site it should read as calm and precise. The new layout gets the big structure right: one wide chart, then three quiet folded sections. But the rows above the chart repeat themselves, the date axis can be misread, and the type sizes are too close together for the fund's name to lead.

## What's working

Giving the open fund the whole row was the right call. At over 1,000px wide, the 1Y series reads as a real price history instead of a thumbnail. With all three sections folded, they take up one slim strip, so the chart owns the card. The left edge is disciplined too. The type badge, description, meta line, series pills and all three section labels start on the same line, and that shared edge is most of why the card feels orderly.

## The date axis reads backwards

The 1Y axis reads "May 25, Jul 15, Sep 15 … Mar 15, May 15". The first label means May 2025, but every other label means the 15th of a month. So the axis seems to start and end in May of the same year, and "May 25" looks later than "May 15". On a performance chart, that misreads the one thing the chart exists to show. The labels come straight from the data arrays in `FUND_NAV` (`'May 25','Jun 3','Jun 17',…`), which mix a two-digit year with a day of the month. Use one format everywhere: "Jun '25 … May '26" for 1Y and 3Y, and "2021 … 2026" for 5Y. The illustrative charts (Allegro and the others) already use `Jan '23`, so this also makes the two kinds of chart look the same.

## The rows above the chart say everything twice

Four rows sit between the card header and the chart, and two of them repeat what's already on screen. The centred "□ I Series" legend restates the green I Series pill about 50px above it. Its hollow green square also looks like an unticked checkbox. It costs roughly 30px of height and adds nothing.

The meta line reads "HUF · EUR · USD   HUF +10.5% · EUR +4.4% · USD +16.6%". The figures repeat the currency list in front of them, and they have no label. Nothing on the card says they are year-to-date; the only explanation is the disclaimer at the bottom of the page. Turn the legend off for fund charts (`plugins: {legend: {display: false}}`). Replace the meta line with one labelled row: "YTD" in 12px neutral-400, then each currency with its return, with 16px between the pairs.

The description needs the same treatment. At 12px in neutral-500, it runs as one line of over 1,000px, far past a comfortable reading width. Set it to 14px in neutral-600 with `max-width: 65ch`.

## The fund name doesn't lead

Once the card opens, it's the focus of the page. But the fund name stays at 14px semibold, the same size as on a closed card. The section labels below it are 12px bold uppercase with wide letter-spacing. At that weight, "FACTS AND REGULATORY DOCUMENTS" pulls as hard as "Marketprog Bond Derivativ".

The card uses five type sizes between 9px and 14px: 9px for the badge, 10px for the controls and axis ticks, 11px for the legend and fund details, 12px for the description and section labels, and 14px for the title and return. Those steps are too small to read as hierarchy. They read as accidents. On an open card, take the title and return to 18px. Drop the section labels to 11px semibold in neutral-500; they help people find their way, they aren't headlines. Keep them uppercase. Put everything else at 12px, and move the badge up from 9px to 10px.

## Two toggles, two visual styles

The series choice is a fully rounded green pill. The period choice, on the same row, is a black square with 4px corners. Both do the same job (pick one option from a set), so the different styling suggests they behave differently.

Green is also doing too many jobs on this card. It marks a positive return, the brand, the selected state and the star, and on an open card it colours the report-year links too. Give both toggles one segmented style: 28px tall, 6px corner radius, black when selected. Keep green for performance and brand. Make the report years neutral-800 links that turn green on hover.

## The tinted column reads as a selected tab

With all three sections closed, only Monthly reports has a green-tinted background. The row looks like a tab bar with Monthly reports selected, but nothing is selected. Give all three the same background. If you want the tint, put it on whichever section is open.

## When open, the documents column truncates labels and leaves gaps

When you open Facts and regulatory documents, the three documents appear as 120px tiles, each with a large generic PDF icon and a two-line label. The labels get cut off ("Rule Book and information in.."), because the column is too narrow for tiles. With Fund details open next to it, the documents column also ends about 200px higher than its neighbour, leaving a gap.

Show the documents as list rows in the same style as the monthly reports: a 14px PDF icon, the full title in 13px, and a download arrow on the right. No title gets truncated, the column is about half as tall, and all three sections share one visual style.

## Where I'd start

Delete the chart legend and turn the meta line into a labelled YTD row. It's about ten lines of code. It removes the two repeats a first-time visitor notices right away, and it frees up roughly 40px above the chart. Fix the axis labels next. That takes longer because every label array has to change, but it's the only problem here that makes the chart show something untrue.
