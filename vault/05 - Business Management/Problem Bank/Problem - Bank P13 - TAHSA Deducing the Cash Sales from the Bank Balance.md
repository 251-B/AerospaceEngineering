---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P13
title: "TAHSA: deducing the share of cash sales from the bank balance"
category: extra_practice_problem
archetype: narrative-case
unit: 3
difficulty: 3
points: 4.0
time_minutes: 60
official: false
number_format: eu
origen: "Exam-style practice exercise written for the problem bank (not an official exercise), in the style of T3_Additional_EXERCISES.pdf"
tags:
  - problem-bank
  - extra-practice
  - exam-style
  - accrual-vs-cash
  - uncalled-capital
  - bad-debts
  - early-payment-discount
---

# Bank P13 — TAHSA: deducing the share of cash sales from the bank balance

> [!info] Exam-style practice exercise
> Written for the problem bank in the style of `T3_Additional_EXERCISES.pdf`. It is not an official exercise and has no official key. Numbers follow the European format of the exam: dots for thousands, commas for decimals.

## Statement

The external auditor of **TALLERES AERONÁUTICOS DEL HENARES S.A. (TAHSA)**, a company of Alcalá de Henares dedicated to the machining of titanium brackets and fittings for the aircraft structures industry, must issue the audit report on the financial statements (balance sheet and Income Statement) as of 31 December 2019 (31/12/2019). The auditor has the balance of the company as of 31 December 2018 (31/12/2018), which is included below, and the following operations that have taken place during the period from 1 January 2019 (01/01/2019) to 31 December 2019 (31/12/2019).

**I.** The company has sold during the year 2.400 brackets at a price of 8 m.u. / unit (every month the same amount, 200 u.). A part of the sales of each month, always the same percentage, is charged in cash in the moment of the sale; the rest is payable to 90 days. Unfortunately the commercial department has lost the contract that fixes this percentage.

**II.** During the first quarter of 2019, the unpaid taxes and the outstanding supplier balances of the previous year were paid. The customer debt outstanding from the previous year was charged in January, except 160 m.u. from an airline component maker declared in insolvency on 1 March 2019 (01/03/2019), which is definitively lost.

**III.** At 31 December 2018 (31/12/2018) there is a stock (stock in stock) of 800 kg of titanium bar valued at 1,50 m.u. / kg. On 1 February 2019 (01/02/2019) the company purchased 3.000 kg at 1,50 m.u. / kg, 50% payable to 60 days and the other 50% deferred until 1 February 2020 (01/02/2020). On 1 August 2019 (01/08/2019) it purchased 2.000 kg more at the same price, payable to 120 days. The count of 31 December 2019 (31/12/2019) shows 900 kg in the warehouse.

**IV.** Personnel expenses have been 400 m.u. / month (to which 120 m.u. / month must be added for Social Security); salaries are paid in the month in which they are produced and Social Security the month after. General expenses (electricity, insurance, cleaning) amount to 150 m.u. / month and are paid two months after being made.

**V.** The machinery of the balance of 2018 was bought on 1 January 2016 (01/01/2016) and is amortized linearly in 10 years with residual value zero. On 1 April 2019 (01/04/2019) the company bought a 5-axis CNC centre that cost 4.800 m.u., paid in full in cash that day. To finance it, the same day a bank granted a loan of 3.600 m.u. at 5% annual interest, to be returned in one single payment on 1 April 2022 (01/04/2022); the interest is paid every 1 April for the year that ends that day. The CNC centre will be amortized linearly in 8 years with a residual value of 480 m.u.

**VI.** The long-term loan of the balance of 2018 bears 4% annual interest. The company returns 300 m.u. of principal every 30 June and every 31 December, paying the same days the interest of the semester calculated on the debt at the beginning of the semester.

**VII.** On 1 October 2019 (01/10/2019) the shareholders subscribed a capital increase of 500 new shares of 2 m.u. nominal value, without issue premium, disbursing that day only 50%; the rest will be called in 2020. On 15 November 2019 (15/11/2019) the company received in cash a dividend of 80 m.u. from its financial shares in AEROPIEZAS S.A., a permanent investment.

**VIII.** The bank statement at 23:00 hrs on 31 December 2019 (31/12/2019), before any operation of the closing, shows a balance of 3.024 m.u. The results are declared at 23:59 hrs; the corporation tax of 30% is paid immediately, and 50% of the profit after taxes is paid as dividends before the final balance at 24:00 on 31 December 2019 (31/12/2019); the rest goes to reserves.

**BALANCE 31 December 2018 (31/12/2018)**

