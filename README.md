# VaranasiPooja Icon Kit — 200 icons to generate

Brief for the designer / AI that will generate the final professional icon set for
[varanasipooja.com](https://varanasipooja.com) (Varanasi Pooja Center, ShivBodh Trust).

## What is in this repo

| Path | What |
|---|---|
| `ICON-LIST.md` | Visual list of all 200 icons: current prototype, file name, name, status, what to draw |
| `icons.json` / `icons.csv` | Same list, machine-readable, with the **full prompt** for every icon |
| `prototypes/*.svg` | 169 current icons. They are **rough references only** (concept/subject), not the quality target |
| `output/svg/` | **Put the finished icons here** |

`status: redesign` = redraw the prototype professionally. `status: new` = 31 icons with no prototype yet.

## Task

Generate **all 200 icons** in one consistent professional set and commit them to `output/svg/`.

### Deliverable rules (strict)

1. File name = exact `slug` + `.svg` (e.g. `output/svg/rudrabhishek.svg`). No other names, no folders inside.
2. Clean vector SVG, `viewBox="0 0 512 512"`, transparent background, no embedded raster images, no external refs.
3. One icon per file, centred, 48px safe padding on every side.
4. Every icon must follow the **master style** below so the 200 look like one family.
5. Do not edit `prototypes/`, `icons.json`, `icons.csv` or this README.

### Master style (applies to every icon)

- Premium devotional icon, flat vector, single symbol, geometric and symmetric.
- Monoline: 20px uniform stroke at 512px, round caps and joins; small filled accents only where useful.
- Colours: gold gradient `#F3D48A → #B08A4C` (main), kumkum red `#C0392B` only for tilak/bindu/small accent, ivory `#FFF8E8` highlight.
- Must read clearly at 24px and look premium at 512px — same optical weight across the set.

### Never

Text or letters (only exception: `om-symbol`), background tile/square, glossy glass, bevel, 3D, photorealism,
drop shadow, outer glow, sketchy/hand-drawn or uneven lines, human faces, deity bodies or idols
(deities are shown **only through their symbols** — lingam, trishul, gada, chakra, shankh, lotus, modak…),
brand logos, clutter. A diya/flame appears **only** where the subject is lamp, aarti, havan, fire or deep-daan.

## Quality bar

Think Apple SF Symbols / Phosphor / Stripe icon quality, in gold, for a Hindu temple-services brand.
If an icon looks like a child's sketch, it fails — redraw it.

## After generation

The site team pulls `output/svg/`, reviews a preview of all 200, and only after approval builds
desktop / tablet / mobile exports from these SVGs and installs them on the site.
