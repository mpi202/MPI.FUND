# Critique: Photo candidates for the About hero

The About hero is a dark split layout. The copy takes the left 5 of 12 columns, and the right 7 hold a landscape photo box, about 624×468 at 4:3 on a 1440px screen. The photo has two jobs: show that Marketprog races, and put the mpi.fund name in front of the visitor clearly and on its own. I rendered both new photos in that exact box, at normal and retina resolution, and compared them with the two earlier candidates. Neither new photo beats the first one, `PHOTO-2026-09-22-21-28-18.jpg`. Of the two, `sailboat_back.jpg` is the only one that can work in this slot. `sailboat_side.jpg` doesn't fit the slot at all.

## What's working

`sailboat_side.jpg` is the best sailing photo of the four. The catamaran is flying a hull, with a red foil cutting the water and a clean blue sky, and that sense of speed is exactly the feeling a fund manager would want. `sailboat_back.jpg` is the only new photo where mpi.fund is the sole brand on the sails. Both are worth keeping, just not for this spot.

## sailboat_back.jpg: the lettering reads as a typo

From behind, the jib sits in front of the mainsail, and both sails carry the logo. The two prints overlap into "mpi.funi.fund" on one line and "KETPROG INVESTMEN INVESTMENT" under it. At hero size the lettering is about 180px wide, big enough that every visitor will read the garbled version. A misspelled brand name is worse than a small one, because it looks like a printing mistake on the company's own sail. The "m" is also clipped by the edge of the sail, and a crew member stands in front of "MAR". The ratio isn't the problem. The photo is 3:4, and cropping to 4:3 with `object-[50%_60%]` keeps the lettering, the crew and the hull, and at 1200px wide it stays sharp on retina screens. But two things work against it. The white-on-black "Mobil 1" on the crossbeam is the second most readable text in the frame. And the overcast grey sky and grey-green water give the magenta nothing to stand out against on a near-black page.

## sailboat_side.jpg: the ratio doesn't fit this slot

The file is 738×1600, roughly 1:2.2. A 4:3 box can show only about 35% of its height, and whichever 35% you keep loses what makes the photo good. I tried the crop that keeps the mpi.fund jib, the hull and the foil (`object-[50%_86%]`). It cuts off both sail tips and turns the giant "audax" into a two-letter "au" at the top edge, which looks like a cropping mistake. Resolution is the second problem. 738 source pixels stretched to a 624px box need about 1,250 pixels on a retina screen, so the image is enlarged about 1.7 times. At 2x the letters are visibly soft and edged with sharpening artefacts. The file size matches an iPhone screenshot of a zoomed-in photo rather than the camera original, which would explain the low resolution. Brand-wise it has the same flaw as the regatta shot: this is the audax boat. The yellow "audax" and "Connect to what matters" are larger and brighter than the mpi.fund jib, which shows at about 100px wide.

## Where the four candidates rank

The first photo, `PHOTO-2026-09-22-21-28-18.jpg`, fits best on both counts. It is natively 4:3, so there's no crop. The mpi.fund lettering is about 330px wide, spelled correctly, and the only brand in frame. The magenta and green stand out against a black sail and a blue sky. Its one flaw is the crew sitting in front of "MARKETPROG", and the other photos have worse versions of that problem. Next comes `sailboat_back.jpg`, which fits the ratio but has the doubled lettering. Then `regatta-start.jpg`, the one currently live, which fits after the zoom but gives the hero to audax. Last is `sailboat_side.jpg`, which fits neither the ratio nor the resolution.

## Where I'd start

Put `PHOTO-2026-09-22-21-28-18.jpg` back in the hero. It's a one-line `src` change, and the plain 4:3 box needs no zoom, so the `scale-[1.2]` wrapper can go too. If you want to use the side shot somewhere, get the original camera file rather than this screenshot, and give it a tall slot of its own further down the page. A crop as tight as this hero's isn't the place for it.
