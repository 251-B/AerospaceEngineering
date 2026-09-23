---
materia: Business Management
tema: "Topic 1: The Firm - Types and Objectives"
tags:
  - teoria
  - concepto-clave
  - business-management
  - gobierno-corporativo
dificultad: media
prerrequisitos: []
---

# 📖 Concept: Legal Forms of Business Ownership and the Agency Problem

> **Core Intuition in One Sentence:** The legal structure of a business defines who owns residual control rights and who bears financial liability, while the modern corporate separation of ownership from control creates the Agency Problem, necessitating robust governance mechanisms.

---

## 🎯 1. Fundamental Rationale & Comparative Taxonomy

Choosing an enterprise's legal form balances four fundamental economic forces:
1. **Financial Liability:** Are personal assets shielded from business creditors?
2. **Access to Capital:** How easily can the firm raise large-scale external equity or debt?
3. **Continuity & Permanence:** Does the enterprise survive the death, withdrawal, or bankruptcy of an owner?
4. **Administrative & Tax Costs:** Is taxation levied at the personal or corporate level, and what regulatory reporting is required?

```
┌─────────────────────────┬───────────────────────┬────────────────────────┬────────────────────────┐
│ Legal Form              │ Ownership & Control   │ Liability of Owners    │ Capital Raising Power  │
├─────────────────────────┼───────────────────────┼────────────────────────┼────────────────────────┤
│ Sole Proprietorship     │ 1 Individual          │ Unlimited (Personal)   │ Very Limited           │
│ General Partnership     │ 2+ Co-owners          │ Unlimited & Joint      │ Moderate (Pooled)      │
│ Limited Partnership/LLP │ General + Limited     │ General: Unlimited     │ Moderate to High       │
│                         │ Partners              │ Limited: Capital only  │                        │
│ Corporation (S.A./Inc.) │ Dispersed Stockholders│ Limited to shares paid │ Immense (Public Markets│
│ Cooperative             │ Member-users          │ Limited to capital     │ Member subscriptions   │
└─────────────────────────┴───────────────────────┴────────────────────────┴────────────────────────┘
```

---

## 🔍 2. Deep Analysis of Legal Forms

### A. Sole Proprietorship (Empresario Individual / Autónomo)
* **Structure:** Unincorporated entity owned, financed, and managed by a single person.
* **Advantages:** Minimal startup costs; full managerial discretion; owner retains 100% of generated profits; transparent single taxation (profits taxed directly via personal income tax); straightforward liquidation.
* **Disadvantages:** **Unlimited personal liability** (creditors can seize personal real estate, savings, and personal property); severe capital constraints; reliance on a single person's cognitive bandwidth and health; lack of legal perpetuity.

### B. Partnerships & Joint Ventures
* **General Partnership (Sociedad Colectiva):** All partners actively manage operations and bear **joint and several unlimited liability** ($\text{Partner Liability} = \infty$). A lawsuit against one partner can target all partners' personal assets.
* **Limited Liability Partnership (LLP) / Sociedad Comanditaria:**
  * *General Partners (Socios Colectivos):* Manage operations, retain executive control, and assume unlimited liability.
  * *Limited Partners (Socios Comanditarios):* Passive financial investors whose liability is strictly capped at their contributed capital.
* **Joint Venture:** A legally formalized contractual or equity association formed by two or more corporate entities to execute a specific, capital-intensive, high-risk aerospace project (e.g., Airbus consortium roots, CFM International between GE and Safran).

### C. The Corporation (Sociedad Anónima — S.A.)
* **Legal Personality:** The corporation is an independent legal entity distinct from its owners, granted legal personhood (it can own property, enter binding contracts, sue, and be sued).
* **Capital Division:** Capital is divided into identical, freely transferable negotiable instruments called **shares (stocks)**.
* **Core Strengths:**
  1. *Limited Liability:* Shareholders cannot lose more than their invested capital:
     $$\text{Maximum Loss} = \text{Initial Share Subscription Price}$$
  2. *Perpetual Succession:* Share transfers or deaths of investors do not disrupt corporate existence.
  3. *Massive Liquidity:* High liquidity via secondary stock markets (e.g., Madrid Stock Exchange, NYSE).
