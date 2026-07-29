---
title: enclosure_manuf
tags: [extension/manuf]
created: 2022-03-12T20:30:08.146Z
modified: 2022-06-14T12:26:20.645Z
jupyter: {jupytext: {formats: 'ipynb,md', text_representation: {extension: .md, format_name: markdown, format_version: '1.3', jupytext_version: 1.13.7}}, kernelspec: {display_name: Python 3 (ipykernel), language: python, name: python3}}
---

# Manufactures, Structural Transformation

:::{admonition} Superseded — kept as the historical source
:class: warning

This draft is where the three-sector extension was worked out, and it is retained for
provenance. **It is no longer the reference.** As of 2026-07-29 the material lives in:

| What | Where |
|---|---|
| Derivations, eqs (35)–(43) | `docs/online_appendix.md` §6.4 (mirrored at `content/04-derivations.md` on the site) |
| Exposition and figures | `open-enclose.github.io/content/03-manufacturing.md` |
| Implementation and tests | `open-enclose.github.io/enclose/manufacturing.py` |
| Interpretation and research agenda | `notes/manuf_paper_ideas.md` |

Three errors originating in this draft have been corrected downstream — a missing
governance wedge $A_\mu$, an over-reach from the labor margin to the enclosure margin, and
a backwards statement of the sign of $\partial l_m/\partial t_e$. The corrections have been
applied to the equations and code cells below, but **prefer the appendix**; see
`notes/MANUFACTURING_HANDOFF.md` §3.

This file is jupytext-paired with `enclosure_manuf.ipynb`, which has **not** been synced
since these corrections and therefore still contains the errors.
:::

```python tags=["hide_input"]
%load_ext autoreload
%autoreload 2
```

```python tags=["hide_input"]
from enclose import *
from scipy.optimize import fsolve
```


## Introduction

This extends the model of land enclosures to include a non-agricultural "manufacturing" sector in order to study structural transformation questions.

## A model of enclosures

As before, there is an economy-wide labor force that inelastically supplies labor $\bar L$ to the economy. The total supply of land is $\bar T$, with $T_e$ denoting enclosed land.  $t_e=\frac{T_e}{\bar T}$ is the share of land enclosed.

Laborers can now move between manufacturing and agriculture, and within agriculture between the unenclosed and enclosed sectors. In equilibrium, labor moves until the competitive market wage $w$ it can earn in the "enclosed production" and/or in the manufacturing sectors is also equal to the value average product of (local wage plus land rents) the same labor could earn in the unenclosed sector.


Production on enclosed and unenclosed production sites employs land $T$ and labor $L$ with the following homogenous of degree 1 Cobb-Douglas production technologies:

|                                    |                   |
|:-----------------------------------|:------------------| 
| $p \cdot \theta_M \cdot G(K,L)= {K}^{1-\beta}\cdot L^\beta$  |  Manufacturing sector |     
| $F(T,L)= {T}^{1-\alpha}\cdot L^\alpha$  |  Unenclosed agriculture sector |
| $\theta \cdot F(T,L)$  |  Enclosed agriculture sector|


Labor moves between manufacturing and agriculture, and within the agricultural sector:

$$
L_e + L_u = 1 - L_m
$$

or

$$
l_e + l_u = 1 - l_m
$$

<!-- #region -->
Production in the manufacturing sector can be expressed in terms of potential sector output: 

$$
p \cdot \theta_M \cdot l_m^\beta \cdot G(\bar K, \bar L)
$$

because $L_M = l_m \bar L$ and $K_m$. The value marginal products of labor (MPL_i) in sector $i \in \{m, e, u\}$ can then be written:

$$
MPL_m = 
\beta \cdot \left ( \frac{1}{l_m} \right ) ^{1-\beta} \cdot  \bar k^{1-\beta}
$$

$$
MPL_e = 
 \alpha \cdot \theta \cdot \left ( \frac{t_e}{l_e} \right ) ^{1-\alpha} \cdot \bar t^{1-\alpha}
$$


The value Average product of labor in unenclosed agriculture as:
$$
\begin{aligned}
APL_u &= \frac{F(t_u, l_u)}{l_e} \cdot \frac{F(\bar T, \bar L)}{\bar L} \\
   &=  \left ( \frac{1-t_e}{1-l_m-l_e} \right ) ^{1-\alpha} \cdot  \bar t^{1-\alpha}
