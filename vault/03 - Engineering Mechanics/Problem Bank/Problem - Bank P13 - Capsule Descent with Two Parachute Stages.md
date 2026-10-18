---
materia: Engineering Mechanics
tema: "Unit 2: equations of motion with a velocity-dependent force, quadratures and work-energy"
bank_id: P13
title: "Capsule descent under quadratic drag with two parachute stages: terminal speed, quadratures and the work of drag"
category: midterm_problem
archetype: dynamics
level: standard
unit: 2
difficulty: 2
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2011 to 2019); not an official exercise. Verified with scripts/mechanics/p13.py"
tags:
  - problem-bank
  - midterm-1
  - quadratic-drag
  - terminal-velocity
  - separation-of-variables
  - work-energy
---

# Bank P13 — Capsule descent with two parachute stages

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §4.3 (equations of motion and their integration), §4.4 (power and work) and §4.5 (mechanical energy). The quadratic drag law is a model given in the statement. Every equation and number was checked with SymPy and with a numerical integration.

## Statement

In a drop test, a capsule of mass $m$ is released **from rest** from a hovering helicopter at the point $O$ and falls vertically. Its drogue parachute is open from the release: the air exerts on the capsule the drag $-c_1v^2$ along the motion, where $v=\dot y\ge0$ is the speed and $y$ the distance fallen, measured **downward** from $O$. When the speed reaches $v_1$, the main parachute opens instantaneously and the drag becomes $-c_2v^2$, with $c_2\gg c_1$. Gravity $g$ is uniform and points down; buoyancy and the variation of air density with height are neglected.

![[attachments/EM-M1/p13-two-stage-descent.svg]]

## Setup

- Data: $m=1000$ kg, $g=9.81$ m s$^{-2}$. The parachutes are given by their terminal speeds: $v_{t1}=50$ m s$^{-1}$ (drogue) and $v_{t2}=8$ m s$^{-1}$ (main). The main parachute opens at $v_1=40$ m s$^{-1}$.
- Hypotheses: point particle, vertical motion (released with no horizontal velocity, no wind), constant drag coefficients within each stage, instantaneous opening.
- The time of stage 2 is counted from the opening, and $\Delta y$ is the distance fallen since the opening.

## (a) Degrees of freedom, forces and equation of motion [1.0 pts]

How many degrees of freedom has the capsule? Write the forces and the equation of motion for $v$.

### Hint

The drag opposes the velocity: in vector form it is $-c|\mathbf v|\mathbf v$.

### Checkpoint

- 1 degree of freedom, $y(t)$, positive downward.
- $m\dot v=mg-cv^2$ (for $v\ge0$).

### Solution

#### Step 1. Count

With no horizontal force and no horizontal initial velocity the motion is along the vertical: 1 degree of freedom, the coordinate $y$, with unit vector $\mathbf e_y$ pointing **down**.

#### Step 2. Forces and Newton

Weight $mg\,\mathbf e_y$ (positive: it points down). Drag $-c|\mathbf v|\mathbf v=-cv^2\,\mathbf e_y$ for $v\ge0$ (upward). Newton (Notes §4.3), with $\mathbf a=\dot v\,\mathbf e_y$:

$$m\dot v=mg-cv^2$$

## (b) Terminal speed and $v(t)$ in stage 1 [2.0 pts]

Define the terminal speed $v_t$ and integrate the equation for the drogue stage, from rest at $t=0$, to get $v(t)$ and $y(t)$.

### Hint

Separate variables: $\dfrac{dv}{1-v^2/v_t^2}=g\,dt$. Check the antiderivative by differentiating it.

### Checkpoint

- $v_t=\sqrt{mg/c}$, i.e. $c=mg/v_t^2$; $\ c_1=3.924$ kg m$^{-1}$.
- $\displaystyle\int\frac{dv}{1-v^2/v_t^2}=v_t\,\text{artanh}\frac{v}{v_t}$ for $v<v_t$.
- $v=v_t\tanh\dfrac{gt}{v_t}$, $\ y=\dfrac{v_t^2}{g}\ln\cosh\dfrac{gt}{v_t}$.

### Solution

#### Step 1. Terminal speed

The acceleration vanishes when $mg=cv^2$: $v_t=\sqrt{mg/c}$. With it the equation reads $\dot v=g\big(1-v^2/v_t^2\big)$. For the drogue, $c_1=mg/v_{t1}^2=9810/2500=3.924$ kg m$^{-1}$.

#### Step 2. Separation of variables

For $0\le v<v_t$:

$$\frac{dv}{1-v^2/v_t^2}=g\,dt$$

The antiderivative of the left side is $F(v)=v_t\,\text{artanh}(v/v_t)$. Check with the chain rule: $\dfrac{dF}{dv}=v_t\cdot\dfrac{1}{1-(v/v_t)^2}\cdot\dfrac{1}{v_t}=\dfrac{1}{1-v^2/v_t^2}$.

