"""Topic 2 figures for Business Management: diagrams redrawn from Topic 2_ Value creation.pdf."""
from figures.bm_common import arrow, box, elbow, mid
from figures.svgkit import Canvas, Registry, line, text

REG = Registry("BM-T2")


def stakeholders():
    c = Canvas(620, 330)
    m = (240, 140, 140, 50)
    others = [((20, 20, 170, 44), "Shareholders", "top", "bottom"),
              ((430, 20, 170, 44), ["Banks and other", "financial agents"], "top", "bottom"),
              ((440, 143, 160, 44), "Customers", "right", "left"),
              ((430, 266, 170, 44), "Suppliers", "bottom", "top"),
              ((240, 276, 140, 40), "State", "bottom", "top"),
              ((20, 266, 170, 44), ["Employees /", "labour unions"], "bottom", "top"),
              ((20, 143, 160, 44), "Society (CSR)", "left", "right")]
    for bb, s, ms, os_ in others:
        start = mid(m, ms)
        if ms in ("top", "bottom") and bb[0] != 240:
            start = (start[0] + (-40 if bb[0] < 240 else 40), start[1])
        line(c, start, mid(bb, os_), "EDGE", 1.4)
        box(c, *bb, s, "BLUE", size=12)
    box(c, *m, "MANAGEMENT", "ACC", weight="700")
    REG.put("stakeholders", c, "Stakeholders of the firm",
            "The stakeholders around management: shareholders, banks and other financial agents, customers, "
            "suppliers, the State, employees and labour unions, and society")


def unified_vision():
    c = Canvas(640, 370)
    pm = box(c, 20, 20, 170, 50, ["Products / markets", "(current and new)"], "PINK", size=12)
    sa = box(c, 260, 25, 110, 40, "Sales", "BLUE")
    pr = box(c, 450, 25, 150, 40, "Profits", "PINK", weight="700")
    rp = box(c, 250, 110, 160, 50, ["Retained profits", "(for future investments)"], "GREEN", size=12)
    dv = box(c, 450, 120, 150, 40, "Dividends", "BLUE")
    cm = box(c, 440, 205, 170, 56, ["Capital market", "valuation of the company"], "BLUE", size=12)
    ea = box(c, 240, 300, 170, 50, ["Equity attributable", "to investors"], "BLUE", size=12)
    te = box(c, 20, 290, 170, 50, "Total equity", "GREEN", weight="700")
    iv = box(c, 20, 170, 170, 40, "Investments", "PINK", weight="700")
    arrow(c, mid(pm, "right"), mid(sa, "left"), "EDGE", 2); arrow(c, mid(sa, "right"), mid(pr, "left"), "EDGE", 2)
    arrow(c, (470, 65), (400, 110), "EDGE", 2); arrow(c, mid(pr, "bottom"), mid(dv, "top"), "EDGE", 2)
    arrow(c, mid(dv, "bottom"), mid(cm, "top"), "EDGE", 2)
    elbow(c, [(525, 261), (525, 325), (410, 325)], "EDGE", 2)
    arrow(c, (240, 325), (190, 325), "EDGE", 2)
    elbow(c, [(250, 135), (215, 135), (215, 302), (190, 302)], "EDGE", 2)
    arrow(c, mid(te, "top"), mid(iv, "bottom"), "EDGE", 2); arrow(c, mid(iv, "top"), mid(pm, "bottom"), "EDGE", 2)
    REG.put("unified-vision", c, "A unified vision: survival, profit and growth",
            "Survival, profit and growth as one cycle: products and markets bring sales and profits; profits are "
            "retained or paid as dividends; both feed total equity, which finances new investments")


def decisions():
    c = Canvas(660, 110)
    labels = [["Business", "objective"], ["Define a", "strategy"], ["Strategic", "decisions"], ["Tactic", "decisions"], ["Operative", "decisions"]]
    cols = ["ACC", "BLUE", "PINK", "PINK", "PINK"]
    prev = None
    for k, (s, col) in enumerate(zip(labels, cols)):
        b = box(c, 10 + k * 130, 30, 110, 50, s, col, size=12, head_first=True)
        if prev:
            arrow(c, mid(prev, "right"), mid(b, "left"), "EDGE", 2)
        prev = b
    REG.put("decisions", c, "From objective to decisions",
            "To reach the objective the firm defines a strategy, which unfolds into strategic, tactic and "
            "operative decisions")


