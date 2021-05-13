import numpy as np 
from scipy import constants

#10)
# Get latice spacing give diffraction angle  
def get_d(theta,lambda_,n):
    return (lambda_*constants.nano) / (2*np.sin(theta))
# degrees to radians
def get_radians(theta):
    return theta*(constants.pi/180)
#magnitude of indicies vector
def get_mag(a,b,c):
    return ((a**2)+(b**(2))+(c**(2)))**(1/2)


#radius of W given BCC structure
def get_R_BCC(theta,a,b,c,n):
    # get spacing d
    rad = get_radians(theta)

    d_hkl = get_d(rad,0.1542,1)
    d = get_d(rad,0.1542,n)
    print(f'2Theta = {theta}, d_spacing for ({a}{b}{c}) indicies are {d/constants.nano} - (nm)')
    # get radius 
    mag = get_mag(a,b,c)
    return (d_hkl*mag*3**(1/2))/4

# feed the functions 
angles = [[40,(1,1,0)],[55,(2,0,0)],[75,(2,1,1)],[85,(2,2,0)],[100,(3,1,0)]] 
for i,a in enumerate(angles):
    phi = a[0]
    A,B,C = a[1]
    r_bcc = get_R_BCC(phi,A,B,C,i+1)
    print(f'Radius is {r_bcc/constants.nano} (nm)')
    print('\n')