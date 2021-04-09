import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# inverse temp
iT = [i**(-1) for i in range(700, 1150, 50)]
# rate um/min
r = [0.04, 0.09, 0.2, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8]
# convert rate to m/s
r = [((i * 10**(-6))/60) for i in r]

# convert to np_array
iT, r = np.array(iT).reshape(-1, 1), np.array(r).reshape(-1, 1)


rv = []

def mk_graph(t, r):
    #plot data
    plt.scatter(t, r)
    plt.title('Growth Rate (m/s) vs. 1/T (K)')
    # fit linear regression here to determine -Ea/R and ln(A)
    model = LinearRegression()
    model.fit(t, r)
    Ea = (model.coef_ * 8.3144)[0] * -1
    # accounting
    rv.append(float(Ea))
    print(
        f" Ea from ({float(t[0])**(-1)} K - {float(t[-1])**(-1)} K) =  {float(Ea)} J/mol")
    print('\n')
    plt.show()
    print('\n')


# full plot
mk_graph(iT, r)
# smaller plots
mk_graph(iT[0:3], r[0:3])
mk_graph(iT[3:6], r[3:6])
mk_graph(iT[6:8], r[6:8])

# get the percentage diff btw largest and smallest Ea
ub, lb = max(rv), min(rv)
e = (ub-lb)/lb
print(e*100, '%')

