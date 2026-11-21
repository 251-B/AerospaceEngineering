---
materia: Business Management
tema: "Unit 4: choice between two production processes, operating leverage and price elasticity"
bank_id: M09
title: "Tessera Brackets: a robotic or a manual cell, economic risk and a price rise"
category: mt2_problem
archetype: bep-ol-elasticity
level: trap
unit: 4
difficulty: 3
points: 2.5
time_minutes: 24
official: false
origen: "Problem written for the bank in the style of Exercise 1 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf and of Exercise 3 of BEP  OL Statements  Solutions.pdf; not an official exercise. Method: Topic 4, Slides 17, 37-42; Topic 5, Slide 17 and topic 5.2.2.pdf, pp. 2-3."
tags:
  - problem-bank
  - midterm-2
  - bep-ol-elasticity
  - break-even
  - operating-leverage
  - production-process
  - price-elasticity
---

# Bank M09 — Tessera Brackets: a robotic or a manual cell

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Exercise 1 of the examples PDF (Pegasus S.A.) and of Exercise 3 of the break-even sheet (BEP  OL Statements  Solutions.pdf, pp. 4-5), where a firm chooses between two production processes. Differences from Pegasus: two cost structures are compared, the economic risk of each is judged with the operating leverage, the leverage is used to forecast a fall in sales, and a price rise with elastic demand moves the volume across the crossing point of the two profit lines. Method: Topic 4, Slides 17 and 37 to 42; price elasticity from Topic 5, Slide 17 and topic 5.2.2.pdf, pp. 2-3.

## Statement

Tessera Aero S.A. will machine a new titanium bracket for aircraft seats, sold at 100 € per unit. It must choose one of two production processes for the whole volume:

| | Robotic cell (R) | Manual cell (M) |
| :--- | ---: | ---: |
| Annual fixed costs | 960,000 € | 360,000 € |
| Variable cost per bracket | 40 € | 70 € |

The robotic cell needs a large investment in machines and programming but little labour per unit; the manual cell uses general-purpose machines and operators paid per bracket. The sales forecast is 24,000 brackets a year.

a) Calculate the break-even point of each process and the volume at which both processes give the same operating profit. Which process gives more profit below and above that volume? (0.5 points)

b) Calculate the operating profit and the operating leverage (OL) of each process at the forecast of 24,000 brackets. Which process carries more economic risk, and why? (0.75 points)

c) Suppose the sales turn out 25% below the forecast. Use the OL of part (b) to predict the profit of each process, check the predictions directly, and say which process would then have been the better choice. (0.5 points)

d) Back at the forecast of 24,000 brackets, the price elasticity of demand is 2.5. Marketing proposes a 10% price rise. Calculate the new volume, the new operating profit of each process and the change in sales revenue. With the price rise, which process gives more profit? Is the price rise advisable? (0.75 points)

## Setup

| Item | Robotic cell (R) | Manual cell (M) |
| :--- | ---: | ---: |
| Price $P$ (€/bracket) | 100 | 100 |
| Fixed costs $FC$ (€/year) | 960,000 | 360,000 |
| Variable cost $VC$ (€/bracket) | 40 | 70 |
| Unit margin $m = P - VC$ (€/bracket) | 60 | 30 |

Forecast volume $Q = 24{,}000$ brackets a year; price elasticity at the forecast $E_d = 2.5$ (absolute value); price change in part (d) +10%.

Model of the course:

- Profit $= Q\,(P - VC) - FC = Q\,m - FC$, break-even point $Q_0 = FC/m$ (Topic 4, Slide 37); two cost structures with different fixed costs give profit lines of different slopes (Topic 4, Slide 38), and a rigid system starts with a higher total cost but grows more slowly (Topic 4, Slide 17).
- Operating leverage $OL = (\Delta\text{Profit}/\text{Profit})/(\Delta Q/Q) = Q\,m/(Q\,m - FC) = Q/(Q - Q^*)$, an index of economic risk that, ceteris paribus, grows with the fixed costs (Topic 4, Slides 39 to 42).
- The volume at which both processes give the same profit is the crossing point of the two profit lines, found by equating them, as in BEP  OL Statements  Solutions.pdf, Exercise 3.
- Price elasticity $E_d = (\Delta Q/Q)/(\Delta P/P)$ in absolute value, so $\Delta Q/Q = -E_d\,\Delta P/P$ (Topic 5, Slide 17; topic 5.2.2.pdf, p. 2), as in Examples PDF, Exercise 1 (d).

