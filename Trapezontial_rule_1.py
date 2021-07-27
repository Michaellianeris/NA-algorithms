import numpy as np


def f(x):
   
     s=x**2+x+1
 
     return s


def F(x):
 
    
   s=x**3/3+x**2/2+x
 
   return s


x=[0,1]

quad=(1/2)*(f(x[0])+f(x[1]))


print('approximation with Trapezontial rule :', quad)
print('real solution of integration : ', F(1)-F(0))

