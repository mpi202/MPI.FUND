# MPI.Fund Website Redesign — Handoff V3

**Last updated:** 16 May 2026 (evening session)  
**Primary site file:** `C:\Users\torok\mpi.fund\index.html`  
**GitHub repo:** [github.com/mpi202/MPI.FUND](https://github.com/mpi202/MPI.FUND)  
**Previous handoff:** `C:\Users\torok\OneDrive\CLAUDE\handoff V2.md`

---

## What We Did Today (16 May 2026)

### 1. Refreshed all fund YTD data

Scraped **Hozam Plaza** ([alapkezelok/261/marketprog](https://hozamplaza.hu/alapkezelok/261/marketprog)) and updated every fund card in index.html with current YTD returns (NAV date: 13 May 2026).

Key changes:
- **Fund count:** 30 → **32** (new share classes discovered)
- **Allegro** now has YTD data: HUF +6.39%, EUR +4.41%, USD +4.98% (previously had none)
- **Convexity** now has YTD data: HUF +3.42%, EUR +2.71%, USD +1.66% (previously had none)
- **Bond Derivativ** gained USD share class: +16.14%
- **Diverz Nimbus** gained HUF share class: +3.15%
- **Himalaja** gained EUR share class: -4.21%
- **Prestige** gained EUR share class: +2.29%
- **Prestige Start** gained EUR +8.51%, USD +8.51%
- All other funds had minor decimal precision updates

Updated: stats bar, fund page heading, About section text, JS `FD` array, date stamp.

### 2. Added real regulatory PDFs to Documents tab

Fetched the Firebase Storage bucket (`marketprog-bf7d3.appspot.com`) and found all regulatory document paths. Replaced the 3 placeholder items in Regulatory Publications with **9 real documents** linked to Firebase:

| Document | Firebase path |
|----------|--------------|
| Uzletszabalyzat (Business Rules) | `AssetManager/Uzletszabalyzat_2025_03_28_13_as_verzio.pdf` |
| Dijszabalyzat (Fee Schedule) | `AssetManager/Dijszabalyzat_2025_09_10.pdf` |
| Vegrehajtasi politika (Execution Policy) | `AssetManager/Vegrehajtasi_politika_2024_02_20_14-es verzio_.pdf` |
| Osszeferhetetlensegi politika (Conflict of Interest) | `AssetManager/Osszeferhetetlensegi_politika.pdf` |
| Javadalmazasi Politika (Compensation Policy) | `AssetManager/Javadalmazasi_Politika_Szabalyzata.pdf` |
| Panaszkezelesi Szabalyzat (Complaint Handling Policy) | `AssetManager/Panaszkezelesi_Szabalyzat_2025_03_27_11-es verzio.pdf` |
| Panaszkezelesi Eljarasrend (Complaint Procedure) | `AssetManager/Panaszkezelesi_Eljarasrend_2025_03_27_11-es verzio.pdf` |
| Adatkezelesi tajekoztato (Data Protection) | `AssetManager/Adatkezelesi_tajekoztato_2024_02_16_4-es verzio.pdf` |
| Belso visszaeles bejelentesi szabalyzat (Whistleblower) | `AssetManager/Belso_visszaeles_bejelentesi_szabalyzat_20230724_1-es verzio.pdf` |

### 3. Added FATCA/CRS PDFs

Copied 3 local PDF files from `C:\Users\torok\Pictures\` into `mpi.fund\docs\` and linked them in the FATCA & CRS section:

- `docs/CRS-tajekoztatas.pdf` — CRS Tajekoztatàs
- `docs/FATCA-CRS-fogalomtar-1.pdf` — FATCA/CRS Fogalomtàr I.
- `docs/FATCA-CRS-fogalomtar-2.pdf` — FATCA/CRS Fogalomtàr II.

### 4. Created `/refresh-mpi` skill

Saved at `C:\Users\torok\.claude\commands\refresh-mpi.md`. When invoked, it:
1. Fetches all 32 fund YTDs from Hozam Plaza in one shot
2. Updates the fund grid cards in index.html
3. Updates the JS FD array
4. Updates the date stamp

Includes the full verified ISIN list (32 funds, May 2026).

### 5. Pushed to GitHub

- Initialized git repo at `C:\Users\torok\mpi.fund`
- Remote: `https://github.com/mpi202/MPI.FUND.git`
- Branch: `main`
- Git identity: `olivermink@icloud.com` / `Tamas Torok` (local config only)
- 3 commits pushed:
  1. `8f40eb5` — Initial commit (index.html, chart-preview.html, serve.ps1, README.md)
  2. `d0bc58e` — Add regulatory PDFs and FATCA/CRS documents
  3. `d4a4d06` — Remove chart preview demo

### 6. ODS file test

Extracted data from `C:\Users\torok\OneDrive\CLAUDE\EXCEL test 1.ods` (AUM data 2017-2025, 10M-40M EUR). Built a standalone interactive chart (`chart-preview.html`) with Chart.js slider — worked as a proof of concept, then removed from repo. Data can be integrated into the main site if needed.

---

## Problems We Faced

| Problem | What happened | Status |
|---------|--------------|--------|
| **Preview panel shows wrong page** | Preview kept showing `chart-preview.html` even after deletion. Needed `preview_eval` to navigate to `index.html`. | Workaround: use `preview_eval` to navigate, or refresh |
| **No Python or Node.js** | Machine has neither runtime. Can't use `npx serve` or `python -m http.server`. | Used PowerShell HttpListener in `serve.ps1` |
| **PowerShell server slow** | `preview_screenshot` times out after 30s. Page loads fine but screenshots fail. | Page works, just can't auto-screenshot for verification |
| **Hozam Plaza URL format changed** | Direct ISIN URLs (`/alap/ISIN`) return 404. | Correct format: `/befektetesi-alapok/ISIN/slug` or use overview page `/alapkezelok/261/marketprog` |
| **marketprog.hu Flutter SPA** | WebFetch returns empty HTML shell. `main.dart.js` too large to parse for PDF URLs. | Used Firebase Storage API directly to list bucket contents |
| **Git identity not configured** | First commit failed — no global git config. | Set local repo config with user's email |

---

## Current State

- **Site:** Functional single-page site, all 7 sections populated with real data
- **Funds:** 32 funds, 17 families, fresh YTD from Hozam Plaza (13 May 2026)
- **Documents:** 9 regulatory PDFs (Firebase links) + 3 FATCA/CRS PDFs (local files)
- **Charts:** Still illustrative (random NAV history, not real API data)
- **GitHub:** 3 commits on `main`, pushed to `mpi202/MPI.FUND`
- **Not deployed yet** to Vercel/Netlify

---

## Files

| Path | Purpose |
|------|---------|
| `C:\Users\torok\mpi.fund\index.html` | Main site — edit this |
| `C:\Users\torok\mpi.fund\docs\` | Local FATCA/CRS PDFs (3 files) |
| `C:\Users\torok\mpi.fund\serve.ps1` | PowerShell dev server (port from $env:PORT or 8000) |
| `C:\Users\torok\mpi.fund\README.md` | GitHub readme |
| `C:\Users\torok\.claude\commands\refresh-mpi.md` | `/refresh-mpi` skill for updating fund YTDs |
| `C:\Users\torok\.claude\launch.json` | Preview server config |
| `C:\Users\torok\OneDrive\CLAUDE\handoff V3.md` | **This handoff document** |
| `C:\Users\torok\OneDrive\CLAUDE\handoff V2.md` | Previous handoff |

---

## Goals for Tomorrow

- [ ] **Deploy to Vercel** — connect GitHub repo `mpi202/MPI.FUND`, zero-config static deploy
- [ ] **Replace illustrative charts with real NAV data** — if API or CSV source is available
- [ ] **Add ISINs on fund cards** — the full ISIN list is in the `/refresh-mpi` skill
- [ ] **Wire remaining PDF buttons** — Customer Information section still has placeholder `<button>` tags, not real links
- [ ] **Add Hungarian/English toggle** — live site has HU/EN, ours is English only
- [ ] **Fill Distribution account numbers** — currently says "Contact for details"
- [ ] **Install Node.js or Python** — would fix the preview panel performance issues and enable proper dev server
- [ ] **Clean up unused Next.js files** — `src/`, `package.json`, `tsconfig.json` etc. still on disk (not in git)
- [ ] **Test all regulatory PDF links** — verify Firebase URLs still work and open correctly
- [ ] **Re-run `/refresh-mpi`** — if fresh YTD data is needed

---

## Quick Reference

| Resource | URL |
|----------|-----|
| GitHub repo | https://github.com/mpi202/MPI.FUND |
| Hozam Plaza (Marketprog funds) | https://hozamplaza.hu/alapkezelok/261/marketprog |
| Firebase Storage bucket | `marketprog-bf7d3.appspot.com` |
| Firebase bucket listing | https://firebasestorage.googleapis.com/v0/b/marketprog-bf7d3.appspot.com/o/ |
| marketprog.hu (Flutter SPA) | https://www.marketprog.hu/ |
| mpi.fund (same SPA) | https://mpi.fund/ |
| MNB registry | https://intezmenykereso.mnb.hu/ |