#### Step 3. Limits (Barrow's rule)

Integrating from $(t=0,v=0)$ to $(t,v)$:

$$\Big[v_t\,\text{artanh}\frac{v'}{v_t}\Big]_0^{v}=\big[g\,t'\big]_0^{t}\ \Longrightarrow\ v_t\,\text{artanh}\frac{v}{v_t}-0=gt\ \Longrightarrow\ v=v_t\tanh\frac{gt}{v_t}$$

Since $\tanh<1$, $v$ approaches $v_t$ but never reaches it in finite time.

#### Step 4. Position

$y=\int_0^tv\,dt'$. With $w=\cosh(gt'/v_t)$, $dw=\dfrac{g}{v_t}\sinh(gt'/v_t)\,dt'$, so $\tanh(gt'/v_t)\,dt'=\dfrac{v_t}{g}\dfrac{dw}{w}$ and

$$y=v_t\cdot\frac{v_t}{g}\big[\ln w\big]_{w=1}^{w=\cosh(gt/v_t)}=\frac{v_t^2}{g}\ln\cosh\frac{gt}{v_t}$$

## (c) Speed as a function of the distance fallen [1.5 pts]

Obtain $v(y)$ for stage 1 directly from the equation of motion, without using $t$.

### Hint

$\dot v=\dfrac{dv}{dy}\dfrac{dy}{dt}=v\dfrac{dv}{dy}$. Then substitute $w=1-v^2/v_t^2$.

### Checkpoint

- $v\dfrac{dv}{dy}=g\Big(1-\dfrac{v^2}{v_t^2}\Big)$.
- $v^2=v_t^2\Big(1-e^{-2gy/v_t^2}\Big)$.

### Solution

#### Step 1. Chain rule

With $v=v(y(t))$: $\dot v=\dfrac{dv}{dy}\dot y=v\dfrac{dv}{dy}$, so $v\dfrac{dv}{dy}=g\big(1-v^2/v_t^2\big)$ and, separating, $\dfrac{v\,dv}{1-v^2/v_t^2}=g\,dy$.

#### Step 2. Substitution

$w=1-v^2/v_t^2$, $dw=-\dfrac{2v}{v_t^2}dv$, so $v\,dv=-\dfrac{v_t^2}{2}dw$. Limits: $v=0\mapsto w=1$, $v\mapsto w=1-v^2/v_t^2$:

$$-\frac{v_t^2}{2}\int_1^{1-v^2/v_t^2}\frac{dw}{w}=-\frac{v_t^2}{2}\Big[\ln w\Big]_1^{1-v^2/v_t^2}=-\frac{v_t^2}{2}\ln\Big(1-\frac{v^2}{v_t^2}\Big)=g\,y$$

#### Step 3. Result

$$v^2=v_t^2\Big(1-e^{-2gy/v_t^2}\Big)$$

Cross-check: inserting $y(t)$ of (b), $e^{-2gy/v_t^2}=\cosh^{-2}(gt/v_t)$ and $1-\cosh^{-2}=\tanh^2$, which is $v(t)^2/v_t^2$ of (b).

## (d) Numbers for the drogue stage [1.5 pts]

If the main parachute never opened, how long and how far would the capsule fall before reaching $95\,\%$ of $v_{t1}$? When and where does it actually reach $v_1=40$ m s$^{-1}$?

### Hint

Invert the formulas of (b) and (c).

### Checkpoint

- $t_{95}=\dfrac{v_{t1}}{g}\text{artanh}\,0.95=9.336$ s; $\ y_{95}=\dfrac{v_{t1}^2}{2g}\ln\dfrac{1}{1-0.95^2}=296.6$ m.
- $v_1=0.8\,v_{t1}$ is reached at $t_1=5.600$ s, $y_1=130.2$ m.

### Solution

#### Step 1. $95\,\%$ of the terminal speed

$v_{t1}/g=50/9.81=5.097$ s and $\text{artanh}\,0.95=\tfrac12\ln(1.95/0.05)=1.8318$, so $t_{95}=9.336$ s. From (c), $y=-\dfrac{v_t^2}{2g}\ln\big(1-v^2/v_t^2\big)$ with $v_t^2/2g=127.4$ m and $\ln(1/0.0975)=2.3279$: $y_{95}=296.6$ m.

#### Step 2. Opening of the main parachute

$\text{artanh}\,0.8=\tfrac12\ln9=1.0986$, so $t_1=5.097\cdot1.0986=5.600$ s, and $y_1=127.4\cdot\ln(1/0.36)=127.4\cdot1.0217=130.2$ m. A numerical integration of the equation of motion gives the same values.

## (e) Stage 2: the main parachute [2.0 pts]

At the opening $v_1>v_{t2}$. Find the acceleration just after the opening, solve for $v(t)$ in stage 2, and compute the time and the distance needed to come down to $1.05\,v_{t2}$. Why can the formula of (b) not be used?

### Hint

The same antiderivative, valid for $v>v_t$, is $v_t\,\text{arcoth}(v/v_t)$, with $\text{arcoth}\,x=\tfrac12\ln\dfrac{x+1}{x-1}$.

### Checkpoint

- $c_2=153.3$ kg m$^{-1}$; $\dot v(0^+)=g\big(1-v_1^2/v_{t2}^2\big)=-24\,g=-235.4$ m s$^{-2}$ (a **deceleration**; drag $245.3$ kN against a weight of $9.81$ kN).
- $v=v_{t2}\coth\Big(\dfrac{gt}{v_{t2}}+\text{arcoth}\dfrac{v_1}{v_{t2}}\Big)$, decreasing towards $v_{t2}$ from above.
- To $8.4$ m s$^{-1}$: $t=1.349$ s, $\Delta y=17.80$ m.

### Solution

#### Step 1. Acceleration at the opening

$c_2=mg/v_{t2}^2=9810/64=153.3$ kg m$^{-1}$ ($c_2/c_1=39.06$). Just after the opening $v=40$ m s$^{-1}$, so $\dot v=g\big(1-(40/8)^2\big)=-24g=-235.4$ m s$^{-2}$: the drag $c_2v_1^2=245.3$ kN is 25 times the weight.

#### Step 2. Why not $\tanh$

The formula $v=v_t\tanh(\dots)$ is bounded by $v_t$, so it can never start at $v_1=5v_{t2}$; equivalently the constant of integration would be $\text{artanh}\,5$, which is not real. For $v>v_t$ the antiderivative of $1/(1-v^2/v_t^2)$ is $v_t\,\text{arcoth}(v/v_t)$: $\dfrac{d}{dv}\big[v_t\,\text{arcoth}(v/v_t)\big]=\dfrac{1}{1-v^2/v_t^2}$, the same derivative as $\text{artanh}$ on the other branch.

#### Step 3. Integration

From $(t=0,v=v_1)$ to $(t,v)$:

$$\Big[v_{t2}\,\text{arcoth}\frac{v'}{v_{t2}}\Big]_{v_1}^{v}=\big[g\,t'\big]_0^t\ \Longrightarrow\ v=v_{t2}\coth\Big(\frac{gt}{v_{t2}}+\text{arcoth}\frac{v_1}{v_{t2}}\Big)$$

$\coth>1$ and decreases, so $v$ decreases monotonically to $v_{t2}$ from above.

#### Step 4. Time to $1.05\,v_{t2}$

$t=\dfrac{v_{t2}}{g}\Big(\text{arcoth}\,1.05-\text{arcoth}\,5\Big)$, with $\text{arcoth}\,1.05=\tfrac12\ln41=1.8568$ and $\text{arcoth}\,5=\tfrac12\ln1.5=0.2027$: $t=0.8155\cdot1.6541=1.349$ s.

#### Step 5. Distance

As in (c), $\dfrac{v\,dv}{1-v^2/v_{t2}^2}=g\,dy$, now integrated from $(\Delta y=0,\ v=v_1)$ to $(\Delta y,\ v)$. Substitute $w=1-v'^2/v_{t2}^2$, $dw=-\dfrac{2v'}{v_{t2}^2}dv'$, so $v'\,dv'=-\dfrac{v_{t2}^2}{2}dw$; the limits become $w_1=1-v_1^2/v_{t2}^2=-24$ and $w=1-v^2/v_{t2}^2$. In stage 2 $v'>v_{t2}$, so $w<0$ on the whole interval and the antiderivative of $1/w$ is $\ln|w|$ (not $\ln w$):

$$g\,\Delta y=-\frac{v_{t2}^2}{2}\int_{w_1}^{w}\frac{dw'}{w'}=-\frac{v_{t2}^2}{2}\Big[\ln|w'|\Big]_{w_1}^{w}=-\frac{v_{t2}^2}{2}\big(\ln|w|-\ln|w_1|\big)=\frac{v_{t2}^2}{2}\ln\frac{|w_1|}{|w|}$$

With $|w_1|=(v_1^2-v_{t2}^2)/v_{t2}^2$ and $|w|=(v^2-v_{t2}^2)/v_{t2}^2$ the factors $v_{t2}^2$ cancel in the quotient; solving for $\Delta y$ and, inversely, for $v^2$:

$$v^2=v_{t2}^2+\big(v_1^2-v_{t2}^2\big)e^{-2g\Delta y/v_{t2}^2},\qquad \Delta y=\frac{v_{t2}^2}{2g}\ln\frac{v_1^2-v_{t2}^2}{v^2-v_{t2}^2}$$

With $v=8.4$ m s$^{-1}$: $\Delta y=3.262\cdot\ln(1536/6.56)=3.262\cdot5.456=17.80$ m.

## (f) Work of the drag and energy balance [2.0 pts]

Is the mechanical energy conserved? Compute the work done by the drag (i) in stage 1, from the release to the opening, and (ii) in stage 2, from the opening to $v=8.4$ m s$^{-1}$, from the energy balance; then check (ii) by integrating the drag force along the path.

### Hint

$\Delta E_{kin}=W_{weight}+W_{drag}$ with $W_{weight}=mg\,\Delta y$. For the direct integral use $v^2(y)$ of (e) and $c_2v_{t2}^2=mg$.

### Checkpoint

- No: the drag power $-cv^3<0$ dissipates energy ($9.81$ MW just after the opening).
- (i) $W_{drag,1}=\tfrac12mv_1^2-mgy_1=800.0-1277.1=-477.1$ kJ.
- (ii) $W_{drag,2}=\tfrac12m(8.4^2-40^2)-mg\Delta y=-764.7-174.6=-939.3$ kJ; the direct integral gives $-\big(mg\Delta y+\tfrac12m(v_1^2-v^2)\big)$, the same.

### Solution

#### Step 1. Energy is not conserved

The power of the drag is $(-cv^2\,\mathbf e_y)\cdot(v\,\mathbf e_y)=-cv^3<0$ (Notes §4.4): it removes mechanical energy as long as the capsule moves. Only the weight is conservative ($V=-mgy$ with $y$ downward), so $\dfrac{d}{dt}\big(\tfrac12mv^2-mgy\big)=-cv^3$. At the opening the dissipated power is $c_2v_1^3=153.3\cdot64\,000$ W $=9.81$ MW.

#### Step 2. Stage 1

From $v=0$, $y=0$ to $v_1=40$ m s$^{-1}$, $y_1=130.2$ m: $\Delta E_{kin}=\tfrac12\cdot1000\cdot1600=800.0$ kJ and $W_{weight}=mgy_1=1277.1$ kJ, so $W_{drag,1}=800.0-1277.1=-477.1$ kJ.

#### Step 3. Stage 2 from the energy balance

$\Delta E_{kin}=\tfrac12\cdot1000\,(70.56-1600)=-764.7$ kJ and $W_{weight}=9810\cdot17.80=174.6$ kJ, so $W_{drag,2}=-764.7-174.6=-939.3$ kJ: in under $18$ m the main parachute absorbs almost twice what the drogue absorbed in $130$ m.

#### Step 4. Direct integral

$W_{drag,2}=-\int_0^{\Delta y}c_2v^2\,ds$ with $v^2=v_{t2}^2+(v_1^2-v_{t2}^2)e^{-2gs/v_{t2}^2}$ and $c_2v_{t2}^2=mg$:

$$W_{drag,2}=-mg\,\Delta y-c_2\big(v_1^2-v_{t2}^2\big)\Big[-\frac{v_{t2}^2}{2g}e^{-2gs/v_{t2}^2}\Big]_0^{\Delta y}=-mg\,\Delta y-\frac m2\big(v_1^2-v_{t2}^2\big)\Big(1-e^{-2g\Delta y/v_{t2}^2}\Big)$$

and by (e), $\big(v_1^2-v_{t2}^2\big)\big(1-e^{-2g\Delta y/v_{t2}^2}\big)=v_1^2-v^2$, so $W_{drag,2}=-\big(mg\Delta y+\tfrac12m(v_1^2-v^2)\big)=-939.3$ kJ, the value of Step 3.

## Interpretation

- **Dimensional check:** $[c]=$ N/(m s$^{-1}$)$^2=$ kg m$^{-1}$, so $\sqrt{mg/c}$ is m s$^{-1}$; $gt/v_t$ and $gy/v_t^2$ are dimensionless (arguments of $\tanh$ and $\exp$); $[cv^3]=$ W.
- **Limits:** for $gt\ll v_t$, $\tanh x\approx x$ gives $v\approx gt$ and $y\approx\tfrac12gt^2$ (free fall); for $t\to\infty$ both $\tanh$ and $\coth$ tend to 1 and $v\to v_t$, from below in stage 1 and from above in stage 2; $y\approx v_t t-\tfrac{v_t^2}{g}\ln2$ for large $t$ in stage 1.
- **Common mistakes in the exam:** (1) writing the drag as $+cv^2$ or $-cv$ (wrong sign or wrong law); (2) using $v=v_t\tanh(\dots)$ after the main parachute opens, which would need $\text{artanh}$ of a number larger than 1; (3) skipping the chain rule $\dot v=v\,dv/dy$; (4) assuming the terminal speed is reached in a finite time; (5) writing energy conservation with drag acting.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
