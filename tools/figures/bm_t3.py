"""Topic 3 figures for Business Management: diagrams redrawn from Topic 3_Financial Management (I).pdf."""
from figures.bm_common import arrow, box, elbow, mid
from figures.svgkit import Canvas, Registry, text

REG = Registry("BM-T3")


def finance_area():
    c = Canvas(600, 230)
    a = box(c, 120, 10, 360, 44, ["Finance area: collection and management", "of the funds (capital) used by the company"], "HEAD", size=12)
    m = box(c, 160, 75, 280, 36, "The finance manager faces two decisions", "ACC", size=12)
    arrow(c, mid(a, "bottom"), mid(m, "top"), "EDGE", 2)
    q1 = box(c, 40, 135, 220, 36, "What to invest in and when?", "BLUE", size=12, rx=18)
    q2 = box(c, 340, 135, 220, 36, "How to obtain the money to invest?", "GREEN", size=12, rx=18)
    arrow(c, (250, 111), mid(q1, "top"), "EDGE", 1.6); arrow(c, (350, 111), mid(q2, "top"), "EDGE", 1.6)
    d1 = box(c, 70, 185, 160, 34, "Investing decisions", "BLUE", weight="700", size=12)
    d2 = box(c, 370, 185, 160, 34, "Financing decisions", "GREEN", weight="700", size=12)
    arrow(c, mid(q1, "bottom"), mid(d1, "top"), "EDGE", 1.6); arrow(c, mid(q2, "bottom"), mid(d2, "top"), "EDGE", 1.6)
    REG.put("finance-area", c, "The finance area and its two decisions",
            "The finance manager's two questions and the decisions they correspond to")


def structures():
    c = Canvas(600, 300)
    text(c, (150, 22), "ECONOMIC STRUCTURE", "BLUE", "middle", weight="700")
    text(c, (450, 22), "FINANCIAL STRUCTURE", "GREEN", "middle", weight="700")
    box(c, 40, 32, 220, 150, ["ASSETS", "what is owned", "investments: goods", "and rights", "", "→ PROFITABILITY"], "BLUE", size=13, head_first=True, rx=4)
    box(c, 340, 32, 220, 150, ["EQUITY + LIABILITIES", "what is owed", "sources of financing", "(debt and liabilities)", "", "→ COST"], "GREEN", size=13, head_first=True, rx=4)
    box(c, 120, 215, 360, 60, ["OBJECTIVE: MAXIMIZE VALUE", "PROFITABILITY > COST"], "ACC", weight="700", size=14)
    REG.put("structures", c, "Economic and financial structure",
            "The two sides of the firm: the assets (economic structure) generate profitability, equity and "
            "liabilities (financial structure) carry a cost; value is created when profitability exceeds cost")


def balance():
    c = Canvas(560, 300)
    text(c, (140, 20), "ASSETS", "BLUE", "middle", weight="700")
    text(c, (420, 20), "LIABILITIES AND EQUITY", "GREEN", "middle", weight="700")
    box(c, 30, 30, 220, 140, ["Non-current assets", "the remainder: long-term", "investments, land, building,", "equipment, patents"], "BLUE", size=12, head_first=True, rx=2)
    box(c, 30, 170, 220, 110, ["Current assets", "used or turned into cash", "within one year"], "BLUE", size=12, head_first=True, rx=2)
    box(c, 310, 30, 220, 100, ["Stockholders' equity", "contributed capital", "+ retained earnings"], "GREEN", size=12, head_first=True, rx=2)
    box(c, 310, 130, 220, 70, ["Long-term liabilities", "not due within the year"], "GREEN", size=12, head_first=True, rx=2)
    box(c, 310, 200, 220, 80, ["Current liabilities", "paid or satisfied", "within the coming year"], "GREEN", size=12, head_first=True, rx=2)
    text(c, (280, 160), "=", "HEAD", "middle", 26, "700")
    REG.put("balance", c, "Layout of the balance sheet",
            "Layout of the balance sheet: total assets (non-current + current) equal total liabilities and "
            "stockholders' equity. Block sizes are only illustrative")


def financial_map():
    c = Canvas(700, 300)
    root = box(c, 10, 125, 120, 50, ["Financial", "structure"], "HEAD", weight="700")
    eq = box(c, 170, 50, 150, 50, ["EQUITY", "company resources"], "GREEN", head_first=True, size=12)
    li = box(c, 170, 200, 150, 50, ["LIABILITIES", "external resources"], "BLUE", head_first=True, size=12)
    elbow(c, [(130, 150), (150, 150), (150, 75), (170, 75)], "EDGE", 1.4)
    elbow(c, [(130, 150), (150, 150), (150, 225), (170, 225)], "EDGE", 1.4)
    leaves = [(10, ["Internal equity: self-financing"], (320, 75), "GREEN"),
              (60, ["External equity: equity capital and shares"], (320, 75), "GREEN"),
              (150, ["Long term: bonds, long-term loans", "and bank credits, leasing"], (320, 225), "BLUE"),
              (220, ["Short term: accounts payable, trade discount,", "short-term loans and bank credits, factoring"], (320, 225), "BLUE")]
    for y, s, src, col in leaves:
        h = 40 if len(s) == 1 else 54
        box(c, 370, y, 320, h, s, col, size=12)
        elbow(c, [src, (345, src[1]), (345, y + h / 2), (370, y + h / 2)], "EDGE", 1.2)
    REG.put("financial-map", c, "The financial structure of the company",
            "The financial structure: equity (the company's own resources, internal or external) and liabilities "
            "(external resources, long term or short term), with the instruments of each")


def build():
    for fn in (finance_area, structures, balance, financial_map):
        fn()
    return REG
