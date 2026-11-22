---
materia: Business Management
tema: "Unit 4: cost structure, break-even point, operating leverage and price elasticity"
bank_id: M08
title: "Orbis Sensors: cost structure from two months, break-even, leverage and a price cut"
category: mt2_problem
archetype: bep-ol-elasticity
level: standard
unit: 4
difficulty: 2
points: 2.5
time_minutes: 22
official: false
origen: "Problem written for the bank in the style of Exercise 1 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf and of Exercise 5 of BEP  OL Statements  Solutions.pdf; not an official exercise. Method: Topic 4, Slides 37-43; Topic 5, Slide 17 and topic 5.2.2.pdf, pp. 2-3."
tags:
  - problem-bank
  - midterm-2
  - bep-ol-elasticity
  - break-even
  - operating-leverage
  - margin-of-safety
  - price-elasticity
---

# Bank M08 — Orbis Sensors: cost structure from two months

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Exercise 1 of the examples PDF (Pegasus S.A.), with the cost structure hidden as in Exercise 5 of the break-even sheet (BEP  OL Statements  Solutions.pdf, p. 6): the price, the variable cost and the fixed costs must be deduced from the accounts of two months. The leverage is checked against the observed change between the two months, and the price cut asks for the elasticity at which it stops reducing profit. Method: Topic 4, Slides 37 to 43; price elasticity from Topic 5, Slide 17 and topic 5.2.2.pdf, pp. 2-3.

## Statement

Orbis Sensors S.L. assembles air-data probes for light aircraft. It sells a single model at the same price to every customer, and its cost structure has not changed during the year. The controller has only the monthly summaries of two months:

| Month | Probes sold | Sales revenue | Total operating costs |
| :--- | ---: | ---: | ---: |
| March | 1,500 | 375,000 € | 330,000 € |
| April | 1,800 | 450,000 € | 360,000 € |

For the coming months the firm forecasts sales of 2,000 probes a month.

a) Deduce the selling price, the variable cost per probe and the monthly fixed costs. (0.5 points)

b) Calculate the monthly break-even point, the operating profit at the forecast of 2,000 probes and the margin of safety at that volume in units, in euros and as a percentage. (0.5 points)

c) Calculate the operating leverage (OL) at 1,500 and at 2,000 probes. Use the OL of March to explain the change in profit from March to April, and say what the two values mean for the firm's economic risk. (0.75 points)

d) At 2,000 probes the price elasticity of demand is 1.6. The firm studies a 10% price cut. Calculate the new volume, the new operating profit and the change in sales revenue. Then find the elasticity above which the same cut would raise the operating profit. (0.75 points)

## Setup

| Item | Value |
| :--- | :--- |
| Observation 1 (March) | $Q_1 = 1{,}500$ probes, revenue 375,000 €, total cost 330,000 € |
| Observation 2 (April) | $Q_2 = 1{,}800$ probes, revenue 450,000 €, total cost 360,000 € |
| Forecast volume | $Q = 2{,}000$ probes a month |
| Price elasticity at 2,000 probes | $E_d = 1.6$ (absolute value) |
| Change of the price in part (d) | −10% |

Model of the course:

- Revenue $R = P\,Q$, total cost $TC = FC + VC\,Q$, profit $= Q\,(P - VC) - FC$, unit margin $m = P - VC$, break-even point $Q_0 = FC/m$ (Topic 4, Slide 37).
- Operating leverage $OL = (\Delta\text{Profit}/\text{Profit})/(\Delta Q/Q) = Q\,m/(Q\,m - FC) = Q/(Q - Q^*)$ (Topic 4, Slides 39, 40 and 42).
- Margin of safety $Q - Q^*$ in units, $(Q - Q^*)\,m$ in monetary units and $(Q - Q^*)/Q^*$ in percentage (Topic 4, Slide 43).
- Price elasticity $E_d = (\Delta Q/Q)/(\Delta P/P)$ in absolute value, so $\Delta Q/Q = -E_d\,\Delta P/P$ (Topic 5, Slide 17; topic 5.2.2.pdf, p. 2), as in Examples PDF, Exercise 1 (d).

