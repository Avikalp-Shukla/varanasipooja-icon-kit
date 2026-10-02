# varanasipooja.com - System Icon Kit (SaaS / Service Management)

Total: **274 icons** across 13 sections. Separate from the 200 devotional service icons in the repo root.

## Summary

| # | Section | Audience | Purpose | Count |
|---|---|---|---|---|
| 1 | `01-core-ui` | Frontend + Backend | Basic actions used on every screen | 40 |
| 2 | `02-navigation-header-footer` | Frontend | Public site header, mega menu, footer, contact | 20 |
| 3 | `03-trust-badges` | Frontend | Conversion and trust strip | 13 |
| 4 | `04-booking-flow` | Frontend | Booking engine steps: service > date > slot > sankalp > pay | 28 |
| 5 | `05-payments-finance` | Frontend + Backend | Razorpay/WooCommerce payments and finance desk | 16 |
| 6 | `06-devotee-account` | Frontend | My Account area for devotees | 22 |
| 7 | `07-live-online-puja` | Frontend + Priest | Live darshan and online sessions | 12 |
| 8 | `08-panchang-jyotish` | Frontend (Panchang app) | Panchang calendar and Jyotish tools | 38 |
| 9 | `09-admin-dashboard` | Backend (vp-app admin) | Booking manager / admin console modules | 38 |
| 10 | `10-priest-app` | Backend (Priest portal) | Pandit daily operations | 14 |
| 11 | `11-logistics-prasad` | Backend | Samagri purchase and prasad shipping | 10 |
| 12 | `12-communication` | Backend | Notifications and messaging | 8 |
| 13 | `13-status-states` | Frontend + Backend | Semantic status icons (use semantic colour as accent) | 15 |

**Grand total: 274**

## Master style (paste once, or append to every prompt)

