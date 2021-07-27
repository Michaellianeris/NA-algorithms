import numpy as np


A=np.array([[10,2,1],[0,4,2],[1,2,2]])
b=np.array([3,2,1])



def my_back_solve(A,b) :
    n=len(A)
    x=np.zeros(n)
    x[n-1] = b[n-1] / A[n-1, n-1]
    for k in range(n-2, -1, -1):
        sums = b[k]
        for j in range(k+1, n):
            sums = sums - (A[k,j] * x[j])
        x[k] = sums / A[k,k]
    return x


x=my_back_solve(A,b)   
print('x=',x)
print('A x=', np.dot(A,x))


