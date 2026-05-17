# MPI.Fund Website Redesign — Handoff

**Last updated:** 16 May 2026  
**Primary site file:** `C:\Users\torok\mpi.fund\index.html` (~620 lines)  
**Live reference:** [marketprog.hu](https://www.marketprog.hu/) / [mpi.fund](https://mpi.fund) (same Flutter SPA)

---

## Goals

1. **Redesign** the public site for **MARKETPROG Asset Management Zrt.** (Budapest) — cleaner, minimal, easier to navigate than the current SPA.
2. **Single-page mockup** with client-side routing (hash navigation): Home, About, Investment Funds, Personalized Portfolios, Services, Documents, Distribution.
3. **Real company data** — fund names, counts, leadership, contact, and performance figures sourced from official/live references, not placeholders.
4. **No build step required** for viewing: one HTML file + CDN (Tailwind, Chart.js, Inter). User preferred this over Next.js.
5. **Preserve design** — white/black/green, Inter font, generous whitespace; content updates only unless user asks for layout changes.

---

## Improvements We Made

### Version history

| Version | What changed |
|--------|----------------|
| **v1** | Next.js scaffold (`src/`, `package.json`) — abandoned (no Node.js on user machine for daily use). |
| **v2** | Single `index.html`, 5 generic pages. |
| **v3** | Rebuilt to match real mpi.fund section structure (6 content areas + nav). |
| **v4** | First pass of real data: fund names, illustrative performance, 2 team members, basic contact. |
| **v5 (current)** | Data sync from **marketprog.hu** app bundle + **Hozam Plaza** YTD (May 2026). See [New Data Fetched](#new-data-fetched). |

### v5 content and UX updates (May 2026)

- **Stats bar:** 30 investment funds, 17 fund families, 3 currencies, MNB / AIFMD.
- **About:** AIFMD service list; "30 funds in 17 families" copy.
- **Leadership (3):** Varkonyi Istvan (CEO), Alexandra Mikecz (COO), Tamas Torok (CIO) — titles aligned with live app.
- **Fund grid:** 17 families with category tags and YTD where available (Hozam Plaza, 13 May 2026).
- **Fund detail tabs (JS):** Allegro, Bond Derivativ, Aurica, Diverz Nimbus — panel shows real YTD for Bond/Aurica/Diverz Nimbus.
- **Distribution:** Csorsz utca 45, MOM Irodapark SAS Tower 5th floor, phone/fax, info@marketproginvestment.com, hours 8:00-16:00, settlement T+3.
- **Services:** Copy aligned with AIFMD offering.
- **Local preview:** http://localhost:3456 via Node static server; Desktop copy at `C:\Users\torok\Desktop\mpi-fund.html`.

### Environment / tooling

- User connected **Claude Code** in Cursor (terminal + optional extension).
- **HANDOFF.md** — prefer local copy (see Files below); OneDrive path can fail to open in editor.

---

## Challenges We Faced

| Challenge | What happened | Workaround |
|-----------|---------------|------------|
| **Next.js** | User wanted instant preview without Node for the app. | Dropped Next; kept only `index.html`. |
| **marketprog.hu / mpi.fund is a Flutter SPA** | WebFetch returns empty shell only. | Parsed `main.dart.js` for fund slugs, copy, team, contact, ISIN map. |
| **marketprog.eu** | Subpages 404. | Used marketprog.hu + Hozam Plaza + MBH Bank instead. |
| **Hozam Plaza incomplete coverage** | Some ISINs have no fund page. | YTD only where Hozam had listings; currencies only elsewhere. |
| **Cursor Read vs disk sync** | IDE sometimes showed older index.html. | Patch `C:\Users\torok\mpi.fund\index.html` directly. |
| **OneDrive HANDOFF.md** | File has ReparsePoint attribute; Cursor "cannot open - unexpected error". | Use `C:\Users\torok\mpi.fund\HANDOFF.md` instead. |
| **Chrome / Claude in Chrome** | Browser automation never connected. | Used static JS bundle + Hozam Plaza instead. |

---

## New Data Fetched

### Sources

1. [marketprog.hu](https://www.marketprog.hu/) — `main.dart.js` (Flutter build, May 2026).
2. [Hozam Plaza](https://hozamplaza.hu/) — fund pages by ISIN (YTD, May 2026).
3. [MBH Bank — Marketprog funds](https://mbhbank.hu/lakossagi/maganszemelyek/marketprog-befektetesi-alapok)
4. Web search — MNB regulation, company registration 2014, Primus Wealth group.

### Fund inventory (from live app)

- **30** investment fund share classes (ISINs in app).
- **17** fund families: Allegro Absolute, Aurica, Bond Derivativ, Compass, Convexity, Creditum, Diverz Nimbus, Diverz Sapiens, Diverz Specific, Himalaja, Investrium, Prestige, Prestige Select, Prestige Start, Reverse Max, Helios, Prospect Fund.

### YTD returns (Hozam Plaza, ~13 May 2026)

| Fund (share class) | YTD |
|--------------------|-----|
| Bond Derivativ HUF | +10.4% |
| Bond Derivativ EUR | +4.1% |
| Aurica HUF / EUR / USD | +5.2% / +5.8% / +4.8% |
| Creditum HUF / EUR / USD | -2.7% / -3.9% / -3.9% |
| Diverz Sapiens HUF / EUR / USD | +3.1% / +2.4% / +0.2% |
| Diverz Specific HUF / EUR | +3.0% / -1.0% |
| Diverz Nimbus EUR | +2.2% |
| Prestige HUF | +2.7% |
| Prestige Start HUF | +1.7% |
| Prestige Select HUF / EUR / USD | +0.5% / -1.4% / -1.8% |
| Himalaja HUF | -2.3% |

No Hozam YTD at fetch time: Allegro, Convexity, Investrium, Compass, Reverse Max, Helios, Prospect.

### Company and contact

| Field | Value |
|-------|--------|
| Legal name | MARKETPROG Asset Management Befektetesi Alapkezelo Zrt. |
| Founded | 2014 |
| Regulation | MNB, AIFMD |
| Group | Primus Wealth |
| Address | 1124 Budapest, Csorsz utca 45, MOM Irodapark, SAS Tower, 5th floor |
| Phone | +36 1 213 4210 |
| Fax | +36 1 213 4219 |
| Email | info@marketproginvestment.com |
| Hours | Mon-Fri, 8:00-16:00 |
| Settlement | T+3 |

### Leadership

| Name | Role |
|------|------|
| Varkonyi Istvan | CEO |
| Alexandra Mikecz | COO |
| Tamas Torok | CIO |

---

## Current State

- Functional single-page site with hash routing and Chart.js charts.
- v5 real counts, contact, leadership, 17-family grid with partial live YTD.
- Charts still illustrative (NAV history not from API).

### How to view

```powershell
start C:\Users\torok\mpi.fund\index.html
# or local server: http://localhost:3456
```

---

## Files (use these paths)

| Path | Purpose |
|------|---------|
| `C:\Users\torok\mpi.fund\index.html` | Main site — edit this |
| `C:\Users\torok\mpi.fund\HANDOFF.md` | **This handoff (opens reliably in Cursor)** |
| `C:\Users\torok\Desktop\mpi-fund.html` | Site copy |
| `C:\Users\torok\OneDrive\CLAUDE\HANDOFF.md` | OneDrive copy — may not open in editor (cloud reparse point) |

---

## What to Do Next

- [ ] Replace illustrative charts with real NAV series if available.
- [ ] Add ISINs on fund cards.
- [ ] Wire PDF buttons to Firebase URLs from live app.
- [ ] Fill Distribution account numbers.
- [ ] Add Hungarian / English toggle.
- [ ] Deploy (Netlify, Vercel, or static host).
- [ ] Delete unused Next.js scaffold.
- [ ] Re-scrape Hozam Plaza for YTD refresh.

---

## Quick reference URLs

- https://www.marketprog.hu/
- https://mpi.fund/
- https://hozamplaza.hu/befektetesi-alapok?p=man_261
- https://intezmenykereso.mnb.hu/
