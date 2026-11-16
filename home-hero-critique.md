# Critique: Home hero with the animated markets background

Reviewed as the live page in Chrome at 390, 768, 1024, 1200, 1280, 1440 and 1920px wide, in English and Hungarian, with each rotating headline word.

Update, 16 November 2026: after this review the HUF and EUR yield curves and their time axis were removed from the hero, which settles the first finding as far as the curves go. The points about the main line, phones and the button still apply.

The hero has one job: tell a stranger in five seconds that this is a regulated Hungarian fund manager, and send them to the funds. The copy does that. The new background makes the hero look far more like a markets firm than the stock night-skyline video did, but it currently behaves like a foreground chart rather than a background, and that is where every problem below comes from.

## What's working

The left-to-right shade is doing real work on desktop: the copy column sits on at least 78% black, so the headline and paragraph read exactly as they did before, and the line is dimmed where it passes under text. Stopping the main line at a "now" dot 86% of the way across, with a dashed level running on to the edge, gives the right side an anchor that balances the left-aligned copy without filling the whole frame. And at 1440×900 the Top Performers row still shows under the fold, so real numbers are one glance away. The hero also no longer downloads a 20 MB video before it looks finished.

## The chart is labelled like data, and it is invented

The upper-right block says HUF and EUR and carries a 3M–1Y–5Y–10Y–30Y axis. That is a specific, checkable claim: it shows a flat forint curve sitting above a rising euro curve, and over about seventy seconds it shows the two converging and drifting apart again. None of it is real; the shapes are generated. Most visitors will take it as decoration, but this site's visitors include people who look at these curves every morning, and for them a labelled curve that is not today's curve is the one thing in the hero that is simply wrong. On a regulated manager's home page, beside an "Explore Funds" button, that is a credibility cost you do not need to pay.

The main line has a milder version of the same problem. It is a random walk, so at any given moment it may be sliding into the "now" dot directly under the words "absolute return." It is doing exactly that in the PNG you exported.

Decide which it is. As texture: remove the HUF and EUR labels and the tenor axis, leaving two anonymous curves, and halve the main line's swing (volatility 0.013 → 0.006) so it undulates instead of plunging. As content: plot the actual ÁKK and euro benchmark yields with an "as of" date, at which point it becomes the most on-brand element on the site. Texture now, real data when the NAV history is wired in.

## On phones the line runs through the buttons

At 390px the hero is almost all text, and the band the main line lives in (50–80% of the hero's height) is exactly where the last line of the paragraph and both buttons sit. The line passes behind "Explore Funds" and straight through the outline of "Personalized Portfolios," and the pulsing dot beats beside the primary button. The phone shade dims it to about a third, which makes it worse: it reads as a murky green wire through the tap targets, not as a chart. Below 768px, move the line into the empty 112px under the buttons (band at 82–97% of the hero height), where the volume bars already are and nothing sits on top of it.

Separately, and not caused by the background: the English headline breaks on phones as "Structured investing / in / absolute return," leaving "in" alone on a line. Balance the wrap so it breaks "Structured / investing in."

## The button is the quietest green thing in the hero

The old hero had three green elements: the eyebrow, the rotating word, and the button. This one has about ten, and the two brightest are decorative — the main line (2px, full-strength green, 12px glow, a pulse that never stops) and the HUF curve. "Explore Funds" is a flat, slightly darker green block 40px tall with a 14px label, on the opposite side of the frame from the only thing that moves. Green used to mean "this matters"; now it means "this is the hero." Take the glow off the main line and drop it to about 60% opacity, and draw the HUF curve in white at 55% like a brighter EUR. The headline word and the button get their accent back and the background becomes a background.

## A choice, not a defect

A scrolling grid, neon line and volume bars are the vocabulary of retail trading apps. The copy sells structure, regulation and "since 2014." The yield curves are the one motif that is specific to what this firm actually does; the volume bars are the least, since bond and absolute-return funds have no volume to show. I would drop the bars and let the curves carry it. You may reasonably prefer the energy.

## Where I'd start

Remove the HUF/EUR labels and the tenor axis. It is one switch in the drawing code, it removes the only thing in the hero that a knowledgeable visitor can call false, and it takes the busiest corner of the frame down a notch at the same time.
