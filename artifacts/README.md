# Artifacts

Two private claude.ai pages built from this site. Only the owner can open them until they are shared from the page's Share menu.

## Mobile preview

https://claude.ai/artifact/WpTGFXGCMf24mQwQgCbaZS

The site from `index.html`, adapted to run on claude.ai so it can be opened on a phone or tablet. claude.ai pages can't reach outside services, so the preview differs from the live site in three ways:

- Firestore reads come from `mobile-preview/snapshot.json` instead of Firebase.
- The office map on the Contact page is a link to Google Maps instead of an embedded map.
- Every device gets the HD hero video, because the 2K file is over claude.ai's 15 MB upload limit.

To rebuild after changing `index.html`:

```sh
python3 artifacts/mobile-preview/fetch_snapshot.py   # optional: refresh the Firestore data
python3 artifacts/mobile-preview/build_preview.py    # writes mpi-fund-preview.html
```

Publish `mpi-fund-preview.html` to the same artifact together with the `img/` files it references.

## mpi.fund on iPhone

https://claude.ai/artifact/MJNhYnvv9X2oFdZ8rHEiJy

Every page in an iPhone 17 frame that scrolls like the device, captured with Playwright's WebKit, the engine inside Safari. To refresh the screenshots, follow the setup notes at the top of `iphone-gallery/capture.js`, then rebuild the page:

```sh
node artifacts/iphone-gallery/capture.js artifacts/iphone-gallery/shots
python3 artifacts/iphone-gallery/build_gallery.py    # writes mpi-fund-on-iphone.html
```

Publish `mpi-fund-on-iphone.html` with the `shots/` folder.
