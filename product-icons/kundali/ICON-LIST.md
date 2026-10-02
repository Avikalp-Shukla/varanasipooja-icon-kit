# Kundali (apps/jyotisha) - DRAFT

Kundali booking form, report, consultation and admin

**49 icons.** Shared icons (rashi, graha, tithi, calendar, payment, status) come from `system-icons/` and are not repeated.

| Section | Style | Count |
|---|---|---|
| `01-birth-form` | ui | 11 |
| `02-plans` | illus | 4 |
| `03-chart-report` | ui | 28 |
| `04-admin` | ui | 6 |

## Styles

**ui**
```
Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers.
```
**illus**
```
Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, 2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. Export clean SVG viewBox 0 0 64 64.
```

```
Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

Save output as `product-icons/kundali/output/svg/{section}/{slug}.svg`.

## 01-birth-form (ui)

| slug | Name | Used in | Draw |
|---|---|---|---|
| `birth-date` | Date of Birth | dob field | calendar page with small star |
| `birth-time` | Time of Birth | tob field | clock with star at 12 |
| `birth-place` | Place of Birth | pob field, city search | map pin with star in centre |
| `unknown-time` | Time Unknown | unknown_time checkbox | clock with question mark |
| `unknown-gotra` | Gotra Unknown | unknown_gotra checkbox | three-node family tree with question mark |
| `gender-male` | Male | gender | person bust, short hair |
| `gender-female` | Female | gender | person bust, bun hairstyle |
| `gender-other` | Other / Don't know | gender | person bust outline only |
| `latitude-longitude` | Coordinates | auto geo-lookup | globe with crosshair |
| `time-zone-birth` | Birth Time Zone | DST/zone correction | clock over globe |
| `partner-details` | Partner Details | matching form | two busts joined by line |

<details><summary>Prompts</summary>

**birth-date**
```
Icon "Date of Birth" (birth-date). Meaning: dob field. Draw: calendar page with small star. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**birth-time**
```
Icon "Time of Birth" (birth-time). Meaning: tob field. Draw: clock with star at 12. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**birth-place**
```
Icon "Place of Birth" (birth-place). Meaning: pob field, city search. Draw: map pin with star in centre. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**unknown-time**
```
Icon "Time Unknown" (unknown-time). Meaning: unknown_time checkbox. Draw: clock with question mark. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**unknown-gotra**
```
Icon "Gotra Unknown" (unknown-gotra). Meaning: unknown_gotra checkbox. Draw: three-node family tree with question mark. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**gender-male**
```
Icon "Male" (gender-male). Meaning: gender. Draw: person bust, short hair. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**gender-female**
```
Icon "Female" (gender-female). Meaning: gender. Draw: person bust, bun hairstyle. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**gender-other**
```
Icon "Other / Don't know" (gender-other). Meaning: gender. Draw: person bust outline only. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**latitude-longitude**
```
Icon "Coordinates" (latitude-longitude). Meaning: auto geo-lookup. Draw: globe with crosshair. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**time-zone-birth**
```
Icon "Birth Time Zone" (time-zone-birth). Meaning: DST/zone correction. Draw: clock over globe. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**partner-details**
```
Icon "Partner Details" (partner-details). Meaning: matching form. Draw: two busts joined by line. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 02-plans (illus)

| slug | Name | Used in | Draw |
|---|---|---|---|
| `plan-basic` | Basic Kundali | Rs 2100 plan | single scroll, one ring |
| `plan-standard` | Standard Kundali | Rs 2500 plan | scroll with seal |
| `plan-advanced` | Advanced Kundali | Rs 5100 plan | two scrolls with seal and star |
| `plan-complete` | Complete Kundali | Rs 11000 plan | bound book with chart cover and lotus clasp |

<details><summary>Prompts</summary>

