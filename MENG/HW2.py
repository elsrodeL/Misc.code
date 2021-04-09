# Lukas Elsrode -- HW2 (02/12/2021)

import numpy as np
import random

#Question 1
def gen_randomCmatrix(n, m):
    # init stuff
    v = np.zeros(shape=(n, m), dtype='c16')
    # itt cols
    for j in range(m):
        # sample n floats from uniform distrobution ~ [0,2pi]
        phi_n = np.random.uniform(low=0, high=2*np.pi, size=n)
        
        # itt rows
        for i in range(n):             
        # randomly sample from list phi_n
            phi = random.choice(phi_n)
            v[i][j] = np.exp(1j*phi)
    return v

# Make the matrix
v = gen_randomCmatrix(1000, 10)

# Question 2
def overlap(a, b):
    assert a.shape == b.shape, f'A.shape {a.shape} != B.shape {b.shape}'
    O = np.conj(a.T)@b
    return O
   

# Question 3
V = overlap(v, v)

def print_elements(a):
    n, m = a.shape
    for j in range(m):
        for i in range(n):
            print(a[i][j])

print_elements(V)

#Question 4

N, M = v.shape
x = v.copy()
q = np.zeros(shape=(N, M), dtype='c16')

for j in range(M):
    q[:,j] = x[:,j] / (np.sqrt(overlap(x[:,j], x[:,j])))
    for r in range(j+1, M):
        x[:,r] = x[:,r] - (q[:,j]*overlap(q[:,j], x[:,r]))
    
# Question 5
Q = np.round(overlap(q, q))
print_elements(Q)