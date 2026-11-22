---
materia: Business Management
tema: "Unit 4: break-even point, operating leverage and price elasticity"
bank_id: M02
title: "Helix Composites: break-even list price with a discount for one customer, profit margin target, leverage and a price cut"
category: mt2_problem
archetype: bep-ol-elasticity
level: standard
unit: 4
difficulty: 2
points: 2.5
time_minutes: 22
official: false
origen: "Problem written for the bank in the style of Exercise 1 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf; not an official exercise. Method: Topic 4, Slides 37-42; Topic 5, Slide 17 and topic 5.2.2.pdf, pp. 2-3."
tags:
  - problem-bank
  - midterm-2
  - bep-ol-elasticity
  - break-even
  - operating-leverage
  - price-elasticity
---

# Bank M02 — Helix Composites: break-even with a discount for one customer

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Exercise 1 of the examples PDF (Pegasus S.A.). Differences: the commercial discount applies only to part of the customers, the cost list contains an item that is not an operating cost, the profit target is a margin on sales, and the price is cut instead of raised. Method: Topic 4, Slides 37 to 42; price elasticity from Topic 5, Slide 17 and topic 5.2.2.pdf, pp. 2-3.

## Statement

Helix Composites S.L. manufactures carbon-fibre rotor blades for cargo drones. Its expected annual costs are:

- Lease of the autoclave hall: 380,000 €
- Salaries of the lay-up operators, hired on fixed annual contracts: 460,000 €
- Salaries of the engineering and quality staff: 200,000 €
- Depreciation of the moulds and the autoclave: 100,000 €
- Insurance and administration: 60,000 €
- Interest on the bank loan that financed the autoclave: 60,000 €
- Carbon prepreg and resin: 36 € per blade
- Autoclave energy: 7 € per blade
- Packaging and transport to the customer: 5 € per blade

The sales forecast is 25,000 blades a year. 40% of the blades are sold to one drone manufacturer (OEM) under a framework contract that gives it a 10% discount on the list price; the other customers buy the remaining 60% at the list price.

a) Classify the costs and calculate the list price per blade that makes the firm break even (zero operating profit) at the forecast volume of 25,000 blades. (0.5 points)

b) Using the list price found in (a), calculate the volume of blades the firm must sell to earn an operating profit equal to 10% of its net sales revenue. (0.5 points)

c) Calculate the operating leverage (OL) at the volume found in (b) and at a volume of 40,000 blades. What do these values mean? (0.75 points)

d) At 40,000 blades the price elasticity of demand is 1.5. The firm cuts its list price by 4%, keeping the OEM discount and the share of each group of customers. Calculate the new expected volume, the new operating profit and the change in sales revenue, and explain the result. (0.75 points)

## Setup

| Item | Value |
| :--- | :--- |
| Forecast volume | $Q = 25{,}000$ blades |
| Share of the OEM (10% discount) | 40% of the units |
| Share of the other customers (list price) | 60% of the units |
| Target of part (b) | operating profit = 10% of net sales revenue |
| Second volume of part (c) | 40,000 blades |
| Price elasticity at 40,000 blades | $E_d = 1.5$ (absolute value) |
| Change of the list price in part (d) | −4% |

Model of the course:

- Profit $= P\,Q - (VC\,Q + FC) = Q\,(P - VC) - FC$, unit margin $m = P - VC$, break-even point $Q_0 = FC/m$ (Topic 4, Slide 37).
- Operating leverage $OL = Q\,m/(Q\,m - FC) = Q/(Q - Q^*)$ (Topic 4, Slides 39, 40 and 42).
- Price elasticity $E_d = (\Delta Q/Q)/(\Delta P/P)$, used in absolute value, so $\Delta Q/Q = -E_d\,\Delta P/P$ (Topic 5, Slide 17; topic 5.2.2.pdf, p. 2), as in Examples PDF, Exercise 1 (d).

