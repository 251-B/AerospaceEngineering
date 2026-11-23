"""Build the AeroVanguard final presentation (Canva base PPTX), its charts and its guide.

One source of truth: every on-screen text, speaker script, source line and Q&A answer
lives in this file; the PPTX (slides + speaker notes), the three charts and the Markdown
guide are all generated from it, so they cannot drift apart. Slide timings are computed
from the spoken script (numbers are written as they are said), never typed by hand.

Every figure comes from the final Business Plan (.tex) and the Excel model
(AeroVanguard_Financial_Model.xlsx). Run:  python build_deck.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
OUT_PPTX = HERE / "AeroVanguard_Canva_Base.pptx"
OUT_MD = HERE / "AeroVanguard_Presentation_Guide.md"

NAVY = RGBColor(0x1F, 0x38, 0x64)
ICE = RGBColor(0xE7, 0xEC, 0xF5)
MIDNAVY = RGBColor(0x2B, 0x4A, 0x7E)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
INK = RGBColor(0x1A, 0x1F, 0x2B)
MUTED = RGBColor(0x4A, 0x55, 0x68)
TEAL = RGBColor(0x23, 0x70, 0x6C)    # darkened teal: 5.6:1 on white
ORANGE = RGBColor(0xE8, 0x93, 0x3A)  # accent used only on navy (contrast > 4.5:1)
HEX = {"navy": "#1F3864", "teal": "#2E8B87", "orange": "#D9822B", "grey": "#8C8C8C",
       "ink": "#1A1F2B", "muted": "#4A5568"}
HEAD, BODY = "Cambria", "Calibri"
TOTAL = 12        # presented slides; the rest are backup
WPM = 140         # speaking rate for non-native speakers
PAUSE = 2         # seconds per slide change
SWAP = 3          # extra seconds when the speaker changes

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
BLANK = prs.slide_layouts[6]
L, R = 0.6, 12.73     # content margins
TOP, BAND_Y = 1.4, 5.78


# ---------- drawing helpers ----------
def text(slide, x, y, w, h, runs, size=16, color=INK, bold=False, font=BODY,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, name=None, space=4):
    """runs: str, or list of paragraphs; a paragraph is str or list of (text, opts)."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    paras = [runs] if isinstance(runs, str) else runs
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space)
        for t, o in ([(para, {})] if isinstance(para, str) else para):
            r = p.add_run()
            r.text = t
            f = r.font
            f.name = o.get("font", font)
            f.size = Pt(o.get("size", size))
            f.bold = o.get("bold", bold)
            f.color.rgb = o.get("color", color)
    return tb


def box(slide, x, y, w, h, fill=ICE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, line=None, lw=1.25):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(lw)
    s.shadow.inherit = False
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = 0.08
    return s


def kpi(slide, x, y, w, h, big, label, fill=ICE, big_color=NAVY, label_color=INK, big_size=28,
        label_size=14):
    box(slide, x, y, w, h, fill=fill)
    text(slide, x + 0.2, y + 0.1, w - 0.4, 0.55, big, size=big_size, bold=True, color=big_color,
         font=HEAD, anchor=MSO_ANCHOR.BOTTOM)
    text(slide, x + 0.2, y + 0.72, w - 0.4, h - 0.8, label, size=label_size, color=label_color)


def card(slide, x, y, w, h, head, body, fill=ICE, fg=INK, hc=NAVY, hs=17, bs=14):
    box(slide, x, y, w, h, fill=fill)
    text(slide, x + 0.2, y + 0.08, w - 0.4, h - 0.16, [[(head, {"bold": True, "size": hs, "color": hc})],
                                                        [(body, {"size": bs, "color": fg})]],
         anchor=MSO_ANCHOR.MIDDLE)


def arrow(slide, x, y, w=0.5, h=0.42, color=TEAL):
    a = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(x), Inches(y), Inches(w), Inches(h))
    a.fill.solid()
    a.fill.fore_color.rgb = color
    a.line.fill.background()
    return a


def band(slide, runs):
    """The single conclusion of a content slide: same place and style on every slide."""
    box(slide, L, BAND_Y, R - L, 0.85, fill=NAVY)
    text(slide, L + 0.25, BAND_Y, R - L - 0.5, 0.85, runs, size=17, color=WHITE,
         anchor=MSO_ANCHOR.MIDDLE, name="Conclusion")


def label(slide, x, y, w, s):
    text(slide, x, y, w, 0.3, s, size=13, bold=True, color=MUTED)


def picture(slide, name, x, y, w):
    return slide.shapes.add_picture(str(FIG / name), Inches(x), Inches(y), width=Inches(w))


def table(slide, x, y, w, rows, col_w, font=14, header_fill=NAVY, row_h=0.42, left_cols=(0,), bold_rows=(),
          header_fg=WHITE):
    shp = slide.shapes.add_table(len(rows), len(rows[0]), Inches(x), Inches(y),
                                 Inches(w), Inches(row_h * len(rows)))
    t = shp.table
    for j, cw in enumerate(col_w):
        t.columns[j].width = Inches(cw)
    for i, row in enumerate(rows):
        t.rows[i].height = Inches(row_h)
        for j, val in enumerate(row):
            c = t.cell(i, j)
            c.margin_left = c.margin_right = Inches(0.08)
            c.margin_top = c.margin_bottom = Inches(0.02)
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            c.fill.solid()
            c.fill.fore_color.rgb = header_fill if i == 0 else (ICE if i % 2 else WHITE)
            p = c.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT if j in left_cols else PP_ALIGN.CENTER
            r = p.add_run()
            r.text = str(val)
            r.font.name = BODY
            r.font.size = Pt(font)
            r.font.bold = i == 0 or i in bold_rows
            r.font.color.rgb = header_fg if i == 0 else INK
    return t


def frame(slide, n, title, source, dark=False):
    """Action title (one line, top-anchored), source line and group tag: identical on every slide."""
    bg = slide.background.fill
    bg.solid()
    bg.fore_color.rgb = NAVY if dark else WHITE
    text(slide, L, 0.42, R - L, 0.6, title, size=27, bold=True, color=WHITE if dark else NAVY,
         font=HEAD, name="Action title")
    text(slide, L, 6.85, 9.3, 0.35, "Source: " + source, size=11, color=ICE if dark else MUTED,
         name="Source")
    tag = f"{n}/{TOTAL}" if n <= TOTAL else "Backup"
    text(slide, 9.95, 6.85, R - 9.95, 0.35, f"Group B · Group 46 · {tag}", size=11,
         color=ICE if dark else MUTED, align=PP_ALIGN.RIGHT, name="Group tag")


# ---------- charts (matplotlib, Calibri, drawn at their placed size so 1 pt = 1 pt) ----------
REV = {"UAV systems": [960000, 3200000, 7200000, 12800000, 19200000],
       "Docks": [135000, 450000, 990000, 1800000, 2700000],
       "VanguardOS licences": [20250, 259200, 785700, 1798200, 3418200],
       "Training and support": [87600, 292000, 655200, 1168000, 1752000]}
CASH = [2315434, 1443241, 779919, 2331404, 6811778]
NET = [-1340448, -584480, 586685, 2787040, 5364206]
YEARS = ["Y1", "Y2", "Y3", "Y4", "Y5"]


def _style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=14, colors=HEX["ink"])
    for s in ("left", "bottom"):
        ax.spines[s].set_color(HEX["muted"])