**plan-basic**
```
Icon "Basic Kundali" (plan-basic). Meaning: Rs 2100 plan. Draw: single scroll, one ring. Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, 2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. Export clean SVG viewBox 0 0 64 64. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**plan-standard**
```
Icon "Standard Kundali" (plan-standard). Meaning: Rs 2500 plan. Draw: scroll with seal. Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, 2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. Export clean SVG viewBox 0 0 64 64. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**plan-advanced**
```
Icon "Advanced Kundali" (plan-advanced). Meaning: Rs 5100 plan. Draw: two scrolls with seal and star. Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, 2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. Export clean SVG viewBox 0 0 64 64. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**plan-complete**
```
Icon "Complete Kundali" (plan-complete). Meaning: Rs 11000 plan. Draw: bound book with chart cover and lotus clasp. Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, 2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. Export clean SVG viewBox 0 0 64 64. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 03-chart-report (ui)

| slug | Name | Used in | Draw |
|---|---|---|---|
| `chart-north` | North Indian Chart | chart style toggle | square with inner diamond and diagonals |
| `chart-south` | South Indian Chart | chart style toggle | 4x4 grid with empty centre 2x2 |
| `chart-east` | East Indian Chart | chart style toggle | square with 3x3 and corner diagonals |
| `lagna` | Lagna (Ascendant) | report | horizon line with rising arrow and star |
| `bhava-houses` | 12 Bhava | report | wheel of 12 segments |
| `navamsha-d9` | Navamsha (D9) | divisional charts | small chart with 9 dots |
| `divisional-charts` | Varga Charts | report | three stacked mini charts |
| `dasha` | Vimshottari Dasha | report | timeline bar with segments |
| `antardasha` | Antardasha | report | segmented bar with zoom lens |
| `transit-gochar` | Gochar (Transit) | report | planet moving along arc with arrow |
| `planet-degree` | Planet Degrees | report | protractor arc with marker |
| `retrograde` | Vakri (Retrograde) | planet table | planet with backward loop arrow |
| `combust` | Asta (Combust) | planet table | planet partly covered by sun rays |
| `exalted` | Uchcha (Exalted) | planet table | planet with upward chevron |
| `debilitated` | Neecha (Debilitated) | planet table | planet with downward chevron |
| `yoga-detected` | Yoga Found | report | two linked stars |
| `dosha-manglik` | Manglik Dosha | dosha check | triangle (Mangal) with alert dot in red |
| `dosha-kaalsarp` | Kaal Sarp Dosha | dosha check | serpent encircling a chart |
| `dosha-pitru` | Pitru Dosha | dosha check | three ancestral diyas in row |
| `sade-sati` | Sade Sati | dosha check | ringed planet over 3-segment bar |
| `gun-milan` | Guna Milan (36) | matching | two charts with link and score ring |
| `remedy-suggest` | Suggested Remedy | report | lotus with plus |
| `gemstone` | Gemstone | remedy | faceted gem |
| `rudraksha` | Rudraksha | remedy | rudraksha bead with mukhi lines |
| `mantra-remedy` | Mantra | remedy | mala loop around sound wave |
| `pdf-report` | PDF Report | download | document with chart thumbnail and down arrow |
| `consult-astrologer` | Talk to Astrologer | consultation CTA | astrologer bust with speech bubble |
| `expert-reviewed` | Expert Reviewed | trust badge | chart with check seal |

<details><summary>Prompts</summary>

