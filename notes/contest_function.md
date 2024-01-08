
# Enclosure contest functions

```{note}
The following is a preliminary exploration ...
```

This note lays out a more general contest function and variable enclosure effort, or what I will call a property appropriation activity.  This adapts Matt's extension on the topic to to the notation of our earlier paper.   This allows us to re-use several key equations and reveals insights.

Each of $\bar L (=n)$ individuals has one unit of labor endowment that they can divide between working in the enclosed sector $l_e$, working in the customary (commons) sector $l_c$ or working to enclose (or guard) land in order to make it exclusive:

$$
l_e+l_c+g=1
$$

Labor that is not engaged in creating/protecting property is available for work, or  $l_e + l_c = 1 - g$. This will imply that we write labor use in the agricultural sector as  $L_e=l_e (1-g) \bar L $  and $L_c=(1-l_e)(1-g)\bar L$ and $L_g = g \bar L$.

We can think of this as a specific factors model with labor mobile across the three sectors. The household maximizes income across the three activities:

$$
w_e l_e + APL_c\cdot l_c+r \cdot f(g)
$$

Here $f(g)$ is the amount of land appropriated and enclosed via labor effort $g$. We can think of this land being then rented out at a market rate.  This function $f(g)$ will be described by an appropriation contest function below.

The agricultural production technologies are as follows[^1]

[^1]: This returns to the original model. Matt's note has the exponents reversed as $AT^\alpha L^{1-\alpha}$

|                                                      |                                                          |
| :--------------------------------------------------- | :------------------------------------------------------- |
| $F(T,L)= A_c \cdot {T_e}^{1-\alpha}\cdot L_e^\alpha$ | Production technology in unenclosed agriculture sector   |
| $G(T,L)= A_e \cdot {T_c}^{1-\alpha}\cdot L_c^\alpha$ | Production technology in the enclosed agriculture sector |

Note that $T_e = t_e \cdot \bar T$ and $L_e=l_e (1-g) \bar L $ .   In equilibrium, the household has no incentive to reallocate labor across activities. At an interior solution we will have $w_e=APL_c=MPL_e$ where

$$
MPL_e = 
 \alpha \cdot A_e \cdot 
 \left ( \frac{t_e}{l_e}  \right ) ^{1-\alpha} 
 \cdot \bar t^{1-\alpha}
$$


and

$$
\begin{aligned}
APL_c &= \frac{F(t_c, l_c)}{l_c} \cdot \frac{F(\bar T, \bar L)}{\bar L} \\
   &=  A_c \left ( \frac{1-t_e}{(1-g-l_e)} \right ) ^{1-\alpha} \cdot  \bar t^{1-\alpha}
\end{aligned}
$$

In what follows we will at times employ:

$$
\theta = \frac{A_e}{A_c}
$$

**Labor allocation as a function of the enclosure rate $t_e$** 

Examining our equality condition above

$$
(\alpha \theta)^\frac{1}{1-\alpha} \left ( \frac{t_e}{l_e}   \right ) 
= \left ( \frac{1-t_e}{1-g-l_e} \right )
$$

and solving for labor allocations as a function of $t_e$:

$$
l_e^*(t_e) = \frac{\Lambda t_e}{(1+(\Lambda-1) t_e)} \cdot (1-g)
$$

where  $\Lambda = (\alpha \theta )^{\frac{1}{1-\alpha}}$ . This is very similar to the benchmark model (and identical thus far to the manufacturing extension) except that now $(1-g)$ replaces $1$ as the labor supply.

Using this expression for $l_e^*$ for any level of enclosure $t_e$ and $l_m$ we can find an expression for rural inverse 'labor demand' (substitute $l_e^*(t_e)$ into $MPL_e$):
$$
\begin{aligned}
w(t_e)^d &= \alpha A_e \cdot \bar t^ {1-\alpha} \cdot \left ( \frac{t_e}{l_e(t_e)^*} \right ) ^{1-\alpha}  \\
 &= \alpha A_e \cdot \bar t^ {1-\alpha} \cdot \left ( \frac{1+(\Lambda-1) t_e}{\Lambda(1-g)} \right ) ^{1-\alpha} 
\end{aligned}
$$

Note that $g$ (and therefore also $t_e$ which depends on $g$) is  yet to be determined by the appropriation activities that will determine how much land will be enclosed $t_e$ and how much labor is left over to 'supply' the sector $(1-g)$.    

We can think of this as the total demand from wage employment (a weighted demand from enclosed and unenclosed sectors). We can't determine this until we have also accounted for the  'supply' of labor $(1-g)$.  This will be determined by the opportunity cost that must be paid to draw labor out of the competing property appropriation activity 



## Appropriation activities -- contest functions

