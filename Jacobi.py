import numpy as np


x0=np.zeros(4)
TOL=10**(-5)
NMAX=100
A=np.ones((4,4))
A[0,0]=6
A[1,1]=7
A[2,2]=8
A[3,3]=9

x_sol=np.ones((4))
b=np.dot(A,x_sol)

def Jacobi(A,b,NMAX,TOL,x0):
    m=A.shape[0]
    
    D=np.diag(np.diag(A))
    U=np.triu(-A,1)
    L=np.tril(-A,-1)
   
    
    y=np.dot(L+U,x0)+b
    x=np.linalg.solve(D,y)
    e=np.linalg.norm(x-x0)
    
    M=D
    N=(L+U)
    n=1
    while ( n < NMAX) and (e > TOL ):
        x0=x
        y=np.dot(N,x0)+b
        x=np.linalg.solve(M,y)
        e=np.linalg.norm(x-x0)
        n=n+1
        
        
    return x,n,e

print(Jacobi(A,b,NMAX,TOL,x0))
