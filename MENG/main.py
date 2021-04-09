from math import *

# orders of magnitude 
mu = 10**(-6)
p = 10**(-12)
n =  10**(-9)
m = 10**(-3)
c = 100
k = 1000

# Question 1 
print('---- Question 1 ---- ')
print('\n')

# assumptions
Kb = 1.38 * 10**(-23) # boltzman constant (Jk^-1)
d_N2 = 0.375*n  # Diameter of nitrogen molecule (m) 
L_min, L_max = 0.02, 5 # critical dimension (m)

# get molecular density in cylinder
def get_n(p,t):
    return p/(Kb*t)

# get mean free path 
def get_lambda(d,n):
    return ((2**(1/2))*pi*n*(d**(2)))**(-1)

# get knusen number 
def get_Kn(d,n,L):
    return get_lambda(d,n)/L


# get range 

def get_Kn_range(Tmin,Tmax,Pmin,Pmax):

    # find min,max (n)
    ns_min = get_n(Pmin,Tmax)
    ns_max = get_n(Pmax,Tmin)
    
    Kn_min = get_Kn(d_N2,ns_min,L_max)
    Kn_max = get_Kn(d_N2,ns_max,L_min)

    return Kn_min, Kn_max
 
# Sputtering
Ts_min, Ts_max = 373, 473  # K
Ps_min, Ps_max = (0.02 * 133.322), (0.1 * 133.322)  # Nm^-2
Kns_min, Kns_max = get_Kn_range(Ts_min,Ts_max,Ps_min,Ps_max)
print(f'Sputtering Kn range ~ ({Kns_min},{Kns_max}) (J/N)')

# Evaporation
Te_min, Te_max = 300,350   # K
Pe_min, Pe_max = ((10**(-9)) * 133.322), ((10**(-7)) * 133.322)  # Nm^-2
Kne_min, Kne_max = get_Kn_range(Te_min, Te_max, Pe_min, Pe_max)
print(f'Evaporation Kn range ~ ({Kne_min},{Kne_max}) (J/N)')

# MBE
Tm_min, Tm_max = 300, 350  # K
Pm_min, Pm_max = ((10**(-11)) * 133.322), ((10**(-9)) * 133.322)  # Nm^-2
Knm_min, Knm_max = get_Kn_range(Tm_min, Tm_max, Pm_min, Pm_max)
print(f'MBE Kn range ~ ({Knm_min},{Knm_max}) (J/N)')

# RIE 
Tr_min, Tr_max = 290, 340  # K
Pr_min, Pr_max = (0.001 * 133.322), (0.3 * 133.322)  # Nm^-2
Knr_min, Knr_max = get_Kn_range(Tr_min, Tr_max, Pr_min, Pr_max)
print(f'RIE Kn range ~ ({Knr_min},{Knr_max}) (J/N)')
print('\n')


##########################################
# Question 4 
print('---- Question 4 ----')
print('\n')

A_min, A_max = pi * (0.0001)**(2), pi * (0.1)**(2) 
m_N2 = 4.6528 * 10**(-26)

def get_Jleak(p,A,T):
    return ((p*A)/(4*Kb*T))*(((8*Kb*T)/(pi*m))**(1/2))

# Pm_min = 10^(-11) torr 
J_min = get_Jleak(Pm_min, A_min, Tm_max)
J_max = get_Jleak(Pm_min,A_max,Tm_min)

print(f' The leak rate required for an MBE system to achieve base pressure is in the range of ({J_min},{J_max}) - (molecules/s)')
print('\n')


# Question 6 

print(' ----  Question 6 ----')
print('\n')

print('''
A 99.9999% pure sample means that 0.0001%  of atoms in the layer are impurities. 
table 33.1 indicates that this level of impurity is incroperated at a deposition rate 
of (10 -100) (nm/s) and a partial pressure of (10^(-9) -  10^(-8)) (torr) 
if the deposition rate is lower than the pressure will be closer 10^(-9) torr and
if the deposition rate is higher than the pressure will be on the lower range.
This is because as more atoms on the substrate a lower pressure or penetrating power 
is required to allow more impurities to impregnate the substrate ''')

print('\n')


print(' ---- Question 8 ---- ')
print('\n')

V = 50 #L 
fr = (200 * 0.000000017)  # m^(3)/s
p = (20 * m)* 133.322 #N/m^(2)
T_min, T_max = 100,170 # K 


def residence_time(p,v,f,t):
    return (p*(v/f)*(273/t))


tau_max, tau_min = residence_time(p, V, fr, T_min),  residence_time(p, V, fr, T_max)
t_min, t_max = tau_max**(-1), tau_min**(-1)
print(f'The shortest possible pulsing period for the Bosh process is {t_min} (s^(-1)) for these conditions')
print('\n')
