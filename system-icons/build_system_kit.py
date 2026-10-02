#!/usr/bin/env python3
"""Builds the system (SaaS / service-management) icon list for varanasipooja.com.

Output: SYSTEM-ICON-LIST.md, system-icons.json, system-icons.csv
Each row: section | slug | name | where it is used | symbol (what to draw).
"""
import csv, json, pathlib

HERE = pathlib.Path(__file__).parent

UI_STYLE = (
    "Professional product UI icon, one consistent family. 24x24 grid, 2px live padding, "
    "20x20 safe area, 1.75px stroke, round caps and joins, 2px corner radius. "
    "Duotone: primary outline #A97824 (antique gold), secondary flat fill #F1D592 at 100% "
    "placed only inside key shapes, max one accent #C0392B (kumkum red) for the meaning-carrying detail. "
    "Pixel-snapped, optically balanced, geometric, no gradients, no shadows, no texture, no text/letters "
    "unless specified. Must read clearly at 16px, 20px, 24px and 48px on cream #F3E9D6 and dark #0F0A06. "
    "Export a single clean SVG, viewBox 0 0 24 24, outlined strokes, no hidden layers."
)
STATUS_STYLE = UI_STYLE.replace(
    "max one accent #C0392B (kumkum red)",
    "the semantic colour given in the subject instead of red as accent",
)
NEGATIVE = (
    "Avoid: emoji look, clip-art, cartoon faces, thin hairlines, 3D, glow, sparkles, halos, "
    "random dots, mixed stroke widths, filled blobs, illegible micro-detail, stock-icon clones."
)