def make_charts():
    FIG.mkdir(exist_ok=True)
    plt.rcParams.update({"font.family": "Calibri", "font.size": 14})
    # revenue by line (slide 7)
    fig, ax = plt.subplots(figsize=(6.6, 3.05), dpi=220)
    cols = [HEX["navy"], "#8FA3C7", HEX["teal"], "#5A6F99"]
    bottom = [0] * 5
    for (name, vals), c in zip(REV.items(), cols):
        ax.bar(YEARS, [v / 1e6 for v in vals], 0.62, bottom=bottom, color=c, label=name)
        bottom = [b + v / 1e6 for b, v in zip(bottom, vals)]
    for x, tot in enumerate(bottom):
        ax.text(x, tot + 0.5, f"{tot:.1f}", ha="center", va="bottom", fontsize=14, fontweight="bold",
                color=HEX["ink"])
    lic = REV["VanguardOS licences"]
    for x in (4,):
        share = lic[x] / sum(v[x] for v in REV.values())
        ax.text(x + (0.0 if x == 0 else 0.36), bottom[x] + (3.4 if x == 0 else -2.2), f"licences {share:.1%}",
                fontsize=13, fontweight="bold", color=HEX["teal"], va="top", ha="center" if x == 0 else "left")
    ax.set_ylim(0, 31)
    ax.set_xlim(-0.6, 4.95)
    ax.set_yticks([0, 10, 20, 30])
    ax.legend(frameon=False, fontsize=13, loc="upper left")
    _style(ax)
    fig.tight_layout(pad=0.3)
    fig.savefig(FIG / "chart_revenue.png")
    plt.close(fig)
    # cash and net income (slide 10)
    fig, ax = plt.subplots(figsize=(6.0, 2.75), dpi=220)
    ax.bar(YEARS, [c / 1e6 for c in CASH], 0.6, color=HEX["teal"], label="Cash at year end")
    ax.plot(YEARS, [n / 1e6 for n in NET], color=HEX["navy"], lw=2.5, marker="o", label="Net income")
    for x, (c, n) in enumerate(zip(CASH, NET)):
        ax.text(x, max(c, n) / 1e6 + 0.3, f"{c / 1e6:.2f}", ha="center", va="bottom", fontsize=13,
                fontweight="bold", color=HEX["teal"], zorder=5)
    for x in (0, 4):
        ax.text(x + (0.12 if x == 0 else -0.36), NET[x] / 1e6 + (-0.55 if x == 0 else 0.25),
                f"{NET[x] / 1e6:.2f}", ha="left" if x == 0 else "right", fontsize=13, fontweight="bold",
                color=HEX["navy"])
    ax.axhline(0, color=HEX["muted"], lw=0.8)
    ax.set_ylim(-2.2, 8)
    ax.set_yticks([-2, 0, 2, 4, 6, 8])
    ax.legend(frameon=False, fontsize=13, loc="upper left")
    _style(ax)
    fig.tight_layout(pad=0.3)
    fig.savefig(FIG / "chart_cash.png")
    plt.close(fig)
    # break-even, Year 3 (slide 11): BreakEven sheet, column Year 3
    fixed, contrib, rev_unit = 3885040, 99371.67, 9630900 / 45
    xs = [0, 55]
    fig, ax = plt.subplots(figsize=(6.4, 3.55), dpi=220)
    ax.plot(xs, [x * rev_unit / 1e6 for x in xs], color=HEX["navy"], lw=2.5, label="Revenue")
    ax.plot(xs, [(fixed + x * (rev_unit - contrib)) / 1e6 for x in xs], color=HEX["teal"], lw=2.5,
            label="Total cost")
    ax.plot([0, 55], [fixed / 1e6] * 2, color="#8FA3C7", lw=2, ls="--", label="Fixed cost")
    be = fixed / contrib
    ax.plot([be], [be * rev_unit / 1e6], "o", color=HEX["ink"], ms=8)
    ax.annotate("Break-even: 39.1 systems", (be, be * rev_unit / 1e6), (3, 10.6), fontsize=14,
                fontweight="bold", color=HEX["ink"], arrowprops={"arrowstyle": "->", "color": HEX["ink"]})
    ax.axvline(45, color=HEX["teal"], lw=1.8, ls=":")
    ax.text(45.6, 11.6, "45 sold", fontsize=14, fontweight="bold", color=HEX["navy"])
    ax.set_xlim(0, 55)
    ax.set_ylim(0, 12.5)
    ax.set_xlabel("Systems sold in Year 3", fontsize=14)
    ax.legend(frameon=False, fontsize=13, loc="upper left", bbox_to_anchor=(0.0, 0.82))
    _style(ax)
    fig.tight_layout(pad=0.3)
    fig.savefig(FIG / "chart_breakeven.png")
    plt.close(fig)


