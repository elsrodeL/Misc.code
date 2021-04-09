# Lukas Elsrode -MENG 25610 2021- HW 1 - (01/26/2021)

from math import *

# Question 1
def gen_spherical(i,j):
    ''' Generates a randomish list of spherical co-ordinates 
        
        inputs : i,j - int 
        

    '''
    N = [i for i in range(i,j)]
    M = [i for i in range(i,j,2)]

    spherical = []

    # nested for loop for to independantly vary N,M
    for n in N:
        phi = pi/n
        for m in M:
            fi = pi/m
            rv = 1,phi,fi
            spherical.append(rv)

    return spherical

# list generated as in the question 
spherical = gen_spherical(2,7)

# Question 2 
def get_cartesian(corr_s):
    ''' Converts a list of 
    '''
    cart = []
    
    for r,phi,fi in corr_s:
        
        x = r * sin(phi)*cos(fi)
        y = r * sin(phi) *sin(fi)
        z = r * cos(phi)

        rv = x,y,z
        cart.append(rv)
    return cart


cartesian = get_cartesian(spherical)

#Question 3 
# return value
rv = zip(spherical,cartesian)


if __name__ == "__main__":
    print('\n')
    for i in rv:
        print(i)
    print('\n')