## (a) Classify the costs and find the break-even list price [0.5 pts]

### Hint

A cost is fixed when its yearly amount does not depend on the number of blades. Revenue is earned at the average net price that the two groups of customers pay, not at the list price. Ask whether the interest on the loan is an operating cost.

### Checkpoint

- $FC$ = 1,200,000 €; $VC$ = 48 € per blade; the interest (60,000 €) is not an operating cost
- Average net price = 0.96 × list price
- Net price = 96 € per blade; list price = 100 € per blade

### Solution

#### Classify the costs

The lease, the salaries of the operators (fixed annual contracts, as the direct labour of Examples PDF, Exercise 1), the salaries of the engineering and quality staff, the depreciation and the insurance and administration are the same whatever the number of blades: they are fixed costs.

$$FC = 380{,}000 + 460{,}000 + 200{,}000 + 100{,}000 + 60{,}000 = 1{,}200{,}000\ \text{€}$$

The prepreg and resin, the energy of the autoclave and the packaging and transport are spent once per blade: they are variable costs per unit.

$$VC = 36 + 7 + 5 = 48\ \text{€/blade}$$

The interest on the bank loan is a financial expense, a non-operating item of the income statement (Topic 3, Slide 11): it lies below the operating profit (EBIT) and does not enter a break-even point defined on the operating profit. It is left out of $FC$.

#### Average net price

Of every 100 blades, 40 are sold at $0.90\,P_L$ (list price minus the 10% discount) and 60 at $P_L$. The average net price per blade is the weighted mean:

$$P = 0.40 \times 0.90\,P_L + 0.60 \times P_L = (0.36 + 0.60)\,P_L = 0.96\,P_L$$

#### Break-even condition at 25,000 blades

At the break-even point revenue equals total cost, $P\,Q_0 = FC + VC\,Q_0$ (Topic 4, Slide 37). Solving for the net price:

$$P = \frac{FC + VC\,Q_0}{Q_0} = \frac{1{,}200{,}000 + 48 \times 25{,}000}{25{,}000} = \frac{2{,}400{,}000}{25{,}000} = 96\ \text{€/blade}$$

#### From the net price to the list price

$$P_L = \frac{P}{0.96} = \frac{96}{0.96} = 100\ \text{€/blade}$$

Check: $m = 96 - 48 = 48$ € and $Q_0 = FC/m = 1{,}200{,}000/48 = 25{,}000$ blades, the forecast volume. Units: € divided by € per blade gives blades. Had the interest been counted as a fixed cost, the net price would be $(1{,}260{,}000 + 1{,}200{,}000)/25{,}000 = 98.4$ € and the list price 102.5 €; had the discount been applied to all customers, as in Pegasus, the list price would be $96/0.90 = 106.67$ €.

## (b) Volume for an operating profit of 10% of net sales [0.5 pts]

### Hint

Write the target as an equation in $Q$: the profit $Q\,m - FC$ must equal 10% of the revenue $P\,Q$. The target profit is not a fixed number, so $Q = (\text{Profit} + FC)/m$ cannot be used directly.

### Checkpoint

- Unit margin $m$ = 48 € per blade, 10% of the net price = 9.60 € per blade
- $Q$ = 31,250 blades
- Revenue 3,000,000 €, operating profit 300,000 €

### Solution

#### Set the target as an equation

With the list price of 100 €, the net price is $P = 96$ € and $m = P - VC = 96 - 48 = 48$ € per blade. The target is

$$Q\,m - FC = 0.10 \times P\,Q$$

#### Solve for the volume

Move the terms in $Q$ to the left and factor $Q$:

$$Q\,(m - 0.10\,P) = FC \quad\Longrightarrow\quad Q = \frac{FC}{m - 0.10\,P} = \frac{1{,}200{,}000}{48 - 0.10 \times 96} = \frac{1{,}200{,}000}{38.40} = 31{,}250\ \text{blades}$$

