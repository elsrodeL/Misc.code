import numpy as np
from scipy import constants

# Question 1)
# Properties of CaCo3 and Water
p_trav = 2  # g/cm3
c_content = 8*constants.milli   # mol/L

# Properties of smallest possible pond
h_cell = 0.03  # (m)
w_cell = 5  # (m)


# Number of Cells required for 1m height
num_cells = round(h_cell**(-1))
# each entry is height(Ci)
heights = [None]*num_cells


def set_h(H):
    for i, _ in enumerate(H):
        H[i] = 1 - (i*h_cell)
    return H

heights = set_h(heights)



## SOME CHEMISTRTY ##
# Ca(2+) + 2HCO3(-) <-> CO2 + CaCO3 + H2O
# Assume that all 8mill molar of C found in reactants is converted to products or K >> 1
# nC_products = nC_reactants
# nC_CaCo3 = 1/2 * n_C_reactants
Ca_Co3_conc = c_content/2  # mol/L
mconc_CaCo3 = Ca_Co3_conc/100.08  # g/L
# cm3/L (How much volume of CaCo3 precipitates per L of water)
vconc_CaCo3 = mconc_CaCo3/p_trav
# (m3/L) - Deposit per unit Liter flowed
vconc_CaCo3 = (vconc_CaCo3/(1*10**(6)))
####


def v_flow(d, s):
    # 1m3 : 1000L
    return (10*((d*s)**(1/2)))*1000


# Advance Cells one Day
def get_daily_deposit(H):
    for i, h in enumerate(H):
        if i == 0: 
            d = 0
        else:
            # estimate dh/dx = [d(hieght at midpoint for Ci)/(width_of_Ci))
            a_next = np.arctan((H[i-1] - H[i])/w_cell)
            a_prime = np.arctan((H[i] - H[-1])/((num_cells-(i))*w_cell))
            print(a_next,a_prime)
            a = a_prime
            # Get the daily deposit of CaCo3 on each cell
            d = v_flow(h_cell,a) *vconc_CaCo3  #(L/s) * (m3/L) = (m3/s)
            d = d*(60**2)*24*365.25  #(m3/day)
        H[i] = h + d
    return H
