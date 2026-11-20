---
materia: Business Management
tema: "Unit 4: cost classification, break-even point, operating leverage, production systems and productivity"
bank_id: B02
title: "Break-even point, operating leverage and production"
category: mt2_mcq_block
unit: 4
concepts:
  - u4-cost-classification
  - u4-bep-calculation
  - u4-bep-commercial-discount
  - u4-operating-leverage-meaning
  - u4-ol-from-bep
  - u4-ol-losses
  - u4-production-system-types
  - u4-just-in-time
  - u4-total-productivity
  - u4-fixed-costs-economic-risk
difficulty: 2
origen: "Questions written for the bank for the multiple-choice part of the simulated Midterm 2 (a practice format of the portal; the examples PDF has no multiple-choice part); not official exercises. Content from Topic 4, Slides 7-9, 21-23, 34, 37, 40-42, and Exercise 1 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf."
tags:
  - problem-bank
  - midterm-2
  - multiple-choice
  - unit-4
---

# Bank B02 — Break-even point, operating leverage and production

> [!info] Practice item, not an official exercise
> Ten multiple-choice questions written for the bank (four options, one right answer; +0.25 right, −0.08 wrong, 0 blank). Content: Topic 4 (The Production Function), Slides 7 to 42, and Exercise 1 of the examples PDF.

## B02.1 Which cost is variable

- id: B02-Q1
- concept_id: u4-cost-classification
- format: identify
- asks: classification

A machining shop makes titanium brackets for aircraft seats. Which of the following costs is a variable cost:

a) The annual lease of the workshop
b) The salary of the plant manager
c) The titanium bar consumed by each bracket
d) The depreciation of the CNC machines

### Answer

c

### Explanation

A variable cost grows with the volume produced, so total cost is $TC = FC + VC\,Q$ with $VC$ per unit (Topic 4, Slide 37). The titanium consumed by each bracket is spent once per unit, so it is a variable cost; the other three are paid whatever the volume, as the rent and the fixed staff costs of Exercise 1 of the examples PDF.

- a) The lease is paid in full whether the shop makes one bracket or ten thousand, so it is a fixed cost.
- b) A manager's salary does not depend on the number of brackets produced; it is a fixed cost of the period.
- d) The yearly depreciation of the machines is the same at any volume of output, so it belongs to the fixed costs.

### Source

Topic 4, Slide 37; Examples PDF, Exercise 1.

## B02.2 Break-even volume

- id: B02-Q2
- concept_id: u4-bep-calculation
- format: numeric
- asks: calculation
- calc: 900000/(250-175)

A maker of avionics cooling fans has fixed costs of 900,000 € per year, sells each fan at 250 € and has a variable cost of 175 € per fan. Its break-even point is:

a) 12,000 units
b) 3,600 units
c) 5,143 units
d) 2,118 units

### Answer

a

### Explanation

The unit margin is $m = P - VC = 250 - 175 = 75$ € per fan, and the break-even point is $Q_0 = FC/m = 900{,}000/75 = 12{,}000$ units (Topic 4, Slide 37).

- b) 3,600 units divides the fixed costs by the price, 900,000/250, forgetting that each unit must also pay its own variable cost.
- c) 5,143 units divides the fixed costs by the variable cost per unit, 900,000/175, which has no economic meaning.
- d) 2,118 units adds price and variable cost, 900,000/(250 + 175), instead of subtracting them to get the margin.

### Source

Topic 4, Slide 37.

## B02.3 Break-even point with a commercial discount

- id: B02-Q3
- concept_id: u4-bep-commercial-discount
- format: numeric
- asks: application
- calc: 360000/(80*0.9-54)

A supplier of cabin LED strips has a list price of 80 € per unit and gives a 10% commercial discount on the list price to all its customers. Its variable cost is 54 € per unit and its fixed costs are 360,000 € per year. Its break-even point is:

a) 13,846 units
b) 15,385 units
c) 5,000 units
d) 20,000 units

### Answer

d

### Explanation