## (a) Deduce the price, the variable cost and the fixed costs [0.5 pts]

### Hint

The price comes from revenue divided by volume. Between the two months the fixed costs do not change, so the difference in total cost is due only to the extra probes. Subtract the two total-cost equations.

### Checkpoint

- Price $P$ = 250 € per probe in both months
- Variable cost $VC$ = 30,000/300 = 100 € per probe
- Fixed costs $FC$ = 180,000 € a month; unit margin $m$ = 150 €

### Solution

#### Selling price

With one price for every customer, revenue is $R = P\,Q$, so

$$P = \frac{R_1}{Q_1} = \frac{375{,}000}{1{,}500} = 250\ \text{€/probe} \qquad \frac{R_2}{Q_2} = \frac{450{,}000}{1{,}800} = 250\ \text{€/probe}$$

Both months give the same price, which confirms that the price did not change.

#### Variable cost per probe

Write the total cost of each month as $TC = FC + VC\,Q$ (Topic 4, Slide 37):

$$TC_2 - TC_1 = (FC + VC\,Q_2) - (FC + VC\,Q_1) = VC\,(Q_2 - Q_1)$$

The fixed costs cancel. Solving for $VC$:

$$VC = \frac{TC_2 - TC_1}{Q_2 - Q_1} = \frac{360{,}000 - 330{,}000}{1{,}800 - 1{,}500} = \frac{30{,}000}{300} = 100\ \text{€/probe}$$

#### Fixed costs

Substitute $VC$ into the March equation:

$$FC = TC_1 - VC\,Q_1 = 330{,}000 - 100 \times 1{,}500 = 330{,}000 - 150{,}000 = 180{,}000\ \text{€/month}$$

Check with April: $FC + VC\,Q_2 = 180{,}000 + 100 \times 1{,}800 = 360{,}000$ €, the observed total cost. The unit margin is $m = P - VC = 250 - 100 = 150$ € per probe. Units: € divided by probes gives € per probe.

## (b) Break-even point, forecast profit and margin of safety [0.5 pts]

### Hint

$Q_0 = FC/m$. The margin of safety measures how far the forecast is above the break-even point; the percentage form of the course divides by the break-even volume, not by the forecast.

### Checkpoint

- $Q^*$ = 1,200 probes a month
- Profit at 2,000 probes = 120,000 €
- Margin of safety 800 probes, 120,000 €, 66.67% of $Q^*$

### Solution

#### Break-even point

$$Q^* = \frac{FC}{m} = \frac{180{,}000}{150} = 1{,}200\ \text{probes/month}$$

#### Operating profit at the forecast

$$\text{Profit} = Q\,m - FC = 2{,}000 \times 150 - 180{,}000 = 300{,}000 - 180{,}000 = 120{,}000\ \text{€/month}$$

#### Margin of safety

With the three forms of Topic 4, Slide 43:

$$MS = Q - Q^* = 2{,}000 - 1{,}200 = 800\ \text{probes}$$

$$MS = (Q - Q^*)\,m = 800 \times 150 = 120{,}000\ \text{€}$$

$$MS = \frac{Q - Q^*}{Q^*} = \frac{800}{1{,}200} = 0.6667 = 66.67\%$$

Above the break-even point the margin of safety in euros equals the operating profit, because $(Q - Q^*)\,m = Q\,m - Q^*\,m = Q\,m - FC$. Sales could fall by 800 probes a month before Orbis makes a loss.

## (c) Operating leverage at 1,500 and 2,000 probes [0.75 pts]

### Hint

Compute the March and April profits from the table. From March to April the sales rose by a known percentage; multiply it by the OL of March and compare with the observed change in profit.

### Checkpoint

- OL at 1,500 probes = 225,000/45,000 = 5.00
- OL at 2,000 probes = 300,000/120,000 = 2.50
- March to April: sales +20%, profit +100% (45,000 € to 90,000 €), equal to 5.00 × 20%

