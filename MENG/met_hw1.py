import numpy as np 
import matplotlib.pyplot as plt
from scipy import constants

# Question 3
def Ea(r):
    return -1.436/r

def Er(r):
    return (7.32*10**(-6))/r**(8)

def En(r):
    return Ea(r) + Er(r)
#a)
# make numberline
L = np.linspace(0,1,10000, endpoint=True)
# map functions
E_rep = list(map(lambda x: Er(x),L))
E_att = list(map(lambda x: Ea(x), L))
E_net = list(map(lambda x: En(x), L))
# plot the functions mapped to numberline
#plt.plot(L,E_att,label='E_attractive')
#plt.plot(L,E_net,label='E_net')
#En(r) is an exponential function with both +,- numbers so 
#plt.yscale("symlog")
# save picture
#plt.title('Energies of Na(+) and Cl(-) pair vs. Distance (nm)')
#plt.legend()
#plt.autoscale(enable=True)
#plt.savefig('fig.jpg')


#b) just use the data
#i)
# find r0 roughly 
r0s = []
for i, k in enumerate(E_net):
    if np.round(k,decimals=1) == 0:
        r0s.append(L[i])
# take mean value
r0 = (sum(r0s)/len(r0s))
print(f'Where (E_net = 0) <=> r0 = {r0} (nm)')

#ii)
# now get E0 given that dE/dr = 0 
# make function for dE/dr
def dEdr(r):
    # use an infintesimal to estimate a symetric derrivitive 
    h = constants.pico
    return (En(r+h) - En(r-h))/(2*h)
# derivitive of number line
dEs = list(map(lambda x: dEdr(x),L))
# find where dEn/dr roughly  = 0 
E0s = []
for i, k in enumerate(dEs):
    if np.round(k,decimals=1) == 0:
        E0s.append(L[i])
# get distance and then get Energy given En
E0_empirical = En((sum(E0s)/len(E0s)))
print(f'Where (dEn/dr = 0) is at energy min <=> E0 = En(r0) = {E0_empirical} (eV)')

#c)
# Make Energy function given derivation in Q2
def E0_ideal(A,B,n):
    k = ((n*B)/A)
    exp_a = -1/(n-1)
    exp_r = -n/(n-1)
    Ea = -A*k**exp_a
    Er = B*k**exp_r
    return Ea + Er

# input values from Q3
E0_m = E0_ideal(A=1.436,B=7.32*10**(-6),n=8)
print(f'Given [A=1.436,B=7.32e-6,n=8] <=> E0 = En(dEn/dr = 0): {E0_m} (eV)')

#Q4)
be = [68,324,406,849]
bp = [-39,660,1538,3410]
plt.plot(be,bp)
plt.xlabel('Bonding Energy (kJ/mol)')
plt.ylabel('Melting Temp (C)')
plt.title('Bonding Energy vs. Melting Point of Metals')
plt.savefig('bp.jpg')
# around 650 Kj/mol

# 5 
# Florine is a highly electronegative molecule. It also forms 
# hydrogen bonds 

# 6 : calculate degree of covalancy of bonding 
def IC(Xa,Xb):
    v = -((Xa - Xb)**2)/4
    return 1 - np.exp(v)

print(f'%IC MgO : {IC(3.44,1.31)}')
print(f'%IC GaP : {IC(2.19,1.81)}')
print(f'%IC CsF : {IC(3.98,0.79)}')
print(f'%IC CdS : {IC(2.58,1.69)}')
print(f'%IC CdS : {IC(3.44,1.83)}')

# 7: degree of covalancy in intermetallic compounds 
IC_MnAl6 = IC(1.61,1.55)
print(f'% IC Al6Mn: {IC_MnAl6}')
# 8: show that packing of HCP = 0.74

# 9: determine crystal structure of Nb 

# 10: a,b,c = 0.286,0.587,0.495  for Uranium what is the packing factor ? 
 
v = (0.286 * 0.587 * 0.495)*constants.nano 
mcell = v*19.05
print(f'mass ucell = {mcell} ')