"""Topic 1 figures for Business Management: diagrams redrawn from Topic 1_The Firm_Types  Objectives.pdf."""
from figures.bm_common import arrow, box, elbow, mid
from figures.svgkit import Canvas, Registry, line, text

REG = Registry("BM-T1")


def bread():
    c = Canvas(600, 230)
    ins = ["Sea salt", "Baking powder", "Wheat flour", "Sugar", "Water"]
    text(c, (95, 22), "INPUTS", "HEAD", "middle", weight="700")
    for i, s in enumerate(ins):
        box(c, 30, 34 + i * 38, 130, 30, s, "BLUE")
    b = box(c, 240, 95, 110, 50, "?", "ACC", weight="700", size=22)
    for i in range(5):
        arrow(c, (160, 49 + i * 38), (238, 120), "EDGE", 1.2)
    o = box(c, 430, 85, 140, 70, ["OUTPUT", "Bread"], "GREEN", head_first=True)
    arrow(c, mid(b, "right"), mid(o, "left"), "ACC", 2.4)
    REG.put("bread", c, "Production process of bread",
            "Production process of bread: ingredients (inputs) must be transformed by a business activity, the "
            "question mark, before they become the output")


def circular_flow():
    c = Canvas(680, 400)
    h = box(c, 20, 165, 150, 60, "HOUSEHOLDS", "HEAD", weight="700", fill=False)
    f = box(c, 460, 165, 150, 60, "FIRMS", "HEAD", weight="700", fill=False)
    box(c, 245, 15, 140, 100, ["Market of", "goods and", "services"], "BLUE")
    box(c, 245, 280, 140, 100, ["Market of", "factors of", "production"], "BLUE")
    # top loop: goods (real) and expenditures (money)
    elbow(c, [(560, 165), (560, 38), (385, 38)], "BLUE", 2)
    elbow(c, [(245, 38), (70, 38), (70, 165)], "BLUE", 2)
    text(c, (472, 30), "goods and services", "BLUE", "middle", 12)
    text(c, (158, 30), "goods and services", "BLUE", "middle", 12)
    elbow(c, [(120, 165), (120, 95), (245, 95)], "GREEN", 2)
    elbow(c, [(385, 95), (510, 95), (510, 165)], "GREEN", 2)
    text(c, (182, 88), "expenditures", "GREEN", "middle", 12)
    text(c, (448, 88), "revenues", "GREEN", "middle", 12)
    # bottom loop: factors (real) and incomes (money)
    elbow(c, [(70, 225), (70, 357), (245, 357)], "BLUE", 2)
    elbow(c, [(385, 357), (560, 357), (560, 225)], "BLUE", 2)
    text(c, (158, 372), "factors of production", "BLUE", "middle", 12)
    text(c, (472, 372), "factors of production", "BLUE", "middle", 12)
    elbow(c, [(510, 225), (510, 300), (385, 300)], "GREEN", 2)
    elbow(c, [(245, 300), (120, 300), (120, 225)], "GREEN", 2)
    text(c, (392, 318), "wages, rents, dividends", "GREEN", "start", 11)
    text(c, (182, 318), "incomes", "GREEN", "middle", 12)
    arrow(c, mid(f, "right"), (650, 195), "ACC", 2)
    text(c, (650, 182), "profit", "ACC", "end", 12, "700")
    line(c, (250, 205), (275, 205), "BLUE", 2); text(c, (282, 209), "real flows", "BLUE", size=12)
    line(c, (250, 228), (275, 228), "GREEN", 2); text(c, (282, 232), "financial flows", "GREEN", size=12)
    REG.put("circular-flow", c, "Circular flow of income",
            "Circular flow of income: real flows (goods, services, factors) run one way and financial flows "
            "(expenditures, revenues, wages, rents, dividends) run the opposite way through the two markets")