\end{aligned}
$$
<!-- #endregion -->

**Labor allocations as a function of the enclosure rate $t_e$** 

Suppose share $t_e$ of agricultural land has been enclosed. Workers will move across sectors (from agriculture to manufacturing) or from the enclosed to the unenclosed agricultural sectors until:

$$
w = p \cdot MPL_m = MPL_e = APL_u
$$

Focusing on the last equality first, and simplifying:

$$
(\alpha \theta)^\frac{1}{1-\alpha} \left ( \frac{t_e}{l_e}   \right ) 
= \left ( \frac{1-t_e}{(1-l_m)-l_e} \right )  
$$

and solving for labor allocations as a function of $t_e$:

$$
l_e^*(t_e) = \frac{\Lambda t_e }{(1-t_e+\Lambda t_e)} \cdot (1-l_m)
$$

where  $\Lambda = (\alpha \theta )^{\frac{1}{1-\alpha}}$ 


These expressions are just like what we derived for the agriculture-only economy except that now $(1-l_m)$ replaces $1$.

With this expression for $l_e^*(t_e)$ we can find an expression for the agricultural 'wage' as a function of $t_e$ and $l_m$

$$
\begin{aligned}
w(t_e)^* &=  \bar t^ {1-\alpha} \cdot \left ( \frac{t_e}{l_e(t_e)^*} \right ) ^{1-\alpha}  \\
 &=  \bar t^ {1-\alpha} \cdot (1-t_e+\Lambda t_e) ^{1-\alpha} \cdot \left (\frac{1}{1-l_m} \right )^{1-\alpha}  
\end{aligned}
$$




Labor will move across sectors in search of the highest wage.  An equilibrium is reached when the  labor share to manufacturing $l_m$ equalizes returns to workers across sectors:

$$
p \cdot \beta \bar k ^{1-\beta} \left (\frac{1}{l_m}   \right )^{1-\beta}  
= \bar t^ {1-\alpha} \cdot  (1-t_e+\Lambda t_e) ^{1-\alpha}  \cdot \left (\frac{1}{1-l_m} \right )^{1-\alpha}
$$

The right hand side represents a weighted average of the demand for labor in the enclosed or unenclosed sector.  We can think of the mode as an augmented specific factors model with mobile labor, capital specific to the manufacturing sector, and land specific to agriculture. The twist to the model is that land may be enclosed or unenclosed, which can affect agricultural labor demands and hence also labor supply to the manufacturing sector. 


The above equilibrium condition will in general lead to a unique equilibrium in $l_m$ since there is dimininishing marginal productivity of labor.

Except for the special case where $\alpha = \beta$ there will be no clean closed form solution, but graphical and numerical analysis is straightforward. 



## Graphical analysis

The `weq` function takes labor supply as an input.  Without manufacturing, it's $\bar t = \frac{\bar T}{\bar L}$ but in the adapted case here it's just

```python
def Fmplm(lm, p=1, kb= 1, b=0.5):
    C = (p*b) * kb**(1-b)
    return C * (1/lm)**(1-b)

def Fmapla(lm, te, tb = 1, a=0.5, th=1):
    """private labor demand in agriculture..."""
    Lambda = (a*th)**(1/(1-a))
    C = tb**(1-a) *  (1 + (Lambda-1)*te)**(1-a) 
    return C * (1/(1-lm))**(1-a)

def Fmaplae(lm, te, tb = 1, a=0.5, th=1):
    """social labor demand in agriculture; planner optimum... Lambda_o

    NOTE (corrected 2026-07-28): the leading `a` is NOT optional. Lambda_o is not the
    only difference from the private case -- the planner also values labor at its
    marginal rather than average product in the commons, a factor of alpha. Dropping it
    inflates this curve by 1/alpha. See `enclose/manufacturing.py`."""
    Lambda = th**(1/(1-a))
    C = a * tb**(1-a) *  (1 + (Lambda-1)*te)**(1-a)
    return C * (1/(1-lm))**(1-a)

 
    
def pl(te, th=1, p=1, kb= 1,  a=0.5, b=0.5, tb=1):
    lm = np.linspace(0,1,100)
    plt.plot(lm, mplm(lm, p, kb, b))
    plt.plot(lm, mapla(lm, te, tb, a, th))
    plt.grid()
    plt.xlim(0,1)
    plt.ylim(0,2)
    def f(m):
        return  mplm(m, p, kb, b) - mapla(m, te, tb, a, th)
    lme = fsolve(f,[0.01, 0.99])[1]
    wme = mapla(lme,te, tb, a, th)
    print(f'lme = {lme: 0.2f}, wme = {wme:0.2f}')
    plt.scatter(lme, wme)
    plt.scatter(lme, 0)
    plt.vlines(lme, 0, wme)
    
```

