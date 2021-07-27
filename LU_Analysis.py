import scipy.linalg as spla
import numpy as np
import matplotlib.pyplot as plt 



def LU(A) :
    
                      
    P,L,U=spla.lu(A)
    
    return P,L,U



def my_back_solve(U,y) :
    n=len(U)
    x=np.zeros(n)
    x[n-1] = y[n-1] / U[n-1, n-1]
    for k in range(n-2, -1, -1):
        sums = y[k]
        for j in range(k+1, n):
            sums = sums - (U[k,j] * x[j])
        x[k] = sums / U[k,k]
    return x



def my_fwd_solve(L,b) :
    n=len(L)
    y=np.zeros(n)
    y[0] = b[0] / L[0, 0]
    for k in range(1,n):
        sums = b[k]
        for j in range(0, n):
            sums = sums - (L[k,j] * y[j])
        y[k] = sums / L[k,k]
    return y

#----------------Main Programme ----------------------------------#

A=np.array([10,-7,0],[-3,2,6],[5,-1,5])
b=np.array([9,-17,-31,11])


P,L,U=LU(A)

b=np.dot(P.T,b)


y=my_fwd_solve(L,b)
x=my_back_solve(U,y)

print(x)
k=np.linalg.solve(A,b)
print(k)




