"""Topic 6 figures for Business Management: diagrams redrawn from Topic 6_ The Management Function.pdf."""
import textwrap

from figures.bm_common import arrow, box, mid
from figures.svgkit import Canvas, Registry, line, poly, text

REG = Registry("BM-T6")


def functions():
    c = Canvas(600, 120)
    names = ["Planning", "Organizing", "Leading", "Controlling"]
    bs = [box(c, 10 + k * 150, 30, 130, 44, s, ["BLUE", "GREEN", "ACC", "PINK"][k], weight="700", size=13) for k, s in enumerate(names)]
    for a, b in zip(bs, bs[1:]):
        arrow(c, mid(a, "right"), mid(b, "left"), "EDGE", 1.4)
    line(c, mid(bs[-1], "bottom"), (535, 100), "EDGE", 1.2, "4 3")
    line(c, (535, 100), (75, 100), "EDGE", 1.2, "4 3")
    line(c, (75, 100), mid(bs[0], "bottom"), "EDGE", 1.2, "4 3", head=True)
    text(c, (305, 114), "control feeds the next round of planning", "TEXT", "middle", 11)
    REG.put("functions", c, "The four managerial functions",
            "Planning, organizing, leading and controlling (Slides 3-4); planning and controlling are inseparable (Slide 24)")


def decision_process():
    c = Canvas(640, 190)
    steps = ["1. Recognizing the problem or opportunity", "2. Gathering information", "3. Identifying the critical factors",
             "4. Considering alternative courses of action", "5. Evaluating the results", "6. Choosing an alternative",
             "7. Implementing the decision", "8. Implementing changes"]
    for k, s in enumerate(steps):
        r, col = divmod(k, 4)
        col = col if r == 0 else 3 - col  # second row runs right to left
        num, rest = s.split(". ", 1)
        b = box(c, 10 + col * 157, 20 + r * 90, 145, 56, textwrap.wrap(f"{num}. {rest}", 22), "BLUE", size=11)
        if k in (0, 1, 2):
            arrow(c, (b[0] + b[2], b[1] + 28), (b[0] + b[2] + 12, b[1] + 28), "EDGE", 1.2)
        if k in (4, 5, 6):
            arrow(c, (b[0], b[1] + 28), (b[0] - 12, b[1] + 28), "EDGE", 1.2)
    arrow(c, (553, 76), (553, 110), "EDGE", 1.2)
    REG.put("decision-process", c, "The decision-making process",
            "The eight steps of the decision-making process, from recognizing the problem to implementing the changes "
            "(Slide 6)")


def pyramid():
    c = Canvas(560, 250)
    poly(c, [(150, 15), (280, 235), (20, 235)], "ACC", 1.6, fill="ACC", opacity=0.18, close=True)
    for y in (85, 160):
        line(c, (20, y), (300, y), "EDGE", 1, "4 3")
    text(c, (150, 70), "Top management", "HEAD", "middle", 12, "700")
    text(c, (150, 130), "Middle management", "HEAD", "middle", 12, "700")
    text(c, (150, 200), "Low management", "HEAD", "middle", 12, "700")
    text(c, (150, 216), "(first-line supervisors)", "TEXT", "middle", 11)
    box(c, 330, 40, 100, 40, "Strategic", "BLUE", weight="700", size=12)
    box(c, 440, 40, 100, 40, "General", "GREEN", weight="700", size=12)
    box(c, 330, 150, 100, 40, "Tactical", "BLUE", weight="700", size=12)
    box(c, 440, 150, 100, 40, "Functional", "GREEN", weight="700", size=12)
    text(c, (435, 20), "Scope of activities", "HEAD", "middle", 12, "700")
    REG.put("pyramid", c, "The management pyramid",
            "Top, middle and low management; by the scope of their activities, top management is strategic and general, "
            "middle and low management tactical and functional (Slide 7)")


def skills():
    c = Canvas(560, 260)
    x0, y0, w, h = 70, 220, 440, 190
    X = lambda u: x0 + u * w  # noqa: E731
    Y = lambda p: y0 - p / 100 * h  # noqa: E731
    tech = [(0, 55), (0.5, 30), (1, 12)]
    inter = [(0, 85), (0.5, 75), (1, 55)]
    poly(c, [(X(0), Y(0))] + [(X(u), Y(p)) for u, p in tech] + [(X(1), Y(0))], "ACC", 1.4, fill="ACC", opacity=0.3, close=True)
    poly(c, [(X(u), Y(p)) for u, p in tech] + [(X(u), Y(p)) for u, p in reversed(inter)], "GREEN", 1.4, fill="GREEN", opacity=0.25, close=True)
    poly(c, [(X(u), Y(p)) for u, p in inter] + [(X(1), Y(100)), (X(0), Y(100))], "BLUE", 1.4, fill="BLUE", opacity=0.2, close=True)
    line(c, (x0, y0), (x0, y0 - h - 10), "EDGE", 1.4, head=True)
    line(c, (x0, y0), (x0 + w + 10, y0), "EDGE", 1.4, head=True)
    for p in (0, 50, 100):
        text(c, (x0 - 8, Y(p) + 4), str(p), "TEXT", "end", 11)
    text(c, (x0 + 8, Y(100) - 12), "Use of skills (%)", "HEAD", "start", 11)
    for u, lab in [(0, "Low"), (0.5, "Middle"), (1, "Top")]:
        text(c, (X(u), y0 + 18), lab, "HEAD", "middle", 12, "700")
    text(c, (X(0.65), Y(90)), "Conceptual: see the firm as a whole", "BLUE", "middle", 12, "700")
    text(c, (X(0.45), Y(55)), "Interpersonal: work with people", "GREEN", "middle", 12, "700")
    text(c, (X(0.22), Y(15)), "Technical", "ACC", "middle", 12, "700")
    REG.put("skills", c, "Basic managerial skills along the hierarchy",
            "Share of technical, interpersonal and conceptual skills from low to top management: technical skills weigh "
            "most at the bottom, conceptual skills at the top (Slide 8; shares only qualitative)")


def parts():
    c = Canvas(600, 260)
    apex = box(c, 230, 10, 140, 40, ["Strategic apex", "top management"], "BLUE", size=11, head_first=True)
    mid_ = box(c, 230, 95, 140, 40, ["Middle line", "middle management"], "BLUE", size=11, head_first=True)
    core = box(c, 170, 190, 260, 50, ["Operating core", "employees"], "GREEN", size=11, head_first=True)
    tech = box(c, 20, 95, 170, 54, ["Technostructure", "analysts who design", "systems and processes"], "ACC", size=11, head_first=True)
    supp = box(c, 410, 95, 170, 54, ["Support staff", "outside the operating", "workflow"], "PINK", size=11, head_first=True)
    arrow(c, mid(apex, "bottom"), mid(mid_, "top"), "EDGE", 1.3)
    arrow(c, mid(mid_, "bottom"), mid(core, "top"), "EDGE", 1.3)
    for b in (tech, supp):
        line(c, mid(b, "right" if b is tech else "left"), mid(mid_, "left" if b is tech else "right"), "EDGE", 1.1, "4 3")
    REG.put("parts", c, "Common parts of a formal organizational structure",
            "Strategic apex, middle line and operating core in the line of authority, flanked by the technostructure and "
            "the support staff (Slide 14)")


def build():
    for fn in (functions, decision_process, pyramid, skills, parts):
        fn()
    return REG