* **Structural Weaknesses:** Double taxation (corporate profit taxed via corporate income tax $t = 30\%$, and distributions taxed again via personal dividend taxes); expensive incorporation; mandatory public disclosure (CNMV/SEC audits).

### D. Cooperative Associations (Sociedades Cooperativas)
* Democratic enterprises governed on the principle of **one member, one vote**, regardless of capital contributed.
* Primary objective is mutual service and economic benefit rather than maximizing external capital returns. Surpluses are returned as cooperative patronage refunds based on member utilization.

---

## ⚖️ 3. The Agency Problem (Separation of Ownership and Control)

In small firms, the owner and manager are the same individual. In modern corporations, millions of dispersed shareholders delegate operational management to hired professional executives.

```
       PRINCIPALS                                              AGENTS
┌─────────────────────────┐                            ┌─────────────────────────┐
│      SHAREHOLDERS       │      Delegates Decision    │   EXECUTIVE MANAGERS    │
│                         ├───────────────────────────►│                         │
│ Objective:              │          Control           │ Objective:              │
│ • Maximize Share Value  │                            │ • High Compensation     │
│ • Long-term Dividends   │◄───────────────────────────┤ • Empire Building/Power │
│ • Prudent Capital Use   │    Information Asymmetry   │ • Job Security / Perks  │
└─────────────────────────┘      & Potential Agency    └─────────────────────────┘
                                       Costs
```

### The Conflict of Interest:
* **Shareholders (Principals):** Bear residual risk and desire the maximization of share price and long-term enterprise valuation.
* **Managers (Agents):** May prioritize short-term personal benefits: excessive executive compensation, luxurious perks, risk-averse strategies to protect personal job tenure, or prestige-driven mergers ("empire building") that destroy shareholder value.
* **Core Causes:**
  1. *Information Asymmetry:* Managers possess daily operational visibility that external shareholders cannot match.
  2. *Dispersed Ownership:* Individual small shareholders lack the financial incentive to monitor management ("free-rider problem").

---

## 🛡️ 4. Corporate Governance Control Mechanisms

To align managerial incentives with shareholder wealth, modern governance deploys four interlocking mechanisms:

### 1. The Board of Directors (Consejo de Administración)
The supreme governing body elected by shareholders to oversee senior management:
* **Executive Directors (Consejeros Ejecutivos):** Senior company managers (CEO, CFO) who sit on the board.
* **Proprietary Directors (Consejeros Dominicales):** Directors representing substantial shareholding blocks.
* **Independent Directors (Consejeros Independientes):** External, impartial professionals chosen for prestige and competence, free from managerial or shareholder conflicts.
* **CNMV Good Governance Recommendations (Spain / IBEX 35):**
  * *Size (Rec. 13):* Board size should ideally range between **10 and 15 members**.
  * *Executive Directors (Rec. 15):* Must constitute a strict minority of the board.
  * *Independent Directors (Rec. 17):* Should represent at least **50% of total board seats** in large listed firms.

### 2. Incentive-Aligned Compensation Contracts
* Structuring executive compensation with a substantial performance-contingent variable component: stock options, restricted stock grants, and multi-year bonuses tied to Return on Invested Capital ($\text{ROIC}$) and Total Shareholder Return ($\text{TSR}$).

### 3. Independent External Financial Audits
* Independent public accounting firms (e.g., Big Four) rigorously audit corporate financial statements to guarantee that reported figures reflect a true and fair view of corporate assets and performance.

### 4. External Market Discipline (Hostile Takeover Threat)
* If managers mismanage corporate assets, share prices drop below fundamental value. Outside corporate raiders or rival firms can launch a **hostile takeover bid**, acquiring control and replacing inefficient management.

---

## 🔗 Related Notes
* `[[05 - Business Management/Tema 1 - The Firm - Types and Objectives|Topic 1: The Firm — Types and Objectives]]`
* `[[05 - Business Management/Practica 1.2 - Corporate Governance and CNMV Good Governance Code|Practice 1.2: Corporate Governance in the IBEX 35]]`
* `[[05 - Business Management/Gestion de Empresas MOC|Back to Business Management MOC]]`