### Solution

#### Leverage at 1,500 probes

The March profit is $375{,}000 - 330{,}000 = 45{,}000$ €, which is also $1{,}500 \times 150 - 180{,}000$.

$$OL_{1500} = \frac{Q\,m}{Q\,m - FC} = \frac{1{,}500 \times 150}{1{,}500 \times 150 - 180{,}000} = \frac{225{,}000}{45{,}000} = 5.00$$

Check with the break-even point (Topic 4, Slide 42): $OL = 1{,}500/(1{,}500 - 1{,}200) = 1{,}500/300 = 5.00$.

#### Leverage at 2,000 probes

$$OL_{2000} = \frac{2{,}000 \times 150}{2{,}000 \times 150 - 180{,}000} = \frac{300{,}000}{120{,}000} = 2.50$$

Check: $OL = 2{,}000/(2{,}000 - 1{,}200) = 2{,}000/800 = 2.50$.

#### The change from March to April

The OL is the relative change of the profit divided by the relative change of the volume (Topic 4, Slide 39). From March to April:

$$\frac{\Delta Q}{Q} = \frac{1{,}800 - 1{,}500}{1{,}500} = \frac{300}{1{,}500} = 0.20 \qquad \frac{\Delta\text{Profit}}{\text{Profit}} = \frac{90{,}000 - 45{,}000}{45{,}000} = 1.00$$

where the April profit is $450{,}000 - 360{,}000 = 90{,}000$ €. The ratio is $1.00/0.20 = 5.00$, the OL measured at the March volume: a 20% rise in sales doubled the profit. The OL is exact here because the profit is linear in $Q$ and the leverage is evaluated at the starting volume.

#### Meaning

At 1,500 probes, a 1% change in sales changes the operating profit by 5%; at 2,000 probes, by 2.5% (Topic 4, Slide 40). Both are above 1 because the firm is above its break-even point, and the leverage falls as the volume moves away from it (Topic 4, Slide 42). The OL is an index of economic risk (Topic 4, Slide 41): Orbis was riskier in March, only 300 probes above $Q^*$, than it will be at the forecast of 2,000 probes. The leverage is a pure number.

## (d) A 10% price cut with an elasticity of 1.6 [0.75 pts]

### Hint

Apply $\Delta Q/Q = -E_d\,\Delta P/P$ at the starting point of 2,000 probes. The variable cost does not change with the price, so the unit margin falls by the whole price cut. For the last question, write the new profit as a function of $E_d$ and set it equal to the present profit.

### Checkpoint

- New volume 2,320 probes, new price 225 €, new margin 125 €
- New operating profit 110,000 € (−10,000 €)
- Revenue from 500,000 € to 522,000 € (+22,000 €)
- The cut raises profit only if $E_d$ > 2.0

### Solution

#### New volume

$\Delta P/P = -0.10$ and $E_d = 1.6$ in absolute value (Topic 5, Slide 17; topic 5.2.2.pdf, p. 2):

$$\frac{\Delta Q}{Q} = -E_d\,\frac{\Delta P}{P} = -1.6 \times (-0.10) = +0.16$$

$$Q_{new} = 2{,}000 \times (1 + 0.16) = 2{,}320\ \text{probes}$$

#### New price, margin and operating profit

$$P_{new} = 250 \times (1 - 0.10) = 225\ \text{€} \qquad m_{new} = 225 - 100 = 125\ \text{€/probe}$$

$$\text{Profit}_{new} = Q_{new}\,m_{new} - FC = 2{,}320 \times 125 - 180{,}000 = 290{,}000 - 180{,}000 = 110{,}000\ \text{€}$$

The profit falls from 120,000 € to 110,000 €, by 10,000 €.

#### Change in revenue

Revenue before: $2{,}000 \times 250 = 500{,}000$ €. Revenue after: $2{,}320 \times 225 = 522{,}000$ €, a rise of 22,000 €. The demand is elastic ($E_d > 1$), so the price cut raises revenue (topic 5.2.2.pdf, p. 3), but the profit falls: the margin drops by $25/150 = 16.7\%$ while the volume grows by only 16%.

