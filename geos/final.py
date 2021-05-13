from scipy import constants 
import numpy as np 

# Fuvial Processes 
# 12 -> 14 - Anderson 
#  10.3    - Melosh 


#Channel Depth 
H = 8.5 #(m)
# incline of the bank
THETA = 5*constants.pi/180
# dynamic viscosity 
MU = 
# fluid density
RHO =

#Reynolds number 
def Re(H,u,v):
    '''Reynolds Number in an open channel 
        H - height of river (m)
        u - mean velocity (m/s)
        v - kinematic velocity (m/s) 
    '''
    return H*u/v

# Get Flow Speed where Re << 1 - (laminar flow) 
def 



# Reach average of morphology 
def basal_shear_stress(p,h,phi):
    return p*h*constants.g*np.sin(phi)
 