```python tags=["hide_input"]
def mplm(lm, p, kb, b ):
    C = (p*b) * kb**(1-b)
    return C * (1/lm)**(1-b)

def mpla(lm, te, tb = 1, a=0.5, th=1, mu=0):
    """labor demand in agriculture; 
    mu = 0  full tragedy private
    mu = 1  planner

    CORRECTED 2026-07-28: mu enters TWICE, and in opposite directions -- through lam
    (the slope) and through the wedge A_mu = 1 - mu*(1-a) (the level, i.e. the share of
    the commons average product that labor takes home). A_0 = 1, so the private case was
    right and the planner case was overstated by 1/alpha. Default changed from mu=1 to
    mu=0 to match LM() below, which defaulted the other way."""
    lam = Lambda(th, a, mu)
    A = 1 - mu*(1-a)
    C = A * tb**(1-a) *  (1 + (lam-1)*te)**(1-a)
    return C * (1/(1-lm))**(1-a)


def LM(te, b, a, th, tb, kb, p, mu):
    '''Solve for private or social labor share to manufacturing
       mu = 0   APL = MPL
       mu = 1   MPL = MPL '''
    
    def f(m):
        return  mplm(m, p, kb, b) - mpla(m, te, tb, a, th, mu)
    
    lmp = fsolve(f,[0.01, 0.99])[1]
    return lmp

    
def pl(te, th=1, p=1, kb= 1,  a=0.5, b=0.5, tb=1, mu =0):
    lm = np.linspace(0,1,100)
    plt.plot(lm, mplm(lm, p, kb, b))
    plt.plot(lm, mpla(lm, te, tb, a, th, mu))
    plt.grid()
    plt.xlim(0,1)
    plt.ylim(0,2)
    
    lmp = LM(te, b, a, th,  tb, kb, p, mu = 0)
    wmp = mpla(lmp, te, tb, a, th, mu = 0)
    
    lme = LM(te, b, a, th, tb, kb, p, mu=1)
    wme = mpla(lme, te, tb, a, th, mu=1)
    
    print(f'lme = {lme: 0.2f}, wme = {wme:0.2f}')
    plt.scatter(lmp, wmp)
    plt.scatter(lmp, 0)
    plt.vlines(lmp, 0, wmp)
    
    
    plt.scatter(lme, wme)
    plt.scatter(lme, 0)
    plt.vlines(lme, 0, wme)
```

```python
LM(te = 1, b=0.5, a=0.5, th=1,  tb=1, kb=1, p=1, mu = 1)
```

```python
pl(te=1, th=1, p=1, kb= 1,  a=0.4, b=0.7, tb=1, mu =0)
```

## The effect of enclosure on structural transformation

Thus far we have only set things up to find the equilibrium level of manufacturing employment $l_m$, conditional on an arbitrary initial enclosure rate $t_e$.  We must still work out how to derive the equilibrium level $t_e$ which will depend on the cost of enclosures and how decentralized enclosure games are played out.  We will get to that in the next section.  

But first, it is interesting to explore graphically how the enclosure rate $t_e$ can have an important influence on the level of structural transformation. 

Conider first an an economy without any enclosure, so $t_e=0$. For the parameter values shown below, only about 20 percent of the population moves into manufacturing.

```python
pl(te=0, th=1, p=1, kb= 1,  a=0.4, b=0.7, tb=1)
```

Now consider the same economy, but with complete land enclosure, so $t_e=1$.  Notice that in this economy $\theta=1$ so enclosure does not raise plot level TFP.

