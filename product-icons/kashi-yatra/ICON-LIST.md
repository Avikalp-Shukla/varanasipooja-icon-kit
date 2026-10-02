# Kashi Yatra - 3D map (scaffolded)

Interactive 3D map of Varanasi across eras

**51 icons.** Shared icons (rashi, graha, tithi, calendar, payment, status) come from `system-icons/` and are not repeated.

| Section | Style | Count |
|---|---|---|
| `01-map-markers` | map | 20 |
| `02-eras-timeline` | illus | 5 |
| `03-routes-yatra` | ui | 12 |
| `04-map-controls` | ui | 14 |

## Styles

**ui**
```
Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers.
```
**illus**
```
Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, 2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. Export clean SVG viewBox 0 0 64 64.
```
**map**
```
3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin.
```

```
Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

Save output as `product-icons/kashi-yatra/output/svg/{section}/{slug}.svg`.

## 01-map-markers (map)

| slug | Name | Used in | Draw |
|---|---|---|---|
| `pin-jyotirlinga` | Jyotirlinga | Kashi Vishwanath | shivling with crescent |
| `pin-shiva-temple` | Shiva Temple | temples | trishul |
| `pin-devi-temple` | Devi Temple | Annapurna, Durga Kund | lotus with trident tips |
| `pin-bhairav` | Bhairav | Kaal Bhairav | danda staff with dog silhouette small |
| `pin-hanuman` | Hanuman | Sankat Mochan | gada (mace) |
| `pin-vishnu-ram` | Vishnu / Ram | Tulsi Manas Mandir | conch and chakra |
| `pin-ghat` | Ghat | 84 ghats | steps descending into water |
| `pin-cremation-ghat` | Moksha Ghat | Manikarnika, Harishchandra | flame over steps |
| `pin-aarti` | Ganga Aarti | Dashashwamedh | multi-tier aarti lamp |
| `pin-kund` | Kund / Tank | Durga Kund, Lolark | square water tank |
| `pin-buddhist` | Buddhist Site | Sarnath, Dhamek | stupa |
| `pin-fort` | Fort / Palace | Ramnagar Fort | fort wall with turrets |
| `pin-university` | University | BHU | book with gate arch |
| `pin-heritage` | Heritage Landmark | history layer | column |
| `pin-craft` | Living Craft | Banarasi weaving | loom shuttle |
| `pin-music` | Music Gharana | living traditions | tanpura |
| `pin-food` | Food Trail | living traditions | kulhad cup |
| `pin-boat` | Boat Ride | ghats | wooden boat |
| `pin-puja-service` | Book Puja Here | integration CTA | diya with plus |
| `pin-you-are-here` | You Are Here | navigation | filled circle with pulse ring |

<details><summary>Prompts</summary>

**pin-jyotirlinga**
```
Icon "Jyotirlinga" (pin-jyotirlinga). Meaning: Kashi Vishwanath. Draw: shivling with crescent. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-shiva-temple**
```
Icon "Shiva Temple" (pin-shiva-temple). Meaning: temples. Draw: trishul. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-devi-temple**
```
Icon "Devi Temple" (pin-devi-temple). Meaning: Annapurna, Durga Kund. Draw: lotus with trident tips. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-bhairav**
```
Icon "Bhairav" (pin-bhairav). Meaning: Kaal Bhairav. Draw: danda staff with dog silhouette small. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-hanuman**
```
Icon "Hanuman" (pin-hanuman). Meaning: Sankat Mochan. Draw: gada (mace). 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-vishnu-ram**
```
Icon "Vishnu / Ram" (pin-vishnu-ram). Meaning: Tulsi Manas Mandir. Draw: conch and chakra. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-ghat**
```
Icon "Ghat" (pin-ghat). Meaning: 84 ghats. Draw: steps descending into water. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-cremation-ghat**
```
Icon "Moksha Ghat" (pin-cremation-ghat). Meaning: Manikarnika, Harishchandra. Draw: flame over steps. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-aarti**
```
Icon "Ganga Aarti" (pin-aarti). Meaning: Dashashwamedh. Draw: multi-tier aarti lamp. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-kund**
```
Icon "Kund / Tank" (pin-kund). Meaning: Durga Kund, Lolark. Draw: square water tank. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-buddhist**
```
Icon "Buddhist Site" (pin-buddhist). Meaning: Sarnath, Dhamek. Draw: stupa. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-fort**
```
Icon "Fort / Palace" (pin-fort). Meaning: Ramnagar Fort. Draw: fort wall with turrets. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-university**
```
Icon "University" (pin-university). Meaning: BHU. Draw: book with gate arch. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-heritage**
```
Icon "Heritage Landmark" (pin-heritage). Meaning: history layer. Draw: column. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-craft**
```
Icon "Living Craft" (pin-craft). Meaning: Banarasi weaving. Draw: loom shuttle. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-music**
```
Icon "Music Gharana" (pin-music). Meaning: living traditions. Draw: tanpura. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-food**
```
Icon "Food Trail" (pin-food). Meaning: living traditions. Draw: kulhad cup. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-boat**
```
Icon "Boat Ride" (pin-boat). Meaning: ghats. Draw: wooden boat. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-puja-service**
```
Icon "Book Puja Here" (pin-puja-service). Meaning: integration CTA. Draw: diya with plus. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**pin-you-are-here**
```
Icon "You Are Here" (pin-you-are-here). Meaning: navigation. Draw: filled circle with pulse ring. 3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 02-eras-timeline (illus)

| slug | Name | Used in | Draw |
|---|---|---|---|
| `era-pauranik` | Pauranik Kaal | Phase 1 | Shiva trident with Ganga flowing from crescent |
| `era-historical` | Historical Kaal | Phase 2 | stupa and temple shikhara side by side |
| `era-modern` | Modern Kashi | Phase 3 | Vishwanath Dham corridor gateway |
| `timeline` | Timeline | era slider | horizontal line with three nodes |
| `time-travel` | Switch Era | era change | hourglass with circular arrow |

<details><summary>Prompts</summary>

**era-pauranik**
```
Icon "Pauranik Kaal" (era-pauranik). Meaning: Phase 1. Draw: Shiva trident with Ganga flowing from crescent. Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, 2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. Export clean SVG viewBox 0 0 64 64. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**era-historical**
```
Icon "Historical Kaal" (era-historical). Meaning: Phase 2. Draw: stupa and temple shikhara side by side. Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, 2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. Export clean SVG viewBox 0 0 64 64. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**era-modern**
```
Icon "Modern Kashi" (era-modern). Meaning: Phase 3. Draw: Vishwanath Dham corridor gateway. Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, 2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. Export clean SVG viewBox 0 0 64 64. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**timeline**
```
Icon "Timeline" (timeline). Meaning: era slider. Draw: horizontal line with three nodes. Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, 2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. Export clean SVG viewBox 0 0 64 64. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**time-travel**
```
Icon "Switch Era" (time-travel). Meaning: era change. Draw: hourglass with circular arrow. Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, 2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. Export clean SVG viewBox 0 0 64 64. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 03-routes-yatra (ui)