# (section, audience, description, [ "slug|Name|Used where|Draw" ])
SECTIONS = [
("01-core-ui", "Frontend + Backend", "Basic actions used on every screen", [
 "menu|Menu|Mobile header, admin sidebar toggle|three horizontal lines, middle shorter",
 "close|Close|Modals, drawers, chips|X made of two rounded strokes",
 "search|Search|Header search, admin tables|magnifier, lens filled light gold",
 "filter|Filter|Service list, admin tables|funnel with fill inside cone",
 "sort|Sort|Tables, listings|up arrow and down arrow side by side",
 "add|Add|Create booking/service/slot|plus inside rounded square",
 "edit|Edit|Edit any record|pencil at 45deg, tip in red",
 "delete|Delete|Remove records|trash bin with lid, two inner lines",
 "save|Save|Forms|check mark inside a document with folded corner",
 "copy|Copy|Copy links/IDs|two overlapping rounded rectangles",
 "share|Share|Service pages, blog|three connected nodes",
 "download|Download|Invoices, reports, recordings|arrow down into tray",
 "upload|Upload|Media, priest photo upload|arrow up out of tray",
 "print|Print|Invoice, receipt|printer with paper",
 "refresh|Refresh|Reload data|circular arrow 300deg",
 "more-horizontal|More|Row actions|three dots horizontal",
 "more-vertical|More (vertical)|Card menus|three dots vertical",
 "chevron-left|Chevron left|Sliders, back|left chevron",
 "chevron-right|Chevron right|Sliders, links|right chevron",
 "chevron-up|Chevron up|Accordions|up chevron",
 "chevron-down|Chevron down|Dropdowns, FAQ|down chevron",
 "arrow-left|Arrow left|Back navigation|arrow with shaft left",
 "arrow-right|Arrow right|CTA buttons|arrow with shaft right",
 "external-link|External link|Outbound links|arrow leaving a square corner",
 "link|Link|Copy URL|two chain links",
 "eye|Show|Password, preview|eye with filled iris",
 "eye-off|Hide|Password|eye with diagonal slash",
 "lock|Lock|Secure payment, locked slot|padlock closed, body filled",
 "unlock|Unlock|Released slot|padlock open shackle",
 "settings|Settings|Account, admin|gear with 8 teeth, centre hole",
 "help|Help|Help centre, tooltips|question mark in circle",
 "info|Info|Notes, hints|letter i in circle",
 "home|Home|Breadcrumb, nav|house with door filled",
 "grid-view|Grid view|Listings toggle|2x2 rounded squares",
 "list-view|List view|Listings toggle|three bullets with lines",
 "fullscreen|Fullscreen|Video, gallery|four corner brackets outward",
 "language|Language|Hindi/English switch|globe with meridian, small 'अ' allowed",
 "dark-mode|Dark mode|Theme toggle|crescent moon",
 "light-mode|Light mode|Theme toggle|sun with 8 short rays",
 "drag-handle|Drag|Reorder lists|six dots 2x3",
]),
("02-navigation-header-footer", "Frontend", "Public site header, mega menu, footer, contact", [
 "phone-call|Call Now|Header CTA, footer|phone handset with two signal arcs",
 "whatsapp|WhatsApp|Booking CTA|speech bubble with handset (brand-safe, not the logo)",
 "email|Email|Footer, contact|envelope with flap filled",
 "location-pin|Location|Ghat/temple address|map pin with filled centre",
 "map|Map|Directions|folded map with route dot in red",
 "clock-hours|Working hours|Footer|clock at 10:10",
 "user-account|My Account|Header|person bust in circle",
 "cart|Cart|Header, checkout|shopping cart with two wheels",
 "book-now|Book Now|Primary CTA|calendar with check mark, check in red",
 "gift-puja|Gift a Puja|Mega menu|gift box with diya on top",
 "blog|Blog|Mega menu|open book with bookmark",
 "gallery|Gallery|Mega menu|photo frame with mountain and sun",
 "video|Videos|Mega menu|play triangle in rounded rectangle",
 "about-trust|About Trust|Footer|shield with lotus",
 "faq|FAQ|Help centre|two speech bubbles with ? and !",
 "social-youtube|YouTube|Footer|rounded rectangle with play (generic)",
 "social-instagram|Instagram|Footer|rounded square camera (generic)",
 "social-facebook|Facebook|Footer|rounded square with f",
 "social-x|X|Footer|letter X in square",
 "breadcrumb-sep|Breadcrumb separator|Breadcrumbs|small chevron dot",
]),
("03-trust-badges", "Frontend", "Conversion and trust strip", [
 "verified-pandit|Verified Pandit|Service cards|priest silhouette with check badge",
 "authentic-vedic|Authentic Vedic|Hero eyebrow|scroll with om mark",
 "secure-payment|Secure Payment|Checkout|shield with padlock",
 "live-streaming|Live Streaming|Service cards|broadcast tower waves around diya",
 "video-proof|Video Proof|Service cards|camera with check",
 "prasad-delivery|Prasad Delivery|Service cards|box with leaf and motion lines",
 "rating-star|Rating|Testimonials|5-point star, filled gold",
 "rating-half|Half star|Testimonials|half-filled star",
 "years-experience|Years of Experience|Stats strip|laurel around number-free medal",
 "devotees-served|Devotees Served|Stats strip|three people group",
 "support-24x7|24x7 Support|Stats strip|headset with mic",
 "nri-friendly|NRI Friendly|Service cards|globe with diya",
 "money-back|Refund Guarantee|Policies|coin with circular arrow",
]),
("04-booking-flow", "Frontend", "Booking engine steps: service > date > slot > sankalp > pay", [
 "step-service|Choose Service|Stepper 1|diya in square",
 "step-date|Choose Date|Stepper 2|calendar page",
 "step-slot|Choose Slot|Stepper 3|clock with filled sector",
 "step-sankalp|Sankalp Details|Stepper 4|hand holding water drop (sankalp)",
 "step-payment|Payment|Stepper 5|card with rupee",
 "step-confirm|Confirmation|Stepper 6|seal with check",
 "calendar|Calendar|Date picker|calendar with two rings",
 "calendar-auspicious|Auspicious Date|Date picker highlight|calendar with small red dot and star",
 "slot-available|Slot Available|Slot grid|clock with check",
 "slot-full|Slot Full|Slot grid|clock with X",
 "slot-held|Slot Held|Reservation timer|hourglass half filled",
 "timer|Hold Timer|Checkout countdown|stopwatch",
 "gotra|Gotra|Sankalp form|family tree with three nodes",
 "devotee-name|Devotee Name|Sankalp form|person with tag",
 "family-members|Family Members|Sankalp form|two adults one child",
 "birth-details|Birth Details|Kundali form|star over calendar",
 "nakshatra-input|Nakshatra|Sankalp form|star cluster of three",
 "intention|Purpose / Wish|Sankalp form|folded hands with spark",
 "pandit-choice|Choose Pandit|Booking options|priest bust with tilak",
 "location-temple|Temple / Ghat Choice|Booking options|temple shikhara with flag",
 "online-mode|Online Puja|Mode selector|laptop with diya on screen",
 "offline-mode|In-person Puja|Mode selector|two people at a havan kund",
 "add-on|Add-on|Upsell|plus in circle with leaf",
 "samagri-included|Samagri Included|Package|basket with flowers",
 "coupon|Coupon|Checkout|ticket with percent",
 "package|Package Tier|Pricing|stack of three layers",
 "quote|Get Quote|Custom puja|document with rupee",
 "dakshina|Dakshina|Checkout|hand offering coin",
]),
("05-payments-finance", "Frontend + Backend", "Razorpay/WooCommerce payments and finance desk", [
 "rupee|Rupee|Prices|rupee sign ₹ bold",
 "upi|UPI|Payment method|phone with arrow tick (generic, no logo)",
 "card|Card|Payment method|credit card with chip",
 "netbanking|Net Banking|Payment method|bank building with pillars",
 "wallet|Wallet|Payment method|wallet with flap",
 "international-pay|International Pay|NRI|globe with card",
 "invoice|Invoice|Account, admin|document with lines and rupee",
 "receipt|Receipt|Account|torn-edge paper",
 "refund|Refund|Admin finance|rupee with back arrow",
 "payout|Priest Payout|Finance|hand receiving coins",
 "gst-tax|GST / Tax|Finance|percent in document",
 "ledger|Ledger|Finance|book with columns",
 "donation|Donation|Trust|hand with heart and coin",
 "80g-certificate|80G Certificate|Donation receipts|certificate with ribbon",
 "revenue|Revenue|Dashboard|rising bar chart with rupee",
 "payment-failed|Payment Failed|Checkout|card with X in red",
]),
("06-devotee-account", "Frontend", "My Account area for devotees", [
 "dashboard-devotee|My Dashboard|Account home|four tiles, one filled",
 "my-bookings|My Bookings|Account|calendar list with diya",
 "upcoming|Upcoming Puja|Account|calendar with right arrow",
 "past-puja|Past Puja|Account|calendar with history arrow",
 "profile|Profile|Account|person card",
 "addresses|Addresses|Prasad delivery|house with pin",
 "saved-family|Saved Family|Sankalp autofill|family with heart",
 "favourites|Favourites|Saved services|heart",
 "notifications|Notifications|Header bell|temple bell with clapper (ghanta)",
 "recordings|Recordings|After puja|film reel with play",
 "photos-proof|Photo Proof|After puja|stacked photos",
 "certificate|Puja Certificate|After puja|scroll with seal",
 "track-prasad|Track Prasad|Delivery|truck with box",
 "reschedule|Reschedule|Booking actions|calendar with circular arrow",
 "cancel-booking|Cancel Booking|Booking actions|calendar with X",
 "rebook|Book Again|Booking actions|repeat arrows around diya",
 "write-review|Write Review|After puja|star with pencil",
 "logout|Logout|Account|door with arrow out",
 "login|Login|Header|door with arrow in",
 "register|Register|Signup|person with plus",
 "otp|OTP|Login|phone with 4 dots",
 "social-google|Google Sign-in|Login|G in circle (generic)",
]),
("07-live-online-puja", "Frontend + Priest", "Live darshan and online sessions", [
 "live-badge|Live|Session pages|dot in red with broadcast arcs",
 "video-call|Video Call|Session join|camera with person",
 "join-session|Join Session|Reminders|door with play",
 "mic-on|Mic On|Session|microphone",
 "mic-off|Mic Off|Session|microphone with slash",
 "camera-on|Camera On|Session|video camera",
 "camera-off|Camera Off|Session|video camera with slash",
 "screen-share|Screen Share|Session|monitor with up arrow",
 "time-zone|Time Zone|NRI scheduling|globe with clock",
 "replay|Replay|Recordings|circular arrow with play",
 "chat|Chat|Session|speech bubble with three dots",
 "raise-hand|Raise Hand|Session|open palm",
]),
("08-panchang-jyotish", "Frontend (Panchang app)", "Panchang calendar and Jyotish tools", [
 "tithi|Tithi|Panchang|moon phase half",
 "nakshatra|Nakshatra|Panchang|star with orbit",
 "yoga-panchang|Yoga|Panchang|two interlocked circles",
 "karana|Karana|Panchang|half circle with dot",
 "vaar|Vaar (weekday)|Panchang|calendar with sun",
 "sunrise|Sunrise|Panchang|half sun over line, arrow up",
 "sunset|Sunset|Panchang|half sun over line, arrow down",
 "moonrise|Moonrise|Panchang|crescent over line, arrow up",
 "moonset|Moonset|Panchang|crescent over line, arrow down",
 "rahu-kaal|Rahu Kaal|Panchang|clock with shaded red sector",
 "abhijit-muhurat|Abhijit Muhurat|Panchang|sun at zenith with check",
 "muhurat|Muhurat|Panchang|hourglass with star",
 "ekadashi|Ekadashi|Festival tag|crescent with leaf",
 "purnima|Purnima|Festival tag|full moon filled",
 "amavasya|Amavasya|Festival tag|outline-only dark moon",
 "festival|Festival|Calendar|diya with flame red",
 "kundali|Kundali|Jyotish|north-Indian diamond chart",
 "rashi-mesh|Mesh (Aries)|Rashifal|ram horns",
 "rashi-vrishabh|Vrishabh (Taurus)|Rashifal|bull head",
 "rashi-mithun|Mithun (Gemini)|Rashifal|twin figures",
 "rashi-kark|Kark (Cancer)|Rashifal|crab claws",
 "rashi-simha|Simha (Leo)|Rashifal|lion mane profile",
 "rashi-kanya|Kanya (Virgo)|Rashifal|maiden with wheat",
 "rashi-tula|Tula (Libra)|Rashifal|balance scale",
 "rashi-vrishchik|Vrishchik (Scorpio)|Rashifal|scorpion tail",
 "rashi-dhanu|Dhanu (Sagittarius)|Rashifal|bow and arrow",
 "rashi-makar|Makar (Capricorn)|Rashifal|crocodile/makara curl",
 "rashi-kumbh|Kumbh (Aquarius)|Rashifal|water pot pouring",
 "rashi-meen|Meen (Pisces)|Rashifal|two fish circling",
 "graha-surya|Surya|Navagraha|sun disc with 12 rays",
 "graha-chandra|Chandra|Navagraha|crescent",
 "graha-mangal|Mangal|Navagraha|triangle in red",
 "graha-budh|Budh|Navagraha|arrow-tipped circle",
 "graha-guru|Guru|Navagraha|yellow disc with stripe",
 "graha-shukra|Shukra|Navagraha|bright 6-point star",
 "graha-shani|Shani|Navagraha|ringed planet",
 "graha-rahu|Rahu|Navagraha|serpent head",
 "graha-ketu|Ketu|Navagraha|serpent tail with flag",
]),
("09-admin-dashboard", "Backend (vp-app admin)", "Booking manager / admin console modules", [
 "admin-dashboard|Dashboard|AdminDashboard|gauge with needle",
 "bookings-admin|Bookings|vp_manage_bookings|clipboard with diya",
 "reservations|Reservations|Reservation table|ticket stub with clock",
 "availability|Availability|vp_manage_availability|calendar grid with green check cells",
 "sessions|Sessions|vp_manage_sessions|calendar with video play",
 "catalog|Service Catalog|Catalog|book with diya on cover",
 "pricing|Pricing Registry|vp-pricing-registry|price tag with rupee",
 "devotees-crm|Devotees (CRM)|vp_view_devotees|address card with person",
 "priests|Priests|vp_priest|three priest busts",
 "roles|Roles|Roles.php|person with shield",
 "permissions|Permissions|Roles.php|key with check",
 "audit-log|Audit Log|vp_view_audit|document with magnifier",
 "reminders|Reminders|Reminders.php|bell with clock",
 "rules|Rules|Rules.php|flowchart with branch",
 "reports|Reports|vp_view_reports|bar chart document",
 "analytics|Analytics|Dashboard|line chart rising",
 "conversion|Conversion|Analytics|funnel with arrow",
 "traffic|Traffic|Analytics|cursor with waves",
 "inventory|Samagri Inventory|Stock|shelves with jars",
 "orders|Orders|WooCommerce|bag with check",
 "coupons-admin|Coupons|Marketing|tickets stack",
 "campaign|Campaign|Marketing|megaphone",
 "content-pages|Pages|CMS|stack of documents",
 "media-library|Media Library|CMS|images grid",
 "seo|SEO|Rank Math|magnifier with up arrow",
 "faq-admin|FAQ Manager|vp-service-faq|list with question mark",
 "import|Import|WP All Import|arrow into database",
 "export|Export|Reports|arrow out of database",
 "integrations|Integrations|Settings|puzzle piece",
 "api|API|REST|curly braces",
 "webhook|Webhook|Integrations|hook with arc",
 "backup|Backup|Ops|cloud with up arrow",
 "security|Security|vp-edge-hardening|shield with check",
 "cache|Cache|Redis|lightning in cylinder",
 "server-health|Server Health|Ops|server with pulse line",
 "content-integrity|Content Integrity|vp-content-integrity|document with shield",
 "users-admin|Users|Admin|two people",
 "branch-ghat|Locations / Ghats|Settings|ghat steps with river",
]),
("10-priest-app", "Backend (Priest portal)", "Pandit daily operations", [
 "my-assignments|My Assignments|Priest home|clipboard with person",
 "today-schedule|Today|Priest home|sun over calendar",
 "check-in|Check-in|Attendance|pin with check",
 "check-out|Check-out|Attendance|pin with arrow out",
 "ritual-checklist|Ritual Checklist|Per booking|checklist with diya",
 "samagri-list|Samagri List|Per booking|basket with list",
 "start-ritual|Start Ritual|Session|play inside diya",
 "complete-ritual|Complete Ritual|Session|lotus with check",
 "upload-proof|Upload Proof|After ritual|camera with up arrow",
 "earnings|Earnings|Priest finance|coins stack",
 "leave|Leave / Unavailable|Availability|calendar with minus",
 "navigation|Navigate to Ghat|Directions|compass needle",
 "devotee-contact|Contact Devotee|Booking detail|person with phone",
 "notes|Notes|Booking detail|sticky note",
]),
("11-logistics-prasad", "Backend", "Samagri purchase and prasad shipping", [
 "packing|Packing|Fulfilment|open box",
 "packed|Packed|Fulfilment|closed box with tape",
 "shipped|Shipped|Fulfilment|truck",
 "out-for-delivery|Out for Delivery|Tracking|scooter with box",
 "delivered|Delivered|Tracking|box with check",
 "returned|Returned|Tracking|box with back arrow",
 "courier|Courier Partner|Settings|handshake over box",
 "vendor|Vendor / Supplier|Purchasing|shop awning",
 "purchase-order|Purchase Order|Purchasing|document with cart",
 "low-stock|Low Stock|Inventory alert|jar with low level in red",
]),
("12-communication", "Backend", "Notifications and messaging", [
 "sms|SMS|Reminders|phone with bubble",
 "push|Push Notification|App|phone with bell",
 "template|Message Template|Settings|document with brackets",
 "broadcast|Broadcast|Marketing|tower with waves",
 "inbox|Inbox|Support|tray with envelope",
 "ticket|Support Ticket|Support|ticket with headset",
 "feedback|Feedback|Reviews|bubble with star",
 "schedule-send|Scheduled Send|Reminders|envelope with clock",
]),
("13-status-states", "Frontend + Backend", "Semantic status icons (use semantic colour as accent)", [
 "status-held|Held|Reservation status|hourglass, accent amber #D99A1E",
 "status-confirmed|Confirmed|Reservation status|circle check, accent green #1F7A4D",
 "status-expired|Expired|Reservation status|clock with slash, accent grey #8A7F70",
 "status-cancelled|Cancelled|Reservation status|circle X, accent red #C0392B",
 "status-pending|Pending|Orders|three dots in circle, accent amber #D99A1E",
 "status-in-progress|In Progress|Sessions|half-filled circle, accent blue #2C6E9B",
 "status-completed|Completed|Sessions|lotus with check, accent green #1F7A4D",
 "status-refunded|Refunded|Orders|rupee with back arrow, accent blue #2C6E9B",
 "alert-success|Success|Toasts|check in circle, accent green #1F7A4D",
 "alert-error|Error|Toasts|exclamation in octagon, accent red #C0392B",
 "alert-warning|Warning|Toasts|exclamation in triangle, accent amber #D99A1E",
 "alert-info|Info|Toasts|i in circle, accent blue #2C6E9B",
 "empty-state|Empty State|Empty lists|unlit diya (illustration-size 96px allowed)",
 "offline|Offline|Network|cloud with slash, accent grey #8A7F70",
 "loading|Loading|Spinners|three-quarter ring",
]),
]