## (a) Break-even points and the crossing volume [0.5 pts]

### Hint

Each process has its own unit margin. For the crossing volume write the two profits as functions of $Q$ and set them equal; the price appears on both sides.

### Checkpoint

- $Q^*_R$ = 16,000 brackets, $Q^*_M$ = 12,000 brackets
- Crossing volume = 600,000/30 = 20,000 brackets, profit 240,000 € in both
- Below 20,000 the manual cell gives more profit; above it, the robotic cell

### Solution

#### Break-even point of each process

$$Q^*_R = \frac{FC_R}{m_R} = \frac{960{,}000}{100 - 40} = \frac{960{,}000}{60} = 16{,}000\ \text{brackets}$$

$$Q^*_M = \frac{FC_M}{m_M} = \frac{360{,}000}{100 - 70} = \frac{360{,}000}{30} = 12{,}000\ \text{brackets}$$

#### Crossing volume

The two profits are equal when

$$Q\,(100 - 40) - 960{,}000 = Q\,(100 - 70) - 360{,}000$$

The term $100\,Q$ appears on both sides and cancels, so the price does not affect the crossing volume:

$$-40\,Q - 960{,}000 = -70\,Q - 360{,}000 \quad\Longrightarrow\quad (70 - 40)\,Q = 960{,}000 - 360{,}000$$

$$Q = \frac{FC_R - FC_M}{VC_M - VC_R} = \frac{600{,}000}{30} = 20{,}000\ \text{brackets}$$

At that volume: $\text{Profit}_R = 20{,}000 \times 60 - 960{,}000 = 240{,}000$ € and $\text{Profit}_M = 20{,}000 \times 30 - 360{,}000 = 240{,}000$ €.

#### Which process where

The profit line of R is steeper (60 € per extra bracket against 30 €) but starts lower ($-960{,}000$ € against $-360{,}000$ € at $Q = 0$), as in the two cost structures of Topic 4, Slide 38. Below 20,000 brackets the manual cell gives more profit; above 20,000 the robotic cell does. The forecast of 24,000 lies above the crossing volume.

## (b) Profit, leverage and economic risk at 24,000 brackets [0.75 pts]

### Hint

Compute $Q\,m$ and the profit of each process, then $OL = Q\,m/\text{Profit}$. Check with $Q/(Q - Q^*)$. Compare how far 24,000 is from each break-even point and which process has the larger share of fixed costs.

### Checkpoint

- R: $Q\,m$ = 1,440,000 €, profit 480,000 €, OL = 3.00
- M: $Q\,m$ = 720,000 €, profit 360,000 €, OL = 2.00
- R has more economic risk: higher fixed costs, a break-even point closer to the forecast in relative terms, higher OL

### Solution

#### Robotic cell

$$\text{Profit}_R = 24{,}000 \times 60 - 960{,}000 = 1{,}440{,}000 - 960{,}000 = 480{,}000\ \text{€}$$

$$OL_R = \frac{Q\,m_R}{Q\,m_R - FC_R} = \frac{1{,}440{,}000}{480{,}000} = 3.00$$

Check (Topic 4, Slide 42): $OL_R = 24{,}000/(24{,}000 - 16{,}000) = 24{,}000/8{,}000 = 3.00$.

#### Manual cell

$$\text{Profit}_M = 24{,}000 \times 30 - 360{,}000 = 720{,}000 - 360{,}000 = 360{,}000\ \text{€}$$

$$OL_M = \frac{720{,}000}{360{,}000} = 2.00$$

Check: $OL_M = 24{,}000/(24{,}000 - 12{,}000) = 24{,}000/12{,}000 = 2.00$.

#### Which process is riskier, and why

At the forecast the robotic cell gives 120,000 € more profit, but it carries more economic risk: a 1% change in sales changes its profit by 3%, against 2% for the manual cell (Topic 4, Slide 40). The reason is its cost structure. The robotic cell has more fixed costs (960,000 € against 360,000 €), and, ceteris paribus, the higher the fixed costs, the higher the OL (Topic 4, Slide 41). In terms of the break-even point, 24,000 brackets is only 1.5 times $Q^*_R$ but 2 times $Q^*_M$, so R is relatively closer to its break-even point, and the closer to it, the larger the leverage (Topic 4, Slide 42). The robotic cell is the rigid system of Topic 4, Slide 17: a high total cost to start with that grows slowly with the volume. Choosing it means a higher profit if the forecast holds and a larger exposure if it does not.