def types():
    c = Canvas(660, 290)
    root = box(c, 10, 120, 140, 50, ["Strategic", "decisions"], "PINK", weight="700")
    cs = box(c, 200, 45, 170, 44, "Corporate strategy", "BLUE", weight="700")
    bs = box(c, 200, 200, 170, 44, ["Competitive or", "business strategy"], "GREEN", head_first=True, size=12)
    elbow(c, [(150, 145), (175, 145), (175, 67), (200, 67)], "EDGE", 1.4)
    elbow(c, [(150, 145), (175, 145), (175, 222), (200, 222)], "EDGE", 1.4)
    for k, s in enumerate(["Product scope (diversification)", "Geographical scope (internationalization)", "Vertical scope (vertical integration)"]):
        y = 5 + k * 42
        box(c, 410, y, 240, 32, s, "BLUE", size=11)
        elbow(c, [(370, 67), (390, 67), (390, y + 16), (410, y + 16)], "EDGE", 1.2)
    for k, s in enumerate(["Cost-leadership strategy", "Differentiation strategy"]):
        y = 180 + k * 46
        box(c, 410, y, 240, 34, s, "GREEN", size=12)
        elbow(c, [(370, 222), (390, 222), (390, y + 17), (410, y + 17)], "EDGE", 1.2)
    REG.put("types", c, "Types of strategic decisions",
            "Strategic decisions split into corporate strategy (product, geographical and vertical scope) and "
            "competitive or business strategy (cost leadership or differentiation)")


def success():
    c = Canvas(600, 250)
    s = box(c, 200, 10, 200, 50, "Successful strategy", "ACC", weight="700")
    e = box(c, 40, 95, 520, 36, "EFFECTIVE IMPLEMENTATION", "BLUE", weight="700")
    arrow(c, mid(e, "top"), mid(s, "bottom"), "EDGE", 2.4)
    ps = [["Long-term, simple and", "agreed objectives"], ["Deep understanding of the", "competitive environment"], ["Objective appraisal", "of resources"]]
    for k, p in enumerate(ps):
        b = box(c, 40 + k * 180, 175, 160, 56, p, "GREEN", size=12)
        arrow(c, mid(b, "top"), (120 + k * 180, 131), "EDGE", 2)
    REG.put("success", c, "What makes a successful strategy",
            "A successful strategy rests on effective implementation of agreed long-term objectives, a deep "
            "understanding of the competitive environment and an objective appraisal of resources")


def environment():
    c = Canvas(680, 330)
    c.add('<rect x="5" y="5" width="670" height="320" rx="14" fill="BLUE" fill-opacity="0.04" stroke="BLUE" stroke-width="1.4" stroke-dasharray="6,4"/>')
    text(c, (20, 28), "GENERIC ENVIRONMENT", "BLUE", weight="700")
    box(c, 20, 40, 205, 100, ["Economic factors", "Macroeconomic variables", "Business cycle period", "Type of economic policy", "Country resources"], "BLUE", size=11, head_first=True)
    box(c, 20, 155, 205, 160, ["Socio-cultural factors", "Value system", "Level of education", "Class structure", "Income distribution", "Population distribution", "Etc."], "BLUE", size=11, head_first=True)
    box(c, 455, 40, 205, 85, ["Political-legal factors", "Monetary and fiscal policies", "Labour market regulation", "Industry regulation"], "BLUE", size=11, head_first=True)
    box(c, 455, 155, 205, 85, ["Technological factors", "Basic technologies", "Key technologies", "Incipient technologies"], "BLUE", size=11, head_first=True)
    c.add('<rect x="238" y="40" width="204" height="275" rx="12" fill="GREEN" fill-opacity="0.06" stroke="GREEN" stroke-width="1.6"/>')
    text(c, (340, 60), "SPECIFIC ENVIRONMENT", "GREEN", "middle", weight="700")
    box(c, 250, 70, 180, 56, ["Rivalry within the industry", "concentration, rate of growth,", "product differentiation"], "GREEN", size=10, head_first=True)
    for k, s in enumerate(["Barriers to entry", "Barriers to exit", "Substitutes", "Relationship with customers", "Relationship with suppliers"]):
        box(c, 250, 134 + k * 36, 180, 30, s, "GREEN", size=11)
    REG.put("environment", c, "The business environment",
            "The two layers of the business environment: the generic environment (economic, political-legal, "
            "socio-cultural and technological factors) around the specific environment of the industry")


