# Lukas Elsrode - (04/27/2021)
# pnorm() :: pnorm(R)->[0,1] and  qnorm([0,1]) -> R
#1) 
#a) P(z > -1.13) - Symetric around (x = 0) so  
print(pnorm(1.13,mean=0,sd=1))
#b) P(|z| < 0.5) ~ symmetric  
print(pnorm(0.5,mean=0,sd=1) - pnorm(-0.5,mean=0,sd=1))
# find x s.t  integral(P(x)|[-inf,x]) = y 
#c) y=0.06, x=qnorm(y)
print(qnorm(0.06,mean=0,sd=1))
#d) y=0.08, x=qnorm(y)
print(qnorm(0.08,mean=0,sd=1))
#2)
#a) P(x < 48)
print(pnorm(48,mean=55,sd=6))
#b)P(60 < x < 65) 
print(pnorm(65,mean=55,sd=6) - pnorm(60,mean=55,sd=6))
#c) P(x>y) = 0.1 so  1 - P(x>y) = 0.9 
print(qnorm(0.9,mean=55,sd=6))
#3)
# Matrix __repr__ of this table 
PMF <- matrix(
  data = c(
    0.10, 0.04, 0.02,
    0.08, 0.20, 0.06,
    0.06, 0.14, 0.30
  ),
  nrow = 3,
  ncol = 3,
  byrow = TRUE,
  dimnames = list(c("x0", "x1","x2"), c("y0","y1", "y2"))
)
#a) for P(x+y= 4) = P(x=2) + P(y=2)
print(PMF["x2", "y2"])
#b) P(X + Y = 1) = P(X=1,Y=0) + P(X=1,Y=0)
print(PMF["x0", "y1"] + PMF["x1", "y0"])
#c) Marginal pmf of X.sum P(x) for any Y.
print(apply(X = PMF, MARGIN = 1, FUN = sum))
#d) Marginal pmf of X.sum P(y) for any X
print(apply(X = PMF, MARGIN = 2, FUN = sum))
#e) P(X = 2)
print(sum(PMF["x2", ]))
#f) Conditional pmf of Y given X = 2
print(PMF["x2", ] / sum(PMF["x2", ]))
#g) P(X|Y=0)
print(PMF[, "y0"] / sum(PMF[, "y0"]))
#h) if X and X are indpendant then P(X = x | Y = y) = P(X = x) for any  {x,y}
#P(X=2)
p_x2 <- sum(PMF["x2", ])
# P(X=2 | Y=0) = P(x=2 AND y =0)/P(y=0)
p_x2_y0 <- PMF["x2", "y0"] / sum(PMF[, "y0"])
print(p_x2 == p_x2_y0)