| slug | Name | Used in | Draw |
|---|---|---|---|
| `route-panchkoshi` | Panch-Koshi Parikrama | 50 km circuit | closed loop path with five dots |
| `route-antargrihi` | Antargrihi Yatra | inner circuit | small loop inside larger loop |
| `route-ghat-walk` | Ghat Walk | riverfront route | footprints along wavy line |
| `route-custom` | My Yatra Plan | itinerary builder | path with flag and plus |
| `waypoint` | Waypoint | route stop | diamond marker |
| `distance` | Distance | route info | ruler with arrows |
| `walk-time` | Walking Time | route info | footprint with clock |
| `river-ganga` | Ganga | map layer | three wavy lines |
| `itinerary-day` | Day Plan | itinerary | calendar with path |
| `audio-guide` | Audio Guide | location card | headphones with leaf |
| `story-myth` | Katha / Legend | location card | open scroll with flame |
| `photo-360` | 360 View | location card | camera with circular arrow |

<details><summary>Prompts</summary>

**route-panchkoshi**
```
Icon "Panch-Koshi Parikrama" (route-panchkoshi). Meaning: 50 km circuit. Draw: closed loop path with five dots. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**route-antargrihi**
```
Icon "Antargrihi Yatra" (route-antargrihi). Meaning: inner circuit. Draw: small loop inside larger loop. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**route-ghat-walk**
```
Icon "Ghat Walk" (route-ghat-walk). Meaning: riverfront route. Draw: footprints along wavy line. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**route-custom**
```
Icon "My Yatra Plan" (route-custom). Meaning: itinerary builder. Draw: path with flag and plus. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**waypoint**
```
Icon "Waypoint" (waypoint). Meaning: route stop. Draw: diamond marker. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**distance**
```
Icon "Distance" (distance). Meaning: route info. Draw: ruler with arrows. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**walk-time**
```
Icon "Walking Time" (walk-time). Meaning: route info. Draw: footprint with clock. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**river-ganga**
```
Icon "Ganga" (river-ganga). Meaning: map layer. Draw: three wavy lines. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**itinerary-day**
```
Icon "Day Plan" (itinerary-day). Meaning: itinerary. Draw: calendar with path. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**audio-guide**
```
Icon "Audio Guide" (audio-guide). Meaning: location card. Draw: headphones with leaf. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**story-myth**
```
Icon "Katha / Legend" (story-myth). Meaning: location card. Draw: open scroll with flame. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**photo-360**
```
Icon "360 View" (photo-360). Meaning: location card. Draw: camera with circular arrow. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>