```
Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers.

Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

## Output rules

- Save each as `system-icons/output/svg/{section}/{slug}.svg` (viewBox 0 0 24 24).
- Status icons (section 13) use their semantic accent colour instead of red.
- No emoji, no brand logos copied verbatim (social/payment icons are generic).

## 01-core-ui - Basic actions used on every screen
_Audience: Frontend + Backend - 40 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `menu` | Menu | Mobile header, admin sidebar toggle | three horizontal lines, middle shorter |
| `close` | Close | Modals, drawers, chips | X made of two rounded strokes |
| `search` | Search | Header search, admin tables | magnifier, lens filled light gold |
| `filter` | Filter | Service list, admin tables | funnel with fill inside cone |
| `sort` | Sort | Tables, listings | up arrow and down arrow side by side |
| `add` | Add | Create booking/service/slot | plus inside rounded square |
| `edit` | Edit | Edit any record | pencil at 45deg, tip in red |
| `delete` | Delete | Remove records | trash bin with lid, two inner lines |
| `save` | Save | Forms | check mark inside a document with folded corner |
| `copy` | Copy | Copy links/IDs | two overlapping rounded rectangles |
| `share` | Share | Service pages, blog | three connected nodes |
| `download` | Download | Invoices, reports, recordings | arrow down into tray |
| `upload` | Upload | Media, priest photo upload | arrow up out of tray |
| `print` | Print | Invoice, receipt | printer with paper |
| `refresh` | Refresh | Reload data | circular arrow 300deg |
| `more-horizontal` | More | Row actions | three dots horizontal |
| `more-vertical` | More (vertical) | Card menus | three dots vertical |
| `chevron-left` | Chevron left | Sliders, back | left chevron |
| `chevron-right` | Chevron right | Sliders, links | right chevron |
| `chevron-up` | Chevron up | Accordions | up chevron |
| `chevron-down` | Chevron down | Dropdowns, FAQ | down chevron |
| `arrow-left` | Arrow left | Back navigation | arrow with shaft left |
| `arrow-right` | Arrow right | CTA buttons | arrow with shaft right |
| `external-link` | External link | Outbound links | arrow leaving a square corner |
| `link` | Link | Copy URL | two chain links |
| `eye` | Show | Password, preview | eye with filled iris |
| `eye-off` | Hide | Password | eye with diagonal slash |
| `lock` | Lock | Secure payment, locked slot | padlock closed, body filled |
| `unlock` | Unlock | Released slot | padlock open shackle |
| `settings` | Settings | Account, admin | gear with 8 teeth, centre hole |
| `help` | Help | Help centre, tooltips | question mark in circle |
| `info` | Info | Notes, hints | letter i in circle |
| `home` | Home | Breadcrumb, nav | house with door filled |
| `grid-view` | Grid view | Listings toggle | 2x2 rounded squares |
| `list-view` | List view | Listings toggle | three bullets with lines |
| `fullscreen` | Fullscreen | Video, gallery | four corner brackets outward |
| `language` | Language | Hindi/English switch | globe with meridian, small 'अ' allowed |
| `dark-mode` | Dark mode | Theme toggle | crescent moon |
| `light-mode` | Light mode | Theme toggle | sun with 8 short rays |
| `drag-handle` | Drag | Reorder lists | six dots 2x3 |

<details><summary>Prompts</summary>

**menu**
```
Icon "Menu" (menu). Meaning: Mobile header, admin sidebar toggle. Draw: three horizontal lines, middle shorter. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**close**
```
Icon "Close" (close). Meaning: Modals, drawers, chips. Draw: X made of two rounded strokes. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**search**
```
Icon "Search" (search). Meaning: Header search, admin tables. Draw: magnifier, lens filled light gold. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**filter**
```
Icon "Filter" (filter). Meaning: Service list, admin tables. Draw: funnel with fill inside cone. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**sort**
```
Icon "Sort" (sort). Meaning: Tables, listings. Draw: up arrow and down arrow side by side. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**add**
```
Icon "Add" (add). Meaning: Create booking/service/slot. Draw: plus inside rounded square. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**edit**
```
Icon "Edit" (edit). Meaning: Edit any record. Draw: pencil at 45deg, tip in red. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**delete**
```
Icon "Delete" (delete). Meaning: Remove records. Draw: trash bin with lid, two inner lines. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**save**
```
Icon "Save" (save). Meaning: Forms. Draw: check mark inside a document with folded corner. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**copy**
```
Icon "Copy" (copy). Meaning: Copy links/IDs. Draw: two overlapping rounded rectangles. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**share**
```
Icon "Share" (share). Meaning: Service pages, blog. Draw: three connected nodes. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**download**
```
Icon "Download" (download). Meaning: Invoices, reports, recordings. Draw: arrow down into tray. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**upload**
```
Icon "Upload" (upload). Meaning: Media, priest photo upload. Draw: arrow up out of tray. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**print**
```
Icon "Print" (print). Meaning: Invoice, receipt. Draw: printer with paper. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**refresh**
```
Icon "Refresh" (refresh). Meaning: Reload data. Draw: circular arrow 300deg. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**more-horizontal**
```
Icon "More" (more-horizontal). Meaning: Row actions. Draw: three dots horizontal. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**more-vertical**
```
Icon "More (vertical)" (more-vertical). Meaning: Card menus. Draw: three dots vertical. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**chevron-left**
```
Icon "Chevron left" (chevron-left). Meaning: Sliders, back. Draw: left chevron. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**chevron-right**
```
Icon "Chevron right" (chevron-right). Meaning: Sliders, links. Draw: right chevron. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**chevron-up**
```
Icon "Chevron up" (chevron-up). Meaning: Accordions. Draw: up chevron. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**chevron-down**
```
Icon "Chevron down" (chevron-down). Meaning: Dropdowns, FAQ. Draw: down chevron. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**arrow-left**
```
Icon "Arrow left" (arrow-left). Meaning: Back navigation. Draw: arrow with shaft left. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**arrow-right**
```
Icon "Arrow right" (arrow-right). Meaning: CTA buttons. Draw: arrow with shaft right. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**external-link**
```
Icon "External link" (external-link). Meaning: Outbound links. Draw: arrow leaving a square corner. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**link**
```
Icon "Link" (link). Meaning: Copy URL. Draw: two chain links. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**eye**
```
Icon "Show" (eye). Meaning: Password, preview. Draw: eye with filled iris. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**eye-off**
```
Icon "Hide" (eye-off). Meaning: Password. Draw: eye with diagonal slash. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**lock**
```
Icon "Lock" (lock). Meaning: Secure payment, locked slot. Draw: padlock closed, body filled. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**unlock**
```
Icon "Unlock" (unlock). Meaning: Released slot. Draw: padlock open shackle. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**settings**
```
Icon "Settings" (settings). Meaning: Account, admin. Draw: gear with 8 teeth, centre hole. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**help**
```
Icon "Help" (help). Meaning: Help centre, tooltips. Draw: question mark in circle. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**info**
```
Icon "Info" (info). Meaning: Notes, hints. Draw: letter i in circle. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**home**
```
Icon "Home" (home). Meaning: Breadcrumb, nav. Draw: house with door filled. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**grid-view**
```
Icon "Grid view" (grid-view). Meaning: Listings toggle. Draw: 2x2 rounded squares. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**list-view**
```
Icon "List view" (list-view). Meaning: Listings toggle. Draw: three bullets with lines. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**fullscreen**
```
Icon "Fullscreen" (fullscreen). Meaning: Video, gallery. Draw: four corner brackets outward. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**language**
```
Icon "Language" (language). Meaning: Hindi/English switch. Draw: globe with meridian, small 'अ' allowed. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**dark-mode**
```
Icon "Dark mode" (dark-mode). Meaning: Theme toggle. Draw: crescent moon. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**light-mode**
```
Icon "Light mode" (light-mode). Meaning: Theme toggle. Draw: sun with 8 short rays. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**drag-handle**
```
Icon "Drag" (drag-handle). Meaning: Reorder lists. Draw: six dots 2x3. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 02-navigation-header-footer - Public site header, mega menu, footer, contact
_Audience: Frontend - 20 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `phone-call` | Call Now | Header CTA, footer | phone handset with two signal arcs |
| `whatsapp` | WhatsApp | Booking CTA | speech bubble with handset (brand-safe, not the logo) |
| `email` | Email | Footer, contact | envelope with flap filled |
| `location-pin` | Location | Ghat/temple address | map pin with filled centre |
| `map` | Map | Directions | folded map with route dot in red |
| `clock-hours` | Working hours | Footer | clock at 10:10 |
| `user-account` | My Account | Header | person bust in circle |
| `cart` | Cart | Header, checkout | shopping cart with two wheels |
| `book-now` | Book Now | Primary CTA | calendar with check mark, check in red |
| `gift-puja` | Gift a Puja | Mega menu | gift box with diya on top |
| `blog` | Blog | Mega menu | open book with bookmark |
| `gallery` | Gallery | Mega menu | photo frame with mountain and sun |
| `video` | Videos | Mega menu | play triangle in rounded rectangle |
| `about-trust` | About Trust | Footer | shield with lotus |
| `faq` | FAQ | Help centre | two speech bubbles with ? and ! |
| `social-youtube` | YouTube | Footer | rounded rectangle with play (generic) |
| `social-instagram` | Instagram | Footer | rounded square camera (generic) |
| `social-facebook` | Facebook | Footer | rounded square with f |
| `social-x` | X | Footer | letter X in square |
| `breadcrumb-sep` | Breadcrumb separator | Breadcrumbs | small chevron dot |

<details><summary>Prompts</summary>

**phone-call**
```
Icon "Call Now" (phone-call). Meaning: Header CTA, footer. Draw: phone handset with two signal arcs. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**whatsapp**
```
Icon "WhatsApp" (whatsapp). Meaning: Booking CTA. Draw: speech bubble with handset (brand-safe, not the logo). Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**email**
```
Icon "Email" (email). Meaning: Footer, contact. Draw: envelope with flap filled. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**location-pin**
```
Icon "Location" (location-pin). Meaning: Ghat/temple address. Draw: map pin with filled centre. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**map**
```
Icon "Map" (map). Meaning: Directions. Draw: folded map with route dot in red. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**clock-hours**
```
Icon "Working hours" (clock-hours). Meaning: Footer. Draw: clock at 10:10. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**user-account**
```
Icon "My Account" (user-account). Meaning: Header. Draw: person bust in circle. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**cart**
```
Icon "Cart" (cart). Meaning: Header, checkout. Draw: shopping cart with two wheels. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**book-now**
```
Icon "Book Now" (book-now). Meaning: Primary CTA. Draw: calendar with check mark, check in red. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**gift-puja**
```
Icon "Gift a Puja" (gift-puja). Meaning: Mega menu. Draw: gift box with diya on top. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**blog**
```
Icon "Blog" (blog). Meaning: Mega menu. Draw: open book with bookmark. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**gallery**
```
Icon "Gallery" (gallery). Meaning: Mega menu. Draw: photo frame with mountain and sun. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**video**
```
Icon "Videos" (video). Meaning: Mega menu. Draw: play triangle in rounded rectangle. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**about-trust**
```
Icon "About Trust" (about-trust). Meaning: Footer. Draw: shield with lotus. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**faq**
```
Icon "FAQ" (faq). Meaning: Help centre. Draw: two speech bubbles with ? and !. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**social-youtube**
```
Icon "YouTube" (social-youtube). Meaning: Footer. Draw: rounded rectangle with play (generic). Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**social-instagram**
```
Icon "Instagram" (social-instagram). Meaning: Footer. Draw: rounded square camera (generic). Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**social-facebook**
```
Icon "Facebook" (social-facebook). Meaning: Footer. Draw: rounded square with f. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**social-x**
```
Icon "X" (social-x). Meaning: Footer. Draw: letter X in square. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**breadcrumb-sep**
```
Icon "Breadcrumb separator" (breadcrumb-sep). Meaning: Breadcrumbs. Draw: small chevron dot. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 03-trust-badges - Conversion and trust strip
_Audience: Frontend - 13 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `verified-pandit` | Verified Pandit | Service cards | priest silhouette with check badge |
| `authentic-vedic` | Authentic Vedic | Hero eyebrow | scroll with om mark |
| `secure-payment` | Secure Payment | Checkout | shield with padlock |
| `live-streaming` | Live Streaming | Service cards | broadcast tower waves around diya |
| `video-proof` | Video Proof | Service cards | camera with check |
| `prasad-delivery` | Prasad Delivery | Service cards | box with leaf and motion lines |
| `rating-star` | Rating | Testimonials | 5-point star, filled gold |
| `rating-half` | Half star | Testimonials | half-filled star |
| `years-experience` | Years of Experience | Stats strip | laurel around number-free medal |
| `devotees-served` | Devotees Served | Stats strip | three people group |
| `support-24x7` | 24x7 Support | Stats strip | headset with mic |
| `nri-friendly` | NRI Friendly | Service cards | globe with diya |
| `money-back` | Refund Guarantee | Policies | coin with circular arrow |

<details><summary>Prompts</summary>

**verified-pandit**
```
Icon "Verified Pandit" (verified-pandit). Meaning: Service cards. Draw: priest silhouette with check badge. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**authentic-vedic**
```
Icon "Authentic Vedic" (authentic-vedic). Meaning: Hero eyebrow. Draw: scroll with om mark. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**secure-payment**
```
Icon "Secure Payment" (secure-payment). Meaning: Checkout. Draw: shield with padlock. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**live-streaming**
```
Icon "Live Streaming" (live-streaming). Meaning: Service cards. Draw: broadcast tower waves around diya. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**video-proof**
```
Icon "Video Proof" (video-proof). Meaning: Service cards. Draw: camera with check. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**prasad-delivery**
```
Icon "Prasad Delivery" (prasad-delivery). Meaning: Service cards. Draw: box with leaf and motion lines. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rating-star**
```
Icon "Rating" (rating-star). Meaning: Testimonials. Draw: 5-point star, filled gold. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rating-half**
```
Icon "Half star" (rating-half). Meaning: Testimonials. Draw: half-filled star. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**years-experience**
```
Icon "Years of Experience" (years-experience). Meaning: Stats strip. Draw: laurel around number-free medal. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**devotees-served**
```
Icon "Devotees Served" (devotees-served). Meaning: Stats strip. Draw: three people group. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**support-24x7**
```
Icon "24x7 Support" (support-24x7). Meaning: Stats strip. Draw: headset with mic. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**nri-friendly**
```
Icon "NRI Friendly" (nri-friendly). Meaning: Service cards. Draw: globe with diya. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**money-back**
```
Icon "Refund Guarantee" (money-back). Meaning: Policies. Draw: coin with circular arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 04-booking-flow - Booking engine steps: service > date > slot > sankalp > pay
_Audience: Frontend - 28 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `step-service` | Choose Service | Stepper 1 | diya in square |
| `step-date` | Choose Date | Stepper 2 | calendar page |
| `step-slot` | Choose Slot | Stepper 3 | clock with filled sector |
| `step-sankalp` | Sankalp Details | Stepper 4 | hand holding water drop (sankalp) |
| `step-payment` | Payment | Stepper 5 | card with rupee |
| `step-confirm` | Confirmation | Stepper 6 | seal with check |
| `calendar` | Calendar | Date picker | calendar with two rings |
| `calendar-auspicious` | Auspicious Date | Date picker highlight | calendar with small red dot and star |
| `slot-available` | Slot Available | Slot grid | clock with check |
| `slot-full` | Slot Full | Slot grid | clock with X |
| `slot-held` | Slot Held | Reservation timer | hourglass half filled |
| `timer` | Hold Timer | Checkout countdown | stopwatch |
| `gotra` | Gotra | Sankalp form | family tree with three nodes |
| `devotee-name` | Devotee Name | Sankalp form | person with tag |
| `family-members` | Family Members | Sankalp form | two adults one child |
| `birth-details` | Birth Details | Kundali form | star over calendar |
| `nakshatra-input` | Nakshatra | Sankalp form | star cluster of three |
| `intention` | Purpose / Wish | Sankalp form | folded hands with spark |
| `pandit-choice` | Choose Pandit | Booking options | priest bust with tilak |
| `location-temple` | Temple / Ghat Choice | Booking options | temple shikhara with flag |
| `online-mode` | Online Puja | Mode selector | laptop with diya on screen |
| `offline-mode` | In-person Puja | Mode selector | two people at a havan kund |
| `add-on` | Add-on | Upsell | plus in circle with leaf |
| `samagri-included` | Samagri Included | Package | basket with flowers |
| `coupon` | Coupon | Checkout | ticket with percent |
| `package` | Package Tier | Pricing | stack of three layers |
| `quote` | Get Quote | Custom puja | document with rupee |
| `dakshina` | Dakshina | Checkout | hand offering coin |