#### Elasticity at which the cut stops lowering profit

With a general elasticity $E_d$, the new volume is $2{,}000\,(1 + 0.10\,E_d)$. The cut leaves the profit unchanged when

$$2{,}000\,(1 + 0.10\,E_d) \times 125 - 180{,}000 = 120{,}000$$

Add 180,000 to both sides and divide by $2{,}000 \times 125 = 250{,}000$:

$$1 + 0.10\,E_d = \frac{300{,}000}{250{,}000} = 1.20 \quad\Longrightarrow\quad E_d = \frac{1.20 - 1}{0.10} = 2.0$$

The cut raises the operating profit only if the elasticity is above 2.0: the volume must grow by more than 20% to make up for a margin that falls from 150 € to 125 €, since $150/125 = 1.20$. With $E_d = 1.6$ the cut is not advisable. (This threshold is an application of the course formulas, not a separate concept of the course.)

## Interpretation

Two monthly summaries are enough to recover the whole cost structure because the costs are linear in the volume: the difference between the months isolates the variable cost and the fixed costs follow. Orbis breaks even at 1,200 probes; at the forecast of 2,000 its margin of safety is 800 probes and its leverage 2.50, half the 5.00 it had in March, so its profit is now less exposed to a fall in sales. The observed doubling of the profit for a 20% rise in sales from March to April is the operating leverage at work. The price cut gains revenue but loses profit unless the demand is more elastic than 2.0. Limiting cases: at $Q = Q^* = 1{,}200$ the OL is not defined (zero profit); with $E_d = 2.0$ exactly the cut leaves the profit at 120,000 €. Dimensions: prices, costs per probe and margins in € per probe, volumes in probes a month, profits and revenues in € a month, OL and elasticity dimensionless.

## Verification

- (a) price (€) | 375000/1500 | 250
- (a) price from April (€) | 450000/1800 | 250
- (a) variable cost per probe (€) | (360000-330000)/(1800-1500) | 100
- (a) fixed costs (€) | 330000-100*1500 | 180000
- (a) April total cost check (€) | 180000+100*1800 | 360000
- (a) unit margin (€) | 250-100 | 150
- (b) break-even point (probes) | 180000/150 | 1200
- (b) profit at 2,000 probes (€) | 2000*150-180000 | 120000
- (b) margin of safety (probes) | 2000-1200 | 800
- (b) margin of safety (€) | (2000-1200)*150 | 120000
- (b) margin of safety (%) | 100*(2000-1200)/1200 | 66.67
- (c) March profit (€) | 375000-330000 | 45000
- (c) OL at 1,500 probes | 1500*150/(1500*150-180000) | 5.00
- (c) OL at 2,000 probes | 2000*150/(2000*150-180000) | 2.50
- (c) April profit (€) | 450000-360000 | 90000
- (c) relative change in sales | (1800-1500)/1500 | 0.20
- (c) relative change in profit | (90000-45000)/45000 | 1.00
- (c) observed leverage March to April | ((90000-45000)/45000)/((1800-1500)/1500) | 5.00
- (d) new volume (probes) | 2000*(1+1.6*0.10) | 2320
- (d) new price (€) | 250*(1-0.10) | 225
- (d) new unit margin (€) | 250*0.90-100 | 125
- (d) new operating profit (€) | 2000*(1+1.6*0.10)*(250*0.90-100)-180000 | 110000
- (d) change in operating profit (€) | (2320*125-180000)-120000 | -10000
- (d) revenue before (€) | 2000*250 | 500000
- (d) revenue after (€) | 2320*225 | 522000
- (d) change in revenue (€) | 2320*225-2000*250 | 22000
- (d) relative fall of the margin (%) | 100*25/150 | 16.7
- (d) threshold elasticity | ((120000+180000)/(2000*125)-1)/0.10 | 2.0

**Back to:** [[Problem Set - Business Management Problem Bank]]
