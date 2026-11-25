---
materia: "Advanced Maths"
tema: "Tema 6: The Heat Equation, Sturm-Liouville Problems and Fourier Series"
origen: "probls_ch6_2627.pdf - Exercise 7"
dificultad: media
id: "e7"
pill: "Orthogonality proofs"
tags:
  - problema-resuelto
  - orthogonality
  - fourier-series
---

# Problem 6.7: Orthogonality Relations of Sine and Cosine Families

> Official exercise 7 of the sheet `probls_ch6_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 6]]. Method and notation: [[Topic 6 - Heat Equation, Sturm-Liouville Problems and Fourier Series]].

## Statement

Show that the functions $y_n(x)=\sin\left(\frac{n\pi x}{L}\right)$ satisfy
$$\int_{-L}^{L}y_n(x)y_m(x)\,dx=\begin{cases}0,&n\ne m,\\ L,&n=m,\end{cases}\qquad m,n=0,1,2,\dots$$
Show that a similar property holds for $u_n(x)=\cos\left(\frac{n\pi x}{L}\right)$:
$$\int_{-L}^{L}u_n(x)u_m(x)\,dx=\begin{cases}0,&n\ne m,\\ L,&n=m\ne0,\\ 2L,&n=m=0,\end{cases}\qquad m,n=0,1,2,\dots$$

## Tools: Product-to-Sum Identities and One Basic Integral

From $\cos(A\mp B)=\cos A\cos B\pm\sin A\sin B$ (subtract and add):

$$\sin A\sin B=\tfrac12\left[\cos(A-B)-\cos(A+B)\right],\qquad\cos A\cos B=\tfrac12\left[\cos(A-B)+\cos(A+B)\right].$$

Basic integral. For an integer $k$, put $I_k=\int_{-L}^{L}\cos\frac{k\pi x}{L}\,dx$.

- If $k\ne0$, the antiderivative is $\frac{L}{k\pi}\sin\frac{k\pi x}{L}$ and by Barrow's rule $I_k=\frac{L}{k\pi}\left[\sin k\pi-\sin(-k\pi)\right]=\frac{2L\sin k\pi}{k\pi}=0$, since $\sin k\pi=0$ for integer $k$.
- If $k=0$, $I_0=\int_{-L}^{L}dx=[x]_{-L}^{L}=2L$.

So $I_k=2L\,\delta_{k0}$.

## Sines

Take $A=\frac{n\pi x}{L}$, $B=\frac{m\pi x}{L}$:

$$\int_{-L}^{L}y_ny_m\,dx=\tfrac12\left[I_{n-m}-I_{n+m}\right].$$

- **$n\ne m$:** $n-m\ne0$ gives $I_{n-m}=0$; $n+m\ge1$ (the pair cannot be $(0,0)$) gives $I_{n+m}=0$. The integral is $0$.
- **$n=m\ge1$:** $I_0=2L$ and $I_{2n}=0$ (as $2n\ne0$), so the integral is $\tfrac12(2L-0)=L$.
- **Edge case $n=m=0$:** here $y_0(x)=\sin0=0$ identically, so $\int_{-L}^{L}0\,dx=0$. The formula $\frac12[I_0-I_0]=0$ confirms it. Therefore the value $L$ holds only for $n=m\ge1$ (and $y_0$ is the zero function, not a genuine eigenfunction). Likewise if exactly one of $n,m$ is $0$, the integrand is $0$ and the result $0$ agrees with the case $n\ne m$.

## Cosines

$$\int_{-L}^{L}u_nu_m\,dx=\tfrac12\left[I_{n-m}+I_{n+m}\right].$$

- **$n\ne m$:** $I_{n-m}=0$, $I_{n+m}=0$ ($n+m\ge1$), so $0$.
- **$n=m\ge1$:** $\tfrac12\left[I_0+I_{2n}\right]=\tfrac12(2L+0)=L$.
- **$n=m=0$:** $u_0=1$, and directly $\int_{-L}^{L}1\,dx=2L$ (in the formula $\tfrac12[I_0+I_0]=2L$).

## Result and Checks

> [!result] Orthogonality
> $$\int_{-L}^{L}\sin\frac{n\pi x}{L}\sin\frac{m\pi x}{L}dx=L\,\delta_{nm}\ (n,m\ge1),\qquad\int_{-L}^{L}\cos\frac{n\pi x}{L}\cos\frac{m\pi x}{L}dx=\begin{cases}L\,\delta_{nm},&n\ \text{or}\ m\ge1,\\2L,&n=m=0.\end{cases}$$
> These are the relations behind the coefficient formulas $a_n=\frac1L\int f\cos$ and $b_n=\frac1L\int f\sin$ ([[Problem - Ch6-P5 Fourier Series of Nine Functions]]; Haberman, Sec. 3.3).

Checks. Dimensions: $[y_n]$ is dimensionless, so the integral has dimension of $L$ ✓. Limiting check $L=\pi$, $n=m=1$: $\int_{-\pi}^{\pi}\sin^2x\,dx=\int\frac{1-\cos2x}{2}dx=\pi$ ✓. The two parity facts are also visible directly: $\sin\cdot\sin$ is even in $x$, so the integral is twice $\int_0^L$ and the same Barrow evaluations give the same numbers.
