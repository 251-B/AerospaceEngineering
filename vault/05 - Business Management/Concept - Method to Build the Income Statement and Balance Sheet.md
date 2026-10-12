---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
fuentes:
  - "Topic 3_Financial Management (I).pdf, Slides 7-19, 23, 35"
  - "T3_Financial Statements_EXERCISES.pdf and T3_Additional_EXERCISES.pdf (wording of the statements)"
tags:
  - concept
  - method
  - business-management
  - balance-sheet
  - income-statement
dificultad: medium
---

# 🧭 Method: building the income statement and the balance sheet in an exam problem

> **Central idea:** every operation of an exam problem is read **three times**: does it create a **revenue or expense** of the period (income statement)? does **cash** enter or leave before the closing date (cash account)? what **asset, liability or equity** item remains open at the closing date (balance sheet)? If the three readings are done for every operation, the balance sheet closes by itself.

The rules below come from the Topic 3 slides (cited) and, where the slides say nothing, from the wording of the exercise statements themselves (linear depreciation, residual value, interest rates, payment terms), which define how each operation must be treated.

## Step 0. Read the dates: the period and the closing instant

- Write the **period** of the income statement (a quarter, a semester, a calendar year) and the **closing instant** of the balance sheet (e.g. 31/12 at 24:00). The income statement covers a **period**; the balance sheet is a **point in time** [Slide 7, Slide 12].
- Draw a **timeline** with every dated event: purchases, sales, payments, loan dates, repayments. Months of use inside the period decide depreciation and interest; payment dates decide cash and debts.
- A balance at "24:00 after all payments" includes the payments made that day (taxes, dividends, instalments); a balance "before" them keeps them as liabilities.

## Step 1. Classify every operation with the three questions

For each operation fill one row of this table:

| Operation | Income statement (revenue / expense of the period) | Cash (collected / paid before closing) | Balance sheet item still open at closing |
| :--- | :--- | :--- | :--- |
| Sale on credit | Revenue for the **whole** sale [Slide 8] | Only the part collected | Accounts receivable = sale − collected |
| Purchase of goods for resale or raw materials | Expense only for the part **consumed or sold** (cost of goods sold) [Slide 10] | Only the part paid | Inventory = unconsumed part; accounts payable = unpaid part |
| Salaries, utilities, rent, services | Expense for the period's consumption [Slide 8] | Only the part paid | Payable for the unpaid part |
| Purchase of a fixed asset (machine, building, patent) | No expense on purchase; only the **depreciation** of the months used | Only the part paid | Asset at cost minus accumulated depreciation; debt for the unpaid part |
| Loan received | Nothing (it is not a revenue) | Cash in | Liability: current part (due within one year) and long-term part [Slide 16] |
| Interest on a loan | Expense for the months of the period (non-operating item) [Slide 11] | Only the interest actually paid | Interest payable for the accrued but unpaid part |
| Repayment of principal | Nothing (it is not an expense) | Cash out | The liability decreases |
| Capital contributed by owners | Nothing | Cash in (or the asset contributed) | Contributed capital [Slide 17] |
| Income taxes | Expense = income before taxes × rate [Slide 11] | Only if paid before closing | Taxes payable otherwise |
| Dividends | Nothing (a distribution of profit, not an expense) [Slide 23] | Only if paid before closing | Dividends payable if declared and unpaid; retained earnings = profit − dividends |

Two consequences are worth memorising: **a revenue is not a collection and an expense is not a payment** [Slide 8]; and **depreciation is an expense that is never a payment**, while **buying a machine or repaying a loan are payments that are never expenses**.

## Step 2. Compute the special items

**Depreciation** (when the statement says linear / straight-line, with or without residual value):

$$\text{Depreciation of the period} = \frac{\text{Cost} - \text{Residual value}}{\text{Useful life in years}} \times \frac{\text{months used in the period}}{12}$$

The asset appears in the balance sheet at its **net value**: cost − accumulated depreciation. Land is not depreciated in the exercises (no useful life is given for it).

**Interest** (simple interest at an annual rate, as in all the exercises):

$$\text{Interest of the period} = \text{Principal outstanding} \times \text{annual rate} \times \frac{\text{months}}{12}$$

If the principal changes during the period (instalments), split the period into the stretches where the principal is constant and add the pieces.

**Cost of goods sold** with stocks:

$$\text{COGS} = \text{Initial inventory} + \text{Purchases} - \text{Ending inventory}$$

This is the same rule as "expense only for the part consumed": whatever was bought or held and is no longer in stock was consumed.

## Step 3. Build the income statement (format of [Slide 9])

| Line | Content |
| :--- | :--- |
| Sales revenue | Sales of the period (net of the discounts the statement gives) |
| − Cost of goods sold | COGS of Step 2 |
| = Gross profit | |
| − Operating expenses | Salaries, social security, rent, utilities, services, depreciation |
| = Income from operations | |
| ± Non-operating items | Interest expense and interest revenue; gains and losses on the sale of equipment and investments [Slide 11] |
| = Income before taxes | |
| − Income taxes | Income before taxes × tax rate [Slide 11] |
| = Net income | Then split it: dividends and retained earnings [Slide 23] |

## Step 4. Compute cash with a cash account

$$\text{Cash}_{\text{end}} = \text{Cash}_{\text{start}} + \sum \text{collections} - \sum \text{payments}$$

List every inflow (capital, loans, collections from customers, old receivables collected) and every outflow (purchases paid, salaries, investments paid, interest, principal, taxes, dividends). Depreciation never appears here.

## Step 5. Build the balance sheet (format of [Slide 18])

| Assets | Liabilities and equity |
| :--- | :--- |
| **Non-current assets:** land, buildings, machinery, equipment, patents, licences (at net value); long-term investments; receivables due in more than one year [Slide 15] | **Equity:** contributed capital; retained earnings / reserves; net income of the period not distributed [Slide 17] |
| **Current assets:** inventory, accounts receivable due within one year, cash [Slide 14] | **Long-term liabilities:** debts due after one year [Slide 16] |
| | **Current liabilities:** suppliers, other payables, taxes payable, interest payable, dividends payable, the part of any loan due within one year [Slide 16] |

The one-year boundary is counted **from the balance-sheet date**: a debt due on 1/2 of next year is current at 31/12; a customer debt deferred to July of the year after next is non-current.

## Step 6. Check

1. $\text{Total assets} = \text{Total liabilities} + \text{Equity}$ [Slide 12]. If it fails, the difference is almost always one operation that was recorded on only one side.
2. **Cash cross-check:** the change in equity due to the period equals net income − dividends; the change in cash equals collections − payments. Re-adding each operation should explain both.
3. **Sign and size:** receivables, payables and inventory can never be negative; depreciation can never exceed cost − residual value.

---

**Back to:** [[Business Management MOC]]

**Related notes:** [[Topic 3 - Financial Management I - Financial Statements]] · [[Problem - T3 Extra 1 - Circonsa Balance Sheet and Income Statement]]