Each blade leaves 48 € of margin, of which 9.60 € must be kept as profit, so only 38.40 € per blade is left to cover the fixed costs.

#### Check

Revenue $= 96 \times 31{,}250 = 3{,}000{,}000$ €. Operating profit $= 31{,}250 \times 48 - 1{,}200{,}000 = 1{,}500{,}000 - 1{,}200{,}000 = 300{,}000$ €, which is $300{,}000/3{,}000{,}000 = 10\%$ of the revenue. The volume is above the break-even point (25,000 blades), as a positive profit requires.

## (c) Operating leverage at 31,250 and at 40,000 blades [0.75 pts]

### Hint

Use $OL = Q\,m/(Q\,m - FC)$ and check it with $OL = Q/(Q - Q^*)$, where $Q^*$ is the break-even point of part (a).

### Checkpoint

- At 31,250 blades: $Q\,m$ = 1,500,000 €, profit 300,000 €, OL = 5.00
- At 40,000 blades: $Q\,m$ = 1,920,000 €, profit 720,000 €, OL = 2.67
- Meaning: a 1% change in sales changes the operating profit by 5% and by 2.67%

### Solution

#### Leverage at 31,250 blades

$$OL = \frac{Q\,m}{Q\,m - FC} = \frac{31{,}250 \times 48}{31{,}250 \times 48 - 1{,}200{,}000} = \frac{1{,}500{,}000}{300{,}000} = 5.00$$

Check with the break-even point, $Q^* = 25{,}000$ (Topic 4, Slide 42): $OL = 31{,}250/(31{,}250 - 25{,}000) = 31{,}250/6{,}250 = 5.00$.

#### Leverage at 40,000 blades

$$OL = \frac{40{,}000 \times 48}{40{,}000 \times 48 - 1{,}200{,}000} = \frac{1{,}920{,}000}{720{,}000} = 2.67$$

Check: $OL = 40{,}000/(40{,}000 - 25{,}000) = 40{,}000/15{,}000 = 2.67$.

#### Meaning

The OL measures how a change in sales translates into a change in operating profit (Topic 4, Slide 40). At 31,250 blades a 1% change in sales changes the operating profit by 5% in the same direction (a 10% fall in sales would cut profit by 50%); at 40,000 blades the same 1% changes the profit by only 2.67%. Both values are greater than 1 because the firm has profits ($Q > Q^*$), and the leverage falls as the volume moves away from the break-even point (Topic 4, Slide 42). The OL is an index of economic risk (Topic 4, Slide 41): Helix is riskier at 31,250 blades, close to its break-even point, than at 40,000. The leverage is a pure number: € over €, or blades over blades.

## (d) A 4% cut in the list price with an elasticity of 1.5 [0.75 pts]

### Hint

Because the discount is a percentage and the customer mix does not change, the average net price falls by the same 4% as the list price. Apply $\Delta Q/Q = -E_d\,\Delta P/P$ at the starting point of 40,000 blades, then recompute margin and profit.

### Checkpoint

- $\Delta Q/Q$ = +6%, new volume 42,400 blades
- New net price 92.16 €, new margin 44.16 €
- New operating profit 672,384 € (was 720,000 €: −47,616 €)
- Revenue rises from 3,840,000 € to 3,907,584 € (+67,584 €)

### Solution

#### New volume

The relative change of the list price is $\Delta P/P = -4\% = -0.04$. With $E_d = 1.5$ in absolute value (Topic 5, Slide 17; topic 5.2.2.pdf, p. 2):

$$\frac{\Delta Q}{Q} = -E_d\,\frac{\Delta P}{P} = -1.5 \times (-0.04) = +0.06$$

$$Q_{new} = 40{,}000 \times (1 + 0.06) = 42{,}400\ \text{blades}$$

#### New net price and margin

The average net price is $0.96\,P_L$, so it changes in the same proportion as the list price:

$$P_{new} = 96 \times (1 - 0.04) = 92.16\ \text{€/blade} \qquad m_{new} = 92.16 - 48 = 44.16\ \text{€/blade}$$

(New list price $100 \times 0.96 = 96$ €; $0.96 \times 96 = 92.16$ €, the same result.)

#### New operating profit

$$\text{Profit}_{new} = Q_{new}\,m_{new} - FC = 42{,}400 \times 44.16 - 1{,}200{,}000 = 1{,}872{,}384 - 1{,}200{,}000 = 672{,}384\ \text{€}$$

Before the price cut: $\text{Profit} = 40{,}000 \times 48 - 1{,}200{,}000 = 720{,}000$ €. The profit falls by $720{,}000 - 672{,}384 = 47{,}616$ €.

#### Revenue and explanation

Revenue before: $40{,}000 \times 96 = 3{,}840{,}000$ €. Revenue after: $42{,}400 \times 92.16 = 3{,}907{,}584$ €, a rise of 67,584 €. The demand is elastic ($E_d > 1$), so a price cut raises the volume more than proportionally and the revenue rises (topic 5.2.2.pdf, p. 3). The operating profit, however, falls: the unit margin drops from 48 € to 44.16 €, a fall of $3.84/48 = 8\%$, twice the 4% price cut because the variable cost does not fall, and the 6% gain in volume does not make up for it. Higher revenue does not mean higher profit; the decision must be judged on the margin.

## Interpretation

Helix's break-even list price (100 €) already includes the fact that only 40% of the blades carry the discount, which lowers the average price by 4% instead of 10%. The leverage falls from 5.00 to 2.67 as the firm moves from 31,250 to 40,000 blades, so further away from its break-even point its profit is less sensitive to sales. The price cut of part (d) is the opposite of the price rise of Pegasus: with elastic demand it gains revenue but loses operating profit, because each blade sold earns 3.84 € less while the fixed costs stay at 1,200,000 €. Limiting cases: with no OEM customers the factor 0.96 becomes 1 and the list price would be 96 €; at $Q = Q^* = 25{,}000$ the OL is not defined (the profit is zero). Dimensions: prices and margins in € per blade, volumes in blades, profits and revenues in €, OL and elasticity dimensionless.

## Verification

- (a) fixed costs (€) | 380000+460000+200000+100000+60000 | 1200000
- (a) variable cost per blade (€) | 36+7+5 | 48
- (a) average net price factor | 0.40*0.90+0.60 | 0.96
- (a) break-even net price (€) | (1200000+48*25000)/25000 | 96
- (a) break-even list price (€) | ((1200000+48*25000)/25000)/0.96 | 100
- (a) break-even volume check | 1200000/(96-48) | 25000
- (b) volume for a 10% margin on sales | 1200000/((96-48)-0.10*96) | 31250
- (b) revenue (€) | 96*31250 | 3000000
- (b) operating profit (€) | 31250*48-1200000 | 300000
- (c) OL at 31,250 blades | 31250*48/(31250*48-1200000) | 5.00
- (c) OL at 40,000 blades | 40000*48/(40000*48-1200000) | 2.67
- (d) new volume | 40000*(1+1.5*0.04) | 42400
- (d) new net price (€) | 96*(1-0.04) | 92.16
- (d) new unit margin (€) | 96*(1-0.04)-48 | 44.16
- (d) new operating profit (€) | 40000*(1+1.5*0.04)*(96*0.96-48)-1200000 | 672384
- (d) change in operating profit (€) | (40000*1.06*(96*0.96-48)-1200000)-(40000*48-1200000) | -47616
- (d) new revenue (€) | 40000*1.06*96*0.96 | 3907584
- (d) change in revenue (€) | 40000*1.06*96*0.96-40000*96 | 67584

**Back to:** [[Problem Set - Business Management Problem Bank]]