## (c) Sales 25% below the forecast [0.5 pts]

### Hint

The OL gives the relative change of the profit: $\Delta\text{Profit}/\text{Profit} = OL \times \Delta Q/Q$. Then compute both profits at the new volume and compare the volume with the crossing point of part (a).

### Checkpoint

- New volume 18,000 brackets
- R: profit falls 75%, to 120,000 €; M: profit falls 50%, to 180,000 €
- At 18,000 (below 20,000) the manual cell would have been better

### Solution

#### Prediction with the leverage

$\Delta Q/Q = -0.25$, so the volume is $24{,}000 \times (1 - 0.25) = 18{,}000$ brackets. By the definition of the OL (Topic 4, Slide 39):

$$\frac{\Delta\text{Profit}_R}{\text{Profit}_R} = 3.00 \times (-0.25) = -0.75 \quad\Longrightarrow\quad \text{Profit}_R = 480{,}000 \times (1 - 0.75) = 120{,}000\ \text{€}$$

$$\frac{\Delta\text{Profit}_M}{\text{Profit}_M} = 2.00 \times (-0.25) = -0.50 \quad\Longrightarrow\quad \text{Profit}_M = 360{,}000 \times (1 - 0.50) = 180{,}000\ \text{€}$$

#### Direct check

$$\text{Profit}_R = 18{,}000 \times 60 - 960{,}000 = 1{,}080{,}000 - 960{,}000 = 120{,}000\ \text{€}$$

$$\text{Profit}_M = 18{,}000 \times 30 - 360{,}000 = 540{,}000 - 360{,}000 = 180{,}000\ \text{€}$$

The predictions are exact because the profit is linear in the volume and the OL was measured at the starting volume of 24,000.

#### Which process would have been better

At 18,000 brackets, below the crossing volume of 20,000, the manual cell gives 60,000 € more profit than the robotic cell. The higher leverage of R, which multiplied its gains above the forecast, has multiplied its losses of profit here: this is the economic risk measured in part (b).

## (d) A 10% price rise with an elasticity of 2.5 [0.75 pts]

### Hint

Apply $\Delta Q/Q = -E_d\,\Delta P/P$ at 24,000 brackets. The price rise adds the same 10 € to the margin of both processes. Remember from part (a) that the crossing volume does not depend on the price.

### Checkpoint

- New volume 18,000 brackets, new price 110 €
- R: margin 70 €, profit 300,000 €; M: margin 40 €, profit 360,000 €
- Revenue falls from 2,400,000 € to 1,980,000 € (−420,000 €)
- With the rise M is better; the best plan overall is R without the rise (480,000 €)

### Solution

#### New volume

$\Delta P/P = +0.10$ and $E_d = 2.5$ in absolute value (Topic 5, Slide 17; topic 5.2.2.pdf, p. 2):

$$\frac{\Delta Q}{Q} = -E_d\,\frac{\Delta P}{P} = -2.5 \times 0.10 = -0.25 \qquad Q_{new} = 24{,}000 \times (1 - 0.25) = 18{,}000\ \text{brackets}$$

#### New margins and profits

$P_{new} = 100 \times 1.10 = 110$ €, so $m_R = 110 - 40 = 70$ € and $m_M = 110 - 70 = 40$ € per bracket.

$$\text{Profit}_R = 18{,}000 \times 70 - 960{,}000 = 1{,}260{,}000 - 960{,}000 = 300{,}000\ \text{€}$$

$$\text{Profit}_M = 18{,}000 \times 40 - 360{,}000 = 720{,}000 - 360{,}000 = 360{,}000\ \text{€}$$

#### Change in revenue

Revenue before: $24{,}000 \times 100 = 2{,}400{,}000$ €. Revenue after: $18{,}000 \times 110 = 1{,}980{,}000$ €, a fall of 420,000 €. The demand is elastic ($E_d > 1$), so a price rise lowers the revenue (topic 5.2.2.pdf, p. 3). The revenue does not depend on the process chosen.

#### Which process, and is the rise advisable