<details><summary>Prompts</summary>

**step-service**
```
Icon "Choose Service" (step-service). Meaning: Stepper 1. Draw: diya in square. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**step-date**
```
Icon "Choose Date" (step-date). Meaning: Stepper 2. Draw: calendar page. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**step-slot**
```
Icon "Choose Slot" (step-slot). Meaning: Stepper 3. Draw: clock with filled sector. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**step-sankalp**
```
Icon "Sankalp Details" (step-sankalp). Meaning: Stepper 4. Draw: hand holding water drop (sankalp). Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**step-payment**
```
Icon "Payment" (step-payment). Meaning: Stepper 5. Draw: card with rupee. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**step-confirm**
```
Icon "Confirmation" (step-confirm). Meaning: Stepper 6. Draw: seal with check. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**calendar**
```
Icon "Calendar" (calendar). Meaning: Date picker. Draw: calendar with two rings. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**calendar-auspicious**
```
Icon "Auspicious Date" (calendar-auspicious). Meaning: Date picker highlight. Draw: calendar with small red dot and star. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**slot-available**
```
Icon "Slot Available" (slot-available). Meaning: Slot grid. Draw: clock with check. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**slot-full**
```
Icon "Slot Full" (slot-full). Meaning: Slot grid. Draw: clock with X. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**slot-held**
```
Icon "Slot Held" (slot-held). Meaning: Reservation timer. Draw: hourglass half filled. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**timer**
```
Icon "Hold Timer" (timer). Meaning: Checkout countdown. Draw: stopwatch. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**gotra**
```
Icon "Gotra" (gotra). Meaning: Sankalp form. Draw: family tree with three nodes. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**devotee-name**
```
Icon "Devotee Name" (devotee-name). Meaning: Sankalp form. Draw: person with tag. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**family-members**
```
Icon "Family Members" (family-members). Meaning: Sankalp form. Draw: two adults one child. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**birth-details**
```
Icon "Birth Details" (birth-details). Meaning: Kundali form. Draw: star over calendar. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**nakshatra-input**
```
Icon "Nakshatra" (nakshatra-input). Meaning: Sankalp form. Draw: star cluster of three. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**intention**
```
Icon "Purpose / Wish" (intention). Meaning: Sankalp form. Draw: folded hands with spark. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pandit-choice**
```
Icon "Choose Pandit" (pandit-choice). Meaning: Booking options. Draw: priest bust with tilak. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**location-temple**
```
Icon "Temple / Ghat Choice" (location-temple). Meaning: Booking options. Draw: temple shikhara with flag. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**online-mode**
```
Icon "Online Puja" (online-mode). Meaning: Mode selector. Draw: laptop with diya on screen. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**offline-mode**
```
Icon "In-person Puja" (offline-mode). Meaning: Mode selector. Draw: two people at a havan kund. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**add-on**
```
Icon "Add-on" (add-on). Meaning: Upsell. Draw: plus in circle with leaf. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**samagri-included**
```
Icon "Samagri Included" (samagri-included). Meaning: Package. Draw: basket with flowers. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**coupon**
```
Icon "Coupon" (coupon). Meaning: Checkout. Draw: ticket with percent. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**package**
```
Icon "Package Tier" (package). Meaning: Pricing. Draw: stack of three layers. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**quote**
```
Icon "Get Quote" (quote). Meaning: Custom puja. Draw: document with rupee. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**dakshina**
```
Icon "Dakshina" (dakshina). Meaning: Checkout. Draw: hand offering coin. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 05-payments-finance - Razorpay/WooCommerce payments and finance desk
_Audience: Frontend + Backend - 16 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `rupee` | Rupee | Prices | rupee sign ₹ bold |
| `upi` | UPI | Payment method | phone with arrow tick (generic, no logo) |
| `card` | Card | Payment method | credit card with chip |
| `netbanking` | Net Banking | Payment method | bank building with pillars |
| `wallet` | Wallet | Payment method | wallet with flap |
| `international-pay` | International Pay | NRI | globe with card |
| `invoice` | Invoice | Account, admin | document with lines and rupee |
| `receipt` | Receipt | Account | torn-edge paper |
| `refund` | Refund | Admin finance | rupee with back arrow |
| `payout` | Priest Payout | Finance | hand receiving coins |
| `gst-tax` | GST / Tax | Finance | percent in document |
| `ledger` | Ledger | Finance | book with columns |
| `donation` | Donation | Trust | hand with heart and coin |
| `80g-certificate` | 80G Certificate | Donation receipts | certificate with ribbon |
| `revenue` | Revenue | Dashboard | rising bar chart with rupee |
| `payment-failed` | Payment Failed | Checkout | card with X in red |