For these parameter values the labor share in manufacturing rises dramatically from 20 percent to almost 70 percent, but we end up with a significantly lower equilibrium wage (the Weitzman/Samuelson effect).

```python
pl(te=1, th=1, p=1, kb= 1,  a=0.4, b=0.7, tb=1)
```

Below the same diagram with interactive sliders to change parameters:

```python
interact(pl, te=(0,1,0.1), th=(0.9, 3,0.1), p = (0.5,2,0.1), tb=(0.5,2,0.1), mu=(0,1,0.1));
```

We have not yet specified a cost to enclosure. If enclosure were costless, and $\theta \ge 1$ then it would always be worthwhile to enclose. If enclosure is costly we need to compare social benefits to social costs.

<!-- #region -->
## Socially optimal enclosure with manufacturing

The planner wants to choose $(T_e, L_e, L_m)$ to maximize:


$$
\theta F(T_e, L_e) +  F(\bar T - T_e, \bar L - L_m - L_e)  + p \cdot G(\bar K, L_m) - c \cdot T_e
$$



<!-- #endregion -->

In intensive form:

$$
\max_{t_e} \ \ \left[\theta\cdot F(t_e, l_e(t_{e}))+F(1-t_e, 1-l_m(t_e)-l_e(t_{e}))\right]\cdot F(\bar T, \bar L)  
+ p \cdot l_m(t_e)^{1-\alpha} \cdot G(\bar K,  \bar L ) - c \cdot \bar T \cdot t_e
$$


The planner will want to equate marginal value products across sector, so that 

$$
p \cdot MPL_m = MPL_e = MPL_u
$$

(this is slighlty different from the private eqn above ).

Focusing on the first equality, and simplifying:

$$
\Lambda_o \frac{t_e}{l_e}   
= \left ( \frac{1-t_e}{(1-l_m)-l_e} \right )  
$$

and solving for labor allocations as a function of $t_e$:

$$
l_e^*(t_e) = \frac{\Lambda_o t_e }{(1-t_e+\Lambda_o t_e)} \cdot (1-l_m)
$$

where $\Lambda_o = \theta^\frac{1}{1-\alpha}$


<!-- #region -->
The value marginal product in the 'enclosed' sector can then be written


$$
\alpha \theta \cdot \bar t^ {1-\alpha} \cdot \left ( \frac{t_e}{l_e(t_e)^*} \right ) ^{1-\alpha}  
=  \alpha \cdot \bar t^ {1-\alpha} \cdot (1-t_e+\Lambda_o t_e) ^{1-\alpha} \cdot \left (\frac{1}{1-l_m} \right )^{1-\alpha}  
$$

**The leading $\alpha$ matters, and it is easy to lose.** In the private case above the
same substitution produces $\alpha\theta \Lambda^{-(1-\alpha)}$, which equals *exactly one*
by the definition of $\Lambda = (\alpha\theta)^{1/(1-\alpha)}$ — so the factor can be
dropped there and the shorthand $\bar t^{1-\alpha}(t_e/l_e^*)^{1-\alpha}$ is correct.
Here $\Lambda_o^{1-\alpha} = \theta$, so the same factor is $\alpha$, not one. Carrying the
private shorthand across to the planner overstates this curve by $1/\alpha$. In general the
prefactor is $A_\mu = 1-\mu(1-\alpha)$, the share of the commons average product that labor
takes home; $A_0 = 1$ and $A_1 = \alpha$.
<!-- #endregion -->

For this to also equal the value marginal product of labor in manufacturing the social planner will make sure that $l_m$ is chosen so that:

$$
p \cdot \beta \bar k ^{1-\beta} \left (\frac{1}{l_m}   \right )^{1-\beta}  
= \alpha \cdot \bar t^ {1-\alpha} \cdot  (1-t_e+\Lambda_o t_e) ^{1-\alpha}  \cdot \left (\frac{1}{1-l_m} \right )^{1-\alpha}
$$

This looks similar to the condition that emerges from a private economy, except that the planner equalizes marginal value products in agriculture, whereas the private economy equalizes the value marginal product in the enclosed sector to the value average product in the unenclosed sector. That difference is precisely the $\alpha$: it is the whole content of the distortion at this margin, so dropping it makes the planner and the open-access economy look identical at $t_e=0$, which is how the error was eventually caught.