| ASSETS | m.u. | LIABILITIES | m.u. |
| :--- | ---: | :--- | ---: |
| **NON-CURRENT ASSETS** | **7.200** | **OWNERS EQUITY** | **8.100** |
| Land | 2.000 | Paid-in capital (3.500 shares × 2 m.u.) | 7.000 |
| Machinery | 6.000 | Reserves | 1.100 |
| Accum. depreciation | (1.800) | **NON-CURRENT LIABILITIES** | **1.200** |
| Financial shares in AEROPIEZAS S.A. | 1.000 | Long-term loan | 1.200 |
| **CURRENT ASSETS** | **3.700** | **CURRENT LIABILITIES** | **1.600** |
| Stock of titanium | 1.200 | Long-term loan, part due in 2019 | 600 |
| Accounts receivable | 1.600 | Suppliers | 700 |
| Cash | 900 | Unpaid taxes | 300 |
| **Total Assets** | **10.900** | **Total Liabilities + OE** | **10.900** |

**Required:**
1. Deduce, justifying it from the bank statement, the percentage of the sales that is charged in cash, and construct the Income Statement (Profit and Loss Account) of TAHSA for the year 2019.
2. Construct and justify the balance sheet at 24:00 on 31 December 2019 (31/12/2019), showing all the intermediate calculations.
3. Determine the values of the ROA and ROE ratios in 2019.
4. The commercial director proposes for 2020 that 50% of the sales be charged in cash, granting on those cash sales a discount of 4%. Indicate what changes would have occurred in the Income Statement, the cash and the balance sheet of 2019 if this policy had been applied from 1 January 2019 (01/01/2019). In which case is the profit higher, and in which case is the final cash balance higher? Discuss, reasoned, why.

## Setup

**Unknown of the problem:** the share $p$ of each month's sales charged in cash. Every other flow of cash can be computed, so the bank statement before the closing (3.024 m.u.) gives one equation in $p$.

**Collections at 90 days:** a sale of January is collected in April; the sales of October, November and December are still pending at 31/12/2019.

**Uncalled capital:** the shareholders owe the 50% not yet disbursed; it is shown as a deduction of the subscribed capital, as in the Company X exercise of the course.

**Extension (not defined in the course decks).** $\text{ROA} = \text{Income from operations}/\text{Total assets}$ and $\text{ROE} = \text{Net profit}/\text{Owners equity}$, on the balance at 24:00 on 31/12/2019.

## (a) Deduce the percentage of cash sales and prepare the 2019 Income Statement [1.5 pts]

### Hint

Write the cash at 23:00 as initial cash + all inflows − all outflows, leaving the collections from 2019 sales as a function of $p$: $12 \times 1.600\,p + 9 \times 1.600\,(1-p)$.

### Checkpoint

- Outflows before closing 19.336; inflows other than 2019 sales 5.620 m.u.
- $p = 30\%$; collections from 2019 sales 15.840 m.u.
- Titanium consumed 7.350; depreciation 1.005; income from operations 2.645 m.u.
- Financial income 80, financial expenses 201; profit before taxes 2.524; tax 757,20; net profit 1.766,80 m.u.

### Solution

#### Step 1. Outflows before the closing

| Outflow | Computation | m.u. |
| :--- | :--- | ---: |
| Suppliers 2018 and unpaid taxes 2018 | $700 + 300$ | 1.000 |
| Titanium of 01/02, 50% at 60 days (01/04) | $0{,}50 \times 3.000 \times 1{,}50$ | 2.250 |
| Titanium of 01/08, at 120 days (29/11) | $2.000 \times 1{,}50$ | 3.000 |
| Salaries | $12 \times 400$ | 4.800 |
| Social Security, January–November | $11 \times 120$ | 1.320 |
| General expenses, January–October | $10 \times 150$ | 1.500 |
| CNC centre | | 4.800 |
| Old loan: principal | $300 + 300$ | 600 |
| Old loan: interest | $1.800 \times 0{,}04 \times \tfrac{6}{12} + 1.500 \times 0{,}04 \times \tfrac{6}{12} = 36 + 30$ | 66 |
| **Total** | | **19.336** |

#### Step 2. Inflows other than the 2019 sales

$$\underbrace{1.600 - 160}_{\text{2018 receivables}} + \underbrace{3.600}_{\text{new loan}} + \underbrace{0{,}50 \times 1.000}_{\text{capital disbursed}} + \underbrace{80}_{\text{dividend received}} = 1.440 + 3.600 + 500 + 80 = 5.620 \text{ m.u.}$$

#### Step 3. Equation for $p$

