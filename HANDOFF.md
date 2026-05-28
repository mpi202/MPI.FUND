# MPI.Fund — Database & Admin Handoff

> Handoff for a fresh Claude session. Everything you need to continue work on the **Firebase backend + admin panel** for mpi.fund.

---

## 1. The Big Picture

**Project**: Redesign of mpi.fund (Marketprog Asset Management Zrt., Hungarian fund manager).
**Stack**: Single-file static HTML (`index.html`) + Tailwind CDN + Chart.js + **Firebase** (Auth, Firestore, Storage).
**No build step. No Node.js.** Open the HTML files directly in a browser.

Two HTML files:
- `index.html` — public website (~2,277 lines)
- `admin.html` — password-protected admin panel for managing PDFs (~598 lines)

---

## 2. Firebase Project

**Project ID**: `mpifund-v2`
**Owner**: User's personal Firebase account (NOT the legacy `marketprog-test` project)
**Region**: `europe-west10` (Berlin)
**Mode**: **Test mode** — anyone can read/write for 30 days. ⚠️ **Must add security rules before deployment.**

### Web SDK config (already wired into both HTML files)
```js
{
  apiKey: "AIzaSyAWbHaY9iTSzopTKbnwVz03hWWCtzHHzek",
  authDomain: "mpifund-v2.firebaseapp.com",
  projectId: "mpifund-v2",
  storageBucket: "mpifund-v2.firebasestorage.app",
  messagingSenderId: "956363748860",
  appId: "1:956363748860:web:e235858ce8a7a53ce5ee79",
  measurementId: "G-FRK1RBRE7B"
}
```

### Services enabled
- **Authentication** → Email/Password provider only. User account created.
- **Firestore** → test mode, region `europe-west10`.
- **Storage** → bucket `mpifund-v2.firebasestorage.app`.

---

## 3. Firestore Schema (current)

```
(default)/
├── categories/                  ← document categories (15 seeded)
│   └── {slug}                   ← doc id = slug, e.g. "asset-manager"
│       ├── name: string         ← display name (Hungarian)
│       ├── slug: string         ← same as doc id
│       └── order: number        ← display ordering
│
└── documents/                   ← all PDFs across the site
    └── {auto-id}
        ├── name: string         ← display name
        ├── url: string          ← Firebase Storage download URL (or external)
        ├── category: string     ← FK → categories.slug
        ├── order: number        ← Date.now() at creation
        ├── createdAt: timestamp
        ├── updatedAt: timestamp
        └── importedFrom?: string ← legacy collection name (if imported)
```

### The 15 seed categories

**5 "default" → each maps to a dedicated page on the public site:**
| slug | name | site location |
|---|---|---|
| `asset-manager` | Az Alapkezelő dokumentumai | Customer Info accordion + Asset Manager page |
| `regulatory` | Szabályozói kiadványok | Regulatory page |
| `customer-info` | Ügyfél-tájékoztatás | Customer Info page |
| `fatca` | FATCA | FATCA page |
| `crs` | CRS | CRS page |

**10 "granular" → appear as cards on the Documents landing page (only when non-empty):**
| slug | name |
|---|---|
| `account-numbers` | Számlaszámok |
| `authorization-form` | Meghatalmazási nyomtatványok |
| `business-rules` | Üzletszabályzat |
| `complaint-handling-policy` | Panaszkezelési szabályzat |
| `complaint-handling-procedure` | Panaszkezelési eljárásrend |
| `conflict-of-interest-policy` | Összeférhetetlenségi politika |
| `customer-service-offices` | Ügyfélszolgálati irodák |
| `distribution-partners` | Forgalmazási partnerek |
| `enforcement-supplementary` | Végrehajtási politika (kieg.) |
| `fee-policy` | Díjszabályzat |

