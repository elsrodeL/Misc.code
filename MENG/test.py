import numpy as np 
from scipy import constants
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

#CH10)1)
lambdas_ = [436,365,248,248]
apts = [0.38,0.48,0.6,0.65]
k1s = [0.8,0.6,0.6,0.5]
# from the above values calculate resolution given index i (dx)
dxs = []
for i,v in enumerate(lambdas_):
    dx = (k1s[i] * v)/apts[i]
    dxs.append(dx)

DOFs = [1.5,0.8,0.35,0.30]

plt.plot(DOFs,dxs)
plt.xlabel("Focus Depth +- (um)")
plt.ylabel("Resolution (nm)")
plt.show()


#CH10) 2) 

import numpy as np 
def gamma_p(dc,do):
    return (np.log(dc/do))**(-1)


def gamma_n(do, di):
    return (np.log(do/di))**(-1)


dc,dop =  80,30 
don,di = 9,6

yp = np.round(gamma_p(dc,dop),4)
yn = np.round(gamma_n(don,di), 4)

print(f'Contrast of the  (+) Photoresist is {yp}')
print(f'Contrast of the (-) Photoresist is {yn}')
print(f'Mean Constrast of the Photorists is {np.round(np.mean([yp,yn]),4)}')

# Use Arhenius Equation
T, rates = [60, 70, 80, 90], [29, 36, 62, 87]
T = list(map(lambda x: x + 273,T))
x,y = np.array([i**(-1) for i in T]), np.array(rates)
reg = LinearRegression().fit(x.reshape(-1,1),y.reshape(-1,1))
Ea = - reg.coef_/ constants.gas_constant
print(f'Activation Energy is {float(Ea)} J/mol')


# Max, min values for thickness of the oxide
tmax, tmin = 525, 475  # nm
# estimate some etching parameters
etch_rate = 5  # nm/s
etch_time = 2.5  # min
etch_time = etch_time * 60  # s

# Create a range of oxide:Si ectch selectivity
etch_selectivities = np.linspace(0, 1, 20)


def get_Si_erroded():
    rv_max = []
    rv_min = []

    #time it takes to remove oxide layer
    t_oxide_max = tmax/etch_rate
    t_oxide_min = tmin/etch_rate

    #time left to remove Si
    t_si_max = etch_time - t_oxide_max
    t_si_min = etch_time - t_oxide_min

    for s in etch_selectivities:
        # What rate the Si is etched
        si_e_rate = s*etch_rate
        # how much Si is removed
        rv_max.append(si_e_rate * t_si_max)
        rv_min.append(si_e_rate * t_si_min)

    x, ymax = np.array(etch_selectivities), np.array(rv_max)
    ymin = np.array(rv_min)
    plt.plot(x, ymax)
    plt.plot(x, ymin)
    plt.xlabel('Oxide: Si Etch Selectivity')
    plt.ylabel('Silicon Etched after 2.5 min')
    plt.title('Si loss function given Etch Selectivity and Oxide Thickness')
    plt.show()


get_Si_erroded()



