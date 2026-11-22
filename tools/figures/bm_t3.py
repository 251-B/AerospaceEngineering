"""Topic 3 figures for Business Management: crops of Topic 3_Financial Management (I).pdf; the balance sheet layout is a drawing of ours."""
from figures.bm_common import box
from figures.svgkit import Canvas, Registry, text

REG = Registry("BM-T3")


def finance_area():
    REG.raster("finance-area", "The finance area and its two decisions",
               "The slide defines the finance area and shows the finance manager's two questions, what to invest in and "
               "when, and how to obtain the money to invest, which lead to the investing and financing decisions. "
               "Copied from Topic 3 slides, Slide 3", 600)


def structures():
    REG.raster("structures", "Economic and financial structure",
               "The slide sets assets (profitability) against equity plus liabilities (cost): the objective is to "
               "maximize value, which requires profitability above cost. Copied from Topic 3 slides, Slide 5", 520)


def balance():
    # EXTRA: two-column layout summarising slides 14-18; no slide draws it
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
    REG.raster("financial-map", "The financial structure of the company",
               "The slide splits the financial structure into equity (internal and external) and liabilities (long "
               "term and short term), with the instruments of each. Copied from Topic 3 slides, Slide 21", 640)


def build():
    for fn in (finance_area, structures, balance, financial_map):
        fn()
    return REG
