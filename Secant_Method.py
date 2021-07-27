import numpy as np 
import matplotlib.pyplot as plt




def f(x) :
    
    s = np.exp(-x**2) - np.cos(x) - 1
    return s




def Secant(x0,x1,Tol,Nmax) :
    
    slope=(f(x1)-f(x0))/(x1-x0)
    x=(x1-f(x1))/slope
    e=abs(x-x1)
    n=1
    while n < Nmax and e > Tol :
          x0=x1
          x1=x
          slope=f(x1)-f(x0)/(x1-x0)
          x=x1-f(x1)/slope
          e=abs(x-x1)
          n=n+1
          
          
    return x,n,f(x)


#------------ MAIN PROGRAMME -------------#
    
x0=-10 ; x1=-9 ;Tol=10**(-8) ;Nmax=100
x,n,fx = Secant(x0,x1,Tol,Nmax)

print ('Approximate Solution is ' , x )
print ('number of steps is ' , n)
print ('Value at approximate solution is ' , fx)



