"""Topic 7 figures for Business Management: all copied from Topic 7_Entrepreneurship  Innovation.pdf as PNG crops."""
from figures.svgkit import Registry

REG = Registry("BM-T7")


def build():
    REG.raster("network", "Sources of innovation as a system",
               "Firms, universities, government-funded research, private nonprofits and individuals as the players of the "
               "innovation system, with the linkages between them. Copied from Topic 7 slides, Slide 4", 400)
    REG.raster("s-curve", "The S-curve of technology performance",
               "Performance against effort: slow growth at first, then rapid growth, then flattening towards the limit of "
               "the technology. Copied from Topic 7 slides, Slide 14", 600)
    REG.raster("discontinuous", "A discontinuous technology",
               "The S-curves of a first and a second technology in two cases: (a) the second overtakes the first soon, "
               "(b) it starts below the first and overtakes it later. The source image of the slide is cut at its top "
               "edge. Copied from Topic 7 slides, Slide 15", 420)
    REG.raster("adoption", "Adopter categories of a diffusing technology",
               "Innovators, early adopters, early majority, late majority and laggards on the bell-shaped curve of new "
               "adopters, with the share of each category (panel b of the slide). Copied from Topic 7 slides, Slide 16", 600)
    return REG
