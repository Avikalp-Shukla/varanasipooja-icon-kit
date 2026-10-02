#!/usr/bin/env python3
"""Icon kits for draft products: Kundali (apps/jyotisha), Jyotisha Pasha, Kashi Yatra.

Researched from the site repo:
- kundali/kundli-booking-online.php : fields dob, tob, pob, gender, gotra, rashi, nakshatra,
  unknown_time, unknown_gotra, notes; plans Basic 2100 / Standard 2500 / Advanced 5100 / Complete 11000;
  admin login/dashboard/view_booking.
- jyotisha-pasha/docs : 4-faced pashaka (1-4), three ordered casts, 64 keys 111-444, modes A-D,
  question categories, remedy/seva/donation, expert review gate, 3D + sound. No guaranteed outcomes.
- kashi-yatra/docs : 3D map, eras Pauranik/Historical/Modern, temples, ghats, Panch-Koshi,
  Antargrihi, layers, booking from map, panchang overlay.

Shared icons (12 rashi, 9 graha, tithi, nakshatra, calendar, payment, status) are NOT repeated here:
they live in system-icons/ (sections 05, 08, 13). Each product lists only what is new.
Outputs per product: <product>/ICON-LIST.md, icons.json, icons.csv, output/svg/<section>/.gitkeep
"""
import csv, json, pathlib, sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "system-icons"))
from build_system_kit import UI_STYLE, NEGATIVE  # same family as the system kit

ILLUS_STYLE = (
    "Premium feature icon (larger than UI icons), same family as the UI set. 64x64 grid, 4px padding, "
    "2.5px stroke, round caps/joins. Duotone: outline #A97824, flat fill #F1D592, one accent #C0392B. "
    "Authentic Indian iconography drawn with restraint and correct proportions, geometric construction, "
    "no gradients, no shadows, no text. Must read at 32px and 96px on cream #F3E9D6 and dark #0F0A06. "
    "Export clean SVG viewBox 0 0 64 64."
)
MAP_STYLE = (
    "3D-map marker icon for a WebGL city map. 48x48 grid: a teardrop pin (#A97824 outline, #F1D592 fill) "
    "with a 24px symbol inside, 2px stroke, flat, high contrast, readable at 28px over satellite imagery "
    "and over dark night map #0F0A06. Accent #C0392B only for the meaning detail. No text. "
    "Export SVG viewBox 0 0 48 48, plus a symbol-only variant without the pin."
)
STYLES = {"ui": UI_STYLE, "illus": ILLUS_STYLE, "map": MAP_STYLE}

