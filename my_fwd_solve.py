import numpy as np


A=np.array([[1,0,0],[1,2,0],[2,3,4]])
b=np.array([[1],[2],[3]])



def my_fwd_solve(A,b) :
    n=len(A)
    x=np.zeros(n)
    x[0] = b[0] / A[0, 0]
    for k in range(1,n):
        sums = b[k]
        for j in range(0, n):
            sums = sums - (A[k,j] * x[j])
        x[k] = sums / A[k,k]
    return x



x=my_fwd_solve(A,b)   
print('x=',x)
print('A x=', np.dot(A,x))