<details><summary>Prompts</summary>

**rupee**
```
Icon "Rupee" (rupee). Meaning: Prices. Draw: rupee sign ₹ bold. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**upi**
```
Icon "UPI" (upi). Meaning: Payment method. Draw: phone with arrow tick (generic, no logo). Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**card**
```
Icon "Card" (card). Meaning: Payment method. Draw: credit card with chip. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**netbanking**
```
Icon "Net Banking" (netbanking). Meaning: Payment method. Draw: bank building with pillars. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**wallet**
```
Icon "Wallet" (wallet). Meaning: Payment method. Draw: wallet with flap. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**international-pay**
```
Icon "International Pay" (international-pay). Meaning: NRI. Draw: globe with card. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**invoice**
```
Icon "Invoice" (invoice). Meaning: Account, admin. Draw: document with lines and rupee. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**receipt**
```
Icon "Receipt" (receipt). Meaning: Account. Draw: torn-edge paper. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**refund**
```
Icon "Refund" (refund). Meaning: Admin finance. Draw: rupee with back arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**payout**
```
Icon "Priest Payout" (payout). Meaning: Finance. Draw: hand receiving coins. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**gst-tax**
```
Icon "GST / Tax" (gst-tax). Meaning: Finance. Draw: percent in document. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**ledger**
```
Icon "Ledger" (ledger). Meaning: Finance. Draw: book with columns. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**donation**
```
Icon "Donation" (donation). Meaning: Trust. Draw: hand with heart and coin. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**80g-certificate**
```
Icon "80G Certificate" (80g-certificate). Meaning: Donation receipts. Draw: certificate with ribbon. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**revenue**
```
Icon "Revenue" (revenue). Meaning: Dashboard. Draw: rising bar chart with rupee. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**payment-failed**
```
Icon "Payment Failed" (payment-failed). Meaning: Checkout. Draw: card with X in red. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 06-devotee-account - My Account area for devotees
_Audience: Frontend - 22 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `dashboard-devotee` | My Dashboard | Account home | four tiles, one filled |
| `my-bookings` | My Bookings | Account | calendar list with diya |
| `upcoming` | Upcoming Puja | Account | calendar with right arrow |
| `past-puja` | Past Puja | Account | calendar with history arrow |
| `profile` | Profile | Account | person card |
| `addresses` | Addresses | Prasad delivery | house with pin |
| `saved-family` | Saved Family | Sankalp autofill | family with heart |
| `favourites` | Favourites | Saved services | heart |
| `notifications` | Notifications | Header bell | temple bell with clapper (ghanta) |
| `recordings` | Recordings | After puja | film reel with play |
| `photos-proof` | Photo Proof | After puja | stacked photos |
| `certificate` | Puja Certificate | After puja | scroll with seal |
| `track-prasad` | Track Prasad | Delivery | truck with box |
| `reschedule` | Reschedule | Booking actions | calendar with circular arrow |
| `cancel-booking` | Cancel Booking | Booking actions | calendar with X |
| `rebook` | Book Again | Booking actions | repeat arrows around diya |
| `write-review` | Write Review | After puja | star with pencil |
| `logout` | Logout | Account | door with arrow out |
| `login` | Login | Header | door with arrow in |
| `register` | Register | Signup | person with plus |
| `otp` | OTP | Login | phone with 4 dots |
| `social-google` | Google Sign-in | Login | G in circle (generic) |

<details><summary>Prompts</summary>

