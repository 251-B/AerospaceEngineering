---
materia: Fluid Mechanics
tema: "Topic 6: Dimensional Analysis"
tags:
  - problema-examen
  - analisis-dimensional
  - teorema-pi
  - semejanza-fisica
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-06-dimensional-analysis/problemas/DA9.pdf"
id: "da9"
pill: "DA9: Propeller"
sheets:
  - 9
tags_html:
  - "Π theorem"
  - "Reynolds and Mach"
  - "Standard atmosphere"
---

# Problem DA9: Power of an Airplane Propeller

> Official dimensional-analysis sheet of the course (exam of Jan 10, 2012), statement transcribed from the sheet, solution after its handwritten key. Part of [[Topic 6 - Dimensional Analysis]].
> Method: Π theorem with the speed of sound as a governing parameter (Notes.pdf, Eq. 6.25 and p. 66: compressible gas) and full physical similarity (Eqs. 6.57-6.59).

## Statement

The power $W$ needed to move the propeller of a small airplane depends on the airplane velocity $V$, propeller diameter $D$, angular velocity $\Omega$, and also on the air properties, including its density $\rho$, viscosity $\mu$, and sound velocity $c$; the latter, characterizing compressibility effects, has dimensions $[c] = LT^{-1}$. Assuming that the effect of gravity is negligible:

1. Use dimensional analysis to express the propeller power $W$ as a function of the minimum number of dimensionless parameters.

A new airplane with propeller of diameter $D = 1.5$ m is to be designed to fly at an altitude $z = 5000$ m with cruise velocity $V = 300$ Km/h and propeller angular velocity $\Omega = 2500$ rpm. To determine the needed power, an experimental model is to be tested in a wind tunnel at sea level ($z = 0$ m).

2. Determine the model diameter $D_e$, the propeller angular velocity $\Omega_e$, and the wind-tunnel velocity $V_e$ needed to guarantee that the experiment provides a physically similar representation of the airplane flight conditions.

3. For the values of $D_e$, $\Omega_e$, and $V_e$ determined above, the power measured in the experiment (obtained as the product of $\Omega_e$ and the torque acting on the propeller shaft) is $W_e = 6\times 10^7$ Watt. Obtain the power $W$ corresponding to the real airplane.

Note: Physical properties for air according to the standard atmosphere:

| $z$ (m) | $T$ (K) | $\rho$ (kg/m$^3$) | $\mu$ (kg/(m s)) | $c$ (m/s) |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 288.15 | 1.225 | $1.775\times 10^{-5}$ | 340.3 |
| 5000 | 255.65 | 0.736 | $1.630\times 10^{-5}$ | 320.5 |

The value $D = 1.5$ m is written by hand on the printed sheet, next to "$D$".

Source: DA9.pdf (page 1, exam of Jan 10, 2012, statement and handwritten key). Notes.pdf, Chapter 6: Π theorem, Eq. 6.25; physical similarity, Eqs. 6.57-6.59.

## Hypotheses, Data and Dimensional Table

- Air is a compressible gas: its compressibility enters through the speed of sound $c$ (Notes.pdf, p. 66). Gravity is negligible.
- Prototype at $z = 5000$ m: $\rho = 0.736$ kg/m$^3$, $\mu = 1.630\times 10^{-5}$ kg/(m s), $c = 320.5$ m/s. Model at $z = 0$: $\rho_e = 1.225$ kg/m$^3$, $\mu_e = 1.775\times 10^{-5}$ kg/(m s), $c_e = 340.3$ m/s.

| Parameter | Dimensions |
| :--- | :--- |
| $W$ (unknown) | $ML^2T^{-3}$ |
| $\rho$ | $ML^{-3}$ |
| $\mu$ | $ML^{-1}T^{-1}$ |
| $c$, $V$ | $LT^{-1}$ |
| $D$ | $L$ |
| $\Omega$ | $T^{-1}$ |

## Application of the Π Theorem

$$ W = W(\rho, \mu, c, V, D, \Omega) $$

$n = 6$; $(\rho, V, D)$ have independent dimensions ($\det = -1$, as in DA1), so $n - k = 3$ groups remain.