Monthly sales are $200 \times 8 = 1.600$ m.u. The cash part of every month is collected (12 months); the credit part only for January to September (9 months):

$$900 + 5.620 + 12 \times 1.600\,p + 9 \times 1.600\,(1 - p) - 19.336 = 3.024$$

$$19.200\,p + 14.400 - 14.400\,p = 3.024 + 19.336 - 900 - 5.620 = 15.840$$

$$4.800\,p = 15.840 - 14.400 = 1.440 \;\Rightarrow\; p = \frac{1.440}{4.800} = 0{,}30 = 30\%$$

Collections from 2019 sales: $19.200 \times 0{,}30 + 9 \times 1.120 = 5.760 + 10.080 = 15.840$ m.u.; pending at 31/12: $3 \times 1.120 = 3.360$ m.u.

#### Step 4. Titanium consumed

$$\text{Consumption} = 1.200 + 3.000 \times 1{,}50 + 2.000 \times 1{,}50 - 900 \times 1{,}50 = 1.200 + 4.500 + 3.000 - 1.350 = 7.350 \text{ m.u.}$$

#### Step 5. Depreciation

$$D_{\text{machinery}} = \frac{6.000}{10} = 600 \quad \left(\text{check: } 3 \text{ years} \times 600 = 1.800 \text{ at } 31/12/2018 \;\checkmark\right)$$

$$D_{\text{CNC}} = \frac{4.800 - 480}{8} \times \frac{9}{12} = 540 \times \frac{9}{12} = 405, \qquad D_{2019} = 600 + 405 = 1.005 \text{ m.u.}$$

#### Step 6. Financial items

$$I_{\text{old loan}} = 66 \text{ (Step 1)}, \qquad I_{\text{CNC loan}} = 3.600 \times 0{,}05 \times \frac{9}{12} = 135 \text{ (accrued, paid 01/04/2020)}$$

$$\text{Financial expenses} = 66 + 135 = 201, \qquad \text{Financial income (dividend received)} = 80 \text{ m.u.}$$

#### Step 7. Income Statement 2019

| Line | Computation | m.u. |
| :--- | :--- | ---: |
| Sales revenue | $2.400 \times 8$ | 19.200 |
| − Titanium consumed | Step 4 | 7.350 |
| − Personnel (salaries and Social Security) | $12 \times (400 + 120)$ | 6.240 |
| − General expenses | $12 \times 150$ | 1.800 |
| − Bad debt loss | item II | 160 |
| − Depreciation | Step 5 | 1.005 |
| **= Income from operations** | $19.200 - 16.555$ | **2.645** |
| + Financial income | dividend from AEROPIEZAS | 80 |
| − Financial expenses | Step 6 | 201 |
| **= Profit before taxes** | $2.645 + 80 - 201$ | **2.524** |
| − Corporation tax (30%) | $0{,}30 \times 2.524$ | 757,20 |
| **= Net profit** | $2.524 - 757{,}20$ | **1.766,80** |

## (b) Prepare the balance sheet at 24:00 on 31 December 2019 [1.25 pts]

### Hint

From the 3.024 m.u. of 23:00, only the tax and the dividend leave before 24:00. Split each debt by its due date; the new loan is repaid in 2022.

### Checkpoint

- Dividends 883,40; reserves 1.983,40 m.u.; cash 1.383,40 m.u.
- Owners equity 9.483,40 (subscribed 8.000, uncalled −500).
- Non-current liabilities 4.200; current liabilities 3.405; total 17.088,40 m.u.

### Solution

#### Step 1. Closing operations

$$\text{Dividends} = 0{,}50 \times 1.766{,}80 = 883{,}40, \qquad \text{to reserves} = 883{,}40 \;\Rightarrow\; \text{Reserves} = 1.100 + 883{,}40 = 1.983{,}40$$

$$\text{Cash}_{24:00} = 3.024 - 757{,}20 - 883{,}40 = 1.383{,}40 \text{ m.u.}$$

#### Step 2. Old loan after 2019

$1.800 - 600 = 1.200$ m.u.: 600 due in 2020 (current) and 600 in 2021 (non-current).

#### Step 3. Balance sheet at 24:00 on 31/12/2019