def industry():
    c = Canvas(620, 320)
    ce = box(c, 215, 105, 190, 110, ["THE INDUSTRY ENVIRONMENT", "Suppliers", "Competitors", "Customers"], "ACC", head_first=True, size=12)
    outs = [((20, 20), ["The national /", "international economy"]), ((20, 135), "Technology"), ((20, 250), ["Government", "and politics"]),
            ((440, 20), ["The natural", "environment"]), ((440, 135), ["Demographic", "structure"]), ((440, 250), ["Social", "structure"])]
    for (x, y), s in outs:
        b = box(c, x, y, 160, 50, s, "BLUE", size=12, rx=25)
        tgt = (215, 160) if x < 300 else (405, 160)
        arrow(c, mid(b, "right") if x < 300 else mid(b, "left"), tgt, "EDGE", 1.4)
    REG.put("industry", c, "From environmental analysis to industry analysis",
            "The industry environment (suppliers, competitors, customers) inside the wider environment that "
            "acts on it")


def five_forces():
    c = Canvas(700, 470)
    cen = box(c, 255, 165, 190, 140, ["INDUSTRY RIVALRY", "Rivalry among existing firms", "Concentration", "Diversity of competitors", "Product differentiation", "Excess capacity and exit barriers", "Cost conditions"], "PINK", size=11, head_first=True)
    sup = box(c, 255, 10, 190, 80, ["SUPPLIER POWER", "Bargaining power of suppliers:", "suppliers' price sensitivity,", "relative bargaining power"], "BLUE", size=11, head_first=True)
    buy = box(c, 255, 380, 190, 80, ["BUYER POWER", "Bargaining power of buyers:", "buyers' price sensitivity,", "relative bargaining power"], "BLUE", size=11, head_first=True)
    ent = box(c, 10, 130, 200, 210, ["THREAT OF ENTRY", "(potential entrants)", "Capital requirements", "Economies of scale", "Absolute cost advantage", "Product differentiation", "Access to distribution", "channels", "Legal / regulatory barriers"], "GREEN", size=11, head_first=True)
    sub = box(c, 490, 150, 200, 170, ["SUBSTITUTE COMPETITION", "(threat of substitutes)", "Buyers' propensity", "to substitute", "Relative prices and", "performance of", "substitutes"], "GREEN", size=11, head_first=True)
    arrow(c, mid(sup, "bottom"), mid(cen, "top"), "EDGE", 2); arrow(c, mid(buy, "top"), mid(cen, "bottom"), "EDGE", 2)
    arrow(c, mid(ent, "right"), mid(cen, "left"), "EDGE", 2); arrow(c, mid(sub, "left"), mid(cen, "right"), "EDGE", 2)
    REG.put("five-forces", c, "Porter's five competitive forces",
            "Porter's five competitive forces (1982) and the determinants of each: supplier power, buyer power, "
            "threat of entry, substitute competition and the rivalry among existing firms")


def strategy_questions():
    c = Canvas(660, 250)
    r = box(c, 10, 85, 190, 80, ["Rate of profit above", "the competitive level", "How do we make money?"], "ACC", size=12, head_first=False)
    ia = box(c, 250, 20, 200, 60, ["Industry attractiveness", "Which businesses should", "we be in?"], "BLUE", size=11, head_first=True)
    ca = box(c, 250, 170, 200, 60, ["Competitive advantage", "How should we compete?"], "GREEN", size=11, head_first=True)
    co = box(c, 500, 30, 150, 40, "CORPORATE STRATEGY", "BLUE", weight="700", size=12)
    bu = box(c, 500, 180, 150, 40, "BUSINESS STRATEGY", "GREEN", weight="700", size=12)
    arrow(c, (200, 110), mid(ia, "left"), "EDGE", 2); arrow(c, (200, 140), mid(ca, "left"), "EDGE", 2)
    arrow(c, mid(ia, "right"), mid(co, "left"), "EDGE", 2); arrow(c, mid(ca, "right"), mid(bu, "left"), "EDGE", 2)
    REG.put("strategy-questions", c, "Corporate strategy and business strategy",
            "A rate of profit above the competitive level comes from two sources: being in attractive industries "
            "(corporate strategy) and holding a competitive advantage (business strategy)")


