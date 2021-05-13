import numpy as np 
from scipy import constants

# Question 1) 
# Properties of CaCo3 and Water 
p_trav = 2 #g/cm3
c_content = 8*constants.milli   # mol/L

# Properties of smallest possible pond
h_cell = 0.03   #m 
w_cell = 5      #m

# Number of Cells required for 1m height
num_cells = h_cell**(-1)

# Get the characteristic slope of water surface - (radians)
def get_s(n_cells):
    #Width of Last Cell 
    w_last = w_cell*(num_cells - n_cells)
    # Vertical Hieght diff between last and first cell
    h = n_cells*h_cell
    # Get the slope
    a = np.arctan(h/w_last)
    return a

# Get the flow velocity (L/s) 
def v_flow(d,s):
    # 1m3 : 1000L
    return (10*((d*s)**(1/2)))*1000


# Ca(2+) + 2HCO3(-) <-> CO2 + CaCO3 + H2O
# Assume that all 8mill molar of C found in reactants is converted to products or K >> 1 
# nC_products = nC_reactants 
# nC_CaCo3 = 1/2 * n_C_reactants

Ca_Co3_conc = c_content/2 # mol/L
mconc_CaCo3 = Ca_Co3_conc/100.08 # g/L
vconc_CaCo3 = mconc_CaCo3/p_trav #cm3/L (How much volume of CaCo3 precipitates per L of water)
vconc_CaCo3 = (vconc_CaCo3/(1*10**(6))) #(m3/L) - Deposit per unit Liter flowed  

# acct for time taken to deposit the Trav given conditions
t_total = []
for i in range(round(num_cells) + 1):
    # Vol required to fill above bottom most cell - (m3) 
    A = w_cell*(w_cell*(i+1))   #(m2) - Assume Area of the base of the cell, assume depth = w_cell regardless of width
    Vol_fill = A*h_cell         #(m3)

    # Get the required water flow for this deposit - (L)
    fluid_vol_needed = Vol_fill/vconc_CaCo3 # (L)


    # Get Flow Rate given the angle and width of last cell - (L/s)
    s = get_s(round(num_cells - i))
    vf = v_flow(h_cell,s) # (L/s)
    
    # Get the time required to percipitate and join adjacent pools
    t_req = fluid_vol_needed/vf # (s)
    t_req = t_req/(60**(2))     # (h)
    t_req = t_req/24            # (days)
    t_req = t_req/365.25        # (years)


    print(f'The {round(num_cells - i)}st Cell joined the pond above after - {t_req} - (years) = {h_cell*i} Has Risen (m)')
    t_total.append(t_req)
# The function is asymptotic so it actually never reaches 1.0m but lets just take the converging value as the final value... 
# and take the second smallest time step before that to encapsulate the entire process
t_total = t_total[:len(t_total)-1]
# Show timescale deposition rates 
print('\n')
print('TOTAL_TIME:',sum(t_total),'(years)')
print('DEPOSITION RATE:',1/sum(t_total),'(m/year)')

# Estimate rate of timelapse
dt_1 = 10/12 #years
dh_1 = 1 # m 
rate_est_y = dh_1/dt_1
print('ESTIMATE CLASS:',rate_est_y,'(m/year)')
# Estimate rate of deposition given a 5m tall temple
dt = 1021   # (years)
dh = 2
rate_est = dh/dt
print('ESTIMATE TEMPLE:',rate_est,'(m/year)')
