import numpy as np


A=np.array([[4,6,10],[6,25,19],[10,19,62]]) # Matrix A

C=np.linalg.inv(A)  # Έτοιμη λύση της numpy

print('A^{-1} = ',C)

def Inverse(A) :   # Μέθοδος που ζητάει η Άσκηση 
    
    
    n=len(A)
    B=np.zeros((n,n))
    
    for i in range(0,n) :
        e=np.zeros(n)
        e[i]=1
        x=np.linalg.solve(A,e)
        B[:,i] = x
    
    return B
    


B=Inverse(A)
print('B=',B)

print(abs(B-C)) # Διαφορά έτοιμης λύσης με την μέθοδο