The amount of land that a household is able to appropriate as exclusive property will depend on their appropriation labor $g$ relative to the activities of others, captured by $\bar g$.  


$$
f(g)=\frac{g}{\bar L \bar g } \cdot \frac{\bar L \bar g  Z}{\bar L \bar g + Z} \cdot \bar T
= \frac{g}{\bar g} \frac{gZ}{\bar L\bar g+Z} \cdot \bar t
$$


Where $Z \in(0,1)$ is a parameter that captures the cost of appropriation activities .  This is a contest function that captures the idea that 

1. those who spend more on appropriation activities relative to others capture more, and
2. total land enclosed is increasing in aggregate effort. 

To see the latter, note that in a symmetric equilibrium $g=\bar g$ and $\bar L$ is the number of households (I'm assuming $n=\bar L$ though one could imagine a situation where they are not the same...).  In a symmetric equilibrium

$$
f(\bar g) =  \frac{\bar g Z}{\bar L \bar g + Z} \cdot \bar t
$$
which is increasing and concave in overall appropriation effort $\bar L \bar g$.   Notice that, in equilibrium, the share of land enclosed $t_e$ will be given by $t_e = \frac{ \bar L \cdot f(\bar g)}{\bar T}$ or simply:


$$
t_e(g) =   \frac{\bar gZ}{\bar L \bar g + Z}
$$


This gives us the level of enclosure. assuming there is appropriation activity ($\bar g>0$).  

Note that at $\bar g =0$ the amount of land that can be appropriated on the margin is high (the cost of enclosure is low), and when there is lots of land ($\bar t$ is large) the amount of land that can be enclosed for any given effort is larger.  However, the decision to enclose or not also depends on the rental rate.  Then as $\bar g$ increases, the return to appropriation falls.  Hence, it's unlikely we'll see zero enclosure in this model (might be modified to add a fixed cost).


$$
f'(g)=\frac{Z}{\bar L \bar g + Z} \cdot \bar t
$$


Parameter $Z$ affects the cost of enclosure.  As we raise $Z$ the marginal return to enclosure $f'(\bar g)$ rises, which is to say, the marginal cost of enclosing falls (less labor to enclose the same amount).  For $Z>0$ there will always be some land left unenclosed ($t_e \le \bar t$)  at $\bar g= 1$.   But for large enough $n$, in a symmetric equilibrium, each household appropriates approximately  $\bar t$  units of land.   This is not unrealistic. In most societies some land and other resources are left unenclosed

However, the decision to enclose or not also depends on the rental rate.  
$$
\begin{aligned}
r(t_e)=MPT_e=&A_e \cdot (1-\alpha) \cdot 
\bar l^\alpha 
\left (\frac{l_e^*(t_e)}{t_e}
\right )^\alpha
\\
=& A_e \cdot (1-\alpha) \cdot \bar l^\alpha 
\left ( \frac{\Lambda(1-g)}{1+(\Lambda-1) t_e} \right ) ^\alpha 
\end{aligned}
$$


## Equilibrium $g$ and $t_e$

We search for the $g=\bar g$ that makes labor indifferent between the three activities. 



$$
\begin{aligned}
w(t_e)^d &= r(t_e)\cdot f'(g)  \\
\alpha A_e \cdot \bar t^ {1-\alpha} \cdot \left ( \frac{1+(\Lambda-1) t_e}{\Lambda(1-g)} \right ) ^{1-\alpha} 
&= 
A_e \cdot (1-\alpha) \cdot \bar l^\alpha 
\left ( \frac{\Lambda(1-g)}{1+(\Lambda-1) t_e} \right ) ^\alpha 
\cdot
\frac{Z}{\bar L \bar g + Z} \cdot \bar t
\end{aligned}
$$



Not sure this is right...   $\bar t$ will drop out. suggesting a result independent of labor-land ratio.   See https://www.geogebra.org/classic/pfjkcj74

I'm not sure the plot is right.  It suggests positive enclosure  only when $\theta =A_e/A_c$ is above a threshold (analogous to $\theta>\theta_H$ in the benchmark?).  In the plot below we have $g$ on the x-axis. The red downward sloping $r\cdot f'(g)$ shows declining return to appropriation (the right hand side above).  The other line is demand for labor into enclosed and unenclosed



As drawn ($\alpha = 0.5, n=50, Z=25, Ae=5, Ac=1$ so $\theta=5$)



This suggests $g=0.42$ which implies $t_e = 0.35$ 


From simple numeric exploration, $g$ rises with $Z$ but falls with $n=\bar L$.  

A Geogebra chart at https://www.geogebra.org/classic/pfjkcj74

<iframe src="https://www.geogebra.org/classic/pfjkcj74?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>