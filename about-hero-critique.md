# Critique: About page hero (sail photo)

The About hero introduces Marketprog as a credible, regulated manager, and with the new photo it also shows off the mpi.fund sail sponsorship. The photo is the brand moment here: the company's own wordmark, in its own colors, on a racing boat. The current layout doesn't work because it treats a photo whose subject is lettering as a background texture. The page text sits on the sail text, the crop removes the boat, and the overlay dulls the brand colors.

## What's working

The photo is a much stronger choice than the office video. A magenta "mpi.fund" and green signal bars on a black sail are recognisably this company, and no stock footage can say that. The copy block itself (label, one heading, one paragraph, one button) is suitably restrained for a regulated firm.

## The page text is printed on top of the sail's text

At 1440px wide the text column runs from about x=168 to x=835. That covers all of "mpi." and the "f" of "fund". The 16px description sits right across the magenta letters, and the MNB Registry button covers "MARK" in "MARKETPROG INVESTMENT". Two blocks of text fight over the same space and neither wins. The eye lands on the white heading, gets pulled into the big magenta "fund", then has to read the paragraph through the letters behind it. A background photo only works when the area behind the text is empty, and here that area is the subject of the photo. No amount of overlay or repositioning fixes that. Take the text off the photo: put the photo in its own column and the copy on white next to it.

## The 3:1 crop removes the boat

The hero is `min-h-[55vh]`. On a 900px-tall screen that is about 1440×495, roughly 2.9:1, but the photo is 4:3. `object-cover` scales it to 1440×1080 and throws away about 585px. That loses the top of the sail and all of the hull, trampoline and crew's seat, which is the bottom quarter of the frame. What's left is a black wall with letters on it, and nothing says "sailboat". Because the height depends on the viewport, the crop also changes from screen to screen and gets worse on shorter laptop screens. Give the photo a fixed box at its native ratio, `aspect-[4/3]` with width and height set to 1600×1200. Then nothing is cropped at any width, and the sail, the wordmark, the crew and the hull all stay in frame.

## The dark gradient mutes the brand colors

`from-black/75 via-black/40 to-black/20` over an already black sail turns the magenta into a dull mauve and the green bars into olive, the two colors that make the photo worth using. The overlay was only there to keep the white text readable. Once the text leaves the photo it has no purpose, so remove it completely.

## Breaking from the video heroes is the right trade

This is a design choice rather than a defect. Home and Distribution use full-bleed video with white text on top, so a split About hero will stand out. That's fine: city and parliament footage has no content of its own where the text sits, so it can take an overlay, and this photo can't. Services and Documents already use a light header with dark text on white, so the split hero fits the site's existing styles and doesn't add a new one.

## Where I'd start

Replace the full-bleed section with a two-column hero. The copy takes 5 of 12 columns: label in `text-accent-600`, a black H1, description in `text-neutral-500`, exactly like the Services header. The photo takes the other 7 at `aspect-[4/3]` with `rounded-xl` and no overlay. At 1440px that makes the photo about 624×468, big enough to read "MARKETPROG INVESTMENT" and see the hull, and the whole hero still fits above the fold. On phones the columns stack with the text first and the full-width photo below it.