**dashboard-devotee**
```
Icon "My Dashboard" (dashboard-devotee). Meaning: Account home. Draw: four tiles, one filled. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**my-bookings**
```
Icon "My Bookings" (my-bookings). Meaning: Account. Draw: calendar list with diya. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**upcoming**
```
Icon "Upcoming Puja" (upcoming). Meaning: Account. Draw: calendar with right arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**past-puja**
```
Icon "Past Puja" (past-puja). Meaning: Account. Draw: calendar with history arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**profile**
```
Icon "Profile" (profile). Meaning: Account. Draw: person card. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**addresses**
```
Icon "Addresses" (addresses). Meaning: Prasad delivery. Draw: house with pin. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**saved-family**
```
Icon "Saved Family" (saved-family). Meaning: Sankalp autofill. Draw: family with heart. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**favourites**
```
Icon "Favourites" (favourites). Meaning: Saved services. Draw: heart. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**notifications**
```
Icon "Notifications" (notifications). Meaning: Header bell. Draw: temple bell with clapper (ghanta). Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**recordings**
```
Icon "Recordings" (recordings). Meaning: After puja. Draw: film reel with play. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**photos-proof**
```
Icon "Photo Proof" (photos-proof). Meaning: After puja. Draw: stacked photos. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**certificate**
```
Icon "Puja Certificate" (certificate). Meaning: After puja. Draw: scroll with seal. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**track-prasad**
```
Icon "Track Prasad" (track-prasad). Meaning: Delivery. Draw: truck with box. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**reschedule**
```
Icon "Reschedule" (reschedule). Meaning: Booking actions. Draw: calendar with circular arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**cancel-booking**
```
Icon "Cancel Booking" (cancel-booking). Meaning: Booking actions. Draw: calendar with X. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rebook**
```
Icon "Book Again" (rebook). Meaning: Booking actions. Draw: repeat arrows around diya. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**write-review**
```
Icon "Write Review" (write-review). Meaning: After puja. Draw: star with pencil. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**logout**
```
Icon "Logout" (logout). Meaning: Account. Draw: door with arrow out. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**login**
```
Icon "Login" (login). Meaning: Header. Draw: door with arrow in. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**register**
```
Icon "Register" (register). Meaning: Signup. Draw: person with plus. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**otp**
```
Icon "OTP" (otp). Meaning: Login. Draw: phone with 4 dots. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**social-google**
```
Icon "Google Sign-in" (social-google). Meaning: Login. Draw: G in circle (generic). Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 07-live-online-puja - Live darshan and online sessions
_Audience: Frontend + Priest - 12 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `live-badge` | Live | Session pages | dot in red with broadcast arcs |
| `video-call` | Video Call | Session join | camera with person |
| `join-session` | Join Session | Reminders | door with play |
| `mic-on` | Mic On | Session | microphone |
| `mic-off` | Mic Off | Session | microphone with slash |
| `camera-on` | Camera On | Session | video camera |
| `camera-off` | Camera Off | Session | video camera with slash |
| `screen-share` | Screen Share | Session | monitor with up arrow |
| `time-zone` | Time Zone | NRI scheduling | globe with clock |
| `replay` | Replay | Recordings | circular arrow with play |
| `chat` | Chat | Session | speech bubble with three dots |
| `raise-hand` | Raise Hand | Session | open palm |

<details><summary>Prompts</summary>

**live-badge**
```
Icon "Live" (live-badge). Meaning: Session pages. Draw: dot in red with broadcast arcs. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**video-call**
```
Icon "Video Call" (video-call). Meaning: Session join. Draw: camera with person. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**join-session**
```
Icon "Join Session" (join-session). Meaning: Reminders. Draw: door with play. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**mic-on**
```
Icon "Mic On" (mic-on). Meaning: Session. Draw: microphone. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**mic-off**
```
Icon "Mic Off" (mic-off). Meaning: Session. Draw: microphone with slash. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**camera-on**
```
Icon "Camera On" (camera-on). Meaning: Session. Draw: video camera. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**camera-off**
```
Icon "Camera Off" (camera-off). Meaning: Session. Draw: video camera with slash. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**screen-share**
```
Icon "Screen Share" (screen-share). Meaning: Session. Draw: monitor with up arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**time-zone**
```
Icon "Time Zone" (time-zone). Meaning: NRI scheduling. Draw: globe with clock. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**replay**
```
Icon "Replay" (replay). Meaning: Recordings. Draw: circular arrow with play. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**chat**
```
Icon "Chat" (chat). Meaning: Session. Draw: speech bubble with three dots. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**raise-hand**
```
Icon "Raise Hand" (raise-hand). Meaning: Session. Draw: open palm. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 08-panchang-jyotish - Panchang calendar and Jyotish tools
_Audience: Frontend (Panchang app) - 38 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `tithi` | Tithi | Panchang | moon phase half |
| `nakshatra` | Nakshatra | Panchang | star with orbit |
| `yoga-panchang` | Yoga | Panchang | two interlocked circles |
| `karana` | Karana | Panchang | half circle with dot |
| `vaar` | Vaar (weekday) | Panchang | calendar with sun |
| `sunrise` | Sunrise | Panchang | half sun over line, arrow up |
| `sunset` | Sunset | Panchang | half sun over line, arrow down |
| `moonrise` | Moonrise | Panchang | crescent over line, arrow up |
| `moonset` | Moonset | Panchang | crescent over line, arrow down |
| `rahu-kaal` | Rahu Kaal | Panchang | clock with shaded red sector |
| `abhijit-muhurat` | Abhijit Muhurat | Panchang | sun at zenith with check |
| `muhurat` | Muhurat | Panchang | hourglass with star |
| `ekadashi` | Ekadashi | Festival tag | crescent with leaf |
| `purnima` | Purnima | Festival tag | full moon filled |
| `amavasya` | Amavasya | Festival tag | outline-only dark moon |
| `festival` | Festival | Calendar | diya with flame red |
| `kundali` | Kundali | Jyotish | north-Indian diamond chart |
| `rashi-mesh` | Mesh (Aries) | Rashifal | ram horns |
| `rashi-vrishabh` | Vrishabh (Taurus) | Rashifal | bull head |
| `rashi-mithun` | Mithun (Gemini) | Rashifal | twin figures |
| `rashi-kark` | Kark (Cancer) | Rashifal | crab claws |
| `rashi-simha` | Simha (Leo) | Rashifal | lion mane profile |
| `rashi-kanya` | Kanya (Virgo) | Rashifal | maiden with wheat |
| `rashi-tula` | Tula (Libra) | Rashifal | balance scale |
| `rashi-vrishchik` | Vrishchik (Scorpio) | Rashifal | scorpion tail |
| `rashi-dhanu` | Dhanu (Sagittarius) | Rashifal | bow and arrow |
| `rashi-makar` | Makar (Capricorn) | Rashifal | crocodile/makara curl |
| `rashi-kumbh` | Kumbh (Aquarius) | Rashifal | water pot pouring |
| `rashi-meen` | Meen (Pisces) | Rashifal | two fish circling |
| `graha-surya` | Surya | Navagraha | sun disc with 12 rays |
| `graha-chandra` | Chandra | Navagraha | crescent |
| `graha-mangal` | Mangal | Navagraha | triangle in red |
| `graha-budh` | Budh | Navagraha | arrow-tipped circle |
| `graha-guru` | Guru | Navagraha | yellow disc with stripe |
| `graha-shukra` | Shukra | Navagraha | bright 6-point star |
| `graha-shani` | Shani | Navagraha | ringed planet |
| `graha-rahu` | Rahu | Navagraha | serpent head |
| `graha-ketu` | Ketu | Navagraha | serpent tail with flag |

<details><summary>Prompts</summary>