**chart-north**
```
Icon "North Indian Chart" (chart-north). Meaning: chart style toggle. Draw: square with inner diamond and diagonals. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**chart-south**
```
Icon "South Indian Chart" (chart-south). Meaning: chart style toggle. Draw: 4x4 grid with empty centre 2x2. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**chart-east**
```
Icon "East Indian Chart" (chart-east). Meaning: chart style toggle. Draw: square with 3x3 and corner diagonals. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**lagna**
```
Icon "Lagna (Ascendant)" (lagna). Meaning: report. Draw: horizon line with rising arrow and star. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**bhava-houses**
```
Icon "12 Bhava" (bhava-houses). Meaning: report. Draw: wheel of 12 segments. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**navamsha-d9**
```
Icon "Navamsha (D9)" (navamsha-d9). Meaning: divisional charts. Draw: small chart with 9 dots. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**divisional-charts**
```
Icon "Varga Charts" (divisional-charts). Meaning: report. Draw: three stacked mini charts. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**dasha**
```
Icon "Vimshottari Dasha" (dasha). Meaning: report. Draw: timeline bar with segments. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**antardasha**
```
Icon "Antardasha" (antardasha). Meaning: report. Draw: segmented bar with zoom lens. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**transit-gochar**
```
Icon "Gochar (Transit)" (transit-gochar). Meaning: report. Draw: planet moving along arc with arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**planet-degree**
```
Icon "Planet Degrees" (planet-degree). Meaning: report. Draw: protractor arc with marker. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**retrograde**
```
Icon "Vakri (Retrograde)" (retrograde). Meaning: planet table. Draw: planet with backward loop arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**combust**
```
Icon "Asta (Combust)" (combust). Meaning: planet table. Draw: planet partly covered by sun rays. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**exalted**
```
Icon "Uchcha (Exalted)" (exalted). Meaning: planet table. Draw: planet with upward chevron. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**debilitated**
```
Icon "Neecha (Debilitated)" (debilitated). Meaning: planet table. Draw: planet with downward chevron. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**yoga-detected**
```
Icon "Yoga Found" (yoga-detected). Meaning: report. Draw: two linked stars. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**dosha-manglik**
```
Icon "Manglik Dosha" (dosha-manglik). Meaning: dosha check. Draw: triangle (Mangal) with alert dot in red. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**dosha-kaalsarp**
```
Icon "Kaal Sarp Dosha" (dosha-kaalsarp). Meaning: dosha check. Draw: serpent encircling a chart. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**dosha-pitru**
```
Icon "Pitru Dosha" (dosha-pitru). Meaning: dosha check. Draw: three ancestral diyas in row. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**sade-sati**
```
Icon "Sade Sati" (sade-sati). Meaning: dosha check. Draw: ringed planet over 3-segment bar. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**gun-milan**
```
Icon "Guna Milan (36)" (gun-milan). Meaning: matching. Draw: two charts with link and score ring. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**remedy-suggest**
```
Icon "Suggested Remedy" (remedy-suggest). Meaning: report. Draw: lotus with plus. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**gemstone**
```
Icon "Gemstone" (gemstone). Meaning: remedy. Draw: faceted gem. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**rudraksha**
```
Icon "Rudraksha" (rudraksha). Meaning: remedy. Draw: rudraksha bead with mukhi lines. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**mantra-remedy**
```
Icon "Mantra" (mantra-remedy). Meaning: remedy. Draw: mala loop around sound wave. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pdf-report**
```
Icon "PDF Report" (pdf-report). Meaning: download. Draw: document with chart thumbnail and down arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**consult-astrologer**
```
Icon "Talk to Astrologer" (consult-astrologer). Meaning: consultation CTA. Draw: astrologer bust with speech bubble. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**expert-reviewed**
```
Icon "Expert Reviewed" (expert-reviewed). Meaning: trust badge. Draw: chart with check seal. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 04-admin (ui)

| slug | Name | Used in | Draw |
|---|---|---|---|
| `kundali-queue` | Report Queue | admin dashboard | stacked scrolls with clock |
| `assign-astrologer` | Assign Astrologer | admin | astrologer bust with arrow |
| `report-draft` | Draft Report | admin status | scroll with pencil |
| `report-review` | Under Review | admin status | scroll with magnifier |
| `report-delivered` | Delivered | admin status | scroll with check, accent green #1F7A4D |
| `data-verify` | Verify Birth Data | admin | clock and pin with check |

<details><summary>Prompts</summary>

**kundali-queue**
```
Icon "Report Queue" (kundali-queue). Meaning: admin dashboard. Draw: stacked scrolls with clock. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**assign-astrologer**
```
Icon "Assign Astrologer" (assign-astrologer). Meaning: admin. Draw: astrologer bust with arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**report-draft**
```
Icon "Draft Report" (report-draft). Meaning: admin status. Draw: scroll with pencil. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**report-review**
```
Icon "Under Review" (report-review). Meaning: admin status. Draw: scroll with magnifier. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**report-delivered**
```
Icon "Delivered" (report-delivered). Meaning: admin status. Draw: scroll with check, accent green #1F7A4D. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**data-verify**
```
Icon "Verify Birth Data" (data-verify). Meaning: admin. Draw: clock and pin with check. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>