Categories auto-seed on every admin load (additive — won't overwrite renames or duplicate).

---

## 4. How the Public Site Reads Documents

`index.html` includes Firebase SDK + queries `documents` by `category` slug.

Key functions in `index.html`:
- `loadDocList(cat, containerId)` — fetches all docs in a category, sorts client-side by `order`, renders into a container.
- `loadDynamicCategories()` — populates the Documents landing page grid. Only shows cards for categories with ≥1 document. Displays document count on each card.
- `showCustomCategory(slug)` — navigates to the dynamic detail page for any category.

Dedicated pages already wired:
- `page-docs-fatca` → loads `fatca` category
- `page-docs-crs` → loads `crs` category
- `page-docs-custom` → generic page for any granular category
- Customer Info page has a "Kapcsolódó dokumentumok" section

**Important**: Firestore queries with `.where(...).orderBy(...)` need composite indexes. We avoid this by sorting **client-side** after the where filter.

---

## 5. The Admin Panel (`admin.html`)

### Login
- Email/password via Firebase Auth.
- Only users you've created in Firebase Console → Authentication → Users can log in.

### UI layout
- **Top bar**: logo + admin email + sign out
- **Left sidebar**: scrollable list of all categories. "Manage categories" button at bottom opens modal.
- **Main area**: title + "Add document" button + document list (hover reveals open/edit/delete icons)

### Modals
- **Add/Edit document**: name + URL field. URL can be pasted OR populated by uploading a PDF (auto-uploads to Storage at path `{slug}/{timestamp}_{filename}`, fills URL field).
- **Manage categories**: list with inline rename + delete button. Add new category via text field (auto-generates slug from Hungarian name, strips accents). Includes "Import from old site" button that pulls from legacy `marketprog-test` collections.
- **Delete confirmation**: shared modal for both docs and categories.

### Key functions (`admin.html`)
- `loadCategories()` — fetches + auto-seeds missing
- `loadDocs()` — fetches docs for `currentCat`, sorts client-side by `order`
- `selectCat(slug)` — switches active sidebar item
- `addCat()` / `renameCat()` / `deleteCat()` — category CRUD
- `saveDoc()` — create or update
- `uploadFile(input)` — pushes to Storage, fills URL field
- `openDelete()` / `confirmDelete()` — doc delete flow
- `importLegacyData()` — one-click bulk import from old `marketprog-test` collections (dedupes by URL)

---

## 6. Recent Work (last session)

Commit `9a503a9`: "Wire admin panel to new mpifund-v2 Firebase project, expand to 15 categories"
- Migrated from `marketprog-test` → `mpifund-v2`
- Added 10 legacy granular categories
- Made sidebar scrollable
- Fixed Firestore composite index errors by sorting client-side
- Added document count display on Documents landing page
- Hid empty category cards from public site
- Added "Kapcsolódó dokumentumok" section to Customer Info

---

## 7. What's NEXT (open requests from user)

### A. Per-fund PDF management ⭐ (most recent request)
The 12 fund families (Bond Derivativ, Aurica, Allegro, Compass, Convexity, Creditum, Diverz Nimbus, Diverz Sapiens, Diverz Specific, Himalaja, Investrium, Prestige, Prestige Select, Prestige Start, Reverse Max, Helios, Prospect) — currently each fund hardcodes 4 PDFs (`kiid`, `info`, `rule`, `report`) in the `FUNDS` array (around line 1695 of `index.html`). The live mpi.fund site has **50+ PDFs per fund**. We need a system to let IT add many PDFs to each fund.

**Proposed schema** (not yet built):
```
(default)/
├── categories/      ← unchanged
├── documents/       ← updated: add optional `fund` field for fund-tagged PDFs
└── funds/           ← NEW
    └── {fund-slug}  ← e.g. "bond-derivativ", "aurica", "allegro"
        ├── name: string
        ├── type: string         ← "Fixed Income", "Absolute Return", etc.
        ├── isin_huf, isin_eur, isin_usd
        ├── inception, mgmtFee, riskLevel, strategy
        └── ...
```

`documents` collection gets two optional new fields:
```
documents/{id}
├── fund?: string           ← "aurica" (which fund this PDF belongs to)
├── documentType?: string   ← "kiid" | "info" | "rule" | "report" | "factsheet" | "annual" | ...
└── period?: string         ← "2025-Q1" (optional, for periodic reports)
```

Admin panel changes needed:
- Add "Funds" section to sidebar with sub-list of all 12 funds
- Clicking a fund shows ALL documents tagged with that `fund` slug
- Add document modal gets two more fields: `fund` dropdown + `documentType` dropdown
- Optionally a "Funds management" modal to add/edit/delete funds (similar to category management)

Public site changes needed:
- Fund detail panel reads from `documents` collection filtered by `fund` (instead of using hardcoded `kiid`/`info`/`rule`/`report` fields)
- Group by `documentType` in the UI

### B. Other pending items
- **Services page redesign** (discussed but not built): collapse to 2 services (Advisory + Institutional), each with a button → hidden "Book a meeting" page (black bg, form with name/email/message, all → `info@mpi.fund.com`). Use Formspree or Firebase Cloud Function for email delivery.
- **Firestore security rules** ⚠️ critical before deploy. Currently `allow read, write: if true` (test mode, expires in 30 days). Need: public read on `documents` and `categories`, authenticated write only.
- **Deployment** — Netlify/Vercel/Firebase Hosting. Once deployed, IT team can use admin.html.
- **5 questions for IT team consultation** (already drafted in previous session):
  1. Hosting & data residency (Firebase OK or need on-prem/EU sovereign?)
  2. Audit & compliance (audit trail requirements?)
  3. Authentication (SSO needed? MFA? Provisioning?)
  4. Scope of admin content (beyond PDFs — fund data, charts, news?)
  5. Ownership, maintenance & DR (long-term ownership? backup policy? RTO/RPO?)

---

## 8. Files & Locations

| File | Purpose |
|---|---|
| `C:\Users\torok\mpi.fund\index.html` | Public website (2,277 lines) |
| `C:\Users\torok\mpi.fund\admin.html` | Admin panel (598 lines) |
| `C:\Users\torok\mpi.fund\CLAUDE.md` | Project overview / shorter handoff |
| `C:\Users\torok\mpi.fund\HANDOFF.md` | This file |

Git: tracked, last commit `9a503a9`.

---

## 9. Gotchas / Lessons Learned

1. **No composite indexes** — Firestore needs them for `.where(...).orderBy(...)`. We sort client-side instead. Apply the same pattern when filtering documents by `fund`.
2. **Test mode expires in 30 days** — set a calendar reminder, or write security rules before then.
3. **User is non-technical** — explain Firebase concepts simply. They open files in Cursor by accident instead of Chrome. Walk them through Firebase Console clicks.
4. **Hungarian accents in slugs** — `addCat()` strips them (`á→a`, `é→e`, `í→i`, `ó→o`, `ú→u`, `ő→o`, `ű→u`).
5. **Category names can duplicate document names** — e.g. "Üzletszabályzat" is both a category and a typical PDF name. Don't be confused.
6. **The user did NOT want legacy categories removed** — they want maximum precision/flexibility. Don't simplify the schema without asking.
7. **`marketprog-test` is the OLD Firebase project**, not ours. The Storage URL prefix `firebasestorage.googleapis.com/v0/b/marketprog-bf7d3.appspot.com/...` in `index.html`'s `FUNDS` array points to the OLD bucket — these hardcoded fund PDFs still work because the old bucket is public, but anything new should go through `mpifund-v2`.

---

## 10. Quick Start for Next Session

1. Read `index.html` lines ~1690–1800 to see the hardcoded `FUNDS` array.
2. Read `admin.html` lines ~160–215 to see the seed categories and Firebase config.
3. If continuing per-fund PDF work: design the `funds/` collection structure, add a "Funds" mode to the admin sidebar, and refactor the public-site fund detail panel to read from Firestore.
4. Always ask before deleting or simplifying — user wants precision over neatness.
