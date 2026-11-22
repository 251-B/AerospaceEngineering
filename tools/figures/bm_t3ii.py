"""Topic 3 (II) figures for Business Management: four crops of Topic 3_Financial Management (II).pdf."""
from figures.svgkit import Registry

REG = Registry("BM-T3II")


def build():
    REG.raster("roa", "Return on assets (ROA)",
               "ROA = EBIT / TA measures the return from the assets' point of view and splits into the sales margin "
               "EBIT / S and the asset turnover S / TA. Copied from Topic 3 (II) slides, Slide 7", 600)
    REG.raster("roe", "Return on equity (ROE)",
               "ROE = NP / E measures the return from the owners' point of view; it depends on ROA, on the level of "
               "debt D/E and on the financial leverage ROA − Ki. Copied from Topic 3 (II) slides, Slide 8", 520)
    REG.raster("npv-irr", "NPV against the interest rate",
               "The NPV of a project falls as the interest rate i grows and crosses zero at the IRR: if IRR > i then "
               "NPV > 0, if IRR < i then NPV < 0. Copied from Topic 3 (II) slides, Slide 32", 560)
    REG.raster("npv-projects", "Comparing two projects: the Fisher rate",
               "The NPV lines of two projects A and B cross at the Fisher rate RF, where NPV_A = NPV_B; on each side "
               "of it a different project has the higher NPV. Copied from Topic 3 (II) slides, Slide 33", 620)
    return REG