PRODUCTS = {
"kundali": ("Kundali (apps/jyotisha) - DRAFT", "Kundali booking form, report, consultation and admin", [
 ("01-birth-form", "ui", [
  "birth-date|Date of Birth|dob field|calendar page with small star",
  "birth-time|Time of Birth|tob field|clock with star at 12",
  "birth-place|Place of Birth|pob field, city search|map pin with star in centre",
  "unknown-time|Time Unknown|unknown_time checkbox|clock with question mark",
  "unknown-gotra|Gotra Unknown|unknown_gotra checkbox|three-node family tree with question mark",
  "gender-male|Male|gender|person bust, short hair",
  "gender-female|Female|gender|person bust, bun hairstyle",
  "gender-other|Other / Don't know|gender|person bust outline only",
  "latitude-longitude|Coordinates|auto geo-lookup|globe with crosshair",
  "time-zone-birth|Birth Time Zone|DST/zone correction|clock over globe",
  "partner-details|Partner Details|matching form|two busts joined by line",
 ]),
 ("02-plans", "illus", [
  "plan-basic|Basic Kundali|Rs 2100 plan|single scroll, one ring",
  "plan-standard|Standard Kundali|Rs 2500 plan|scroll with seal",
  "plan-advanced|Advanced Kundali|Rs 5100 plan|two scrolls with seal and star",
  "plan-complete|Complete Kundali|Rs 11000 plan|bound book with chart cover and lotus clasp",
 ]),
 ("03-chart-report", "ui", [
  "chart-north|North Indian Chart|chart style toggle|square with inner diamond and diagonals",
  "chart-south|South Indian Chart|chart style toggle|4x4 grid with empty centre 2x2",
  "chart-east|East Indian Chart|chart style toggle|square with 3x3 and corner diagonals",
  "lagna|Lagna (Ascendant)|report|horizon line with rising arrow and star",
  "bhava-houses|12 Bhava|report|wheel of 12 segments",
  "navamsha-d9|Navamsha (D9)|divisional charts|small chart with 9 dots",
  "divisional-charts|Varga Charts|report|three stacked mini charts",
  "dasha|Vimshottari Dasha|report|timeline bar with segments",
  "antardasha|Antardasha|report|segmented bar with zoom lens",
  "transit-gochar|Gochar (Transit)|report|planet moving along arc with arrow",
  "planet-degree|Planet Degrees|report|protractor arc with marker",
  "retrograde|Vakri (Retrograde)|planet table|planet with backward loop arrow",
  "combust|Asta (Combust)|planet table|planet partly covered by sun rays",
  "exalted|Uchcha (Exalted)|planet table|planet with upward chevron",
  "debilitated|Neecha (Debilitated)|planet table|planet with downward chevron",
  "yoga-detected|Yoga Found|report|two linked stars",
  "dosha-manglik|Manglik Dosha|dosha check|triangle (Mangal) with alert dot in red",
  "dosha-kaalsarp|Kaal Sarp Dosha|dosha check|serpent encircling a chart",
  "dosha-pitru|Pitru Dosha|dosha check|three ancestral diyas in row",
  "sade-sati|Sade Sati|dosha check|ringed planet over 3-segment bar",
  "gun-milan|Guna Milan (36)|matching|two charts with link and score ring",
  "remedy-suggest|Suggested Remedy|report|lotus with plus",
  "gemstone|Gemstone|remedy|faceted gem",
  "rudraksha|Rudraksha|remedy|rudraksha bead with mukhi lines",
  "mantra-remedy|Mantra|remedy|mala loop around sound wave",
  "pdf-report|PDF Report|download|document with chart thumbnail and down arrow",
  "consult-astrologer|Talk to Astrologer|consultation CTA|astrologer bust with speech bubble",
  "expert-reviewed|Expert Reviewed|trust badge|chart with check seal",
 ]),
 ("04-admin", "ui", [
  "kundali-queue|Report Queue|admin dashboard|stacked scrolls with clock",
  "assign-astrologer|Assign Astrologer|admin|astrologer bust with arrow",
  "report-draft|Draft Report|admin status|scroll with pencil",
  "report-review|Under Review|admin status|scroll with magnifier",
  "report-delivered|Delivered|admin status|scroll with check, accent green #1F7A4D",
  "data-verify|Verify Birth Data|admin|clock and pin with check",
 ]),
]),
"jyotisha-pasha": ("Jyotisha Pasha - RESEARCH PHASE", "Prashna-Jyotisha interactive 3D experience", [
 ("01-pasha-game", "illus", [
  "pashaka-die|Pashaka (four-sided die)|core object|elongated four-sided oblong die, pips on visible face",
  "pasha-face-1|Face 1|cast result|die face with one pip",
  "pasha-face-2|Face 2|cast result|die face with two pips",
  "pasha-face-3|Face 3|cast result|die face with three pips",
  "pasha-face-4|Face 4|cast result|die face with four pips",
  "cast-throw|Cast the Pasha|primary action|hand releasing die with motion arc",
  "cast-count|Three Casts|progress|three die slots, first filled",
  "key-64|64 Keys|result key (111-444)|8x8 grid with one cell accented",
  "oracle-verse|Oracle Verse|result text|palm-leaf manuscript",
  "dual-reading|Dual Reading (Mode C)|mode switch|two open leaves side by side",
  "prashna-chart|Prashna Chart (Mode B)|mode switch|chart square with question dot",
  "historic-oracle|Historic Oracle (Mode A)|mode switch|old manuscript with die",
  "spiritual-game|Spiritual Game (Mode D)|mode switch|die inside lotus",
  "sankalp-question|Ask Your Question|question entry|folded hands with question bubble",
  "shuffle-ritual|Prepare / Dhyana|pre-cast step|diya with breath waves",
 ]),
 ("02-question-categories", "ui", [
  "q-career|Career / Work|question category|briefcase",
  "q-wealth|Wealth|question category|kalash with coins",
  "q-marriage|Marriage|question category|two garlands joined",
  "q-family|Family|question category|house with three people",
  "q-health|Health|question category|leaf with pulse line",
  "q-education|Education|question category|book with quill",
  "q-travel|Travel|question category|path with footprints",
  "q-lost-item|Lost Item|question category|magnifier over box",
  "q-legal|Legal Matter|question category|balance scale",
  "q-spiritual|Spiritual Path|question category|lotus with rising flame",
 ]),
 ("03-remedy-seva", "ui", [
  "seva-gau|Gau Seva|remedy|cow head side profile, gentle",
  "seva-annadan|Anna Daan|remedy|bowl of rice with ladle",
  "seva-bird-feed|Bird Feeding|remedy|grain bowl with bird",
  "seva-fish-feed|Fish Feeding|remedy|fish with grain dots over water line",
  "seva-deep-daan|Deep Daan|remedy|diya on leaf floating on water",
  "seva-vastra-daan|Vastra Daan|remedy|folded cloth",
  "graha-shanti-puja|Graha Shanti|remedy booking|havan kund with nine dots",
  "donate|Donate|donation flow|hand with diya",
  "seva-proof|Seva Proof|fulfilment|camera with leaf",
  "source-cited|Source Cited|research transparency|book with bookmark and check",
  "not-verified|Not Verified|research status|book with question, accent grey #8A7F70",
  "expert-gate|Expert Review|admin gate|scholar bust with seal",
  "disclaimer|Guidance Not Guarantee|safety notice|shield with info i",
 ]),
 ("04-3d-controls", "ui", [
  "rotate-3d|Rotate|3D scene|circular arrow around cube",
  "zoom-in|Zoom In|3D scene|magnifier plus",
  "zoom-out|Zoom Out|3D scene|magnifier minus",
  "sound-on|Sound On|ambient audio|speaker with waves",
  "sound-off|Sound Off|ambient audio|speaker with slash",
  "reduce-motion|Reduce Motion|accessibility|wave with pause bars",
  "replay-cast|Replay Cast|animation|circular arrow with die",
  "share-result|Share Reading|result|leaf with share nodes",
 ]),
]),
"kashi-yatra": ("Kashi Yatra - 3D map (scaffolded)", "Interactive 3D map of Varanasi across eras", [
 ("01-map-markers", "map", [
  "pin-jyotirlinga|Jyotirlinga|Kashi Vishwanath|shivling with crescent",
  "pin-shiva-temple|Shiva Temple|temples|trishul",
  "pin-devi-temple|Devi Temple|Annapurna, Durga Kund|lotus with trident tips",
  "pin-bhairav|Bhairav|Kaal Bhairav|danda staff with dog silhouette small",
  "pin-hanuman|Hanuman|Sankat Mochan|gada (mace)",
  "pin-vishnu-ram|Vishnu / Ram|Tulsi Manas Mandir|conch and chakra",
  "pin-ghat|Ghat|84 ghats|steps descending into water",
  "pin-cremation-ghat|Moksha Ghat|Manikarnika, Harishchandra|flame over steps",
  "pin-aarti|Ganga Aarti|Dashashwamedh|multi-tier aarti lamp",
  "pin-kund|Kund / Tank|Durga Kund, Lolark|square water tank",
  "pin-buddhist|Buddhist Site|Sarnath, Dhamek|stupa",
  "pin-fort|Fort / Palace|Ramnagar Fort|fort wall with turrets",
  "pin-university|University|BHU|book with gate arch",
  "pin-heritage|Heritage Landmark|history layer|column",
  "pin-craft|Living Craft|Banarasi weaving|loom shuttle",
  "pin-music|Music Gharana|living traditions|tanpura",
  "pin-food|Food Trail|living traditions|kulhad cup",
  "pin-boat|Boat Ride|ghats|wooden boat",
  "pin-puja-service|Book Puja Here|integration CTA|diya with plus",
  "pin-you-are-here|You Are Here|navigation|filled circle with pulse ring",
 ]),
 ("02-eras-timeline", "illus", [
  "era-pauranik|Pauranik Kaal|Phase 1|Shiva trident with Ganga flowing from crescent",
  "era-historical|Historical Kaal|Phase 2|stupa and temple shikhara side by side",
  "era-modern|Modern Kashi|Phase 3|Vishwanath Dham corridor gateway",
  "timeline|Timeline|era slider|horizontal line with three nodes",
  "time-travel|Switch Era|era change|hourglass with circular arrow",
 ]),
 ("03-routes-yatra", "ui", [
  "route-panchkoshi|Panch-Koshi Parikrama|50 km circuit|closed loop path with five dots",
  "route-antargrihi|Antargrihi Yatra|inner circuit|small loop inside larger loop",
  "route-ghat-walk|Ghat Walk|riverfront route|footprints along wavy line",
  "route-custom|My Yatra Plan|itinerary builder|path with flag and plus",
  "waypoint|Waypoint|route stop|diamond marker",
  "distance|Distance|route info|ruler with arrows",
  "walk-time|Walking Time|route info|footprint with clock",
  "river-ganga|Ganga|map layer|three wavy lines",
  "itinerary-day|Day Plan|itinerary|calendar with path",
  "audio-guide|Audio Guide|location card|headphones with leaf",
  "story-myth|Katha / Legend|location card|open scroll with flame",
  "photo-360|360 View|location card|camera with circular arrow",
 ]),
 ("04-map-controls", "ui", [
  "layers|Layers|map|three stacked rhombuses",
  "layer-temples|Temples Layer|layer toggle|shikhara",
  "layer-ghats|Ghats Layer|layer toggle|steps",
  "layer-history|History Layer|layer toggle|column",
  "layer-panchang|Panchang Overlay|auspicious times|sun with clock",
  "fly-mode|Fly Mode|camera|bird in flight",
  "walk-mode|Walk Mode|camera|walking person",
  "orbit|Orbit|camera|ellipse orbit around dot",
  "compass|Compass North|map|compass rose N needle red",
  "recenter|Recenter|map|crosshair",
  "terrain-3d|3D Terrain|toggle|mountain wireframe",
  "day-night|Day / Night|lighting|half sun half moon",
  "street-search|Find Place|search|magnifier over pin",
  "bookmark-place|Save Place|user|bookmark with pin",
 ]),
]),
}

