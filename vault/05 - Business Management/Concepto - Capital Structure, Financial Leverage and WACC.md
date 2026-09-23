---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
tags:
  - teoria
  - concepto-clave
  - business-management
  - finanzas-corporativas
dificultad: media
prerrequisitos: []
---

# 📖 Concept: Capital Structure, Financial Leverage and WACC

> **Core Intuition in One Sentence:** The capital structure combines equity and debt to fund corporate assets, where debt amplifies equity returns through financial leverage at the expense of higher default risk, and the Weighted Average Cost of Capital (WACC) sets the minimum hurdle rate for project viability.

---

## 🎯 1. Fundamental Rationale: The Cost of Capital

Every financial resource utilized by an enterprise bears a financial cost:
1. **Explicit Cost of Debt ($K_L$):**
   * The contractual interest rate that lenders, bondholders, and banks demand to compensate for the time value of money and credit default risk.
2. **Implicit Cost of Equity ($K_{EQ}$):**
   * The **opportunity cost** demanded by shareholders. Equity investors do not receive a guaranteed contractual interest payment; instead, they require an expected return equivalent to what they could earn on an alternative investment of comparable financial risk.
   * Because equity absorbs residual losses first in liquidation, equity risk is strictly higher than debt risk:
     $$K_{EQ} > K_L$$

---

## 📐 2. Mathematical Formulations & Leverage Ratios

Let $E$ denote Total Equity and $L$ denote Total Liabilities (Total Debt). Total Financing Capital is given by $V = E + L$.

### Financial Weightings:
$$\text{Equity Weight } (w_e) = \frac{E}{E + L}, \qquad \text{Debt Weight } (w_d) = \frac{L}{E + L}$$
$$w_e + w_d = 1$$

### The Debt-to-Equity Ratio (Financial Leverage):
$$\mathbf{\text{Debt-to-Equity (D/E)}} = \frac{L}{E}$$

* **Economic Interpretation:** Measures the proportion of debt financing per monetary unit of equity.
* **Low D/E ($< 0.5$):** Highly conservative financial structure, low risk of distress, but leaves potential financial leverage unexploited.
* **High D/E ($> 1.5$):** High financial leverage. During economic expansions, Return on Equity ($\text{ROE}$) is magnified; during downturns, rigid fixed debt servicing burdens rapidly push the company toward insolvency.

---

## ⚖️ 3. The Weighted Average Cost of Capital (WACC)

The **Weighted Average Cost of Capital ($K_{WACC}$)** represents the composite minimum return a firm must generate on its aggregate asset base to satisfy all capital providers (shareholders and creditors).

### Standard Formula (Course Slide 37):
$$\mathbf{K_{WACC} = K_{EQ} \cdot \left(\frac{E}{E + L}\right) + K_L \cdot \left(\frac{L}{E + L}\right)}$$

### Extended Corporate Finance Formula (with Tax Shield):
Because debt interest expenses are tax-deductible in corporate income statements, the effective after-tax cost of debt is $K_L(1 - t)$:
$$\mathbf{K_{WACC} = K_{EQ} \cdot \left(\frac{E}{E + L}\right) + K_L(1 - t) \cdot \left(\frac{L}{E + L}\right)}$$
where:
* $K_{EQ}$: Cost of Equity.
* $K_L$: Pre-tax Cost of Debt.
* $E$: Market or Book Value of Total Equity.
* $L$: Market or Book Value of Total Debt (Liabilities).
* $t$: Corporate income tax rate (e.g., $30\%$).

---

## 🏢 4. Comprehensive Taxonomy of Financing Instruments

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       CORPORATE FINANCING ALTERNATIVES                      │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ 1. INTERNAL EQUITY (Self-Financing)  │ • Retained earnings from net profit  │
│                                      │ • Non-cash depreciation reserves     │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ 2. EXTERNAL EQUITY (Share Capital)   │ • Common Stock (acciones ordinarias) │
│                                      │ • Capital increases (Rights-issues)  │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ 3. LONG-TERM DEBT (Maturity > 1 yr)  │ • Corporate Bonds & Debentures       │
│                                      │ • Long-term bank loans               │
│                                      │ • Financial Leasing (arrendamiento)  │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ 4. SHORT-TERM DEBT (Maturity ≤ 1 yr) │ • Trade Credit (Accounts Payable)    │
│                                      │ • Bank Credit Lines (revolving)      │
│                                      │ • Commercial Bill Discounting        │
│                                      │ • Factoring (monetizing receivables) │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### Critical Instrument Characteristics:
* **Corporate Bonds:** Marketable debt securities where the firm acts as the borrower and institutional investors act as lenders. The firm pays regular **coupons** (interest) and redeems the face value principal at **maturity**.
* **Bank Loan vs Credit Line:**
  * *Loan:* Fixed lump-sum; interest accrued on full loan amount from day one.
  * *Credit Line:* Flexible credit ceiling; interest accrued only on the actual amount drawn, with a low maintenance fee on the undrawn portion.
* **Leasing (Finance vs Operating):**
  * *Finance Lease:* Long-term, non-cancellable, transfers substantial risks and rewards of ownership to lessee; includes a bargain purchase option.
  * *Operating Lease:* Shorter-term, cancellable rental where lessor provides maintenance.
* **Commercial Paper Discount:** Endorsing promissory notes to banks before maturity. Bank deducts interest rate and commission in advance:
  $$\text{Cash Received} = \text{Nominal Face Value} - \text{Discount Interest} - \text{Commissions}$$
* **Factoring:** Selling accounts receivable to a specialized factor. In **non-recourse factoring**, the factor assumes total credit default risk, insulating the firm from customer insolvency.

---

## ⚠️ 5. Strategic Hurdle Rate in Project Appraisal
> [!IMPORTANT] Investment Decision Rule
> In corporate investment decisions (Topic 4 preview):
> * A capital expenditure project creates economic value if and only if:
>   $$\text{Expected Project Return (IRR)} > K_{WACC}$$
> * If a project earns less than $K_{WACC}$, executing the project destroys shareholder wealth, even if the project yields a positive accounting profit.

---

## 🔗 Related Notes
* `[[05 - Business Management/Tema 3 - Financial Management I - Financial Statements|Topic 3: Financial Management (I)]]`
* `[[05 - Business Management/Concepto - Financial Statements (Income Statement and Balance Sheet)|Concept: Financial Statements]]`
* `[[05 - Business Management/Formulario - Business Management and Financial Analysis|Formula Sheet: Financial Ratios]]`
* `[[05 - Business Management/Gestion de Empresas MOC|Back to Business Management MOC]]`
