---
title: "Problem Set - Rigid Body Official Key"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Official answers (transcription)"
language: "English"
tags:
  - problems
  - rigid-body
  - official-key
---

# Rigid Body Problems: Official Key (transcription)

Word-for-word transcription of the answers that `Problems.pdf` prints for the rigid body problems (section 2), PDF pages 77 to 81. It is the reference used by the "Check against the official key" step of each solution in the problems of [[Problem Set - Topic 6 Rigid Body Kinematics and Inertia]], [[Problem Set - Topic 7 Rigid Body Momentum, Energy and Dynamics]] and [[Problem Set - Topic 8 Constraints, Rolling, Multibody and Torque-Free Motion]]. Nothing here is solved or corrected: a discrepancy between a worked solution and this key is discussed in that solution. Page numbers are PDF page indices. Subject index: [[Engineering Mechanics MOC]].

A problem marked "no answer" has its number printed in the key with nothing after it, or does not appear at all.

## RB-01 (Problems.pdf, p. 77)

$v_{min} = v_0$. $\boldsymbol{\omega}_{B/0} = (v_0/a)\,\mathbf{j}$. The IAR exists and is the line with direction $\mathbf{e}_\omega \equiv \mathbf{j}$ that passes through point A.

## RB-02 (Problems.pdf, p. 77)

$$\boldsymbol{\omega}_{B/0} = \dot\theta\left(\mathbf{i}_B - \sin\theta\,\mathbf{j}_B - \cos\theta\,\mathbf{k}_B\right) = \dot\theta\left(\cos\theta\,\mathbf{i} - \sin\theta\,\mathbf{j} - \mathbf{k}\right).$$

$$\mathbf{v}_0^P = \frac{a}{\cos^2\theta}\,\dot\theta\,\mathbf{j}.$$

## RB-03 (Problems.pdf, p. 77)

Some partial results are:

$$\boldsymbol{\omega}_{B0} = \mathbf{i}\left(\dot\theta\sin\gamma\sin\beta + \dot\gamma\cos\beta\right) + \mathbf{j}\left(\dot\theta\cos\gamma + \dot\beta\right) + \mathbf{k}\left(\dot\theta\sin\gamma\cos\beta - \dot\gamma\sin\beta\right)$$

$$= \mathbf{i}_B\left(\dot\gamma\cos\theta + \dot\beta\sin\theta\sin\gamma\right) + \mathbf{j}_B\left(\dot\theta + \dot\beta\cos\gamma\right) + \mathbf{k}_B\left(\dot\gamma\sin\theta - \dot\beta\sin\gamma\cos\theta\right)$$

$$\boldsymbol{\alpha}_{B0} = \mathbf{i}\left[\dot\theta\left(\dot\gamma\cos\gamma\sin\beta + \dot\beta\cos\beta\sin\gamma\right) + \ddot\gamma\cos\beta - \dot\gamma\dot\beta\sin\beta\right]$$

$$+ \mathbf{j}\left[\ddot\beta - \dot\theta\dot\gamma\sin\gamma\right] + \mathbf{k}\left[\dot\theta\left(\dot\gamma\cos\gamma\cos\beta - \dot\beta\sin\beta\sin\gamma\right) - \ddot\gamma\sin\beta - \dot\gamma\dot\beta\cos\beta\right]$$

$$= \mathbf{i}_B\left[\dot\beta\left(\dot\theta\cos\theta\sin\gamma + \dot\gamma\cos\gamma\sin\theta\right) + \ddot\gamma\cos\theta - \dot\gamma\dot\theta\sin\theta + \ddot\beta\sin\theta\sin\gamma\right]$$

$$+ \mathbf{j}_B\left[\ddot\beta\cos\gamma - \dot\gamma\dot\beta\sin\gamma\right]$$

$$+ \mathbf{k}_B\left[\ddot\gamma\sin\theta + \dot\theta\dot\gamma\cos\theta - \ddot\beta\sin\gamma\cos\theta - \dot\beta\left(\dot\gamma\cos\gamma\cos\theta - \dot\theta\sin\theta\sin\gamma\right)\right]$$