def build():
    grand = 0
    for prod, (title, desc, sections) in PRODUCTS.items():
        out = HERE / prod
        rows = []
        for sec, sty, items in sections:
            for it in items:
                slug, name, used, draw = it.split("|")
                rows.append(dict(product=prod, section=sec, style=sty, slug=slug, name=name,
                                 used_in=used, draw=draw,
                                 prompt=f'Icon "{name}" ({slug}). Meaning: {used}. Draw: {draw}. {STYLES[sty]} {NEGATIVE}'))
            (out / "output" / "svg" / sec).mkdir(parents=True, exist_ok=True)
            (out / "output" / "svg" / sec / ".gitkeep").touch()
        slugs = [r["slug"] for r in rows]
        assert len(slugs) == len(set(slugs)), prod
        (out / "icons.json").write_text(json.dumps({"product": prod, "count": len(rows),
            "styles": STYLES, "negative": NEGATIVE, "icons": rows}, ensure_ascii=False, indent=1))
        with open(out / "icons.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
        md = [f"# {title}", "", desc, "", f"**{len(rows)} icons.** Shared icons (rashi, graha, tithi, "
              "calendar, payment, status) come from `system-icons/` and are not repeated.", "",
              "| Section | Style | Count |", "|---|---|---|"]
        md += [f"| `{s}` | {st} | {len(i)} |" for s, st, i in sections]
        md += ["", "## Styles", ""] + [f"**{k}**\n```\n{v}\n```" for k, v in STYLES.items()
                                        if any(st == k for _, st, _ in sections)]
        md += ["", "```", NEGATIVE, "```", "",
               f"Save output as `product-icons/{prod}/output/svg/{{section}}/{{slug}}.svg`.", ""]
        for sec, sty, items in sections:
            md += [f"## {sec} ({sty})", "", "| slug | Name | Used in | Draw |", "|---|---|---|---|"]
            md += [f"| `{r['slug']}` | {r['name']} | {r['used_in']} | {r['draw']} |" for r in rows if r["section"] == sec]
            md += ["", "<details><summary>Prompts</summary>", ""]
            md += [f"**{r['slug']}**\n```\n{r['prompt']}\n```" for r in rows if r["section"] == sec]
            md += ["", "</details>", ""]
        (out / "ICON-LIST.md").write_text("\n".join(md))
        print(prod, len(rows)); grand += len(rows)
    idx = ["# Product icon kits (draft products)", "",
           "| Product | Status | Icons | List |", "|---|---|---|---|"]
    for prod, (title, _, secs) in PRODUCTS.items():
        idx.append(f"| {prod} | {title.split(' - ')[-1]} | {sum(len(i) for _,_,i in secs)} | [{prod}/ICON-LIST.md]({prod}/ICON-LIST.md) |")
    idx += ["", f"**Total: {grand}**", "",
            "Build these only when the product leaves draft. Shared base icons: `../system-icons/`."]
    (HERE / "README.md").write_text("\n".join(idx)); print("total", grand)

if __name__ == "__main__":
    build()
