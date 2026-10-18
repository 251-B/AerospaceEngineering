---
materia: Engineering Mechanics
tema: "Unit 4: Kepler problem, areal velocity, vis-viva and a tangential impulse"
bank_id: C08
title: "Apsidal speeds and a perigee impulse: areal velocity, vis-viva and which apse moves"
category: conceptual_question
archetype: central-force
level: conceptual
unit: 4
difficulty: 1
points: 2.0
time_minutes: 15
official: false
origen: "Question written for the bank in the style of the true/false questions of the final exams (MECHANICS_FINALEXAM_2013, 2015 and 2016); not an official exercise. Verified with scripts/mechanics/c08.py"
tags:
  - problem-bank
  - midterm-1
  - kepler
  - vis-viva
  - orbital-manoeuvre
---

# Bank C08 — Apsidal speeds and a perigee impulse

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the true/false questions of the final exams. Method: Notes §4.8.1 (central force motion), §8.1 to §8.4 (Kepler's laws) and §8.5 (vis-viva equation). Every number was checked with SymPy.

## Statement

A satellite moves about the Earth (gravitational parameter $\mu$, the Earth's centre $F$ fixed at a focus) on a Kepler ellipse of eccentricity $e=1/3$ and perigee radius $r_p$. $\Pi$ is the perigee and $A$ the apogee; $a$ is the semi-major axis. Decide whether each statement is TRUE or FALSE and justify the answer. A verdict without a justification scores nothing.

![[attachments/EM-M1/c08-perigee-impulse.svg]]

## (a) Speeds and areal velocity [1.0 pts]

Statement: "The speed at perigee is twice the speed at apogee; consequently the radius vector $\mathbf r$ from $F$ to the satellite sweeps area twice as fast when the satellite passes the perigee as when it passes the apogee."

### Hint

At an apse $\mathbf r\perp\mathbf v$, so $h=rv$ there. What is the areal velocity in terms of $h$?

### Checkpoint

- FALSE (the first half is true).
- $r_a=r_p\dfrac{1+e}{1-e}=2r_p$, $a=\tfrac32r_p$; $h=r_pv_p=r_av_a\Rightarrow v_p/v_a=2$. Vis-viva: $v_p^2=\dfrac{4\mu}{3r_p}$, which equals $\dfrac{2\mu}{a}$ only because $a=\tfrac32r_p$ for this orbit; $v_a^2=\dfrac{\mu}{3r_p}$.
- Areal velocity $\dot A=\tfrac12|\mathbf r\times\mathbf v|=h/2$: the same at every point of the orbit (Kepler's second law).

### Solution

#### Step 1. Geometry of the ellipse

With $r_p=a(1-e)$ and $r_a=a(1+e)$: $a=\dfrac{r_p}{1-1/3}=\dfrac32r_p$ and $r_a=\dfrac32r_p\cdot\dfrac43=2r_p$.

#### Step 2. Speeds at the apsides

The force is central, so $\mathbf h=\mathbf r\times\mathbf v$ is constant (Notes §4.8.1). At both apsides $\mathbf r\perp\mathbf v$, hence $h=r_pv_p=r_av_a$ and $\dfrac{v_p}{v_a}=\dfrac{r_a}{r_p}=2$. The vis-viva equation $v^2=\mu\big(\tfrac2r-\tfrac1a\big)$ (Notes §8.5) confirms it:

$$v_p^2=\mu\Big(\frac{2}{r_p}-\frac{2}{3r_p}\Big)=\frac{4\mu}{3r_p},\qquad v_a^2=\mu\Big(\frac{2}{2r_p}-\frac{2}{3r_p}\Big)=\frac{\mu}{3r_p},\qquad \frac{v_p^2}{v_a^2}=4$$

#### Step 3. Areal velocity

The area swept per unit time is $\dot A=\tfrac12|\mathbf r\times\mathbf v|=\tfrac12h$, a constant: at perigee $\tfrac12r_pv_p$, at apogee $\tfrac12(2r_p)\,\tfrac{v_p}{2}=\tfrac12r_pv_p$, the same. The satellite is faster near perigee precisely because it is closer, so that $rv$ stays fixed. The conclusion is wrong: FALSE.

## (b) A tangential impulse at perigee [1.0 pts]

At $\Pi$ a short engine burn along the velocity raises the speed from $v_p$ to $v_p'=\sqrt{9/8}\,v_p$ (an increase of about $6.07\,\%$) without changing the position. Statement: "The perigee radius is unchanged and the apogee radius grows from $2r_p$ to $3r_p$."

### Hint

After the burn $\mathbf r\perp\mathbf v$ still holds at $\Pi$. Compute the new energy and angular momentum, and find the radii where $\dot r=0$ from $\varepsilon=\dfrac{h^2}{2r^2}-\dfrac{\mu}{r}$.

### Checkpoint

- TRUE.
- $v_p'^2=\tfrac98\cdot\dfrac{4\mu}{3r_p}=\dfrac{3\mu}{2r_p}>\dfrac{\mu}{r_p}$ (above circular speed, so $\Pi$ stays the perigee).
- $\varepsilon'=-\dfrac{\mu}{4r_p}$, $a'=2r_p$; $h'^2=\tfrac32\mu r_p$; the apse equation $\varepsilon'=\dfrac{h'^2}{2r^2}-\dfrac{\mu}{r}$ has roots $r=r_p$ and $r=3r_p$; $e'=1/2$.

### Solution

#### Step 1. The burn point remains an apse

The impulse changes $\mathbf v$ along its own direction, so right after it $\mathbf v'\perp\mathbf r$ at $r=r_p$: the radial velocity is zero and $\Pi$ is an apse of the new orbit. Since $v_p'^2=\dfrac{3\mu}{2r_p}$ exceeds the circular value $\mu/r_p$, the satellite is moving too fast to stay at $r_p$ and rises: $\Pi$ is the **perigee** of the new orbit.

#### Step 2. New energy and angular momentum

$$\varepsilon'=\frac{v_p'^2}{2}-\frac{\mu}{r_p}=\frac{3\mu}{4r_p}-\frac{\mu}{r_p}=-\frac{\mu}{4r_p}\ \Rightarrow\ a'=-\frac{\mu}{2\varepsilon'}=2r_p,\qquad h'^2=r_p^2v_p'^2=\tfrac32\mu r_p$$

#### Step 3. Apse radii

At an apse $v=h'/r$, so $\varepsilon'=\dfrac{h'^2}{2r^2}-\dfrac{\mu}{r}$. Multiplying by $r^2$: $-\dfrac{\mu}{4r_p}r^2+\mu r-\dfrac34\mu r_p=0$, i.e. $r^2-4r_pr+3r_p^2=(r-r_p)(r-3r_p)=0$. The perigee stays at $r_p$ and the new apogee $A'$ is at $3r_p$ (consistent with $r_p+r_a'=2a'=4r_p$), with $e'=\dfrac{3r_p-r_p}{3r_p+r_p}=\dfrac12$. The statement is TRUE.

## Interpretation

- **Dimensional check:** $\mu$ is m$^3$ s$^{-2}$, so $\mu/r$ is m$^2$ s$^{-2}$ (a speed squared and a specific energy); $h^2/\mu$ is a length.
- **Limits:** a burn that brings $v_p'^2$ to $2\mu/r_p$ gives $\varepsilon'=0$ and an escape parabola ($r_a'\to\infty$); a retrograde burn to $v_p'^2<\mu/r_p$ would turn $\Pi$ into the new **apogee**.
- **Common mistakes in the exam:** (1) confusing a constant areal velocity with a constant speed (or the reverse); (2) thinking that a burn raises the point where it is applied, instead of the opposite apse; (3) forgetting that a tangential burn keeps the burn point an apse.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
