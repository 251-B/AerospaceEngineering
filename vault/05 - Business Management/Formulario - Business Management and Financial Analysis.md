---
materia: Business Management
tema: "Topics 1-3 Summary"
fuentes:
  - "Topic 3_Financial Management (I).pdf (Prof. Carmen Paz-Aparicio, UC3M)"
  - "T3_Financial Statements_EXERCISES.pdf (UC3M)"
tags:
  - formulario
  - prontuario
  - business-management
  - finanzas
dificultad: media
---

# 📋 Formula Sheet: Business Management and Financial Analysis

> **Quick Reference Guide:** Mathematical equations, accounting identities, linear depreciation formulas, financial structure leverage ratios, and the Weighted Average Cost of Capital (WACC).

---

## 1. Accounting Identities & Financial Statements

### The Fundamental Balance Sheet Identity:
$$\mathbf{\text{Assets} \equiv \text{Liabilities} + \text{Equity}}$$
$$\text{Current Assets} + \text{Non-Current Assets} = \text{Current Liabilities} + \text{Long-Term Liabilities} + \text{Stockholders' Equity}$$

### Stockholders' Equity Identity:
$$\text{Ending Equity} = \text{Contributed Capital} - \text{Uncalled Capital} + \text{Beginning Retained Earnings} + \text{Current Year Net Income} - \text{Dividends}$$

### The Multi-Step Income Statement Relationships:
$$\begin{aligned}
\text{Net Sales Revenue} &= \text{Gross Sales Revenue} - \text{Discounts and Allowances} \\
\text{Cost of Goods Sold (COGS)} &= \text{Beginning Inventory} + \text{Purchases} - \text{Ending Inventory} \\
\text{Gross Profit} &= \text{Net Sales Revenue} - \text{COGS} \\
\text{Operating Income (EBIT)} &= \text{Gross Profit} - \text{Operating Expenses} \\
\text{Operating Expenses} &= \text{Salaries} + \text{Social Security} + \text{Utilities} + \text{Rent} + \text{Depreciation} \\
\text{Earnings Before Taxes (EBT)} &= \text{EBIT} \pm \text{Non-Operating Items (Net Financial Interest)} \\
\text{Corporate Income Taxes } (T) &= t \times \text{EBT} \quad (\text{with standard } t = 0.30) \\
\text{Net Income } (\Pi_{\text{net}}) &= \text{EBT} - T = \text{EBT} \times (1 - t)
\end{aligned}$$

---

## 2. Linear (Straight-Line) Depreciation

$$\mathbf{\text{Annual Depreciation Expense } (D) = \frac{\text{Acquisition Cost} - \text{Residual Value}}{\text{Useful Lifespan in Years } (n)}}$$

$$\text{Quarterly Depreciation } (D_{\text{quarter}}) = \frac{D}{4} = \frac{\text{Acquisition Cost} - \text{Residual Value}}{4n}$$

$$\text{Net Book Value } (\text{NBV}) = \text{Acquisition Cost} - \text{Accumulated Depreciation}$$

*(Note: Land has an infinite useful life and is strictly non-depreciable).*

---

## 3. Cash Flow & Working Capital Accounting

### Treasury Identity (Cash Position):
$$\text{Ending Cash} = \text{Beginning Cash} + \sum \text{Cash Inflows (Collections)} - \sum \text{Cash Outflows (Payments)}$$

### Working Capital (Fondo de Maniobra):
$$\text{Working Capital} = \text{Current Assets} - \text{Current Liabilities}$$

### Average Collection Period & Accounts Receivable:
If annual sales on credit are $S$ and the average collection period is $T_{\text{coll}}$ months:
$$\text{Ending Accounts Receivable} = S \times \frac{T_{\text{coll}}}{12}$$

---

## 4. Financial Structure, Leverage & Cost of Capital

Let $E$ denote Total Equity and $L$ denote Total Liabilities (Total Debt):

### Proportions of Financing:
$$w_e = \frac{E}{E + L} \quad (\% \text{ Equity}), \qquad w_d = \frac{L}{E + L} \quad (\% \text{ Debt})$$
$$w_e + w_d = 1$$

### Debt-to-Equity Ratio (Financial Leverage):
$$\mathbf{\text{D/E Ratio} = \frac{L}{E}}$$

### Profit Distribution Ratios:
$$\text{Pay-out Ratio} = \frac{\text{Dividends}}{\text{Net Income}}$$
$$\text{Self-Financing Ratio (Retention Rate)} = \frac{\text{Retained Earnings}}{\text{Net Income}} = 1 - \text{Pay-out Ratio}$$

### Weighted Average Cost of Capital (WACC):

#### Standard Course Formulation (Slide 37):
$$\mathbf{K_{WACC} = K_{EQ} \cdot \left(\frac{E}{E + L}\right) + K_L \cdot \left(\frac{L}{E + L}\right)}$$

#### Extended Formula with Interest Tax Shield:
$$\mathbf{K_{WACC} = K_{EQ} \cdot \left(\frac{E}{E + L}\right) + K_L(1 - t) \cdot \left(\frac{L}{E + L}\right)}$$
where:
* $K_{EQ}$: Cost of Equity (implicit opportunity cost).
* $K_L$: Cost of Debt (explicit contractual interest rate).
* $t$: Corporate income tax rate (standard $30\%$).

---

## 🔗 Related Notes
* `[[05 - Business Management/Tema 3 - Financial Management I - Financial Statements|Topic 3: Financial Management (I)]]`
* `[[05 - Business Management/Gestion de Empresas MOC|Back to Business Management MOC]]`