def scope():
    c = Canvas(660, 300)
    text(c, (10, 95), "Single", "HEAD", weight="700"); text(c, (10, 112), "integrated firm", "HEAD", weight="700")
    text(c, (10, 225), "Several", "HEAD", weight="700"); text(c, (10, 242), "specialized firms", "HEAD", weight="700")
    for k, (lab, l) in enumerate((("Vertical scope", "V"), ("Product scope", "P"), ("Geographical scope", "G"))):
        x0 = 150 + k * 175
        text(c, (x0 + 75, 20), lab, "BLUE", "middle", weight="700")
        if l == "V":
            c.add(f'<rect x="{x0 + 45}" y="40" width="60" height="120" rx="8" fill="BLUE" fill-opacity="0.10" stroke="BLUE" stroke-width="1.4"/>')
            for j in range(3):
                text(c, (x0 + 75, 70 + j * 32), f"V{j + 1}", "HEAD", "middle", 14, "700")
            for j in range(3):
                box(c, x0 + 50, 180 + j * 40, 50, 28, f"V{j + 1}", "GREEN", weight="700")
                if j:
                    arrow(c, (x0 + 75, 180 + (j - 1) * 40 + 28), (x0 + 75, 180 + j * 40), "EDGE", 1.4)
        else:
            c.add(f'<rect x="{x0}" y="80" width="150" height="40" rx="8" fill="BLUE" fill-opacity="0.10" stroke="BLUE" stroke-width="1.4"/>')
            for j in range(3):
                text(c, (x0 + 25 + j * 50, 105), f"{l}{j + 1}", "HEAD", "middle", 14, "700")
                box(c, x0 + 3 + j * 50, 215, 44, 28, f"{l}{j + 1}", "GREEN", weight="700")
    REG.put("scope", c, "The three dimensions of scope",
            "The scope of a firm along each dimension: one integrated firm linked by an administrative interface, "
            "or several specialized firms linked by market interfaces (after Grant, 2002)")


def advantage():
    c = Canvas(560, 190)
    t = box(c, 170, 10, 220, 46, "COMPETITIVE ADVANTAGE", "ACC", weight="700")
    a = box(c, 20, 110, 230, 60, ["COST ADVANTAGE", "Similar product at lower cost"], "BLUE", size=12, head_first=True)
    b = box(c, 310, 110, 230, 60, ["DIFFERENTIATION ADVANTAGE", "Price premium from unique product"], "GREEN", size=12, head_first=True)
    arrow(c, (240, 56), mid(a, "top"), "EDGE", 2); arrow(c, (320, 56), mid(b, "top"), "EDGE", 2)
    REG.put("advantage", c, "Sources of competitive advantage",
            "The two sources of competitive advantage: cost advantage and differentiation advantage")


def value_chain():
    c = Canvas(680, 330)
    x0, x1 = 120, 560
    text(c, (10, 75), "Support", "HEAD", weight="700"); text(c, (10, 92), "activities", "HEAD", weight="700")
    for k, s in enumerate(["Firm infrastructure", "Human resources", "Technology development", "Procurement"]):
        box(c, x0, 20 + k * 34, x1 - x0, 30, s, "BLUE", size=12, rx=4)
    prim = [["Inbound", "logistics"], ["Operations"], ["Outbound", "logistics"], ["Marketing", "and sales"], ["Service"]]
    cols = ["BLUE", "ACC", "GREEN", "PINK", "PINK"]
    w = (x1 - x0) / 5
    for k, (s, col) in enumerate(zip(prim, cols)):
        box(c, x0 + k * w, 165, w - 4, 110, s, col, size=12, rx=4)
    c.add(f'<path d="M{x1 + 4},20 L{x1 + 4},275 L{x1 + 100},147 Z" fill="ACC" fill-opacity="0.15" stroke="ACC" stroke-width="1.4"/>')
    text(c, (x1 + 40, 152), "Margin", "HEAD", "middle", 13, "700")
    text(c, (x0 + (x1 - x0) / 2, 300), "Primary activities", "HEAD", "middle", weight="700")
    REG.put("value-chain", c, "Porter's value chain",
            "Porter's value chain (1985): four support activities above five primary activities, whose "
            "combined result is the margin")


def build():
    for fn in (stakeholders, unified_vision, decisions, types, success, environment, industry, five_forces,
               strategy_questions, scope, advantage, value_chain):
        fn()
    return REG