## RB-04 (Problems.pdf, p. 77)

For the letter T, we first consider a frame $S_0$, whose $y$ axis is the vertical symmetric line and the $x$ axis coincides with the bottom line of the upper rectangle. The center of mass is located in $S_0$ as

$$\mathbf{r}_0^G = \frac{wt - (h-t)^2}{2(w+h-t)}\,\mathbf{j}.$$

In the frame with origin on $G$, we have

$$I_{Gx} = \frac{\sigma}{3}\left[wt^3 + (h-t)^3 t\right] - mr^2, \quad r = -\frac{wt - (h-t)^2}{2(w+h-t)},$$

$$I_{Gy} = \frac{\sigma t}{12}\left[w^3 + (h-t)t^2\right].$$

The product of inertia $P_{xz,yz}$ is zero.

## RB-05 (Problems.pdf, pp. 77-78)

**(a)** The radius of the "slender" bar is negligible.

$$\overline{\overline{I}}_G = \frac{mL^2}{12}\begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

**(b)**

$$\overline{\overline{I}}_G = \frac{m}{12}\begin{bmatrix} 3R^2 + L^2 & 0 & 0 \\ 0 & 3R^2 + L^2 & 0 \\ 0 & 0 & 6R^2 \end{bmatrix}$$

**(c)**

$$\overline{\overline{I}}_G = \frac{m}{12}\begin{bmatrix} b^2 + c^2 & 0 & 0 \\ 0 & a^2 + c^2 & 0 \\ 0 & 0 & a^2 + b^2 \end{bmatrix}$$

**(d)**

$$\overline{\overline{I}}_G = \frac{2mR^2}{5}\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

**(e)** (Problems.pdf, p. 78)

$$\overline{\overline{I}}_G = mR^2\begin{bmatrix} 2/5 - 9/64 & 0 & 0 \\ 0 & 2/5 - 9/64 & 0 \\ 0 & 0 & 2/5 \end{bmatrix}$$

**(f)** (Problems.pdf, p. 78)

$$\overline{\overline{I}}_G = \frac{3m}{80}\begin{bmatrix} 8R^2 & 0 & 0 \\ 0 & 4R^2 + L^2 & 0 \\ 0 & 0 & 4R^2 + L^2 \end{bmatrix}$$

**(g)** (Problems.pdf, p. 78)

$$\overline{\overline{I}}_G = \frac{mR^2}{4}\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}$$

## RB-06 (Problems.pdf, p. 78)

The IAR passes point I that can be located from G by $\boldsymbol{GI} = -L(\boldsymbol{i}_B + \sqrt{2}\boldsymbol{k}_B)/2$ and it has the same direction as the angular velocity $\boldsymbol{\omega}_{B0} = \Omega(\sqrt{2}\boldsymbol{i}_B - \boldsymbol{k}_B)$.

$$ T_0 = \frac{M\Omega^2 L^2}{8}(8B + 4D - 8\sqrt{2}E + 9) \ . $$

$$ \boldsymbol{H}_{G,0} = M\Omega L^2[(\sqrt{2}B - E)\boldsymbol{i}_B - F\boldsymbol{j}_B + (\sqrt{2}E - D)\boldsymbol{k}_B] \ . $$

$$ \boldsymbol{H}_{A,0} = M\Omega L^2[(\sqrt{2}B - E)\boldsymbol{i}_B - F\boldsymbol{j}_B + (\sqrt{2}E - D + 3/4)\boldsymbol{k}_B] \ . $$

## RB-07 (Problems.pdf, p. 78)

Mordor ($\mathcal{M}$) exerts a force on The Ring ($\mathcal{R}$) that can be written as:

$$ \boldsymbol{F}_{\mathcal{M}} = \int_{\mathcal{R}} \beta \boldsymbol{r}_0^P \, dm = \beta \boldsymbol{r}_0^G M . $$

The moment exerted by Mordor on The Ring about G can be written as:

$$ \boldsymbol{M}_{G_{\mathcal{M}}} = \int_{\mathcal{R}} \boldsymbol{r}_B^P \times \beta \boldsymbol{r}_0^P \, dm = \beta \int_{\mathcal{R}} \boldsymbol{r}_B^P \times \left(\boldsymbol{r}_0^G + \boldsymbol{r}_B^P\right) dm = \beta \int_{\mathcal{R}} \boldsymbol{r}_B^P \times \boldsymbol{r}_0^G \, dm = \beta \int_{\mathcal{R}} \boldsymbol{r}_B^P \, dm \times \boldsymbol{r}_0^G = 0 . $$

## RB-08 (Problems.pdf, p. 78)

The EOM for 2 DOF are

$$ m\ddot{y}_G = -mg - k\left(y_G + \frac{\sqrt{3}\,a\cos\theta}{3}\right) , $$

$$ ma\ddot{\theta} = 4\sqrt{3}\,k\left(y_G\sin\theta + 2a\cos\theta\right) . $$

The equation to solve the reaction force from the vertical line $R$ (defined positive in $\boldsymbol{i}$ direction) is

$$ R = ak\left(2 - \frac{\sqrt{3}\sin\theta}{3}\right) . $$

The 4 initial conditions required to solve the EOM are

$$ t = 0 \rightarrow y_G = \frac{\sqrt{3}}{6} , \quad \dot{y}_G = v_0, \quad \theta = 0, \quad \dot{\theta} = -\frac{\sqrt{3}\,u_0}{a} . $$

At equilibrium for $\theta = \pi/4$, we have

$$ y_G = -2a , \quad k = \frac{mg}{a\left(2 - \sqrt{6}/6\right)} , \quad R = ka\left(2 - \frac{\sqrt{6}}{6}\right) . $$

After fixing the position of G, the linearized EOM for the perturbation $\phi$

$$ \ddot{\phi} + \frac{8\sqrt{6}\,k}{m}\phi = 0 , $$

which is a harmonic oscillator with the natural frequency being $\Omega = \sqrt{8\sqrt{6}\,k/m}$ .

## RB-09

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-10 (Problems.pdf, p. 79)

The EOM is $L\dot{\theta}^2/2 - g\cos\theta = C$, with $C$ a constant to be determined by IC.

## RB-11 (Problems.pdf, p. 79)

