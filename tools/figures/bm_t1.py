"""Topic 1 figures for Business Management: all copied from the Topic 1_The Firm_Types  Objectives.pdf slides as PNG crops."""
from figures.svgkit import Registry

REG = Registry("BM-T1")


def build():
    REG.raster("bread", "Production process of bread",
               "Production process of bread: five ingredients (inputs) pass through a question mark, the business "
               "activity that transforms them, to give the output, bread. Copied from Topic 1 slides, Slide 4", 560)
    REG.raster("circular-flow", "Circular flow of income",
               "Circular flow of income: households and firms exchange goods and services and factors of production "
               "through two markets, with money flowing the opposite way (expenditures, revenues, incomes). "
               "Copied from Topic 1 slides, Slide 5", 640)
    REG.raster("market-enterprise", "Nature of business: market and enterprise",
               "How needs are satisfied: scarce resources against unlimited wants lead to specialization and "
               "coordination, which is provided by the market or by the enterprise. Copied from Topic 1 slides, Slide 12", 640)
    REG.raster("functions", "Business functional areas",
               "Business functional areas: the real functions, the financial functions that run alongside them and "
               "the management functions of planning, organization and control. Copied from Topic 1 slides, Slide 13", 640)
    REG.raster("fayol", "The management process",
               "The management process as a cycle of planning, organizing, leading and controlling, aimed at achieving "
               "the organization's stated purpose. Copied from Topic 1 slides, Slide 14", 440)
    REG.raster("rights", "The entrepreneur as holder of rights",
               "Why someone supervises team production: the controller is given four rights, and whoever holds them "
               "all is the entrepreneur. Copied from Topic 1 slides, Slide 18", 600)
    REG.raster("forms", "Forms of business ownership",
               "Forms of business ownership: sole proprietorship, partnership, corporation and other forms such as "
               "cooperatives, joint ventures and mutual companies. Copied from Topic 1 slides, Slide 20", 560)
    REG.raster("agency", "Separation of ownership and control",
               "Separation of ownership and control: managers who look for their own benefit create a conflict of "
               "interest between ownership and control, the agency problem. Copied from Topic 1 slides, Slide 25", 360)
    REG.raster("agency-mechanisms", "Mechanisms of control of the agency problem",
               "The solution to the agency problem: the mechanisms shareholders use to control managers. "
               "Copied from Topic 1 slides, Slide 26", 640)
    return REG
