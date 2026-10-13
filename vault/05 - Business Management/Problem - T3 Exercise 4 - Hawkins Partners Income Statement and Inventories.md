---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
origen: "T3_Financial Statements_EXERCISES.pdf, Exercise 4, p. 2"
dificultad: easy
tags:
  - problem
  - solved
  - income-statement
---

# ✏️ Problem: Exercise 4 — Hawkins Partners, income statement with inventories

## 📄 Statement

Prepare the income statement for Hawkins Partners using the following figures (in euros), knowing that the applicable corporate tax rate is 30%:

| # | Item | € | # | Item | € |
| :--- | :--- | ---: | :--- | :--- | ---: |
| 1 | Initial inventory | 600 | 6 | Interests from the long-term debt | 5,500 |
| 2 | Purchase of goods (sold 100%) | 84,000 | 7 | Wages and salaries | 12,700 |
| 3 | Rental costs | 1,000 | 8 | Water, gas and electricity | 1,200 |
| 4 | Property sold to another company (income) | 10,500 | 9 | Sales | 130,800 |
| 5 | Interests received by the company | 15,200 | 10 | Inventory at the end of the period | 500 |

## Phase 1 — Setup: what each figure is

The statement mixes the three kinds of income-statement lines of [Slide 9]: items of the primary operation (sales, goods, wages, rent, utilities), **non-operating items** (interests, the sale of property) [Slide 11], and the tax. It also gives the initial and final **inventory**, which adjust the cost of goods sold.

## Phase 2 — Frames: classification of every item

| Item | Line of the income statement |
| :--- | :--- |
| 9. Sales | Sales revenue |
| 1, 2, 10. Inventories and purchases | Cost of goods sold |
| 3, 7, 8. Rent, wages, utilities | Operating expenses [Slide 10] |
| 4. Property sold (income) | Non-operating item: gain on the sale of property [Slide 11] |
| 5. Interests received | Non-operating item: interest revenue [Slide 8, Slide 11] |
| 6. Interests on long-term debt | Non-operating item: interest expense [Slide 11] |
| Tax 30% | Income taxes [Slide 11] |

## Phase 3 — Derivation

### Step 1. Cost of goods sold

The goods sold are those available (initial inventory + purchases) minus those still in stock at the end:

$$\text{COGS} = 600 + 84{,}000 - 500 = 84{,}100 \text{ €}$$

The inventory fell by $600 - 500 = 100$ €: those 100 € of goods were also sold, so they add to the purchases.

### Step 2. Income statement

| Line | Computation | € |
| :--- | :--- | ---: |
| Sales revenue | | 130,800 |
| − Cost of goods sold | Step 1 | 84,100 |
| **= Gross profit** | $130{,}800 - 84{,}100$ | **46,700** |
| − Wages and salaries | | 12,700 |
| − Rental costs | | 1,000 |
| − Water, gas and electricity | | 1,200 |
| **= Income from operations** | $46{,}700 - 14{,}900$ | **31,800** |
| + Gain on property sold | | 10,500 |
| + Interests received | | 15,200 |
| − Interests on long-term debt | | 5,500 |
| **= Income before taxes** | $31{,}800 + 10{,}500 + 15{,}200 - 5{,}500$ | **52,000** |
| − Income taxes (30%) | $0.30 \times 52{,}000$ | 15,600 |
| **= Net income** | $52{,}000 - 15{,}600$ | **36,400** |

## Phase 4 — Interpretation and checks

- **Non-operating items add 20,200 €** ($10{,}500 + 15{,}200 - 5{,}500$): almost 39% of the income before taxes does not come from the primary operation, which is why the slides separate them [Slide 11].
- **The tax base** is the income before taxes (52,000), not the income from operations [Slide 11].
- **Reading of item 4:** the statement labels the 10,500 € as income from the property sold; no book value of the property is given, so the whole amount is taken as the gain on the sale.
- **Check:** $130{,}800 + 10{,}500 + 15{,}200 = 156{,}500$ of revenues and gains; $84{,}100 + 14{,}900 + 5{,}500 = 104{,}500$ of expenses; $156{,}500 - 104{,}500 = 52{,}000$.

## Check against the official key

> [!info] Official solution, `T3_Financial Statements_SOLUTIONS.pdf`, p. 5
> Cost of goods sold 84,100 (purchases 84,000 plus the inventory variation of 100), operating expenses 14,900, interests received 15,200, interests paid 5,500, income before taxes 52,000, tax 15,600 and net income 36,400 coincide with the key.

> [!warning] Discrepancy with the official solution (EBIT)
> The key includes the 10,500 € of the property sold (labelled "Income from rentals") in the income from operations, so its EBIT is 42,300 €. Here the amount is shown below EBIT, as a non-operating gain, following the definition of Slide 11 (gains and losses on the sale of equipment and investments). Both layouts give the same income before taxes (52,000 €) and the same net income (36,400 €); only the EBIT subtotal changes: 31,800 € here and 42,300 € in the key. For an exam marked against this key, expect EBIT = 42,300 €.

---

**Back to:** [[Business Management MOC]]

**Related notes:** [[Concept - Method to Build the Income Statement and Balance Sheet]] · [[Topic 3 - Financial Management I - Financial Statements]]
