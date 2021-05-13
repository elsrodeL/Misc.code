'''
    Lukas Elsrode - HW4 
        - Pictures are meant to show derivation of steps previous to calculation 
        - Python Code is used as a means to show calculation and answer generation
    
'''
# Libraries I used 
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants
from sklearn.linear_model import LinearRegression

'''
Mississippi River velocity structure and sediment transport. Consider the
following measurements of the flow velocity within a profile of the
Mississippi River, at this time and place flowing with a flow depth of 8.5 m.
The measurements are as follows:

'''

h = 8.5 # (m)
Z = np.array([7.7,5.2,3.2,1.8,0.9,0.6]).reshape((-1,1)) #(m)
U = np.array([1.25,1.2,1.05,1.0,0.9,0.8]).reshape((-1,1)) #(m/s)


'''
1)i) Recalling the law of the wall, what is your best estimate of the shear velocity, u*?
U* is proportional to velocity profile which is linear in the log(z) scale... 

'''
# new ln() scale 
ln_Z = np.array(list(map(lambda x: np.log(x), Z))).reshape((-1, 1))  # (m)

# show the linearity of ln() scale
plt.plot(Z, U, 'b')
plt.plot(ln_Z, U, '-g')
plt.title('Linear Scale (blue) Vs. Log Scale (green)')
plt.ylabel('ln(Dist)/Dist above Riverbed (m)')
plt.xlabel('Avg Velocity (m/s)')
plt.show()

# Instead of fitting parent functions, just us the linear ln_scale()
def get_Uprime_and_Zo(Z,U,k=0.4):
    model = LinearRegression().fit(U,Z)
    U_ = model.coef_ * k
    zo = np.exp(-(k*model.intercept_/U_))
    return U_, zo 

# Get U_prime and Zo
U_ ,zo = get_Uprime_and_Zo(ln_Z,U)
print(f'Shear Velocity of River = {U_} (m/s) ; Length scale grain roughness {zo} (m)')

'''
1)ii) Given this, what is the slope of the river in this reach? You will have to use
      definition of the shear velocity, u* = sqrt(g*H*S), where S is slope
'''

def get_S(Us,H):
    return np.sinh((Us**2) / (constants.g * H))

S = get_S(U_,h)
print(f' The Slope of the river in this reach is {S} ')


'''
Consider a steep-walled river channel with width = 50m, 
bankfull depth of 3m(to the levee tops) and a slope of 0.5 m/km. The bed of
the river is made of coarse sand, organized into ripples that result in an
effective roughness length(z0) of 3 mm. The river at the moment is flooding
at a stage of 0.5 m above bankfull. Recall that the shear velocity u * is defined
as u * = √(tau_b/rho), or u * = √(gHS).

'''

W = 50  # (m)
d_max = 3  # (m)
alpha = np.tanh(0.5/1000)  # (radians)
z0 = 3 * constants.milli  # (m)

# make function to get U_shear
def U_shear(h,S=alpha):
    return (constants.g * h * S)**(1/2)

# make function to get a mean sediment flux rate 
def estimate_sed_flux(U_,h,zo=z0,k=0.4):
    return (U_ / k) * np.log(0.368*h/zo)

# Make a discharge function 
def Q(F,A):
    return F * A
 
'''
Calculate the water discharge in the
channel, in m3/s:
(a) at bankfull;
(b) at 0.5 m above bankfull.

'''
# a)
A_bank = d_max * W
U_bank = U_shear(d_max)
F_bank = estimate_sed_flux(U_bank,d_max)
Q_bank = Q(F_bank,A_bank)

# b)
d_new = d_max + 0.5 
A_new = d_new * W
U_new = U_shear(d_new)
F_new = estimate_sed_flux(U_new, d_new)
Q_new = Q(F_new, A_new)


print(f' When the River is [{d_max}(m),{d_new}(m)] deep it discharges [{Q_bank}(m3/s),{Q_new}(m3/s)]')