Revenue is earned at the net price, $P = 0.90 \times 80 = 72$ € per unit, so $m = 72 - 54 = 18$ € and $Q_0 = 360{,}000/18 = 20{,}000$ units (Topic 4, Slide 37; the discount is handled as in Examples PDF, Exercise 1).

- a) 13,846 units uses the list price, 360,000/(80 − 54), as if no customer received the discount.
- b) 15,385 units applies the 10% discount to the margin, 360,000/(0.9 × 26), instead of to the price; the variable cost is not discounted.
- c) 5,000 units divides the fixed costs by the net price, 360,000/72, and forgets to subtract the variable cost.

### Source

Topic 4, Slide 37; Examples PDF, Exercise 1.

## B02.4 Effect of a fall in sales

- id: B02-Q4
- concept_id: u4-operating-leverage-meaning
- format: what-happens
- asks: effect

A drone maker has an operating leverage of 4 at its current volume. If its sales fall by 5%, what happens to its operating profit:

a) It falls by 1.25%
b) It falls by 20%
c) It falls by 5%, the same as the sales
d) It falls by 4%

### Answer

b

### Explanation

$OL = (\Delta\text{Profit}/\text{Profit})/(\Delta Q/Q)$, so the relative change of the profit is $OL \times \Delta Q/Q = 4 \times (-5\%) = -20\%$ (Topic 4, Slides 39 and 40: with OL = 3 a 10% fall in sales lowers profit by 30%).

- a) 1.25% divides the change in sales by the leverage, inverting the ratio that defines the OL.
- c) A change equal to that of sales would mean OL = 1, which ignores the effect of the fixed costs.
- d) 4% reads the leverage itself as the change in profit, forgetting to multiply it by the 5% change in sales.

### Source

Topic 4, Slides 39 and 40.

## B02.5 Leverage from the break-even point

- id: B02-Q5
- concept_id: u4-ol-from-bep
- format: numeric
- asks: calculation
- calc: 40000/(40000-30000)

A firm that makes oxygen masks for airliners has a break-even point of 30,000 units and sells 40,000 units. Its operating leverage is:

a) 0.25
b) 1.33
c) 4.00
d) 3.00

### Answer

c

### Explanation

Since $FC = Q^*\,m$, the leverage depends only on the distance to the break-even point: $OL = Q/(Q - Q^*) = 40{,}000/(40{,}000 - 30{,}000) = 4$ (Topic 4, Slide 42). A 1% change in sales changes the operating profit by 4%.

- a) 0.25 is $(Q - Q^*)/Q$, the inverse of the right ratio.
- b) 1.33 is $Q/Q^*$, which divides by the break-even volume instead of by the distance to it.
- d) 3.00 is $Q^*/(Q - Q^*)$, with the break-even volume in the numerator instead of the actual volume.

### Source

Topic 4, Slide 42.

## B02.6 Leverage of a firm in losses

- id: B02-Q6
- concept_id: u4-ol-losses
- format: true-statement
- asks: definition

A firm sells fewer units than its break-even point ($Q < Q^*$). Which one of the following statements about its operating leverage is TRUE:

a) It is greater than 1, so profit reacts more than proportionally to sales
b) It lies between 0 and 1, because the firm is in losses
c) It equals 1, because the fixed costs are not covered
d) It is zero or negative, and below −1 it amplifies the effect of a change in sales

### Answer

d

### Explanation

With $Q < Q^*$ the denominator of $OL = Q/(Q - Q^*)$ is negative, so $OL \le 0$; for $OL < -1$ the effect is more than proportional (amplifier) and for $-1 < OL < 0$ it is less than proportional (Topic 4, Slide 42).

- a) OL greater than 1 is the case of a firm with profits ($Q > Q^*$), not of a firm in losses.
- b) No volume gives an OL between 0 and 1: above the break-even point OL > 1 and below it OL ≤ 0.
- c) OL = 1 would need zero fixed costs; at the break-even point itself the leverage is not even defined.

### Source

Topic 4, Slide 42.

## B02.7 Type of production system

- id: B02-Q7
- concept_id: u4-production-system-types
- format: identify
- asks: classification