def functions():
    c = Canvas(660, 340)
    text(c, (10, 22), "REAL FUNCTIONS", "BLUE", weight="700")
    i = box(c, 10, 34, 120, 40, "Inputs", "BLUE")
    r = box(c, 230, 34, 160, 40, "Real activity", "BLUE", weight="700")
    o = box(c, 490, 34, 120, 40, "Outputs", "BLUE")
    arrow(c, mid(i, "right"), mid(r, "left"), "BLUE", 2); arrow(c, mid(r, "right"), mid(o, "left"), "BLUE", 2)
    text(c, (10, 180), "FINANCIAL FUNCTIONS", "GREEN", weight="700")
    fr = box(c, 10, 192, 150, 50, ["Fundraising (search for", "financial resources)"], "GREEN", size=12)
    fa = box(c, 230, 192, 160, 50, "Financial activity", "GREEN", weight="700")
    rc = box(c, 460, 192, 180, 50, ["Return of capital", "and interests"], "GREEN", size=12)
    arrow(c, mid(fr, "right"), mid(fa, "left"), "GREEN", 2); arrow(c, mid(fa, "right"), mid(rc, "left"), "GREEN", 2)
    elbow(c, [(270, 192), (270, 120), (70, 120), (70, 74)], "GREEN", 1.6)
    text(c, (170, 112), "payment for inputs' acquisition", "GREEN", "middle", 11)
    elbow(c, [(550, 74), (550, 140), (350, 140), (350, 192)], "GREEN", 1.6)
    text(c, (450, 155), "revenues from sales", "GREEN", "middle", 11)
    text(c, (10, 290), "MANAGEMENT FUNCTIONS", "ACC", weight="700")
    for k, s in enumerate(("Planning", "Organization", "Control")):
        box(c, 200 + k * 150, 298, 130, 34, s, "ACC")
    REG.put("functions", c, "Business functional areas",
            "Business functional areas: the real cycle (inputs, real activity, outputs), the financial cycle that "
            "runs alongside it, and the management functions that govern both")


def fayol():
    c = Canvas(620, 410)
    box(c, 230, 175, 160, 60, ["Achieving the", "organization's", "stated purpose"], "ACC", size=12)
    org = box(c, 185, 15, 250, 80, ["Organizing", "Determining what needs to be done,", "how it will be done, and who", "is to do it"], "BLUE", size=12, head_first=True)
    pla = box(c, 425, 165, 190, 80, ["Planning", "Defining goals, establishing", "strategy, and developing subplans", "to coordinate activities"], "BLUE", size=11, head_first=True)
    lea = box(c, 5, 165, 190, 80, ["Leading", "Directing and motivating", "all involved parties and", "resolving conflicts"], "BLUE", size=11, head_first=True)
    con = box(c, 185, 315, 250, 80, ["Controlling", "Monitoring activities to ensure", "that they are accomplished", "as planned"], "BLUE", size=12, head_first=True)
    elbow(c, [(520, 165), (520, 55), (435, 55)], "EDGE", 2)
    elbow(c, [(185, 55), (100, 55), (100, 165)], "EDGE", 2)
    elbow(c, [(100, 245), (100, 355), (185, 355)], "EDGE", 2)
    elbow(c, [(435, 355), (520, 355), (520, 245)], "EDGE", 2)
    REG.put("fayol", c, "The management process",
            "The management process as a cycle: planning, organizing, leading and controlling, all aimed at "
            "achieving the organization's stated purpose (Henri Fayol)")


def market_enterprise():
    c = Canvas(560, 330)
    a = box(c, 80, 10, 400, 50, ["Scarce resources (factors of production)", "versus unlimited wants"], "HEAD", size=12)
    b = box(c, 150, 95, 260, 40, "Specialization = division of labour", "BLUE")
    d = box(c, 200, 170, 160, 40, "Coordination", "BLUE", weight="700")
    m = box(c, 80, 250, 150, 44, "MARKET", "GREEN", weight="700")
    e = box(c, 330, 250, 150, 44, "ENTERPRISE", "GREEN", weight="700")
    arrow(c, mid(a, "bottom"), mid(b, "top"), "EDGE", 2); arrow(c, mid(b, "bottom"), mid(d, "top"), "EDGE", 2)
    arrow(c, (260, 210), mid(m, "top"), "EDGE", 2); arrow(c, (300, 210), mid(e, "top"), "EDGE", 2)
    text(c, (405, 320), "arises from a dissatisfied need", "ACC", "middle", 12, "700")
    REG.put("market-enterprise", c, "Nature of business: market and enterprise",
            "How needs are satisfied: specialization calls for coordination, which is provided either by the "
            "market or by the enterprise")


