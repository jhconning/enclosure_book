---
title: derive te
tags: [appendix]
created: 2022-06-20T16:17:04.499Z
modified: 2022-06-20T18:04:09.819Z
---

# derive te


## Planner's $t_e^o$

The planner optimizes:

$$
z_o(t_e)  - c \cdot t_e = \bar l^{\alpha} \cdot \left[ 1+\left(\Lambda^o-1\right)t_e\right]^{1-\alpha}-c  t_e
$$

see [derive z](derive%20z.md) for how we got to this expression for $z_o(t_e)$

## Optimum $t_e^o$

From

$$
z_o'(t_e) = c
$$

from above for $z_o$ :

$$
z_o'(t_e) = \frac{(1-\alpha)(\Lambda_o -1) \bar l^\alpha}
{(1+(\Lambda_o - 1)t_e)^\alpha} = c
$$

hence

$$
\bar l \left [   \frac{(1-\alpha)(\Lambda_o - 1)}{c}  \right ]^\frac{1}{\alpha}
= 1+(\Lambda_o - 1)t_e
$$

and


$$
t_e^o =  \frac{\bar l}{(\Lambda_o - 1)}  \left [   \frac{(1-\alpha)(\Lambda_o - 1)}{c}  \right ]^\frac{1}{\alpha} - \frac{1}{(\Lambda_o - 1)}
$$




## Decentralized $t_e^o$


From the condition 

$$
\alpha\theta\left(\frac{t_e}{l_e}\right)^{1-\alpha}
    =\left(\frac{1-t_e}{1-l_e}\right)^{1-\alpha}
$$

From which we can solve for

$$
l_e^*(t_e) = \frac{\Lambda t_e}{1+(\Lambda-1) t_e } , \quad \Lambda(\theta)=(\alpha\theta)^\frac{1}{1-\alpha}
$$

Private actors enclose when $r(t_e)>c$

$$
(1-\alpha)\cdot \theta \cdot \bar l ^\alpha \cdot \left ( \frac{l_e^*(t_e)}{t_e}  \right )^{\alpha}>c
$$

Substitute in 

$$
r(t_e)={\theta}\cdot(1-\alpha)\cdot \bar l^{\alpha}
\cdot \left ( \frac{\Lambda}{(1+(\Lambda -1)t_e)} \right)^\alpha >c
$$

**Interior**

$$
{\theta}\cdot(1-\alpha)\cdot \bar l^{\alpha}
\cdot  \frac{\Lambda^\alpha}{(1+(\Lambda -1)t_e)}  =c
$$

$$
c(1+(\Lambda -1)t_e)^\alpha={\theta}\cdot(1-\alpha)\cdot \bar l^{\alpha} \cdot  {\Lambda^\alpha}  
$$

$$
c^{1/\alpha}(1+(\Lambda -1)t_e)=[{\theta}\cdot(1-\alpha)]^{1/\alpha}\cdot \bar l \cdot  {\Lambda}  
$$


$$
t_e=  \bar l \cdot  \frac{\Lambda}{\Lambda-1} \cdot \left [\frac{{\theta}\cdot(1-\alpha)}{c} \right]^{1/\alpha} 
- \frac{1}{\Lambda-1}
$$





## Conditional $t_e^c$

See [derive z](derive%20z.md) for $z(t_e)$


$$
z(t_e)- c \cdot t_e = \bar l^\alpha  \cdot  \left [\theta t_e^{1-\alpha}l_e^\alpha + (1-t_e)^{1-\alpha}(1-l_e)^{\alpha}    \right ] - ct_e
$$ 

can be written:
$$
z(t_e)= \bar l^\alpha \cdot \frac{ 1+(\frac{\Lambda}{\alpha}-1)t_e}{(1+(\Lambda-1)t_e)^\alpha} 
$$


So the derivative

$$
z'(t_e) = \bar l^\alpha \cdot  \frac{(1-\alpha)(\frac{\Lambda}{\alpha} -1)}
{(1+(\Lambda_o - 1)t_e)^\alpha} = c
$$

hence

$$
\bar l \left [   \frac{(1-\alpha)(\Lambda_o - 1)}{c}  \right ]^\frac{1}{\alpha}
= 1+(\Lambda_o - 1)t_e
$$

and