| Assets | m.u. | Liabilities and owners equity | m.u. |
| :--- | ---: | :--- | ---: |
| Land | 2.000 | Subscribed capital (4.000 shares × 2) | 8.000 |
| Machinery ($6.000 - 2.400$) | 3.600 | − Uncalled capital | (500) |
| CNC centre ($4.800 - 405$) | 4.395 | Reserves | 1.983,40 |
| Financial shares in AEROPIEZAS S.A. | 1.000 | **Owners equity** | **9.483,40** |
| **Non-current assets** | **10.995** | Bank loan for the CNC (01/04/2022) | 3.600 |
| Stock of titanium (900 kg × 1,50) | 1.350 | Old loan, part due in 2021 | 600 |
| Accounts receivable | 3.360 | **Non-current liabilities** | **4.200** |
| Cash | 1.383,40 | Old loan, part due in 2020 | 600 |
| | | Interest payable (CNC loan) | 135 |
| | | Suppliers of titanium (01/02/2020) | 2.250 |
| | | Social Security payable | 120 |
| | | General expenses payable | 300 |
| **Current assets** | **6.093,40** | **Current liabilities** | **3.405** |
| **Total assets** | **17.088,40** | **Total liabilities and equity** | **17.088,40** |

## (c) Compute ROA and ROE of 2019 [0.5 pts]

### Hint

Year-end balance; income from operations for ROA, net profit for ROE.

### Checkpoint

- ROA = 15,48%; ROE = 18,63% (extension).

### Solution

$$\text{ROA} = \frac{2.645}{17.088{,}40} = 15{,}48\%, \qquad \text{ROE} = \frac{1.766{,}80}{9.483{,}40} = 18{,}63\%$$

## (d) Effect of charging 50% in cash with a 4% discount; which case gives more profit and which more cash? [0.75 pts]

### Hint

The discount lowers revenue; the higher cash share brings collections forward. Then follow the change through the tax and the dividend, both paid at the closing.

### Checkpoint

- Revenue 18.816 (−384); net profit 1.498 (−268,80); dividends 749 (−134,40).
- Collections from 2019 sales 16.416 (+576); receivables 2.400 (−960).
- Cash at 24:00: 2.209 (+825,60). Profit higher with the present policy; cash higher with the new policy.

### Solution

#### Step 1. New revenue and collections

$$\text{Revenue} = 0{,}50 \times 19.200 \times 0{,}96 + 0{,}50 \times 19.200 = 9.216 + 9.600 = 18.816 \text{ m.u.} \;(-384)$$

$$\text{Collections} = 9.216 + 9 \times 800 = 16.416 \;(+576), \qquad \text{Receivables} = 3 \times 800 = 2.400 \;(-960)$$

#### Step 2. Results and closing

$$\text{Profit before taxes} = 2.524 - 384 = 2.140, \qquad \text{Tax} = 0{,}30 \times 2.140 = 642, \qquad \text{Net profit} = 1.498$$

$$\text{Dividends} = 0{,}50 \times 1.498 = 749, \qquad \text{Reserves} = 1.100 + 749 = 1.849$$

$$\text{Cash}_{24:00} = (3.024 + 576) - 642 - 749 = 2.209 \text{ m.u.}$$

#### Step 3. Changes in the statements

| Item | Present policy | New policy | Change |
| :--- | ---: | ---: | ---: |
| Revenue | 19.200 | 18.816 | −384 |
| Corporation tax | 757,20 | 642 | −115,20 |
| Net profit | 1.766,80 | 1.498 | −268,80 |
| Accounts receivable | 3.360 | 2.400 | −960 |
| Cash at 24:00 | 1.383,40 | 2.209 | +825,60 |
| **Total assets** | **17.088,40** | **16.954** | **−134,40** |
| Reserves | 1.983,40 | 1.849 | −134,40 |
| **Total liabilities and equity** | **17.088,40** | **16.954** | **−134,40** |

**Discussion.** The **profit is higher with the present policy**: the discount is a real cost of 384 m.u. (269 m.u. after tax). The **cash is higher with the new policy**: 576 m.u. more are collected in 2019 because more of each sale is charged at once, and the lower profit also means less tax and fewer dividends paid at the closing. The discount buys liquidity at the price of profitability; it is worth it only if the company needs the cash or if the money collected earlier earns more than the discount costs.

## Interpretation

- **Dimensional check:** units × m.u./unit, kg × m.u./kg and m.u./year × months/12 all give m.u.; $p$ and the ratios are dimensionless.
- **Why the bank balance is enough:** all the other flows are fixed by the terms of the contracts, so the cash balance determines the single unknown term, the share of cash sales.
- **Uncalled capital:** the 500 m.u. not disbursed are a debt of the shareholders to the company, not cash; showing them as a deduction keeps equity at the money actually contributed.
- **Typical mistakes:** paying the CNC loan interest in 2019, depreciating the CNC for 12 months, counting the dividend received as revenue from operations, and treating the bad debt as a collection.

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