# ---------- slides ----------
def s1(sl):
    sl.background.fill.solid()
    sl.background.fill.fore_color.rgb = NAVY
    text(sl, 0.8, 0.75, 11.7, 0.4, "GROUP B · GROUP 46 · BUSINESS PLAN", size=14, bold=True, color=ICE)
    text(sl, 0.8, 1.2, 11.7, 0.9, "AeroVanguard Autonomous Systems, S.L.", size=40, bold=True,
         color=WHITE, font=HEAD, name="Action title")
    text(sl, 0.8, 2.2, 11.4, 1.3, [[("In 2025, Spain's drone tender of up to €18M went to a US supplier. ",
                                     {"color": ORANGE, "bold": True}),
                                    ("Europe needs its own eyes in the sky.", {"color": WHITE})]],
         size=26, font=HEAD)
    text(sl, 0.8, 3.3, 11.4, 0.4, "Autonomous surveillance from Getafe: VTOL aircraft + 24/7 dock + fleet software",
         size=18, color=ICE)
    team = [("Founder 1", "CEO"), ("Founder 2", "CTO"),
            ("Founder 3", "Head of AI and Software"), ("Founder 4", "COO"),
            ("Founder 5", "CMO"), ("Founder 6", "CFO")]
    for i, (nm, role) in enumerate(team):
        x = 0.8 + (i % 3) * 3.95
        y = 3.95 + (i // 3) * 1.02
        box(sl, x, y, 3.7, 0.88, fill=MIDNAVY)
        text(sl, x + 0.2, y + 0.1, 3.3, 0.75, [[(nm, {"bold": True, "size": 15, "color": WHITE})],
                                               [(role, {"size": 14, "color": ICE})]], space=2)
    text(sl, 0.8, 6.15, 11.7, 0.35, "Introduction to Engineering Management · BSc Aerospace Engineering "
         "· UC3M · Prof. the CMO Repiso", size=14, color=ICE)
    text(sl, 0.8, 6.85, 8.0, 0.35, "Source: Skydio (2025); SCSP (2025)", size=11, color=ICE)
    text(sl, 9.95, 6.85, R - 9.95, 0.35, f"Group B · Group 46 · 1/{TOTAL}", size=11, color=ICE,
         align=PP_ALIGN.RIGHT)


def s2(sl):
    label(sl, L, TOP, 6.3, "GENERAL ENVIRONMENT (PESTEL)   O = opportunity · T = threat")
    pestel = [("P", "Defence budgets up; preference for EU suppliers", "O"),
              ("E", "European military drones: USD 6.5bn → 11.5bn, 2026–31", "O/T"),
              ("S", "Unarmed drones accepted; few skilled engineers", "O/T"),
              ("T", "GPS-free flight and docks (O); counter-drone systems (T)", "O/T"),
              ("E", "Replace helicopter emissions; battery recycling rules", "O/T"),
              ("L", "BVLOS permits and export licences; NIS2 duties", "T/O")]
    for i, (k, t, ot) in enumerate(pestel):
        x = L + (i % 2) * 3.2
        y = TOP + 0.4 + (i // 2) * 1.3
        box(sl, x, y, 3.05, 1.15)
        text(sl, x + 0.15, y + 0.08, 0.5, 0.5, k, size=22, bold=True, color=NAVY, font=HEAD)
        text(sl, x + 2.25, y + 0.1, 0.65, 0.3, ot, size=14, bold=True, color=TEAL, align=PP_ALIGN.RIGHT)
        text(sl, x + 0.15, y + 0.5, 2.8, 0.62, t, size=14)
    label(sl, 7.25, TOP, 5.5, "INDUSTRY (PORTER'S FIVE FORCES)")
    forces = [("Rivalry", 4, "Strong"), ("Buyer power", 4, "High"), ("Supplier power", 3, "Medium–high"),
              ("New entrants", 2, "Medium"), ("Substitutes", 1, "Low–medium")]
    for i, (f, lv, word) in enumerate(forces):
        y = TOP + 0.42 + i * 0.82
        text(sl, 7.25, y, 1.9, 0.45, f, size=15, bold=True, anchor=MSO_ANCHOR.MIDDLE)
        for k in range(4):
            box(sl, 9.15 + k * 0.42, y + 0.08, 0.36, 0.3, fill=NAVY if k < lv else ICE,
                shape=MSO_SHAPE.RECTANGLE)
        text(sl, 10.95, y, 1.78, 0.45, word, size=15, anchor=MSO_ANCHOR.MIDDLE)
    band(sl, [[("So what  ", {"bold": True}),
               ("Demand moves to European suppliers and buyers are strong: we sell to governments and private operators",
                {})]])


def s3(sl):
    text(sl, L, TOP, 6.1, 0.9, [[("Replaces a crewed helicopter patrol ", {"bold": True, "color": NAVY}),
                                 ("over a base perimeter, power line or border segment", {})]], size=18)
    specs = [("3 h", "endurance, VTOL fixed wing"), ("< 25 kg", "take-off mass (MTOW)"),
             ("GPS-free", "keeps navigating when jammed"), ("On board", "threat detection by edge AI")]
    for i, (big, lab) in enumerate(specs):
        kpi(sl, L + (i % 2) * 3.12, 2.45 + (i // 2) * 1.6, 2.98, 1.45, big, lab, big_size=28)
    items = [("AV-1 Sentinel", "€160,000", "Electric VTOL aircraft; EU and allied components only"),
             ("AV-Dock", "€45,000", "Weatherproof station: lands and recharges unattended"),
             ("VanguardOS", "€18,000 / year", "Fleet-command software, per aircraft")]
    for i, (nm, price, desc) in enumerate(items):
        y = TOP + i * 1.42
        box(sl, 7.05, y, R - 7.05, 1.27)
        text(sl, 7.3, y + 0.12, 3.0, 0.45, nm, size=20, bold=True, color=NAVY, font=HEAD)
        text(sl, 9.9, y + 0.12, 2.6, 0.45, price, size=20, bold=True, color=NAVY, font=HEAD,
             align=PP_ALIGN.RIGHT)
        text(sl, 7.3, y + 0.68, 5.2, 0.45, desc, size=15)
    band(sl, [[("Certification  ", {"bold": True}),
               ("Y1: flight tests, SORA via AESA (civil) · from Y2: RD 866/2015 via DGAM and INTA (defence)",
                {})]])


def s4(sl):
    rows = [["Resource or capability", "V", "R", "I", "O", "Result"],
            ["EU and allied supply chain", "Yes", "Yes", "Partly", "Yes", "Temporary (2–3 yrs)"],
            ["On-board AI, flight without GPS", "Yes", "Yes", "Yes", "Yes", "Sustained*"],
            ["Integrated aircraft, dock, software", "Yes", "Yes", "Partly", "Yes", "Temporary"],
            ["Fleet flight data", "Yes", "No", "No", "Not yet", "Parity → Y3 potential"],
            ["Founding team of six engineers", "Yes", "No", "No", "Yes", "Parity"],
            ["Getafe aerospace cluster", "Yes", "No", "No", "Yes", "Parity"],
            ["Seed capital", "Yes", "No", "No", "Yes", "Parity"],
            ["Brand, references, certificates", "Yes", "No", "No", "Not yet", "Parity"],
            ["Production plant and tooling", "Yes", "No", "No", "Yes", "Parity"]]
    t = table(sl, L, TOP, 8.1, rows, [3.25, 0.55, 0.55, 0.8, 0.95, 2.0], font=14, row_h=0.38)
    for j in range(6):
        t.cell(2, j).fill.fore_color.rgb = RGBColor(0xD6, 0xEF, 0xEC)
    text(sl, L, 5.3, 8.1, 0.25, "* if development continues", size=12, color=MUTED)
    label(sl, 9.0, TOP, 3.73, "WEAKNESSES → OUR RESPONSE")
    weak = [("No references or certificates", "Private clients alongside tenders; paid 30-day trials"),
            ("Small capital vs rivals", "Cells only with signed orders; credit line to negotiate in Y2"),
            ("Few suppliers for key parts", "Two approved sources; 60 days of stock")]
    for i, (w, r) in enumerate(weak):
        y = TOP + 0.4 + i * 1.3
        card(sl, 9.0, y, R - 9.0, 1.18, w, "→ " + r, hs=15, bs=14)
    box(sl, L, BAND_Y, R - L, 0.85, fill=NAVY)
    text(sl, L + 0.25, BAND_Y, R - L - 0.5, 0.85,
         [[("Corporate  ", {"bold": True}), ("one business · Ansoff: market and product development from Y3 · alliances with primes", {})],
          [("Competitive  ", {"bold": True}),
           ("focused differentiation: EU and allied supply chain + flight without GPS + 24/7 dock", {})]],
         size=15, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, space=1, name="Conclusion")


def s5(sl):
    funnel = [("TAM", "≈ €13bn a year", "Military + commercial drones, Europe (M&M 2026; GVR 2025)", 6.0, ICE, INK),
              ("SAM", "€2.1bn → €3.7bn", "Small drones, Europe, 2025–30 (+11.9%/yr)", 5.1,
               RGBColor(0xC5, 0xD2, 0xE8), INK),
              ("SOM", "€9.6M (Y3) → €27.1M (Y5)", "Our sales plan: 0.7% of the 2030 SAM", 4.6, NAVY, WHITE)]
    for i, (k, v, lab, w, fill, fg) in enumerate(funnel):
        y = TOP + i * 1.2
        x = L + (6.0 - w) / 2
        box(sl, x, y, w, 1.08, fill=fill)
        text(sl, x + 0.2, y, w - 0.4, 1.08, [[(f"{k}  ", {"bold": True, "color": ORANGE if fg == WHITE else NAVY}),
                                              (v, {"bold": True, "color": fg})], [(lab, {"size": 14, "color": fg})]],
             size=18, anchor=MSO_ANCHOR.MIDDLE, space=1)
    text(sl, L, 5.1, 6.1, 0.4, "Segments (institution, need): 60% defence · 30% infrastructure · 10% civil",
         size=14)
    rows = [["Rival", "Gap we fill"],
            ["Quantum Systems (DE)", "Over €800k per aircraft with support"],
            ["Tekever (PT)", "Long missions, no autonomous dock"],
            ["Indra-Aertec (ES)", "Large military programmes, slower"],
            ["Parrot / Delair (FR)", "32-min quadcopter / no 24/7 dock"],
            ["Skydio (US)", "Not European; under 1 h of flight"],
            ["DJI (CN)", "Distrusted at sensitive sites"]]
    table(sl, 6.95, TOP, R - 6.95, rows, [2.3, 3.48], font=14, row_h=0.578, left_cols=(0, 1))
    band(sl, [[("Gap  ", {"bold": True}),
               ("We found no European supplier that combines hours of flight, a 24/7 dock and an "
                "affordable price", {})]])


def s6(sl):
    base_x, maxw, heli = 2.75, 5.6, 5_695_000
    for i, (lab, val, fill) in enumerate([("Light helicopter\n(AS350 / H125)", heli, MUTED),
                                          ("AV-1 + AV-Dock", 413_950, NAVY)]):
        y = TOP + i * 1.0
        bw = maxw * val / heli
        text(sl, L, y, 2.1, 0.85, lab, size=14, bold=True, anchor=MSO_ANCHOR.MIDDLE)
        box(sl, base_x, y + 0.08, bw, 0.7, fill=fill, shape=MSO_SHAPE.RECTANGLE)
        inside = i == 0
        text(sl, base_x + (bw - 2.3 if inside else bw + 0.15), y, 2.15, 0.85, f"€{val:,.0f}", size=20,
             bold=True, color=WHITE if inside else INK, font=HEAD, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.RIGHT if inside else PP_ALIGN.LEFT)
    arrow(sl, 8.55, TOP + 0.22)
    kpi(sl, 9.2, TOP + 0.08, R - 9.2, 1.55, "−92.7%", "Five-year cost, both at 300 flight hours a year", fill=NAVY,
        big_color=ORANGE, label_color=WHITE, big_size=40)
    text(sl, L, 3.38, R - L, 0.3, "Five-year TCO at 300 h a year: €311,400 our invoices + "
         "€44,800 energy and spares + €57,750 remote pilot", size=14, color=MUTED)
    mix = [("Product and positioning", "European, dock-based, flies without GPS; for agencies and operators"),
           ("Price", "Value-based against the helicopter; a scored criterion in tenders"),
           ("Place", "Direct in Spain; one vetted integrator per country and primes from Y3"),
           ("Promotion", "FEINDEF May 2027 launch, Eurosatory 2028, paid 30-day trials")]
    w = (R - L - 3 * 0.25) / 4
    for i, (h, b) in enumerate(mix):
        card(sl, L + i * (w + 0.25), 3.8, w, 1.68, h, b, hs=17, bs=14)
    band(sl, [[("Life cycle  ", {"bold": True}),
               ("Introduction Y1–2 (demos, approvals) → growth Y3–5: EU and NATO markets and new payloads",
                {})]])


def s7(sl):
    picture(sl, "chart_revenue.png", L, TOP, 6.6)
    text(sl, L, 4.5, 6.6, 0.3, "Revenue by line, € million", size=12, color=MUTED)
    box(sl, L, 4.85, 6.6, 0.8)
    text(sl, L + 0.2, 4.85, 2.4, 0.8, "€18,000 / yr", size=22, bold=True, color=NAVY, font=HEAD,
         anchor=MSO_ANCHOR.MIDDLE)
    text(sl, L + 2.65, 4.85, 3.8, 0.8, "per aircraft · 90% of the fleet · 15% hosting cost", size=14,
         anchor=MSO_ANCHOR.MIDDLE)
    label(sl, 7.55, TOP, 5.18, "AUTONOMY THAT CUSTOMERS PAY FOR")
    cards = [("Flies without GPS", "Camera-based navigation keeps the AV-1 flying under jamming"),
             ("Detects threats on board", "Edge AI alerts in real time, no link needed"),
             ("Tested legally", "Demos at ATLAS and CIAR; jamming only at authorised ranges")]
    for i, (h, b) in enumerate(cards):
        card(sl, 7.55, TOP + 0.4 + i * 1.33, R - 7.55, 1.2, h, b, hs=16, bs=14)
    band(sl, [[("Data flywheel  ", {"bold": True}),
               ("More flight hours → better models: parity today, potential sustained advantage from Year 3",
                {})]])


def s8(sl):
    stages = ["Inspect parts", "Composite lay-up", "Structural assembly", "Integrate avionics",
              "Software and bench test", "Test flight (ATLAS, CIAR)"]
    w = (R - L - 5 * 0.3) / 6
    for i, s in enumerate(stages):
        x = L + i * (w + 0.3)
        if i:
            arrow(sl, x - 0.27, TOP + 0.42, w=0.24, h=0.3)
        box(sl, x, TOP, w, 1.15)
        text(sl, x + 0.15, TOP + 0.08, w - 0.3, 0.35, str(i + 1), size=18, bold=True, color=NAVY, font=HEAD)
        text(sl, x + 0.15, TOP + 0.45, w - 0.3, 0.65, s, size=14)
    text(sl, L, 2.72, R - L, 0.35, [[("Batch production in cells, assembled to order · Priorities: ",
                                      {"bold": True, "color": NAVY}),
                                     ("quality > dependability (the 24/7 promise) > flexibility > speed > cost", {})]], size=15)
    kpi(sl, L, 3.3, 3.6, 1.12, "1 → 7 cells", "18 aircraft + 9 docks per cell a year")
    kpi(sl, L, 4.55, 3.6, 1.12, "126 ≥ 120", "Year 5 capacity vs systems sold")
    card(sl, 4.45, 3.3, R - 4.45, 1.12, "MAKE (what creates our advantage)",
         "Design and software · composite airframe · assembly · flight test")
    card(sl, 4.45, 4.55, R - 4.45, 1.12, "BUY (EU and allied)",
         "Camera, inertial unit, radio, autopilot, motors, batteries: two approved sources each")
    band(sl, [[("Grow with orders  ", {"bold": True}),
               ("A new cell only with signed orders · BOM €78,000, variable cost €95,200 per AV-1", {})]])


def s9(sl):
    def org(x, y, w, h, lines, fill, fg):
        box(sl, x, y, w, h, fill=fill, line=NAVY if fill == WHITE else None)
        text(sl, x + 0.05, y, w - 0.1, h, lines, size=14, color=fg, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, space=1)

    def vline(x, y1, y2):
        box(sl, x - 0.01, y1, 0.02, y2 - y1, fill=NAVY, shape=MSO_SHAPE.RECTANGLE)

    bw, gap = 1.4, 0.15
    mid = L + (5 * bw + 4 * gap) / 2
    org(mid - 1.8, TOP, 3.6, 0.6, [[("Board", {"bold": True})], "3 founders + 2 investors"], WHITE, NAVY)
    vline(mid, TOP + 0.6, TOP + 0.8)
    org(mid - 1.8, TOP + 0.8, 3.6, 0.6, [[("CEO", {"bold": True})], "Founder 1"], NAVY, WHITE)
    vline(mid, TOP + 1.4, TOP + 1.6)
    box(sl, L + bw / 2, TOP + 1.59, 4 * (bw + gap), 0.02, fill=NAVY, shape=MSO_SHAPE.RECTANGLE)
    heads = [("CTO", "Founder 2", "3 systems engineers"), ("Head of AI", "Founder 3", "3 software engineers"),
             ("COO", "Founder 4", "2 operators\n1 quality"), ("CMO", "Founder 5", "1 sales"),
             ("CFO", "Founder 6", "1 finance")]
    for i, (role, nm, team) in enumerate(heads):
        x = L + i * (bw + gap)
        vline(x + bw / 2, TOP + 1.6, TOP + 1.8)
        org(x, TOP + 1.8, bw, 0.7, [[(role, {"bold": True})], nm], NAVY, WHITE)
        vline(x + bw / 2, TOP + 2.5, TOP + 2.65)
        org(x, TOP + 2.65, bw, 0.95, team, ICE, INK)
    text(sl, L, 5.12, 7.6, 0.3, "Year 1: 17 people", size=12, color=MUTED)
    rows = [["", "Y1", "Y2", "Y3", "Y4", "Y5"], ["People", "17", "26", "43", "63", "85"],
            ["Gross pay €M", "0.67", "0.98", "1.62", "2.33", "3.09"]]
    table(sl, 8.4, TOP, R - 8.4, rows, [1.33, 0.6, 0.6, 0.6, 0.6, 0.6], font=14, row_h=0.45)
    text(sl, 8.4, TOP + 1.42, R - 8.4, 0.3, "Before 32% employer social security", size=12, color=MUTED)
    box(sl, 8.4, 3.25, R - 8.4, 1.75, fill=NAVY)
    text(sl, 8.65, 3.37, R - 8.9, 2.2, [[("Why an S.L.", {"bold": True, "size": 17})],
                                        "• Limited liability; founders keep 60%",
                                        "• Partners decide who enters (art. 107 LSC)",
                                        "• Investors join by capital increase",
                                        "• 4-year founder vesting"], size=15, color=WHITE, space=3)
    band(sl, [[("People follow orders  ", {"bold": True}),
               ("We hire against signed orders, under the metal-industry agreement of Madrid", {})]])


def s10(sl):
    k = 3.91 / 5.2
    for x, head, parts in [(L, "USES", [("1.35", "Fixed assets", 1.35, RGBColor(0x8F, 0xA3, 0xC7)),
                                        ("3.85", "Launch losses and working capital", 3.85, NAVY)]),
                           (3.55, "SOURCES", [("1.20", "Debt 23% at 6%: ENISA 0.30, bank 0.90", 1.20, TEAL),
                                              ("4.00", "Equity 77%: founders 0.30, seed 3.70", 4.00, NAVY)])]:
        label(sl, x, TOP, 2.8, head + " (€M)")
        y = TOP + 0.4
        for big, lab, v, fill in parts:
            h = v * k
            box(sl, x, y, 2.75, h - 0.06, fill=fill, shape=MSO_SHAPE.RECTANGLE)
            text(sl, x + 0.15, y, 2.45, h - 0.06, [[(big, {"bold": True, "size": 20})], lab], size=14,
                 color=NAVY if fill == RGBColor(0x8F, 0xA3, 0xC7) else WHITE, anchor=MSO_ANCHOR.MIDDLE, space=1)
            y += h
    picture(sl, "chart_cash.png", 6.75, TOP, 6.0)
    text(sl, 6.75, TOP + 2.78, 6.0, 0.3, "Cash at year end and net income, € million", size=12, color=MUTED)
    kpi(sl, 6.75, 4.6, 2.9, 1.05, "€0.78M", "Cash trough, Year 3", big_size=26)
    kpi(sl, 9.83, 4.6, R - 9.83, 1.05, "€1.5M", "Credit line to negotiate in Y2", big_size=26)
    band(sl, [[("Structure  ", {"bold": True}),
               ("Debt/equity 0.45 → 0 · leverage index 1.65 → 1.27 (amplifies Y1–2 losses) · solvency 2.8 → 4.7", {})]])


def s11(sl):
    picture(sl, "chart_breakeven.png", L, TOP, 6.4)
    text(sl, L, 5.0, 6.4, 0.3, "Year 3, € million; a system = one aircraft with its share of docks, licences and services", size=12, color=MUTED)
    rows = [["k€", "Y1", "Y2", "Y3", "Y4", "Y5"],
            ["Systems", "6", "20", "45", "80", "120"],
            ["Revenue", "1,203", "4,201", "9,631", "17,566", "27,070"],
            ["EBITDA", "−998", "−212", "1,041", "3,559", "6,869"],
            ["Net income", "−1,340", "−584", "587", "2,787", "5,364"]]
    table(sl, 7.25, TOP, R - 7.25, rows, [1.3, 0.8, 0.72, 0.8, 0.9, 0.96], font=14, row_h=0.5)
    for i, (big, lab) in enumerate([("25.4%", "EBITDA margin, Y5"), ("46.0%", "ROA, Y5 (Y3: 15.8%)"),
                                    ("49.6%", "ROE, Y5 (Y3: 22.0%)")]):
        w = (R - 7.25 - 2 * 0.15) / 3
        kpi(sl, 7.25 + i * (w + 0.15), 4.3, w, 1.3, big, lab, big_size=26)
    band(sl, [[("Break-even  ", {"bold": True}),
               ("€3.89M fixed ÷ 46.4% margin ≈ €8.37M = 39.1 systems (or 60 aircraft sold alone); we sell 45", {})]])


def s12(sl):
    for i, (big, lab) in enumerate([("€2.26M", "NPV with residual value, WACC 14.9%"),
                                    ("31.1%", "IRR with residual value"), ("4.5 years", "Simple payback")]):
        kpi(sl, L + i * 2.78, TOP, 2.6, 1.45, big, lab, fill=WHITE, big_color=NAVY, label_color=INK,
            big_size=28)
    text(sl, L, 3.0, 8.15, 0.65, "Without residual value: NPV −€0.22M, IRR 12.8%. Residual value €4.95M = "
         "assets and working capital the company keeps.", size=15, color=ICE)
    rows = [["Scenario", "Systems Y5", "Min. cash", "NPV (with RV)"],
            ["Pessimistic", "90", "−€1.35M*", "−€1.85M"],
            ["Base", "120", "€0.78M", "€2.26M"],
            ["Optimistic", "144", "€1.67M", "€4.37M"]]
    table(sl, L, 3.8, 8.15, rows, [2.3, 1.95, 1.95, 1.95], font=14, header_fill=WHITE, row_h=0.42, header_fg=NAVY)
    text(sl, L, 5.58, 8.15, 0.55, "Pessimistic: units in Y2–5 −25%, price −5%; optimistic: units +20%. "
         "* Needs the €1.5M credit line (to negotiate in Y2); hiring follows orders.", size=13, color=ICE)
    box(sl, 9.05, TOP, R - 9.05, 4.08, fill=WHITE)
    text(sl, 9.3, TOP + 0.15, R - 9.55, 4.5,
         [[("The ask", {"bold": True, "size": 20, "color": NAVY, "font": HEAD})],
          [("€3.7M for 40%", {"bold": True, "size": 30, "color": NAVY, "font": HEAD})],
          [("Seed equity · post-money €9.25M", {"size": 15, "bold": True})],
          [("Use: certify the AV-1, equip Getafe, deliver the first 26 systems (Y1–2)", {"size": 14})],
          [("Investors: 2 of 5 board seats · founders keep 60%, 4-year vesting", {"size": 14})],
          [("Milestones: FEINDEF May 2027 launch · break-even in Y3", {"size": 14})]], space=16)
    text(sl, L, 6.25, R - L, 0.45, "Europe's own eyes in the sky, built in Getafe.", size=20, bold=True,
         color=ORANGE, font=HEAD)


def b_balance(sl):
    rows = [["€ thousand", "Y1", "Y2", "Y3", "Y4", "Y5"],
            ["Non-current assets", "1,080", "930", "1,030", "950", "710"],
            ["Current assets", "3,081", "2,430", "3,027", "6,403", "13,037"],
            ["  of which cash", "2,315", "1,443", "780", "2,331", "6,812"],
            ["Total assets", "4,161", "3,360", "4,057", "7,353", "13,747"],
            ["Equity", "2,660", "2,075", "2,662", "5,449", "10,813"],
            ["Non-current liabilities", "900", "600", "300", "0", "0"],
            ["Current liabilities", "602", "685", "1,095", "1,904", "2,934"],
            ["Solvency (assets / liabilities)", "2.77", "2.62", "2.91", "3.86", "4.69"],
            ["Financial debt / equity", "0.45", "0.43", "0.23", "0.06", "0.00"],
            ["ROA (EBIT / assets)", "−30.5%", "−15.3%", "15.8%", "41.9%", "46.0%"],
            ["ROE (net income / equity)", "−50.4%", "−28.2%", "22.0%", "51.1%", "49.6%"],
            ["Leverage index (A/E × EBT/EBIT)", "1.65", "1.85", "1.40", "1.33", "1.27"]]
    table(sl, L, TOP, R - L, rows, [4.13, 1.6, 1.6, 1.6, 1.6, 1.6], font=14, row_h=0.31, bold_rows=(4, 5))
    band(sl, [[("Tax  ", {"bold": True}),
               ("Corporate tax 15% in Y4–5 as a new entity, after offsetting Y1–2 losses; then 25% (Ley 27/2014)", {})]])


def b_staff(sl):
    rows = [["Position", "Salary €", "Y1", "Y2", "Y3", "Y4", "Y5"],
            ["Founders in management posts", "45k → 65k", "6", "6", "6", "6", "6"],
            ["Aerospace and systems engineers", "38,000", "3", "5", "8", "11", "14"],
            ["AI and software engineers", "42,000", "3", "5", "8", "12", "16"],
            ["Assembly and test operators", "26,000", "2", "5", "10", "17", "25"],
            ["Quality and certification engineers", "40,000", "1", "1", "2", "3", "4"],
            ["Sales and business development", "40,000", "1", "2", "4", "6", "8"],
            ["Field service and support", "32,000", "0", "1", "3", "5", "8"],
            ["Administration and finance", "28,000", "1", "1", "2", "3", "4"],
            ["Total headcount", "", "17", "26", "43", "63", "85"]]
    table(sl, L, TOP, R - L, rows, [4.43, 1.6, 1.2, 1.2, 1.2, 1.25, 1.25], font=14, row_h=0.42, bold_rows=(9,))
    band(sl, [[("Payroll  ", {"bold": True}),
               ("Gross salaries €0.67M → €3.09M, plus 32% employer social security; permanent contracts for employees",
                {})]])


def b_cash(sl):
    rows = [["€ thousand", "Q1", "Q2", "Q3", "Q4", "Y1", "Y2", "Y3", "Y4", "Y5"],
            ["Revenue", "0", "0", "398", "805", "1,203", "4,201", "9,631", "17,566", "27,070"],
            ["Net income", "−467", "−467", "−294", "−114", "−1,340", "−584", "587", "2,787", "5,364"],
            ["Operating cash flow", "−320", "−399", "−495", "−320", "−1,535", "−422", "137", "2,251", "5,080"],
            ["Investing cash flow", "−1,350", "0", "0", "0", "−1,350", "−150", "−500", "−400", "−300"],
            ["Financing cash flow", "5,200", "0", "0", "0", "5,200", "−300", "−300", "−300", "−300"],
            ["Cash at period end", "3,530", "3,131", "2,635", "2,315", "2,315", "1,443", "780", "2,331", "6,812"]]
    table(sl, L, TOP, R - L, rows, [2.93] + [1.02] * 9, font=14, row_h=0.57, bold_rows=(6,))
    band(sl, [[("Year 1  ", {"bold": True}),
               ("No sales until Q3 (2 systems), then 4 in Q4 · the round enters in Q1 and carries the launch", {})]])


def b_sources(sl):
    refs = ["SCSP (2025). 2025 Gaps Analysis: Commercial Drones.",
            "Skydio (2025). Spain's MoD selects Skydio X10D, EUR 18M tender.",
            "European Commission (2025). Defence Readiness Roadmap 2030.",
            "La Moncloa (2025). Plan for Security and Defence.",
            "MarketsandMarkets (2025, 2026). Europe small and military drones.",
            "Grand View Research (2025). Europe commercial drone market.",
            "Militarnyi (2025). Romania orders German Vector UAVs.",
            "Robotics Press (2026); Dronefly (2026). Skydio and DJI Dock prices.",
            "FlyCraft (2026). AS350 cost per hour.",
            "Reg. (EU) 2019/947; RD 517/2024; RD 866/2015; Reg. (EU) 2021/821.",
            "Ley de Sociedades de Capital; Ley 27/2014; Ley 22/2015; Ley 15/2010.",
            "ENISA (2026). Participative loans without guarantees.",
            "Damodaran (2024); Gompers et al. (2020); Brealey, Myers, Allen (2020).",
            "Barney (1991); Porter (1980, 1985); Ansoff (1957); Kotler, Keller (2016).",
            "AeroVanguard financial model and Business Plan, Group B (2026).",
            "Web sources accessed November 2026; full list in Section 10."]
    half = len(refs) // 2
    for i, col in enumerate((refs[:half], refs[half:])):
        text(sl, L + i * 6.15, TOP, 5.95, 5.3, [[(r, {})] for r in col], size=16, space=14)


SLIDES = [
    dict(fn=s1, who="CEO", title="AeroVanguard Autonomous Systems, S.L.", source="",
         screen="Dark navy. Kicker, company name, the hook sentence (first half in orange), six founder "
         "cards, course line, source line.",
         script="Good morning, we are Group B. In 2025, Spain's Ministry of Defence awarded a drone contract of up "
         "to eighteen million euros to Skydio, an American company. Europe needs its own eyes in the sky. That is "
         "AeroVanguard: autonomous surveillance, designed and assembled in Getafe."),
    dict(fn=s2, who="CEO", title="Europe buys its drones abroad: that gap is our market",
         source="European Commission (2025); La Moncloa (2025); MarketsandMarkets (2026); Porter (1980); "
         "Business Plan, Section 2",
         screen="Left: six PESTEL tiles (letter, fact, O/T). Right: Porter's five forces as level bars. Navy "
         "band: what the analysis means for us.",
         script="Brussels and Madrid are moving defence money to European "
         "suppliers, new security rules force energy and transport companies to protect their sites, and "
         "buyers now audit where components come from. The threats are slow permits and a shortage of "
         "engineers. Porter shows strong rivalry and powerful buyers, so we do not depend on one buyer: we sell to "
         "governments and to private operators. CTO, please."),
    dict(fn=s3, who="CTO", title="One uncrewed system on 24/7 standby: aircraft, dock, software",
         source="Business Plan, Sections 1 and 7; Reg. (EU) 2019/947; RD 517/2024; RD 866/2015",
         screen="Left: the customer pain and four spec tiles. Right: three product cards with prices. Navy "
         "band: Year 1 status and the certification route.",
         script="We sell a system, not a drone. The AV-1 Sentinel is an electric fixed-wing aircraft that "
         "takes off vertically, flies for three hours, keeps navigating when GPS is jammed and detects "
         "threats on board. It costs one hundred and sixty thousand euros. The AV-Dock lets it land and "
         "recharge with nobody around, and VanguardOS runs the whole fleet. Civil clients fly with a permit "
         "from AESA; military aircraft are certified by the Ministry of Defence, with INTA."),
    dict(fn=s4, who="CTO", title="Today only our on-board autonomy is a sustained advantage",
         source="Barney (1991); Business Plan, Section 3 (VRIO and SWOT tables) and Section 4 (risks)",
         screen="Full VRIO table, nine resources (sustained row in light teal). Right: three weakness cards "
         "with the response to each. Navy band: the combination.",
         script="We ran VRIO on nine resources, and we were honest. Today only one gives us a sustained "
         "advantage: our own on-board AI, which flies without GPS. It is hard to copy, and it will improve with "
         "every hour flown. Our European supply chain and our integrated design can be copied in "
         "two or three years, so they are temporary. The rest gives parity. Our weaknesses are no references "
         "yet, little capital and few suppliers; the right side shows our answer to each. So our strategy is focused differentiation: "
         "European parts plus autonomy, and we grow with partners. CMO, please."),
    dict(fn=s5, who="CMO", title="A €2.1bn market where we found no European rival like us",
         source="MarketsandMarkets (2025, 2026); Grand View Research (2025); Militarnyi (2025); "
         "Skydio (2025); Business Plan, Sections 2 and 7",
         screen="Left: TAM-SAM-SOM funnel (SOM in navy) and the segment split. Right: six rivals with the "
         "gap each leaves. Navy band: the gap.",
         script="Small drones in Europe were a two point one billion euro market in 2025, and they should reach three "
         "point seven billion by 2030. In Year 5 we need only zero point seven percent of that. Quantum is too expensive for operators, Skydio "
         "flies under an hour, and DJI is distrusted at sensitive sites. We found no European rival with long "
         "flights, a dock that works day and night, and an affordable price."),
    dict(fn=s6, who="CMO", title="Illustrative five-year TCO: an AV-1 system costs 92.7% less",
         source="Business Plan, Sections 4 and 7 (TCO, distribution, life cycle); FlyCraft (2026); Ansoff (1957)",
         screen="Top: two proportional bars with an arrow to the navy −92.7% card; the TCO build-up line. "
         "Middle: four marketing-mix cards. Navy band: the life cycle.",
         script="Our buyers judge the five-year cost, not the price tag. One AV-1 with its dock, licence, "
         "training, energy, spares and a part-time remote pilot costs about four hundred and fourteen "
         "thousand euros. A light helicopter flying the same three hundred hours a year costs five point "
         "seven million. In this illustrative comparison we are ninety-two point seven percent cheaper, and "
         "that is why we price on value. Head of AI, please."),
    dict(fn=s7, who="Head of AI",
         title="Autonomy sells the aircraft; licences add €3.4M a year by Y5",
         source="Financial model (Excel), sheets Assumptions and IS; Business Plan, Sections 2, 3 and 7",
         screen="Left: revenue-by-line chart with the licence terms under it. Right: three autonomy cards. "
         "Navy band: the data flywheel.",
         script="I lead AI and software. We test jamming only at authorised ranges, and every flight hour "
         "gives us data to retrain the models. Today that data gives parity; "
         "from Year 3 it can become a sustained advantage. And it pays: VanguardOS costs "
         "eighteen thousand euros per aircraft per year, and by Year 5 licences bring in three point four million euros a year. COO, please."),
    dict(fn=s8, who="COO", title="Getafe assembly cells grow with signed orders, not ahead",
         source="Business Plan, Section 6 (production system, competitive dimensions, make-or-buy, capacity) "
         "and Annex A (BOM)",
         screen="Six stage tiles, the production-system line, two capacity KPIs, Make (navy) and Buy cards. "
         "Navy band: grow with orders.",
         script="We use batch production in assembly cells, and we assemble to "
         "order. Quality comes first, then dependability, flexibility, speed and cost. We make what makes us "
         "different, and buy specialised parts from European and allied makers, always from two approved "
         "suppliers. One cell builds up to eighteen aircraft a "
         "year; seven cells in Year 5 cover the hundred and twenty we sell."),
    dict(fn=s9, who="COO", title="From 17 to 85 people, in an S.L. the founders control",
         source="Business Plan, Section 5 (legal form) and Section 9 (organisation, staffing table); "
         "Ley de Sociedades de Capital",
         screen="Left: native org chart of Year 1. Right: headcount and payroll by year, navy S.L. card. "
         "Navy band: hiring follows orders.",
         script="We start with seventeen people: five department heads report to the CEO, who answers to "
         "the board. We grow to eighty-five by Year 5, hiring only against "
         "signed orders. We chose an S.L.: liability is limited, the founders keep sixty percent, the partners "
         "decide who comes in, and investors join through a capital increase. CFO, please."),
    dict(fn=s10, who="CFO", title="We need €5.2M, mainly for launch losses and working capital",
         source="Financial model (Excel), sheets Assumptions and CF; Business Plan, Section 8; ENISA (2026)",
         screen="Uses and sources as two columns to scale. Right: cash chart and two KPI cards. Navy band: "
         "debt terms and Year 5 position.",
         script="Why five point two million, if fixed assets take only one point three five million? Because we "
         "certify for two years before we sell at scale, and we must pay for stock and wait sixty days to get "
         "paid. So most of the money covers launch losses and working capital. Seventy-seven percent is "
         "equity; one point two million is debt from ENISA and a bank. Even so, cash falls to zero point "
         "seven eight million in Year 3."),
    dict(fn=s11, who="CFO", title="We break even in Year 3: 45 systems sold, 39.1 needed",
         source="Financial model (Excel, excl. VAT, constant 2027 prices), sheets IS, BreakEven, Ratios; Business Plan, Section 8",
         screen="Left: break-even chart and its caption. Right: five-year P&L and three KPI cards (EBITDA margin, "
         "ROA, ROE). Navy band: the break-even arithmetic.",
         script="Revenue grows from one point two million in Year 1 to twenty-seven million in Year 5. We lose money in "
         "the two launch years, as planned. In Year 3 we need just over thirty-nine systems to cover all fixed costs, "
         "and we sell forty-five, so Year 3 is profitable. By Year 5, EBITDA is almost seven million, a "
         "twenty-five percent margin, and return on equity is almost fifty percent."),
    dict(fn=s12, who="CFO", title="NPV €2.26M with residual value: we raise €3.7M for 40%",
         source="Financial model (Excel), sheet Investment; scenarios recalculated (Business Plan, Section 8); "
         "Damodaran (2024)",
         screen="Dark slide. Three white KPI cards, the no-residual line, scenario table, white 'The ask' "
         "card with use of funds and milestones, closing line in orange.",
         script="Counting what the company still owns in Year 5, the NPV is two point two six million, with a "
         "thirty-one percent IRR and a simple payback of four and a half years. Without that residual value, NPV is minus zero point two two million. In the pessimistic case NPV turns negative and cash goes one point three five million "
         "below zero, so in Year 2 we will negotiate a credit line of one and a half million. So "
         "our ask is three point seven million euros for forty percent. Europe's own eyes in the sky, built "
         "in Getafe. Thank you."),
    dict(fn=b_balance, who="Backup", title="Equity covers the losses; returns turn positive in Year 3",
         source="Financial model (Excel), sheets BS and Ratios; Business Plan, Section 8 and Annex A",
         screen="Balance-sheet summary and solvency ratios, for the Q&A.", script=""),
    dict(fn=b_staff, who="Backup", title="Headcount grows fivefold, led by operators and AI engineers",
         source="Financial model (Excel), sheet HR; Business Plan, Section 9 (staffing table)",
         screen="Full staffing table by position and year, for the Q&A.", script=""),
    dict(fn=b_cash, who="Backup", title="Cash comes from the round in Year 1, from operations from Year 3",
         source="Financial model (Excel), sheets IS and CF; Business Plan, Annex A",
         screen="Year 1 by quarter and five-year cash-flow statement, for the Q&A.", script=""),
    dict(fn=b_sources, who="Backup", title="Sources",
         source="Full reference list in the Business Plan, Section 10",
         screen="Reference list in two columns.", script=""),
]

QA = [  # (question, who answers, about 15 seconds spoken); 1-10 are the classic traps
    ("Why is NPV negative without residual value?", "CFO",
     "Because in Year 5 we are still growing: one point five million goes into working capital that year. "
     "But the company doesn't close. It keeps four point nine five million of assets and working capital, "
     "at book value only. With it, NPV is two point two six million."),
    ("Why a cost of equity of 18%?", "CFO",
     "VCs quote thirty-one to fifty percent because they put failure risk inside the rate (Gompers, 2020). "
     "Following Damodaran, we put that risk in the cash flows and the scenarios. Even at thirty percent, "
     "NPV with residual value stays positive, about zero point seven five million."),
    ("How do you certify for Defence versus civil customers?", "CTO",
     "Civil: under twenty-five kilos we fly in the EASA specific category, with a SORA authorisation from "
     "AESA. Defence aircraft are State aircraft, certified under Royal Decree 866 of 2015 by the Defence "
     "authority in DGAM, with INTA. That campaign is budgeted from Year 2."),
    ("Why 5.2 M€ if the CAPEX is only 1.35 M€?", "CFO",
     "Because we certify for two years and must finance stock and receivables: three point eight five "
     "million is cash for that. Even so, cash falls to zero point seven eight million in Year 3, so the "
     "round is not too big. Later CAPEX, one point three five million, comes from our own cash."),
    ("What happens in the pessimistic scenario?", "CFO",
     "Units down twenty-five percent from Year 2 and price down five. We still make a profit from Year 4, but cash "
     "would go one point three five million negative. A one-point-five-million credit line, negotiated in "
     "Year 2, covers it, and we slow hiring."),
    ("Why an S.L., and why a 300,000 € ENISA loan?", "COO",
     "S.L.: limited liability, and the partners decide who comes in, which matters under security "
     "screening; investors join by capital increase, and we can become an S.A. later. ENISA is a "
     "participative loan with no personal guarantees, next to a bank loan, at a blended six percent."),
    ("Why should we believe 45 systems in Year 3?", "CMO",
     "Forty-five systems is about two orders the size of Romania's twenty-two Vectors, and thirty percent of "
     "units go to private operators, who decide in three to six months."),
    ("What stops Quantum, Indra or DJI from copying you?", "CTO",
     "Our VRIO is honest: the supply chain and the design can be copied in two or three years. The on-board "
     "autonomy is hard to copy: it is our own software, and it will improve with every hour flown. DJI is distrusted at sensitive sites, "
     "and with Indra we want to be a subcontractor, not a rival."),
    ("Is 160,000 € the right price?", "CMO",
     "It is value-based: the five-year cost is ninety-two point seven percent below a helicopter. It sits "
     "above a Skydio, about twenty thousand euros, and far below a Vector. Variable cost is about ninety-five "
     "thousand, so each aircraft contributes about sixty-five thousand."),
    ("Why does the TCO include a pilot if the system is autonomous?", "CMO",
     "Flights beyond visual line of sight still need a remote pilot to supervise. We count a quarter of a "
     "full-time pilot: about fifty-eight thousand euros over five years. It's the "
     "customer's cost, not ours, and we call the comparison illustrative."),
    ("Is 3.7 M€ for 40% a fair valuation?", "CFO",
     "Post-money is nine point two five million: investors pay one euro of nominal plus seventeen euros and "
     "fifty cents of premium per participation. By our own rough measure that is under two times Year 5 net "
     "income, and founders keep sixty percent with four-year vesting."),
    ("Your NPV is 2.26 M€, but you value the company at 9.25 M€. Why?", "CFO",
     "NPV is not the company's value: it is the value created after paying back every euro invested at "
     "fourteen point nine percent. The share price is agreed with investors, and by our own rough measure "
     "it is under two times Year 5 net income."),
    ("Will you need another round?", "CFO",
     "The base case needs none: Year 5 ends with six point eight one million in cash and no debt. Only the "
     "pessimistic case needs the one-and-a-half-million credit line."),
    ("How exactly do you compute break-even?", "CFO",
     "All fixed charges, including depreciation and interest, are three point eight nine million in Year 3. "
     "Divided by a forty-six point four percent contribution margin, that is eight point three seven million "
     "of revenue: thirty-nine point one full systems, each with its share of docks and licences. Bare "
     "aircraft alone would need about sixty."),
    ("You make a profit in Year 3, so why does cash fall?", "CFO",
     "Revenue more than doubles, so receivables and stock absorb zero point eight five million of extra "
     "working capital. We also invest half a million in equipment and repay three hundred thousand of debt. "
     "Profit is not cash."),
    ("Why a 25% tax shield in the WACC if you pay 0 to 15%?", "CFO",
     "The WACC is a long-run rate, and after the two new-entity years we pay the general twenty-five percent. "
     "We pay fifteen only in Years 4 and 5, the first two years with a positive tax base after offsetting "
     "the launch losses."),
    ("Why take debt at all if you raise equity?", "COO",
     "It costs six percent, interest is tax-deductible, and ENISA asks for no personal guarantees. From "
     "Year 3 return on assets is about sixteen percent, well above the six percent cost of debt, so the "
     "loans raise the return to shareholders while we repay them by Year 5."),
    ("Do you need an external audit?", "COO",
     "Yes, from Year 2. By size alone it would start in Year 4, but public contracts above six hundred "
     "thousand euros and over half of turnover bring it forward under the Audit Act. It is budgeted."),
    ("What does VanguardOS do, and why would 90% keep paying?", "Head of AI",
     "It commands the fleet, plans routes and runs the detection models we retrain and update. Ninety "
     "percent is our estimate. Without licences we would still be profitable in Years 4 and 5, but their "
     "margin is what makes break-even possible in Year 3."),
    ("How does it fly without GPS?", "Head of AI",
     "It navigates with its cameras when GPS is blocked. We test jamming only at authorised ranges, because "
     "jamming needs a spectrum permit."),
    ("What about the AI Act, data and cyberattacks?", "Head of AI",
     "Our civil software follows the AI Act. VanguardOS runs on European cloud servers or, as signed "
     "packages, on the customer's own defence network. Links are encrypted, and we pay for external security audits."),
    ("Your TCO counts one dock per aircraft, but you sell one dock for every two.", "CMO",
     "Right: the TCO shows one aircraft on one site, as a cautious example. When two aircraft share a dock, "
     "the cost per aircraft falls, so the saving is even bigger."),
    ("What is your biggest weakness?", "CEO",
     "No brand, references or certificates yet, little capital against big rivals, and few suppliers for "
     "key parts. So we also sell to private operators, who decide faster, and partner with Indra, Airbus or "
     "Thales instead of fighting them."),
    ("What if certification is late?", "CTO",
     "We hire a compliance engineer in Year 1, we stay under twenty-five kilos so civil flights need no "
     "type certificate, and we sell first in Spain. The pessimistic scenario already assumes slower sales."),
    ("What do SORA and BVLOS mean?", "CTO",
     "BVLOS is flying beyond the pilot's visual line of sight. SORA, the Specific Operations Risk Assessment, "
     "is the safety case AESA approves before it allows those flights."),
    ("Why Getafe if you cannot fly there?", "COO",
     "Getafe gives us the aerospace cluster, suppliers and engineers, at about five euros per square metre a "
     "month. We build there and fly at ATLAS, in Jaén, and CIAR, in Lugo."),
    ("Why assume 60 days to get paid if the public sector pays in 30?", "CFO",
     "It's cautious: sixty days is the legal limit between companies under Ley 15/2010. Assuming sixty "
     "means we finance more receivables, so the plan holds less cash, not more."),
    ("Your payback is 4.5 years. Is that discounted?", "CFO",
     "No, it is simple payback. Discounted at fourteen point nine percent, the five cash flows alone do not pay "
     "back within five years. That is why we show NPV with residual value: in Year 5 the company still owns "
     "four point nine five million of assets and working capital."),
    ("In the pessimistic case NPV is minus 1.85 M€. Why invest?", "CMO",
     "That case cuts units by twenty-five percent and price by five at the same time. Even then we make a "
     "profit from Year 4, and the credit line covers the cash. With twenty percent more units, NPV is four "
     "point three seven million. The risk is sales speed, and we test it with paid thirty-day trials."),
    ("Why is your team the right one?", "CEO",
     "We are six aerospace engineers, and VRIO rates that as parity, so we don't sell the team as our "
     "advantage. What we add is focus: one product family, and partners like Indra for the big programmes. Vesting "
     "keeps the founders here for four years."),
    ("0.7% of which market?", "CMO",
     "Of the European small-drone market forecast for 2030, three point seven billion euros. Today's market "
     "was two point one billion in 2025, so in Year 5 we are about one point three percent of the 2025 market."),
    ("Do you have any proof that customers want this?", "CMO",
     "No signed orders yet, and we say so. What we have is public demand: Spain's eighteen-million Skydio "
     "tender, Romania's order of twenty-two Vectors and the EU Defence Readiness Roadmap. We test it with paid "
     "thirty-day trials, and we only hire against signed orders."),
    ("How do your investors get their money back?", "CFO",
     "The plan doesn't model an exit. Investors own forty percent of a company that earns five point three "
     "six million in Year 5, with six point eight one million in cash and no debt, and they hold two of the "
     "five board seats."),
    ("Why a fixed-wing VTOL and not a quadcopter?", "CTO",
     "A quadcopter like Skydio's flies under an hour. Wings give us three hours, so one aircraft covers a "
     "whole perimeter, and vertical take-off still lets it land on the dock with nobody around."),
    ("24/7 or 300 hours a year?", "CMO",
     "Both: the dock keeps the aircraft ready day and night, and the TCO counts three hundred flight hours a "
     "year, the same hours as the helicopter patrol we compare with."),
    ("Skydio is famous for autonomy. Why is yours different?", "Head of AI",
     "Skydio's autonomy flies short quadcopter missions, under an hour. Ours flies three-hour fixed-wing "
     "patrols and lands on its dock alone. The part our VRIO rates as sustained is the on-board perception "
     "and GPS-free navigation; the dock and the ITAR-free supply chain give us a two-to-three-year lead."),
    ("Who buys your six systems in Year 1?", "CMO",
     "Six systems is one or two small contracts, all in Spain. We target launch pilots with public buyers "
     "and private operators after a paid thirty-day trial, and we hire only against signed orders."),
    ("Which founders sit on the board?", "CEO",
     "The CEO, the CTO and the CFO: the CEO, the CTO and the CFO, with the two seed investors. The other "
     "founders lead their departments and report to the CEO."),
    ("Your leverage index is above one in Year 1. Is debt helping you?", "CEO",
     "Not in Years 1 and 2: with losses, an index above one means the debt makes the loss bigger. From Year 3, "
     "return on assets of about sixteen percent is above the six percent cost of debt, so leverage helps."),
    ("Why constant 2027 prices?", "CEO",
     "The plan states every figure at constant 2027 prices and without VAT, so the five years compare like "
     "with like, and the margins do not depend on an inflation guess."),
    ("Is the payroll on the slide the full cost?", "COO",
     "No, it is gross pay. We add thirty-two percent employer social security, and the model includes it in "
     "personnel costs."),
    ("Year 5 runs at 120 of 126 systems of capacity. What if demand peaks?", "COO",
     "Each cell works one shift, so a second shift is available for delivery peaks, and we open a new cell "
     "only with signed orders."),
    ("How do you handle the dual-use and reputation risk?", "CEO",
     "We build no armed drones, and that is written policy. Every export has end-user control under the EU "
     "dual-use regulation, and our first sales are in Spain."),
]

HEADLINES = ["Price €160,000 (AV-1) · €45,000 (dock) · €18,000 per aircraft per year (licence)",
             "Need €5.2M · ask €3.7M for 40% · post-money €9.25M",
             "Break-even 39.1 systems vs 45 sold in Year 3",
             "NPV €2.26M (with residual value) · IRR 31.1% · WACC 14.9% · payback 4.5 years",
             "Cash trough €0.78M (Year 3) · Year 5 cash €6.81M, zero debt",
             "TCO −92.7% vs helicopter · 17 → 85 people · 60/30/10 segment split"]


def seconds(d, prev_who):
    s = round(len(d["script"].split()) / WPM * 60) + PAUSE
    return s + (SWAP if prev_who and prev_who != d["who"] else 0)


def build():
    make_charts()
    t, prev = 0, None
    for i, d in enumerate(SLIDES, 1):
        sl = prs.slides.add_slide(BLANK)
        if d["fn"] is not s1:
            frame(sl, i, d["title"], d["source"], dark=d["fn"] is s12)
        d["fn"](sl)
        if d["script"]:
            d["t"] = (t, t + seconds(d, prev))
            t, prev = d["t"][1], d["who"]
            a, b = d["t"]
            sl.notes_slide.notes_text_frame.text = (
                f"{d['who']} · {a // 60}:{a % 60:02d}–{b // 60}:{b % 60:02d}\n\n{d['script']}")
    prs.save(OUT_PPTX)
    return t


def guide(total_s):
    words = lambda s: len(s.split())
    out = ["# AeroVanguard: final presentation guide (Group B, Group 46)", "",
           "Generated by `build_deck.py` from the same data as `AeroVanguard_Canva_Base.pptx`. Every figure "
           "comes from the final Business Plan and the Excel model. Numbers in the script are written the way "
           "they are said, so the word count is the spoken length.", "",
           "## Timing", "", "| # | Speaker | Time | Words | Action title |", "|---|---|---|---|---|"]
    for i, d in enumerate(SLIDES, 1):
        if d.get("t"):
            a, b = d["t"]
            out.append(f"| {i} | {d['who']} | {a // 60}:{a % 60:02d}–{b // 60}:{b % 60:02d} | "
                       f"{words(d['script'])} | {d['title']} |")
    n = sum(words(d["script"]) for d in SLIDES)
    out += ["", f"Spoken script: {n} words. At {WPM} words a minute, plus {PAUSE} s per slide and {SWAP} s per "
            f"change of speaker, the talk lasts {total_s // 60}:{total_s % 60:02d}: {480 - total_s} s under "
            f"the 8-minute limit. At a nervous 125 words a minute it would last about "
            f"{(slow := round(n / 125 * 60) + total_s - round(n / WPM * 60)) // 60}:{slow % 60:02d}. Rehearse with a stopwatch at a calm pace; red line 7:15. If a run is over, cut "
            "the last sentence of slide 7, then the credit-line sentence of slide 12 (keep it for the Q&A); "
            "over 7:30, make both cuts permanent.", "",
            "## Delivery notes", "",
            "- The next speaker starts only once standing in place; each part ends with the next speaker's name.",
            "- Say the acronyms the same way every time: V-R-I-O, E-BIT-DA, N-P-V, I-R-R, WACC as \"wack\", "
            "S-L and S-A, SORA as one word.",
            "- Drill the teen/ty pairs (fifteen / fifty, eighteen / eighty, thirteen / thirty) and the words "
            "that start with s + consonant (Spain, strong, State, stock, scale): no extra \"e\" in front.",
            "- Every member learns the headline numbers below: the professor may ask anyone.",
            "- Asked about another member's part: give the headline number in one sentence, then say "
            "\"the CFO (or the owner) can add the detail\". Never stop at \"I don't know\".", ""]
    out += [f"- {h}" for h in HEADLINES]
    out += ["", "## Slides", ""]
    for i, d in enumerate(SLIDES, 1):
        out += [f"### {i}. {d['title']}", "", f"- **Speaker:** {d['who']}",
                f"- **Canva layout:** {d['screen']}",
                f"- **Source line:** {d['source'] or 'Skydio (2025); SCSP (2025)'}", ""]
        if d["script"]:
            out += ["> " + d["script"], ""]
    out += ["## Defence cheat sheet (about 15 seconds each)", "",
            "Questions 1 to 10 are the classic traps; the rest are the next most likely. Every member has at "
            "least one.", ""]
    for i, (q, who, a) in enumerate(QA, 1):
        out += [f"**{i}. {q}** ({who})", "", a, ""]
    OUT_MD.write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    guide(build())
    print(OUT_PPTX, OUT_MD, sep="\n")
