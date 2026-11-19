"""Topic 2 figures for Business Management: all copied from the Topic 2_ Value creation.pdf slides as PNG crops."""
from figures.svgkit import Registry

REG = Registry("BM-T2")


def build():
    REG.raster("stakeholders", "Stakeholders of the firm",
               "The stakeholders around management: shareholders, banks and other financial agents, customers, "
               "suppliers, the State, employees and labour unions, and society. Copied from Topic 2 slides, Slide 5", 640)
    REG.raster("unified-vision", "A unified vision: survival, profit and growth",
               "Survival, profit and growth as one cycle: products and markets bring sales and profits; profits are "
               "retained or paid as dividends; both feed total equity, which finances new investments. "
               "Copied from Topic 2 slides, Slide 7", 640)
    REG.raster("decisions", "From objective to decisions",
               "To reach the business objective the firm defines a strategy, which unfolds into strategic, tactic and "
               "operative decisions. Copied from Topic 2 slides, Slide 8", 640)
    REG.raster("types", "Types of strategic decisions",
               "Strategic decisions split into corporate strategy (product, geographical and vertical scope) and "
               "competitive or business strategy (cost leadership or differentiation). Copied from Topic 2 slides, Slide 9", 680)
    REG.raster("success", "What makes a successful strategy",
               "A successful strategy rests on effective implementation of agreed long-term objectives, a deep "
               "understanding of the competitive environment and an objective appraisal of resources. "
               "Copied from Topic 2 slides, Slide 10", 600)
    REG.raster("environment", "The generic environment",
               "The generic environment and its four groups of factors: economic, socio-cultural, political-legal and "
               "technological, each with its components. Copied from Topic 2 slides, Slide 11", 640)
    REG.raster("environment-specific", "The specific environment",
               "The specific environment of the industry: rivalry within the industry (concentration, industry rate of "
               "growth, product differentiation), barriers to entry and to exit, substitutes, and the relationships with "
               "customers and with suppliers. Copied from Topic 2 slides, Slide 12", 640)
    REG.raster("industry", "From environmental analysis to industry analysis",
               "The industry environment (suppliers, competitors, customers) inside the wider environment that "
               "acts on it. Copied from Topic 2 slides, Slide 13", 640)
    REG.raster("five-forces", "Porter's five competitive forces",
               "Porter's five competitive forces (1982) and the determinants of each: supplier power, buyer power, "
               "threat of entry, substitute competition and the rivalry among existing firms. "
               "Copied from Topic 2 slides, Slide 15", 640)
    REG.raster("strategy-questions", "Corporate strategy and business strategy",
               "A rate of profit above the competitive level comes from two sources: being in attractive industries "
               "(corporate strategy) and holding a competitive advantage (business strategy). "
               "Copied from Topic 2 slides, Slide 17", 600)
    REG.raster("scope", "The three dimensions of scope",
               "The scope of a firm along each dimension: one integrated firm linked by an administrative interface, "
               "or several specialized firms linked by market interfaces (figure of Grant, 2002, as shown on the slide). "
               "Copied from Topic 2 slides, Slide 19", 520)
    REG.raster("advantage", "Sources of competitive advantage",
               "The two sources of competitive advantage: cost advantage and differentiation advantage. "
               "Copied from Topic 2 slides, Slide 20", 640)
    REG.raster("value-chain", "Porter's value chain",
               "Porter's value chain (1985): support activities above the primary activities, whose combined "
               "result is the margin. Copied from Topic 2 slides, Slide 29", 640)
    return REG
