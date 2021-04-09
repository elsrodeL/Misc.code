from math import *
from scipy import constants
# Question 2) 
#volume of pool
lx,ly,lz = 25,50,2.5 # m
Vpool = lx*ly*lz    # m^3
# radius of golf ball is about the same as a squash ball
Rball = 20*10**(-3) # m 
Vb = (4/3)*pi*((Rball)**(3))
# assume random packing of spheres sum(Vb_i)/Vpool = 0.64 
n_balls = 0.64 * (Vpool/Vb)
# get concentration of phosphorous
cP = n_balls**(-1)
# see what that is in cm^-3 
nSi = (2.33/28)*constants.Avogadro  # number of Si atoms per cm^-3
nP = cP * nSi
print(nP)

#Question 7 

# the three surfaces hieghts as along a plane 
s1 = [4,5,9,3,8,3,6,5,18,2,9,6]
s2 = [9,1,10,12,3,10,1,9,3,11,7,6]
s3 = [12,10,8,6,4,2,6,12,10,11,5,4]

# approximate the integral as a finite sum given that (dx = 1)
def rms(surface):
    # dx = 1 unit
    L = len(surface)
    #sum of squares of points in surface
    sum_squares = sum(list(map(lambda x: x**(2),surface)))
    return (sum_squares/L)**(1/2)

print(rms(s1))
print(rms(s2))
print(rms(s3))    