def rights():
    c = Canvas(620, 360)
    a = box(c, 170, 10, 280, 36, "Internal organization = teamwork", "HEAD")
    b = box(c, 170, 70, 280, 36, "Team production requires a CONTROLLER", "BLUE", weight="700")
    q = box(c, 170, 130, 280, 36, "Incentive for this task?", "ACC")
    arrow(c, mid(a, "bottom"), mid(b, "top"), "EDGE", 2); arrow(c, mid(b, "bottom"), mid(q, "top"), "EDGE", 2)
    rs = [["To receive the residual", "income or surplus"], ["To control and reassign the", "other factors of production"],
          ["To be the central party", "in all the contracts", "with the inputs"], ["To sell the", "mentioned rights"]]
    for k, s in enumerate(rs):
        x = 20 + k * 148
        bb = box(c, x, 200, 140, 60, s, "GREEN", size=10)
        arrow(c, mid(q, "bottom"), mid(bb, "top"), "EDGE", 1.4)
        arrow(c, mid(bb, "bottom"), (310, 300), "EDGE", 1.2)
    box(c, 130, 300, 360, 40, "The entrepreneur holds all these rights", "HEAD", weight="700")
    REG.put("rights", c, "The entrepreneur as holder of rights",
            "Why someone supervises team production: the controller is rewarded with four rights, and whoever "
            "holds them all is the entrepreneur")


def forms():
    c = Canvas(640, 330)
    root = box(c, 10, 140, 150, 50, ["Forms of business", "ownership"], "HEAD", weight="700")
    items = [("Sole proprietorship", []), ("Partnership", ["General partnership", "Limited liability partnership (LLP)"]),
             ("Corporation", []), ("Others", ["Cooperative associations", "Joint ventures", "Mutual companies, etc."])]
    ys = [20, 90, 170, 250]
    for (name, subs), y in zip(items, ys):
        b = box(c, 220, y, 150, 40, name, "BLUE", weight="700")
        elbow(c, [(160, 165), (190, 165), (190, y + 20), (220, y + 20)], "EDGE", 1.4)
        for j, s in enumerate(subs):
            sy = y - 10 + j * 30 if len(subs) == 3 else y - 6 + j * 30
            box(c, 420, sy, 210, 26, s, "GREEN", size=12)
            elbow(c, [(370, y + 20), (395, y + 20), (395, sy + 13), (420, sy + 13)], "EDGE", 1.2)
    REG.put("forms", c, "Forms of business ownership",
            "Forms of business ownership: sole proprietorship, partnership (general or limited liability), "
            "corporation, and other forms such as cooperatives, joint ventures and mutual companies")


def agency():
    c = Canvas(660, 300)
    text(c, (130, 20), "PROBLEM", "PINK", "middle", weight="700")
    p1 = box(c, 20, 35, 220, 50, ["Managers look for", "their own benefit"], "PINK")
    p2 = box(c, 20, 120, 220, 50, ["Conflict of interest between", "ownership and control"], "PINK")
    p3 = box(c, 20, 205, 220, 50, "AGENCY PROBLEM", "PINK", weight="700")
    arrow(c, mid(p1, "bottom"), mid(p2, "top"), "EDGE", 2); arrow(c, mid(p2, "bottom"), mid(p3, "top"), "EDGE", 2)
    text(c, (480, 20), "SOLUTION: MECHANISMS OF CONTROL", "GREEN", "middle", weight="700")
    ms = ["Selecting the Board of Directors", "Contracts with managers (goal linked)", "Requesting audits",
          "Additional mechanisms: indicators"]
    for k, s in enumerate(ms):
        box(c, 330, 35 + k * 55, 300, 42, s, "GREEN", size=12)
    arrow(c, mid(p3, "right"), (328, 230), "EDGE", 2)
    REG.put("agency", c, "Separation of ownership and control",
            "Separation of ownership and control: the chain that leads to the agency problem and the mechanisms "
            "shareholders use to control managers")


def build():
    for fn in (bread, circular_flow, functions, fayol, market_enterprise, rights, forms, agency):
        fn()
    return REG