The vector basis $B_1\{\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$ is defined as: $\mathbf{k}_1 \parallel \mathbf{k}$; $\mathbf{i}_1$ is parallel to the perpendicular axis of the disk, from the axis $Oz$ to the disc; $\mathbf{j}_1 = \mathbf{k}_1 \times \mathbf{i}_1$. The angular velocity and acceleration of the disk is $\boldsymbol{\omega}_{B0} = \omega(-\mathbf{i}_1 + \mathbf{k}_1)$ and $\boldsymbol{\alpha}_{B0} = -\omega^2\mathbf{j}_1$. The acceleration of the contact point $C$ is $\mathbf{a}_0^{C(B)} = \omega^2 R(\mathbf{i}_1 + \mathbf{k}_1)$.

## RB-12

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-13 (Problems.pdf, p. 79)

For $\mu = 0$,

$$6\dot{x} + \dot{\theta}R\sin\theta = 6\omega R \quad , \quad 24\dot{x}^2 + 13\dot{\theta}^2R^2 + 8\dot{x}\dot{\theta}R\sin\theta - 8gR\sin\theta = 37\omega^2R^2$$

For $\mu \to \infty$,

$$\dot{\theta}^2R(37 - 8\sin\theta) - 8g\sin\theta = 37\omega^2R \ .$$

## RB-14

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-15

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-16

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-17 (Problems.pdf, p. 79)

The only forces that appear on the fork-disc system arise from the collar joint and the weight of both disk and fork. From the equations of motion in basis $B_2$ it can be noticed that for the disk alone the angular momentum with respect to $\boldsymbol{i}_2$ is conserved. Therefore, one of the quadratures of the problem is:

$$\dot{\phi} = C_1. \tag{7}$$

Furthermore, mechanical energy is conserved due to the fact that $(i)$ the resultant reaction force at the collar does not work since $\boldsymbol{F}\cdot\boldsymbol{v}_0^{O_1} = 0$, and $(ii)$ because the resultant torque has no component along the direction of $\boldsymbol{\omega}_{21}$, the resultant reaction torque does not work either. $(iii)$ Last but not least the other forces present are the disk and fork respective weights, which are conservative forces.

This provide with the following conservation law:

$$\dot{\theta}^2\left(\frac{I_2}{2} + \frac{mR^2}{8} + \frac{mb^2}{2}\right) + \dot{\phi}^2\left(\frac{mR^2}{4}\right) - (mb + Ma)\,g\cos\theta = C_2. \tag{8}$$

The resultant reaction force and torque that the axis $AB$ applies on the fork-disc system at $O_1$ is $\boldsymbol{R}_{O_1} = \left[\ddot{\theta}\,(Ma + mb) + g\sin\theta\,(M + m)\right]\boldsymbol{i}_2 - \left[\dot{\theta}^2\,(Ma + mb) + g\cos\theta\,(M + m)\right]\boldsymbol{k}_2$ and $\boldsymbol{Q}_{O_1} = -\dfrac{mR^2}{2}\dot{\phi}\dot{\theta}\boldsymbol{k}_2$, respectively.

The resultant (internal) reaction force and torque that the axis $CD$ applies on the disk at $O$ is $\boldsymbol{R}_O = \left(mb\ddot{\theta} + mg\sin\theta\right)\boldsymbol{i}_2 - \left(mb\dot{\theta}^2 + mg\cos\theta\right)\boldsymbol{k}_2$ and $\boldsymbol{Q}_O = \dfrac{mR^2}{4}\ddot{\theta}\boldsymbol{j}_2 - \dfrac{mR^2}{2}\dot{\phi}\dot{\theta}\boldsymbol{k}_2$, respectively.

## RB-18 (Problems.pdf, p. 79)

We define $\xi = \dot x_G$, $\eta = \dot y_G$, $\boldsymbol\omega_{B0} = \omega_x\mathbf i + \omega_y\mathbf j + \omega_z\mathbf k$.

For rolling with slip, there are 5 DOF. The EOM are

$$\dot\xi = \frac{-\mu g(\xi - a\omega_y)}{\sqrt{(\xi - a\omega_y)^2 + (\eta + a\omega_x)^2}} \quad , \quad \dot\eta = \frac{-\mu g(\eta + a\omega_x)}{\sqrt{(\xi - a\omega_y)^2 + (\eta + a\omega_x)^2}} \quad ,$$

$$2a\dot\omega_x = 5\dot\eta \quad , \quad 2a\dot\omega_y = -5\dot\xi \quad , \quad \dot\omega_z = 0 \quad .$$

For rolling without slip, there are 3 DOF. The problem can be reduced to quadratures as

$$\xi = a\omega_y = C_1 \quad , \quad \eta = -a\omega_x = C_2 \quad , \quad \omega_z = C_3 \quad ,$$

with the constants to be determined by IC.

The ball hits the pocket with velocity and angular velocity being

$$\mathbf v_0^G = \frac{2\xi_0}{\sqrt 5}\,\mathbf i \quad , \quad \boldsymbol\omega_{B0} = \frac{\xi_0}{a}\left(\frac{11}{4} - \sqrt 5\right)\mathbf j \quad .$$

---

## RB-19

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-20 (Problems.pdf, p. 80)

The length $L$ required to achieve the final angular velocity $\omega_f$ is

$$L^2 = \frac{(I + mR^2)(\omega_0 - \omega_f)}{m(\omega_0 + \omega_f)} \quad .$$

The tension is

$$T = \frac{2KI\omega_0^3 t}{R\left(1 + K\omega_0^2 t^2\right)^2} \quad , \quad \text{with} \quad K = \frac{mR^2}{I + mR^2} \quad .$$

---

## RB-21

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-22

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-23

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-24

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-25 (Problems.pdf, p. 80)

This problem has 4 DOF. To solve the motion of the cylinder, it requires 8 equations to solve for the 8 *unknowns* $x_G$, $y_G$, $z_G$, $\beta$, $\theta$, $\varphi$, $T_C$, and $T_D$. In this case, the *unknown coordinates* have to be solved together with the *unknown reaction forces*. The constraint equations can not be decoupled from the Newton ordinary differential equations.

$$ (\cos\theta\cos\beta - x_G/l)^2 + (\cos\theta\sin\beta - y_G/l)^2 + (\sin\theta + z_G/l)^2 = 1 $$

$$ (\cos\theta\cos\beta + x_G/l)^2 + (3 - \cos\theta\sin\beta - y_G/l)^2 + (\sin\theta - z_G/l)^2 = 1 $$

$$ T\boldsymbol{i} : m\ddot{x}_G = (T_C - T_D)\cos\theta\cos\beta - (T_C + T_D)x_G/l $$

$$ T\boldsymbol{j} : m\ddot{y}_G = (T_C - T_D)\cos\theta\sin\beta - (T_C + T_D)y_G/l + 3T_D $$

$$ T\boldsymbol{k} : m\ddot{z}_G = -mg + (T_D - T_C)\sin\theta - (T_C + T_D)z_G/l $$

$$ R\boldsymbol{i}_2 : \ddot{\varphi} - \ddot{\beta}\sin\theta - \dot{\beta}\dot{\theta}\cos\theta = 0 \rightarrow \dot{\varphi} - \dot{\beta}\sin\theta = \text{const.} $$

$$ \begin{aligned} R\boldsymbol{j}_2 : ml^2\left[\ddot{\theta}\mu - \dot{\beta}^2(\lambda - \mu)\cos\theta\sin\theta + \dot{\beta}\dot{\varphi}\lambda\cos\theta\right] &= (T_D - T_C)\left(x_G\sin\theta\cos\beta + y_G\sin\theta\sin\beta + z_G\cos\theta\right) - 3T_D l\sin\theta\sin\beta \end{aligned} $$

$$ \begin{aligned} R\boldsymbol{k}_2 : ml^2\left[\ddot{\beta}\mu\cos\theta - \dot{\beta}\dot{\theta}(2\mu - \lambda)\sin\theta - \dot{\theta}\dot{\varphi}\lambda\right] &= (T_D - T_C)\left(x_G\sin\beta - y_G\cos\beta\right) + 3T_D l\cos\beta \end{aligned} $$

If the body-fixed vector basis is used to decompose the equations for rotation, it leads to:

$$ \begin{aligned} ml^2\lambda\alpha_{x_B} &= 0 \quad \Rightarrow \dot{\beta}\sin\theta - \dot{\varphi} = \text{const} \\ ml^2\mu\alpha_{y_B} - ml^2(\mu - \lambda)\omega_{x_B}\omega_{z_B} &= -(T_1 - T_2)\left[x_G(\cos\beta\sin\theta\cos\varphi + \sin\beta\sin\varphi) + y_G(\sin\beta\sin\theta\cos\varphi - \cos\beta\sin\varphi) + z_G\cos\theta\cos\varphi\right] - 3T_2 l(\sin\beta\sin\theta\cos\varphi - \cos\beta\sin\varphi) \\ ml^2\mu\alpha_{z_B} + ml^2(\mu - \lambda)\omega_{x_B}\omega_{y_B} &= (T_1 - T_2)\left[x_G(\cos\beta\sin\theta\sin\varphi - \sin\beta\cos\varphi) + y_G(\sin\beta\sin\theta\sin\varphi + \cos\beta\cos\varphi) + z_G\cos\theta\sin\varphi\right] + 3T_2 l(\sin\beta\sin\theta\sin\varphi + \cos\beta\cos\varphi) , \end{aligned} $$

with $T_1 = T_C$ and $T_2 = T_D$. Conservation of mechanical energy gives

$$ \frac{m}{2}\left(\dot{x}_G^2 + \dot{y}_G^2 + \dot{z}_G^2\right) + \frac{ml^2}{2}\left[\lambda\left(\dot{\varphi} - \dot{\beta}\sin\theta\right)^2 + \mu\dot{\theta}^2 + \mu\left(\dot{\beta}\cos\theta\right)^2\right] + mgz_G = \text{const.} $$

## RB-26 (Problems.pdf, pp. 80-81)

The EOM of the system is

$$\frac{425}{64}\,md^2\dot\theta^2 + 5mg\,\frac{\sqrt{2}-1}{4}\,d(1-\sin\theta) = 5mg\,\frac{\sqrt{2}-1}{4}\,d\,.$$

There are two equilibrium positions, given by $\theta = \pi/2$ and $\theta = -\pi/2$. After expanding about the stable equilibrium $\theta = \pi/2$ as $\theta = \pi/2 + \delta$ with $\delta \ll 1$, the EOM reads:

$$\frac{425}{64}\,md^2\dot\delta^2 + 5mg\,\frac{\sqrt{2}-1}{4}\,\frac{d\delta^2}{2} = E\,,$$

whose angular frequency is

$$\sqrt{\frac{8g}{85d}\left(\sqrt{2}-1\right)}$$

## RB-27 (Problems.pdf, p. 81)

Vector $\mathbf i_1$ is $\mathbf{OG}$ and $\mathbf j_1$ is calculated following the right-hand rule so that $\mathbf k = \mathbf k_1$. Two equations come from projecting Newton's second law along $\mathbf i_1$ and $\mathbf j_1$ so that:

$$-2m\left[\ddot\xi + \dot\theta^2(4L-\xi)\right] = 2mg\cos\theta - k\left[4L-\xi-L\sin(\phi-\theta)-2L\sin\theta\right] - T,$$

$$2m\left[\ddot\theta(4L-\xi) - 2\dot\xi\dot\theta\right] = -2mg\sin\theta - k\left[L\cos(\phi-\theta)-2L\cos\theta\right].$$

Tension can be eliminated using Newton's second law for particle P in the $\mathbf j$ direction:

$$-m\ddot\xi = -mg + T,$$

The third equation is the equation of angular momentum of the block at G about $\mathbf k$. The moment of inertia of the block at G about $\mathbf k$ is $I^G_z = 5mL^2/6$. Only the spring causes a torque about G, so:

$$\frac{5mL^2\ddot\phi}{6} = kL\left[(4L-\xi)\cos(\phi-\theta) - 2L\sin\phi\right] \qquad (9)$$

## RB-28

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-29

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-30 (Problems.pdf, p. 81)

The ellipsoid and the plane are tangent if their normals at $P$ coincide.

## RB-31

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-32

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-33 (Problems.pdf, p. 81)

The smaller wheel will leave the ground when the normal at $P$ is $N_P = 0$. Imposing this condition on the first rotational equation, using the rest of equations to reduce the problem to an equation on $N_P$ and $\dot\psi$,

$$\frac{10(A+3B)}{ma^2}\sqrt{3}\,\dot\psi^2/4 + 9\sqrt{3}\left(27\dot\psi^2/10\right) = 13\,\frac{g}{a} \qquad \Rightarrow \qquad \dot\psi^2_{\max} = \frac{104g}{323\sqrt{3}\,a}$$

## RB-34

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-35

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-36 (Problems.pdf, p. 81)

To obtain the force $\mathbf{F}$ we use the equation of motion of the particle:

$$m\mathbf{a}_0^P = -mg[\sin\gamma\,\mathbf{i}_0 + \cos\gamma\,\mathbf{j}_0] - \mathbf{F}.$$

Hence,

$$\mathbf{F} = -mg[\sin\gamma\,\mathbf{i}_0 + \cos\gamma\,\mathbf{j}_0] - m\mathbf{a}_0^P.$$

## RB-37

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-38

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-39

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-40

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-41

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).

## RB-42

No answer in `Problems.pdf` (PDF pages 77 to 81 checked).
