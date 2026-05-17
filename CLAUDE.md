# MPI.Fund Website Redesign — Handoff

## Goal
Redesign the website for **Marketprog Asset Management Zrt.** (mpi.fund), a regulated Hungarian fund manager based in Budapest. The current live site at https://mpi.fund is cluttered and hard to navigate. The goal is a clean, minimal, modern single-page site with interactive charts and real company data.

## Current State
The site is functional as a single HTML file with client-side routing. It uses Tailwind CSS (CDN), Chart.js, and Inter font. No build tools or Node.js required — just open in a browser.

**Design**: White background, black text, green accents. Minimal layout with generous whitespace.

**Pages implemented (6)**:
1. **Home** — Hero section, performance line chart (1Y/3Y/5Y toggle), stats bar, three pillars
2. **About** — Company overview, philosophy/edge, AUM bar chart, board of directors
3. **Investment Funds** — Fund selector tabs with interactive chart + detail panel, grid of all 12 fund families (32 total funds)
4. **Personalized Portfolios** — Interactive risk slider that updates a doughnut chart and allocation bars in real time
5. **Services** — Advisory service cards (investment, wealth/tax, institutional, analytics), CTA
6. **Documents** — Customer info, regulatory publications, FATCA/CRS documents with PDF download buttons
7. **Distribution** — Customer service office, MNB portal link, claims, distribution partners, settlement info, account numbers, T&C

## Files
- `index.html` — The complete website (single file, ~500 lines). This is the only file that matters.
- `HANDOFF.md` — Detailed handoff document with full history
- Desktop copy at `C:\Users\torok\Desktop\mpi-fund.html`
- `src/`, `package.json`, `tsconfig.json`, etc. — Unused Next.js scaffold from initial attempt. Safe to delete.

## What Changed (Version History)
1. **v1**: Next.js project — failed, user has no Node.js
2. **v2**: Single HTML with 5 generic placeholder pages
3. **v3**: Rebuilt with 6 real pages matching live mpi.fund structure
4. **v4 (current)**: Populated with real Marketprog data from web research

## Key Technical Notes
- **No Node.js on this machine** — everything must work as static HTML
- **mpi.fund is a JS-rendered SPA** — WebFetch cannot scrape it, Chrome extension never connected
- **Real data sourced from**: jokamat.hu, hozamplaza.hu, D&B, EMIS, FSMA, LinkedIn
- Fund data current as of May 13, 2026

## What to Do Next
- [ ] Replace illustrative chart data with real NAV history
- [ ] Add real fund ISINs (e.g., HU0000714548 for Bond Derivativ EUR)
- [ ] Fill in actual account numbers on Distribution page
- [ ] Wire up PDF download buttons to actual document URLs
- [ ] Add Hungarian language toggle (live site has HU/EN)
- [ ] Add more team members if provided
- [ ] Consider deploying (Vercel, Netlify, or static hosting)
- [ ] Delete unused Next.js files