Two consequences worth recording. At $t_e=0$ the two curves must stand in the ratio $\alpha$
exactly. At $t_e=1$ there is no commons left, so $\mu$ cannot matter at all and both sides
reduce to $\alpha\theta\bar t^{1-\alpha}$ — meaning **full enclosure implements the
planner's inter-sectoral allocation for any $\theta$.**

This is conditional on $t_e$ and says nothing about whether that $t_e$ is worth reaching.
The planner's remaining first-order condition, in $t_e$, is the enclosure margin. By the
envelope theorem the labor terms drop out and only the land-rent differential survives:

$$
\frac{dY}{dt_e} = (1-\alpha)\,\bar t^{1-\alpha}(\Lambda_o-1)
\left(\frac{1-l_m(t_e)}{1+(\Lambda_o-1)t_e}\right)^{\alpha}
$$

which is the benchmark's $z'(t_e)$ with the agricultural labor share $(1-l_m)$ in place of
the whole labor force. Its sign is the sign of $(\Lambda_o-1)$, hence of $(\theta-1)$ —
note $\Lambda_o$, **not** $\Lambda_\mu$, so this margin turns at $\theta=1$ and not at
$\theta_H$. For $\theta\le1$ the planner encloses nothing at any $c>0$, however
misallocated the decentralized economy's labor is. Full enclosure is first best only for
$\theta>1$ with $c$ small.

At $\theta=1$ the whole gain from enclosure is the repair of the commons distortion — and
regulating the commons ($\mu\to1$) achieves the same allocation at $t_e=0$ without paying
$c\bar T$. **Enclosure is a second-best instrument here, dominated by governance.**

```python

```

<!-- #region -->
## Notes toward a manufacturing paper

The condition just derived is where the analysis below picks up. Writing both sides
compactly, labor allocates until

$$
\underbrace{p \beta \bar k^{1-\beta}}_{C_m} \cdot l_m^{-(1-\beta)}
\;=\;
\underbrace{A_\mu \cdot \bar t^{1-\alpha}\left(1+(\Lambda_\mu-1)t_e\right)^{1-\alpha}}_{C_a}
\cdot (1-l_m)^{-(1-\alpha)}
$$

with $A_\mu = 1-\mu(1-\alpha)$ as above. Note that $\mu$ enters $C_a$ twice and in opposing
directions: it raises $\Lambda_\mu$ (pulling labor back to agriculture) and lowers $A_\mu$
(pushing labor to manufacturing). At $t_e=0$ the second acts alone; at $t_e=1$ they cancel
exactly.

or, rearranged,

$$
\frac{l_m^{1-\beta}}{(1-l_m)^{1-\alpha}} \;=\; \frac{C_m}{C_a}
$$

Four observations follow. (1)-(3) are established — algebraically immediate and confirmed
numerically; (4) is a reading of (3) worth testing further.

### 1. The equilibrium exists and is unique

$MPL_m$ is strictly decreasing in $l_m$ and $MPL_a$ strictly increasing, so the excess
demand crosses zero exactly once on $(0,1)$. Confirmed by parameter sweep: exactly one sign
change for every $(\alpha,\beta)$ combination tested. Practically this means a *bracketed*
root-finder on $(0,1)$ is guaranteed to converge — no starting guess required, no risk of
wandering to a spurious root.

### 2. No closed form in general — but one instructive special case

For $\beta \neq \alpha$ the condition is of the form $x^{p}(1-x)^{q}=K$, which has no
elementary solution: the equilibrium must be found numerically. But when $\beta = \alpha$
the exponents coincide and it collapses to

$$
\left(\frac{l_m}{1-l_m}\right)^{1-\alpha} = \frac{C_m}{C_a}
\qquad\Longrightarrow\qquad
l_m = \frac{R}{1+R},\quad R = \left(\frac{C_m}{C_a}\right)^{\frac{1}{1-\alpha}}
$$

Useful twice over: as a fully worked case for exposition, and as an exact check on the
numerical solver (they agree to 12 significant figures).

### 3. Enclosure's effect on structural transformation *reverses* at $\theta_H$