A company builds satellite ground stations. Each station is designed for one client, and machinery, materials and workers are brought to the site where it is built. Its type of production and plant layout are:

a) Project production with a fixed layout
b) Batch production with a functional layout
c) Mass production with a product layout
d) Continuous production with a product layout

### Answer

a

### Explanation

Individualized products with qualified workers and difficult planning are the project type, and a product that stays in one place while resources are brought to it is the fixed layout (Topic 4, Slides 7, 23 and 26).

- b) Batch production makes a variety of products in batches in a functional layout; it does not build a single one-off unit on site.
- c) Mass production makes standard products for mass markets along a line, the opposite of a design for one client.
- d) Continuous production (petrochemistry) is the high-volume end of the product-process matrix, with no individualized product.

### Source

Topic 4, Slides 7, 23 and 26.

## B02.8 Just in Time tools

- id: B02-Q8
- concept_id: u4-just-in-time
- format: identify
- asks: classification

Which of the following is a mechanism of visual control of Just in Time production:

a) Poka Yoke
b) Job cells
c) Kanban
d) U-shaped plant distribution

### Answer

c

### Explanation

The course lists Andon, control panels, work sheets and Kanban as the mechanisms of visual control of Just in Time (Topic 4, Slide 21).

- a) Poka Yoke is listed, with Jidoka, as a mechanism to support quality, not of visual control.
- b) Job cells are the tool of internal organization of Just in Time, not a visual control.
- d) The U shape is the plant distribution of Just in Time, not a mechanism of visual control.

### Source

Topic 4, Slides 20 and 21.

## B02.9 Total productivity index

- id: B02-Q9
- concept_id: u4-total-productivity
- format: numeric
- asks: calculation
- calc: 540000/(120000+90000+150000+40000)

In one month a workshop that repairs aircraft wheels produces services worth 540,000 €. It uses labour worth 120,000 €, capital worth 90,000 €, raw materials worth 150,000 € and energy worth 40,000 €. Its total productivity index is:

a) 4.50
b) 0.74
c) 2.57
d) 1.35

### Answer

d

### Explanation

Total productivity divides goods and services by all the factors together: $540{,}000/(120{,}000 + 90{,}000 + 150{,}000 + 40{,}000) = 540{,}000/400{,}000 = 1.35$ (Topic 4, Slide 34).

- a) 4.50 is 540,000/120,000, the labour productivity: a partial index, not the total one.
- b) 0.74 is 400,000/540,000, inputs over outputs, the inverse of the index.
- c) 2.57 divides only by labour and capital, 540,000/210,000, leaving out raw materials and energy.

### Source

Topic 4, Slide 34.

## B02.10 Fixed costs and economic risk

- id: B02-Q10
- concept_id: u4-fixed-costs-economic-risk
- format: cause-effect
- asks: comparison

Two firms of the same sector sell the same number of units and earn the same operating profit, but firm A has higher fixed costs than firm B. Which one of the following is TRUE:

a) Both have the same operating leverage, because they earn the same profit
b) Firm A has the higher operating leverage and therefore the higher economic risk
c) Firm B has the higher operating leverage, because its variable costs are higher
d) Firm A has the lower economic risk, because its fixed costs do not change with sales

### Answer

b

### Explanation

$OL = Q\,m/\text{Profit}$. With the same profit, $Q\,m = \text{Profit} + FC$ is larger for the firm with higher fixed costs, so firm A has the higher OL; the OL is an index of economic (operating) risk and, ceteris paribus, higher fixed costs give a higher OL (Topic 4, Slides 39 and 41).

- a) Equal profits do not give equal leverage: the numerator $Q\,m$ also contains the fixed costs, which differ.
- c) Higher variable costs mean a smaller margin and smaller $Q\,m$ for the same profit, so firm B has the lower OL.
- d) Fixed costs that do not change with sales are exactly what makes profit more sensitive to sales, so A carries more risk, not less.

### Source

Topic 4, Slides 39 and 41.

**Back to:** [[Problem Set - Business Management Problem Bank]]