The crossing volume is still $600{,}000/30 = 20{,}000$ brackets, because the price cancels when the two profits are equated (part (a)). The price rise moves the volume to 18,000, below the crossing point, so with the rise the manual cell gives more profit (360,000 € against 300,000 €). The decision on the process depends on the expected volume, and a price change with elastic demand can move it across the crossing point.

The rise is not advisable for either process in its best form. With the robotic cell the profit falls from 480,000 € to 300,000 €; with the manual cell it stays at 360,000 € (its extra margin of 10 € on 18,000 brackets, 180,000 €, exactly makes up for the margin of 30 € lost on 6,000 brackets, 180,000 €). The highest profit of all four combinations is the robotic cell at the present price, 480,000 €. The trap is to read "with the price rise the manual cell is better" as "the manual cell is better": it is better only inside a plan that is itself worse than keeping the price.

## Interpretation

The robotic cell is the fixed-heavy, rigid process: it breaks even later (16,000 against 12,000 brackets) but earns twice the margin per bracket, so it wins above 20,000 brackets and loses below. At the forecast it gives more profit with more economic risk (OL 3.00 against 2.00), and part (c) shows that risk at work: a 25% fall in sales cuts its profit by 75% and makes the manual cell the better choice. A price rise with elastic demand ($E_d = 2.5$) lowers the volume by 25% and the revenue by 420,000 €; it never helps the robotic cell, whose high margin makes every lost bracket costly. Limiting cases: if both processes had the same fixed costs, the one with the lower variable cost would win at every volume and there would be no crossing point; at $Q = Q^*$ the OL is not defined. Dimensions: prices, variable costs and margins in € per bracket, volumes in brackets a year, profits and revenues in € a year, OL and elasticity dimensionless.

## Verification

- (a) unit margin R (€) | 100-40 | 60
- (a) unit margin M (€) | 100-70 | 30
- (a) break-even point R (brackets) | 960000/60 | 16000
- (a) break-even point M (brackets) | 360000/30 | 12000
- (a) crossing volume (brackets) | (960000-360000)/(70-40) | 20000
- (a) profit R at the crossing (€) | 20000*60-960000 | 240000
- (a) profit M at the crossing (€) | 20000*30-360000 | 240000
- (b) contribution R at 24,000 (€) | 24000*60 | 1440000
- (b) profit R at 24,000 (€) | 24000*60-960000 | 480000
- (b) OL R at 24,000 | 24000*60/(24000*60-960000) | 3.00
- (b) contribution M at 24,000 (€) | 24000*30 | 720000
- (b) profit M at 24,000 (€) | 24000*30-360000 | 360000
- (b) OL M at 24,000 | 24000*30/(24000*30-360000) | 2.00
- (b) profit difference R minus M (€) | (24000*60-960000)-(24000*30-360000) | 120000
- (b) forecast over break-even R | 24000/16000 | 1.5
- (b) forecast over break-even M | 24000/12000 | 2
- (c) new volume (brackets) | 24000*(1-0.25) | 18000
- (c) predicted profit R (€) | 480000*(1-3.00*0.25) | 120000
- (c) predicted profit M (€) | 360000*(1-2.00*0.25) | 180000
- (c) direct profit R (€) | 18000*60-960000 | 120000
- (c) direct profit M (€) | 18000*30-360000 | 180000
- (c) advantage of M at 18,000 (€) | (18000*30-360000)-(18000*60-960000) | 60000
- (d) new volume (brackets) | 24000*(1-2.5*0.10) | 18000
- (d) new price (€) | 100*1.10 | 110
- (d) new margin R (€) | 110-40 | 70
- (d) new margin M (€) | 110-70 | 40
- (d) new profit R (€) | 18000*(110-40)-960000 | 300000
- (d) new profit M (€) | 18000*(110-70)-360000 | 360000
- (d) revenue before (€) | 24000*100 | 2400000
- (d) revenue after (€) | 18000*110 | 1980000
- (d) change in revenue (€) | 18000*110-24000*100 | -420000
- (d) crossing volume after the rise (brackets) | (960000-360000)/((110-40)-(110-70)) | 20000
- (d) margin gained by M on 18,000 (€) | 10*18000 | 180000
- (d) margin lost by M on 6,000 (€) | 30*6000 | 180000

**Back to:** [[Problem Set - Business Management Problem Bank]]