This is the substantive result, and it is unaffected by the $A_\mu$ correction above:
$A_\mu$ contains neither $t_e$ nor $l_m$, so it moves the level of the agricultural curve
without touching its slope. $C_a$ carries $\left(1+(\Lambda_\mu-1)t_e\right)^{1-\alpha}$,
so the sign of $\partial l_m/\partial t_e$ is the sign of $(1 - \Lambda_\mu)$ — the
equilibrium condition inverts it, since its left side rises in $l_m$ and so $l_m$ rises
exactly when $C_a$ falls — and
$\Lambda_\mu = 1$ exactly at $\theta_H^\mu = \frac{1}{\alpha}-\mu\frac{1-\alpha}{\alpha}$,
the same threshold that separates strategic complements from substitutes in the main model.

- **$\theta < \theta_H^\mu$:** $\Lambda_\mu<1$, enclosure is labor-*extensive*. Agricultural
  MPL falls as $t_e$ rises, and labor is released **into** manufacturing. Enclosure
  *accelerates* structural transformation.
- **$\theta > \theta_H^\mu$:** $\Lambda_\mu>1$, enclosure is labor-*intensive*. Labor is
  pulled **back into** agriculture. Enclosure *retards* structural transformation.
- **$\theta = \theta_H^\mu$:** $\Lambda_\mu=1$ and enclosure does not shift the sectoral
  allocation at all.

Numerically, at $\alpha=0.5$, $\mu=0$ (so $\theta_H=2$), $l_m$ across
$t_e \in \{0,\,0.3,\,0.6,\,1\}$:

| $\theta$ | $\Lambda$ | $l_m$ over $t_e$ | direction |
|---|---|---|---|
| 1.2 | 0.36 | 0.200, 0.236, 0.289, 0.410 | rising |
| 1.8 | 0.81 | 0.200, 0.210, 0.220, 0.236 | rising |
| **2.0** | **1.00** | 0.200, 0.200, 0.200, 0.200 | **flat** |
| 2.5 | 1.56 | 0.200, 0.176, 0.158, 0.138 | falling |
| 3.5 | 3.06 | 0.200, 0.134, 0.100, 0.076 | falling |

The knife-edge at $\theta_H$ is exact, not approximate.

This cuts against reading enclosure as uniformly "releasing labor for industry." Whether it
does depends entirely on which side of $\theta_H$ the economy sits — and the classic
enclosure-feeds-industrialisation narrative implicitly assumes the low-TFP branch.

### 4. Governance moves the reversal point (worth testing further)

$\theta_H^\mu$ is decreasing in $\mu$, from $1/\alpha$ at $\mu=0$ to $1$ at $\mu=1$. So
improving commons governance *widens* the region in which enclosure retards structural
transformation. Put differently: where the commons is already well regulated, enclosure is
more likely to draw labor back into agriculture than to release it. This follows directly
from (3) and the definition of $\theta_H^\mu$, but its implications have not been worked
through, and it is stated here as a lead rather than a result.

### Caveats and next steps

- The manufacturing price $p$ is taken as given. Endogenising it is the obvious next step
  and could overturn the partial-equilibrium comparative statics above.
- The planner/private distinction enters through $\mu$ in *both* $\Lambda_\mu$ and $A_\mu$
  (this note previously said $\Lambda_\mu$ only — that was the error corrected above). The
  full welfare comparison with a manufacturing sector, netting off the enclosure cost $c$,
  has still not been done.
- The two existing drafts of this material (`enclosure_manuf.md`, 334 lines, and
  `Manufactures and Structural Transformation.md`, 216 lines) have diverged and should be
  reconciled before any of it is written up. The shorter draft has **not** been corrected
  for $A_\mu$ and should not be used as a source.

### Implementation

`enclose/manufacturing.py` in `open-enclose.github.io` implements all of the above:
`mpl_m`, `mpl_a`, `labor_share` (bracketed `brentq`), `labor_share_closed_form` (the
$\beta=\alpha$ oracle) and `agricultural_labor` (eq. 36). `tests/test_manufacturing.py`
pins the uniqueness property, the closed-form agreement, and the sign reversal at
$\theta_H$ including the flat knife-edge.
<!-- #endregion -->
