import numpy as np

def S(s,k,m):
    return 1-(1-s**k)**m

error_best=12737219021
k_best=-1
m_best=-1

for k in np.arange(0,101,0.1):
    for m in np.arange(0,1001,0.1):
        error = max(abs(1/10-S(1/3,k,m)), abs(9/10-S(1/2,k,m)))
        if error < error_best:
            error_best=error
            k_best=k
            m_best=m

print('k:',k_best)
print('m:',m_best)
print('error:',error_best)