- **Power.** $[W] = [\rho][V]^3[D]^2$ (exponents as in DA1): $\Pi_0 = W/(\rho V^3 D^2)$.
- **Viscosity.** $[\mu] = [\rho][V][D]$: the Reynolds number $\rho V D/\mu$.
- **Speed of sound.** $[c] = [V]$: the inverse Mach number $V/c$ is the group.
- **Rotation.** $[\Omega] = [V][D]^{-1}$: the group $\Omega D/V$ (the inverse of the advance ratio).

$$ \frac{W}{\rho V^3 D^2} = f\left(\frac{\rho V D}{\mu}, \frac{V}{c}, \frac{\Omega D}{V}\right) $$

## Physical Similarity at Sea Level

The three groups must be equal. The Mach number fixes the tunnel speed:

$$ \frac{V}{c} = \frac{V_e}{c_e} \;\Longrightarrow\; V_e = \frac{c_e}{c}\,V = \frac{340.3}{320.5}\times 300 = 1.0618\times 300 = 318.5\ \text{km/h} \simeq 319\ \text{km/h} $$

The Reynolds number then fixes the diameter:

$$ \frac{\rho V D}{\mu} = \frac{\rho_e V_e D_e}{\mu_e} \;\Longrightarrow\; D_e = \frac{\mu_e}{\mu}\,\frac{\rho}{\rho_e}\,\frac{V}{V_e}\,D = \frac{\mu_e}{\mu}\,\frac{\rho}{\rho_e}\,\frac{c}{c_e}\,D $$

$$ D_e = \frac{1.775}{1.630}\times\frac{0.736}{1.225}\times\frac{320.5}{340.3}\times 1.5 = 1.0890\times 0.6008\times 0.9418\times 1.5 = 0.924\ \text{m} $$

The advance ratio fixes the rotation:

$$ \frac{\Omega D}{V} = \frac{\Omega_e D_e}{V_e} \;\Longrightarrow\; \Omega_e = \frac{D}{D_e}\,\frac{V_e}{V}\,\Omega = \frac{1.5}{0.924}\times 1.0618\times 2500 = 1.6229\times 1.0618\times 2500 = 4308\ \text{rpm} $$

The ratios $V/V_e$, $\Omega/\Omega_e$ are dimensionless, so km/h and rpm can be kept.

## Power of the Airplane

With the three groups equal, $W/(\rho V^3 D^2)$ is equal:

$$ \frac{W}{\rho V^3 D^2} = \frac{W_e}{\rho_e V_e^3 D_e^2} \;\Longrightarrow\; W = \frac{\rho}{\rho_e}\left(\frac{V}{V_e}\right)^3\left(\frac{D}{D_e}\right)^2 W_e $$

$$ W = 0.6008\times(0.9418)^3\times(1.6229)^2\times 6\times 10^{7} = 0.6008\times 0.8354\times 2.6338\times 6\times 10^{7} = 7.93\times 10^{7}\ \text{W} $$

## Answers and Checks

- Reduced law: $W/(\rho V^3D^2) = f\left(\rho VD/\mu,\, V/c,\, \Omega D/V\right)$.
- Model: $D_e = 0.924$ m, $V_e = 319$ km/h, $\Omega_e = 4308$ rpm.
- Airplane power: $W = 7.9\times 10^7$ W.
- Dimensions: as in DA1, $\rho V^3D^2$ is a power; $V/c$ and $\Omega D/V$ are pure numbers.
- Why the model is smaller: sea-level air is denser ($\rho_e/\mu_e = 6.9\times 10^4$ s/m$^2$ against $4.5\times 10^4$ at 5000 m), so the same Reynolds number needs a smaller diameter; the faster tunnel speed (same Mach in warmer air) helps too.
- On the data: the given $W_e = 6\times 10^7$ W is far above the real power of a small propeller (of order $10^5$ W); the conversion factor $W/W_e = 1.32$ does not depend on it.
- Check against the official key: DA9.pdf gives $D_e = 0.924$ m, $V_e = 319$ km/h, $\Omega_e = 4308$ rpm and $W = 7.9\times 10^7$ W, the same results.