## 04-map-controls (ui)

| slug | Name | Used in | Draw |
|---|---|---|---|
| `layers` | Layers | map | three stacked rhombuses |
| `layer-temples` | Temples Layer | layer toggle | shikhara |
| `layer-ghats` | Ghats Layer | layer toggle | steps |
| `layer-history` | History Layer | layer toggle | column |
| `layer-panchang` | Panchang Overlay | auspicious times | sun with clock |
| `fly-mode` | Fly Mode | camera | bird in flight |
| `walk-mode` | Walk Mode | camera | walking person |
| `orbit` | Orbit | camera | ellipse orbit around dot |
| `compass` | Compass North | map | compass rose N needle red |
| `recenter` | Recenter | map | crosshair |
| `terrain-3d` | 3D Terrain | toggle | mountain wireframe |
| `day-night` | Day / Night | lighting | half sun half moon |
| `street-search` | Find Place | search | magnifier over pin |
| `bookmark-place` | Save Place | user | bookmark with pin |

<details><summary>Prompts</summary>

**layers**
```
Icon "Layers" (layers). Meaning: map. Draw: three stacked rhombuses. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**layer-temples**
```
Icon "Temples Layer" (layer-temples). Meaning: layer toggle. Draw: shikhara. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**layer-ghats**
```
Icon "Ghats Layer" (layer-ghats). Meaning: layer toggle. Draw: steps. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**layer-history**
```
Icon "History Layer" (layer-history). Meaning: layer toggle. Draw: column. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**layer-panchang**
```
Icon "Panchang Overlay" (layer-panchang). Meaning: auspicious times. Draw: sun with clock. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**fly-mode**
```
Icon "Fly Mode" (fly-mode). Meaning: camera. Draw: bird in flight. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**walk-mode**
```
Icon "Walk Mode" (walk-mode). Meaning: camera. Draw: walking person. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**orbit**
```
Icon "Orbit" (orbit). Meaning: camera. Draw: ellipse orbit around dot. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**compass**
```
Icon "Compass North" (compass). Meaning: map. Draw: compass rose N needle red. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**recenter**
```
Icon "Recenter" (recenter). Meaning: map. Draw: crosshair. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**terrain-3d**
```
Icon "3D Terrain" (terrain-3d). Meaning: toggle. Draw: mountain wireframe. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**day-night**
```
Icon "Day / Night" (day-night). Meaning: lighting. Draw: half sun half moon. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**street-search**
```
Icon "Find Place" (street-search). Meaning: search. Draw: magnifier over pin. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```
**bookmark-place**
```
Icon "Save Place" (bookmark-place). Meaning: user. Draw: bookmark with pin. Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, 20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers. Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones.
```

</details>
