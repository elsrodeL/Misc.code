import numpy as np 
from scipy import constants


def get_residence_time(f_net,P,T,V=5000):
    tau = (P/760)*(V/f_net)*(273/(T+273))
    return tau

