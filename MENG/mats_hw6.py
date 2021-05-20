from scipy import constants 

# Question 3) 
# used for some calculations 
def wt_fraction(a,b):
    return a/(a+b) , b/(a+b)

#g)
mNi, mCu = 8.2 * 58.69, 4.3 * 63.546
print(wt_fraction(mNi,mCu))

#h) 
mSn, mPb = 4.5*118.71 , 0.45*207.2
print(wt_fraction(mSn, mPb))

#5) 
print(30/0.14)

# 6)a)
Hf = 1.85 * 10**(9) #(J/m3)
gamma = 0.204 #(J/m^3)
dT = 295 #(K)
Tm = 1538 + 273.15 #(K)
crit_r = -2*gamma*Tm/Hf*(1/dT) #(m)
print(crit_r)

Ae = (16*constants.pi*(gamma**3)*(Tm**2)/(3*Hf**2))*(1/dT**2)
print(Ae)

#b)
# BCC Fe 
n_atoms = 0.75*constants.pi*1.35**3 / 0.292**3
print(n_atoms)




