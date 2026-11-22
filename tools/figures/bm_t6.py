"""Topic 6 figures for Business Management: all copied from Topic 6_ The Management Function.pdf as PNG crops."""
from figures.svgkit import Registry

REG = Registry("BM-T6")


def build():
    REG.raster("functions", "The four managerial functions",
               "The four managerial functions, planning, organizing, leading and controlling, as the slide shows them. "
               "Copied from Topic 6 slides, Slide 4", 520)
    REG.raster("decision-process", "The decision-making process",
               "The eight numbered steps of the decision-making process, from recognizing the problem or opportunity to "
               "implementing changes, arranged as a cycle. Copied from Topic 6 slides, Slide 6", 680)
    REG.raster("pyramid", "The management pyramid",
               "The management pyramid with top, middle and low management and the scope of activities of each level; "
               "the slide spells the top level \"Strategical\". Copied from Topic 6 slides, Slide 7", 640)
    REG.raster("skills", "Basic managerial skills along the hierarchy",
               "How much technical, interpersonal and conceptual skills are used from low to top management, as the "
               "slide draws it. Copied from Topic 6 slides, Slide 8", 560)
    REG.raster("parts", "Common parts of a formal organizational structure",
               "The five common parts of a formal structure: strategic apex, middle line, operating core, "
               "technostructure and support staff. Copied from Topic 6 slides, Slide 14", 640)
    return REG