**tithi**
```
Icon "Tithi" (tithi). Meaning: Panchang. Draw: moon phase half. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**nakshatra**
```
Icon "Nakshatra" (nakshatra). Meaning: Panchang. Draw: star with orbit. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**yoga-panchang**
```
Icon "Yoga" (yoga-panchang). Meaning: Panchang. Draw: two interlocked circles. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**karana**
```
Icon "Karana" (karana). Meaning: Panchang. Draw: half circle with dot. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**vaar**
```
Icon "Vaar (weekday)" (vaar). Meaning: Panchang. Draw: calendar with sun. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**sunrise**
```
Icon "Sunrise" (sunrise). Meaning: Panchang. Draw: half sun over line, arrow up. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**sunset**
```
Icon "Sunset" (sunset). Meaning: Panchang. Draw: half sun over line, arrow down. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**moonrise**
```
Icon "Moonrise" (moonrise). Meaning: Panchang. Draw: crescent over line, arrow up. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**moonset**
```
Icon "Moonset" (moonset). Meaning: Panchang. Draw: crescent over line, arrow down. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rahu-kaal**
```
Icon "Rahu Kaal" (rahu-kaal). Meaning: Panchang. Draw: clock with shaded red sector. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**abhijit-muhurat**
```
Icon "Abhijit Muhurat" (abhijit-muhurat). Meaning: Panchang. Draw: sun at zenith with check. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**muhurat**
```
Icon "Muhurat" (muhurat). Meaning: Panchang. Draw: hourglass with star. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**ekadashi**
```
Icon "Ekadashi" (ekadashi). Meaning: Festival tag. Draw: crescent with leaf. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**purnima**
```
Icon "Purnima" (purnima). Meaning: Festival tag. Draw: full moon filled. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**amavasya**
```
Icon "Amavasya" (amavasya). Meaning: Festival tag. Draw: outline-only dark moon. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**festival**
```
Icon "Festival" (festival). Meaning: Calendar. Draw: diya with flame red. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**kundali**
```
Icon "Kundali" (kundali). Meaning: Jyotish. Draw: north-Indian diamond chart. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-mesh**
```
Icon "Mesh (Aries)" (rashi-mesh). Meaning: Rashifal. Draw: ram horns. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-vrishabh**
```
Icon "Vrishabh (Taurus)" (rashi-vrishabh). Meaning: Rashifal. Draw: bull head. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-mithun**
```
Icon "Mithun (Gemini)" (rashi-mithun). Meaning: Rashifal. Draw: twin figures. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-kark**
```
Icon "Kark (Cancer)" (rashi-kark). Meaning: Rashifal. Draw: crab claws. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-simha**
```
Icon "Simha (Leo)" (rashi-simha). Meaning: Rashifal. Draw: lion mane profile. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-kanya**
```
Icon "Kanya (Virgo)" (rashi-kanya). Meaning: Rashifal. Draw: maiden with wheat. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-tula**
```
Icon "Tula (Libra)" (rashi-tula). Meaning: Rashifal. Draw: balance scale. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-vrishchik**
```
Icon "Vrishchik (Scorpio)" (rashi-vrishchik). Meaning: Rashifal. Draw: scorpion tail. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-dhanu**
```
Icon "Dhanu (Sagittarius)" (rashi-dhanu). Meaning: Rashifal. Draw: bow and arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-makar**
```
Icon "Makar (Capricorn)" (rashi-makar). Meaning: Rashifal. Draw: crocodile/makara curl. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-kumbh**
```
Icon "Kumbh (Aquarius)" (rashi-kumbh). Meaning: Rashifal. Draw: water pot pouring. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rashi-meen**
```
Icon "Meen (Pisces)" (rashi-meen). Meaning: Rashifal. Draw: two fish circling. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**graha-surya**
```
Icon "Surya" (graha-surya). Meaning: Navagraha. Draw: sun disc with 12 rays. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**graha-chandra**
```
Icon "Chandra" (graha-chandra). Meaning: Navagraha. Draw: crescent. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**graha-mangal**
```
Icon "Mangal" (graha-mangal). Meaning: Navagraha. Draw: triangle in red. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**graha-budh**
```
Icon "Budh" (graha-budh). Meaning: Navagraha. Draw: arrow-tipped circle. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**graha-guru**
```
Icon "Guru" (graha-guru). Meaning: Navagraha. Draw: yellow disc with stripe. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**graha-shukra**
```
Icon "Shukra" (graha-shukra). Meaning: Navagraha. Draw: bright 6-point star. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**graha-shani**
```
Icon "Shani" (graha-shani). Meaning: Navagraha. Draw: ringed planet. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**graha-rahu**
```
Icon "Rahu" (graha-rahu). Meaning: Navagraha. Draw: serpent head. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**graha-ketu**
```
Icon "Ketu" (graha-ketu). Meaning: Navagraha. Draw: serpent tail with flag. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 09-admin-dashboard - Booking manager / admin console modules
_Audience: Backend (vp-app admin) - 38 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `admin-dashboard` | Dashboard | AdminDashboard | gauge with needle |
| `bookings-admin` | Bookings | vp_manage_bookings | clipboard with diya |
| `reservations` | Reservations | Reservation table | ticket stub with clock |
| `availability` | Availability | vp_manage_availability | calendar grid with green check cells |
| `sessions` | Sessions | vp_manage_sessions | calendar with video play |
| `catalog` | Service Catalog | Catalog | book with diya on cover |
| `pricing` | Pricing Registry | vp-pricing-registry | price tag with rupee |
| `devotees-crm` | Devotees (CRM) | vp_view_devotees | address card with person |
| `priests` | Priests | vp_priest | three priest busts |
| `roles` | Roles | Roles.php | person with shield |
| `permissions` | Permissions | Roles.php | key with check |
| `audit-log` | Audit Log | vp_view_audit | document with magnifier |
| `reminders` | Reminders | Reminders.php | bell with clock |
| `rules` | Rules | Rules.php | flowchart with branch |
| `reports` | Reports | vp_view_reports | bar chart document |
| `analytics` | Analytics | Dashboard | line chart rising |
| `conversion` | Conversion | Analytics | funnel with arrow |
| `traffic` | Traffic | Analytics | cursor with waves |
| `inventory` | Samagri Inventory | Stock | shelves with jars |
| `orders` | Orders | WooCommerce | bag with check |
| `coupons-admin` | Coupons | Marketing | tickets stack |
| `campaign` | Campaign | Marketing | megaphone |
| `content-pages` | Pages | CMS | stack of documents |
| `media-library` | Media Library | CMS | images grid |
| `seo` | SEO | Rank Math | magnifier with up arrow |
| `faq-admin` | FAQ Manager | vp-service-faq | list with question mark |
| `import` | Import | WP All Import | arrow into database |
| `export` | Export | Reports | arrow out of database |
| `integrations` | Integrations | Settings | puzzle piece |
| `api` | API | REST | curly braces |
| `webhook` | Webhook | Integrations | hook with arc |
| `backup` | Backup | Ops | cloud with up arrow |
| `security` | Security | vp-edge-hardening | shield with check |
| `cache` | Cache | Redis | lightning in cylinder |
| `server-health` | Server Health | Ops | server with pulse line |
| `content-integrity` | Content Integrity | vp-content-integrity | document with shield |
| `users-admin` | Users | Admin | two people |
| `branch-ghat` | Locations / Ghats | Settings | ghat steps with river |

