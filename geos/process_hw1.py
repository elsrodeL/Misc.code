import numpy as np 
import random
from scipy import constants

#Central Pressure
def Pc(M,R):
    return (3*constants.G*(M)**(2))/(8*constants.pi*R**(4))

# other functions
def get_mass(V,p):
    return V*p

def get_vol(r):
    return (4/3)*constants.pi*r**(3)

# get worlds mass by estimating density
Pa_r,Me_r = 112*constants.kilo,141*constants.kilo    #m
p_iceworlds = random.choice(np.linspace(1000,1600,10))  #kg/m^3
Pa_m , Me_m = get_mass(get_vol(Pa_r),p_iceworlds),get_mass(get_vol(Me_r),p_iceworlds)
Pa_p, Me_p = Pc(Pa_m,Pa_r),Pc(Me_m,Me_r)    #Pa

print(f'Central Pressure Pc - Patroclus = {Pa_p/ constants.mega} (MPa) , Menotius = {Me_p/constants.mega} (MPa)')

# Question4

# convert Myr to seconds
def Myr_to_s(t):
    return (60**(2))*24*365*(10**(6))*t

# get the viscosity given shear modulus 
def get_nu(t):
    return Myr_to_s(t) * (constants.giga*65)

n1 = get_nu(1)
n2 = get_nu(10)
n3 = get_nu(100)
n4 = get_nu(1000)

print(f'where Tau = 1Myr ;  n = {n1} (Pa-s)')
print(f'where Tau = 10Myr ;  n = {n2} (Pa-s)')
print(f'where Tau = 100Myr ;  n = {n3} (P-s)')
print(f'where Tau = 1000Myr ;  n = {n4} (Pa-s)')

# no clue how to get the depths