def build():
    rows = []
    for sec, aud, desc, items in SECTIONS:
        style = STATUS_STYLE if sec.startswith("13") else UI_STYLE
        for it in items:
            slug, name, used, draw = it.split("|")
            prompt = f'Icon "{name}" ({slug}). Meaning: {used}. Draw: {draw}. {style} {NEGATIVE}'
            rows.append(dict(section=sec, audience=aud, slug=slug, name=name,
                             used_in=used, draw=draw, prompt=prompt))
    slugs = [r["slug"] for r in rows]
    assert len(slugs) == len(set(slugs)), "duplicate slug"

    (HERE / "system-icons.json").write_text(json.dumps(
        {"style": UI_STYLE, "negative": NEGATIVE, "count": len(rows), "icons": rows},
        ensure_ascii=False, indent=1))
    with open(HERE / "system-icons.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)

    md = ["# varanasipooja.com - System Icon Kit (SaaS / Service Management)", "",
          f"Total: **{len(rows)} icons** across {len(SECTIONS)} sections. "
          "Separate from the 200 devotional service icons in the repo root.", "",
          "## Summary", "", "| # | Section | Audience | Purpose | Count |", "|---|---|---|---|---|"]
    for i, (sec, aud, desc, items) in enumerate(SECTIONS, 1):
        md.append(f"| {i} | `{sec}` | {aud} | {desc} | {len(items)} |")
    md += ["", f"**Grand total: {len(rows)}**", "",
           "## Master style (paste once, or append to every prompt)", "", "```", UI_STYLE, "", NEGATIVE, "```", "",
           "## Output rules", "",
           "- Save each as `system-icons/output/svg/{section}/{slug}.svg` (viewBox 0 0 24 24).",
           "- Status icons (section 13) use their semantic accent colour instead of red.",
           "- No emoji, no brand logos copied verbatim (social/payment icons are generic).", ""]
    for sec, aud, desc, items in SECTIONS:
        md += [f"## {sec} - {desc}", f"_Audience: {aud} - {len(items)} icons_", "",
               "| slug | Name | Used in | Draw |", "|---|---|---|---|"]
        md += [f"| `{r['slug']}` | {r['name']} | {r['used_in']} | {r['draw']} |"
               for r in rows if r["section"] == sec]
        md += ["", "<details><summary>Prompts</summary>", ""]
        md += [f"**{r['slug']}**\n```\n{r['prompt']}\n```" for r in rows if r["section"] == sec]
        md += ["", "</details>", ""]
    (HERE / "SYSTEM-ICON-LIST.md").write_text("\n".join(md))
    for sec, *_ in SECTIONS:
        d = HERE / "output" / "svg" / sec; d.mkdir(parents=True, exist_ok=True)
        (d / ".gitkeep").touch()
    print(len(rows), "icons")

if __name__ == "__main__":
    build()