<details><summary>Prompts</summary>

**admin-dashboard**
```
Icon "Dashboard" (admin-dashboard). Meaning: AdminDashboard. Draw: gauge with needle. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**bookings-admin**
```
Icon "Bookings" (bookings-admin). Meaning: vp_manage_bookings. Draw: clipboard with diya. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**reservations**
```
Icon "Reservations" (reservations). Meaning: Reservation table. Draw: ticket stub with clock. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**availability**
```
Icon "Availability" (availability). Meaning: vp_manage_availability. Draw: calendar grid with green check cells. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**sessions**
```
Icon "Sessions" (sessions). Meaning: vp_manage_sessions. Draw: calendar with video play. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**catalog**
```
Icon "Service Catalog" (catalog). Meaning: Catalog. Draw: book with diya on cover. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pricing**
```
Icon "Pricing Registry" (pricing). Meaning: vp-pricing-registry. Draw: price tag with rupee. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**devotees-crm**
```
Icon "Devotees (CRM)" (devotees-crm). Meaning: vp_view_devotees. Draw: address card with person. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**priests**
```
Icon "Priests" (priests). Meaning: vp_priest. Draw: three priest busts. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**roles**
```
Icon "Roles" (roles). Meaning: Roles.php. Draw: person with shield. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**permissions**
```
Icon "Permissions" (permissions). Meaning: Roles.php. Draw: key with check. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**audit-log**
```
Icon "Audit Log" (audit-log). Meaning: vp_view_audit. Draw: document with magnifier. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**reminders**
```
Icon "Reminders" (reminders). Meaning: Reminders.php. Draw: bell with clock. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rules**
```
Icon "Rules" (rules). Meaning: Rules.php. Draw: flowchart with branch. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**reports**
```
Icon "Reports" (reports). Meaning: vp_view_reports. Draw: bar chart document. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**analytics**
```
Icon "Analytics" (analytics). Meaning: Dashboard. Draw: line chart rising. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**conversion**
```
Icon "Conversion" (conversion). Meaning: Analytics. Draw: funnel with arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**traffic**
```
Icon "Traffic" (traffic). Meaning: Analytics. Draw: cursor with waves. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**inventory**
```
Icon "Samagri Inventory" (inventory). Meaning: Stock. Draw: shelves with jars. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**orders**
```
Icon "Orders" (orders). Meaning: WooCommerce. Draw: bag with check. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**coupons-admin**
```
Icon "Coupons" (coupons-admin). Meaning: Marketing. Draw: tickets stack. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**campaign**
```
Icon "Campaign" (campaign). Meaning: Marketing. Draw: megaphone. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**content-pages**
```
Icon "Pages" (content-pages). Meaning: CMS. Draw: stack of documents. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**media-library**
```
Icon "Media Library" (media-library). Meaning: CMS. Draw: images grid. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**seo**
```
Icon "SEO" (seo). Meaning: Rank Math. Draw: magnifier with up arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**faq-admin**
```
Icon "FAQ Manager" (faq-admin). Meaning: vp-service-faq. Draw: list with question mark. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**import**
```
Icon "Import" (import). Meaning: WP All Import. Draw: arrow into database. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**export**
```
Icon "Export" (export). Meaning: Reports. Draw: arrow out of database. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**integrations**
```
Icon "Integrations" (integrations). Meaning: Settings. Draw: puzzle piece. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**api**
```
Icon "API" (api). Meaning: REST. Draw: curly braces. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**webhook**
```
Icon "Webhook" (webhook). Meaning: Integrations. Draw: hook with arc. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**backup**
```
Icon "Backup" (backup). Meaning: Ops. Draw: cloud with up arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**security**
```
Icon "Security" (security). Meaning: vp-edge-hardening. Draw: shield with check. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**cache**
```
Icon "Cache" (cache). Meaning: Redis. Draw: lightning in cylinder. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**server-health**
```
Icon "Server Health" (server-health). Meaning: Ops. Draw: server with pulse line. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**content-integrity**
```
Icon "Content Integrity" (content-integrity). Meaning: vp-content-integrity. Draw: document with shield. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**users-admin**
```
Icon "Users" (users-admin). Meaning: Admin. Draw: two people. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**branch-ghat**
```
Icon "Locations / Ghats" (branch-ghat). Meaning: Settings. Draw: ghat steps with river. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 10-priest-app - Pandit daily operations
_Audience: Backend (Priest portal) - 14 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `my-assignments` | My Assignments | Priest home | clipboard with person |
| `today-schedule` | Today | Priest home | sun over calendar |
| `check-in` | Check-in | Attendance | pin with check |
| `check-out` | Check-out | Attendance | pin with arrow out |
| `ritual-checklist` | Ritual Checklist | Per booking | checklist with diya |
| `samagri-list` | Samagri List | Per booking | basket with list |
| `start-ritual` | Start Ritual | Session | play inside diya |
| `complete-ritual` | Complete Ritual | Session | lotus with check |
| `upload-proof` | Upload Proof | After ritual | camera with up arrow |
| `earnings` | Earnings | Priest finance | coins stack |
| `leave` | Leave / Unavailable | Availability | calendar with minus |
| `navigation` | Navigate to Ghat | Directions | compass needle |
| `devotee-contact` | Contact Devotee | Booking detail | person with phone |
| `notes` | Notes | Booking detail | sticky note |

<details><summary>Prompts</summary>

**my-assignments**
```
Icon "My Assignments" (my-assignments). Meaning: Priest home. Draw: clipboard with person. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**today-schedule**
```
Icon "Today" (today-schedule). Meaning: Priest home. Draw: sun over calendar. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**check-in**
```
Icon "Check-in" (check-in). Meaning: Attendance. Draw: pin with check. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**check-out**
```
Icon "Check-out" (check-out). Meaning: Attendance. Draw: pin with arrow out. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**ritual-checklist**
```
Icon "Ritual Checklist" (ritual-checklist). Meaning: Per booking. Draw: checklist with diya. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**samagri-list**
```
Icon "Samagri List" (samagri-list). Meaning: Per booking. Draw: basket with list. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**start-ritual**
```
Icon "Start Ritual" (start-ritual). Meaning: Session. Draw: play inside diya. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**complete-ritual**
```
Icon "Complete Ritual" (complete-ritual). Meaning: Session. Draw: lotus with check. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**upload-proof**
```
Icon "Upload Proof" (upload-proof). Meaning: After ritual. Draw: camera with up arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**earnings**
```
Icon "Earnings" (earnings). Meaning: Priest finance. Draw: coins stack. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**leave**
```
Icon "Leave / Unavailable" (leave). Meaning: Availability. Draw: calendar with minus. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**navigation**
```
Icon "Navigate to Ghat" (navigation). Meaning: Directions. Draw: compass needle. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**devotee-contact**
```
Icon "Contact Devotee" (devotee-contact). Meaning: Booking detail. Draw: person with phone. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**notes**
```
Icon "Notes" (notes). Meaning: Booking detail. Draw: sticky note. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 11-logistics-prasad - Samagri purchase and prasad shipping
_Audience: Backend - 10 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `packing` | Packing | Fulfilment | open box |
| `packed` | Packed | Fulfilment | closed box with tape |
| `shipped` | Shipped | Fulfilment | truck |
| `out-for-delivery` | Out for Delivery | Tracking | scooter with box |
| `delivered` | Delivered | Tracking | box with check |
| `returned` | Returned | Tracking | box with back arrow |
| `courier` | Courier Partner | Settings | handshake over box |
| `vendor` | Vendor / Supplier | Purchasing | shop awning |
| `purchase-order` | Purchase Order | Purchasing | document with cart |
| `low-stock` | Low Stock | Inventory alert | jar with low level in red |

<details><summary>Prompts</summary>

**packing**
```
Icon "Packing" (packing). Meaning: Fulfilment. Draw: open box. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**packed**
```
Icon "Packed" (packed). Meaning: Fulfilment. Draw: closed box with tape. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**shipped**
```
Icon "Shipped" (shipped). Meaning: Fulfilment. Draw: truck. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**out-for-delivery**
```
Icon "Out for Delivery" (out-for-delivery). Meaning: Tracking. Draw: scooter with box. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**delivered**
```
Icon "Delivered" (delivered). Meaning: Tracking. Draw: box with check. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**returned**
```
Icon "Returned" (returned). Meaning: Tracking. Draw: box with back arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**courier**
```
Icon "Courier Partner" (courier). Meaning: Settings. Draw: handshake over box. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**vendor**
```
Icon "Vendor / Supplier" (vendor). Meaning: Purchasing. Draw: shop awning. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**purchase-order**
```
Icon "Purchase Order" (purchase-order). Meaning: Purchasing. Draw: document with cart. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**low-stock**
```
Icon "Low Stock" (low-stock). Meaning: Inventory alert. Draw: jar with low level in red. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 12-communication - Notifications and messaging
_Audience: Backend - 8 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `sms` | SMS | Reminders | phone with bubble |
| `push` | Push Notification | App | phone with bell |
| `template` | Message Template | Settings | document with brackets |
| `broadcast` | Broadcast | Marketing | tower with waves |
| `inbox` | Inbox | Support | tray with envelope |
| `ticket` | Support Ticket | Support | ticket with headset |
| `feedback` | Feedback | Reviews | bubble with star |
| `schedule-send` | Scheduled Send | Reminders | envelope with clock |

<details><summary>Prompts</summary>

**sms**
```
Icon "SMS" (sms). Meaning: Reminders. Draw: phone with bubble. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**push**
```
Icon "Push Notification" (push). Meaning: App. Draw: phone with bell. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**template**
```
Icon "Message Template" (template). Meaning: Settings. Draw: document with brackets. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**broadcast**
```
Icon "Broadcast" (broadcast). Meaning: Marketing. Draw: tower with waves. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**inbox**
```
Icon "Inbox" (inbox). Meaning: Support. Draw: tray with envelope. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**ticket**
```
Icon "Support Ticket" (ticket). Meaning: Support. Draw: ticket with headset. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**feedback**
```
Icon "Feedback" (feedback). Meaning: Reviews. Draw: bubble with star. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**schedule-send**
```
Icon "Scheduled Send" (schedule-send). Meaning: Reminders. Draw: envelope with clock. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 13-status-states - Semantic status icons (use semantic colour as accent)
_Audience: Frontend + Backend - 15 icons_

| slug | Name | Used in | Draw |
|---|---|---|---|
| `status-held` | Held | Reservation status | hourglass, accent amber #D99A1E |
| `status-confirmed` | Confirmed | Reservation status | circle check, accent green #1F7A4D |
| `status-expired` | Expired | Reservation status | clock with slash, accent grey #8A7F70 |
| `status-cancelled` | Cancelled | Reservation status | circle X, accent red #C0392B |
| `status-pending` | Pending | Orders | three dots in circle, accent amber #D99A1E |
| `status-in-progress` | In Progress | Sessions | half-filled circle, accent blue #2C6E9B |
| `status-completed` | Completed | Sessions | lotus with check, accent green #1F7A4D |
| `status-refunded` | Refunded | Orders | rupee with back arrow, accent blue #2C6E9B |
| `alert-success` | Success | Toasts | check in circle, accent green #1F7A4D |
| `alert-error` | Error | Toasts | exclamation in octagon, accent red #C0392B |
| `alert-warning` | Warning | Toasts | exclamation in triangle, accent amber #D99A1E |
| `alert-info` | Info | Toasts | i in circle, accent blue #2C6E9B |
| `empty-state` | Empty State | Empty lists | unlit diya (illustration-size 96px allowed) |
| `offline` | Offline | Network | cloud with slash, accent grey #8A7F70 |
| `loading` | Loading | Spinners | three-quarter ring |

<details><summary>Prompts</summary>

**status-held**
```
Icon "Held" (status-held). Meaning: Reservation status. Draw: hourglass, accent amber #D99A1E. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**status-confirmed**
```
Icon "Confirmed" (status-confirmed). Meaning: Reservation status. Draw: circle check, accent green #1F7A4D. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**status-expired**
```
Icon "Expired" (status-expired). Meaning: Reservation status. Draw: clock with slash, accent grey #8A7F70. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**status-cancelled**
```
Icon "Cancelled" (status-cancelled). Meaning: Reservation status. Draw: circle X, accent red #C0392B. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**status-pending**
```
Icon "Pending" (status-pending). Meaning: Orders. Draw: three dots in circle, accent amber #D99A1E. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**status-in-progress**
```
Icon "In Progress" (status-in-progress). Meaning: Sessions. Draw: half-filled circle, accent blue #2C6E9B. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**status-completed**
```
Icon "Completed" (status-completed). Meaning: Sessions. Draw: lotus with check, accent green #1F7A4D. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**status-refunded**
```
Icon "Refunded" (status-refunded). Meaning: Orders. Draw: rupee with back arrow, accent blue #2C6E9B. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**alert-success**
```
Icon "Success" (alert-success). Meaning: Toasts. Draw: check in circle, accent green #1F7A4D. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**alert-error**
```
Icon "Error" (alert-error). Meaning: Toasts. Draw: exclamation in octagon, accent red #C0392B. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**alert-warning**
```
Icon "Warning" (alert-warning). Meaning: Toasts. Draw: exclamation in triangle, accent amber #D99A1E. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**alert-info**
```
Icon "Info" (alert-info). Meaning: Toasts. Draw: i in circle, accent blue #2C6E9B. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**empty-state**
```
Icon "Empty State" (empty-state). Meaning: Empty lists. Draw: unlit diya (illustration-size 96px allowed). Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**offline**
```
Icon "Offline" (offline). Meaning: Network. Draw: cloud with slash, accent grey #8A7F70. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**loading**
```
Icon "Loading" (loading). Meaning: Spinners. Draw: three-quarter ring. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, the semantic colour given in the subject instead of red as accent for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>
