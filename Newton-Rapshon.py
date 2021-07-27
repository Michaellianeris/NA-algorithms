import numpy as np 
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')



def f(x) :
   
    s = np.power(x,3)  - x - 1
    
    return s


def f_p(x):
    
    s = 3*np.power(x,2)  - 1
    
    return s



def Newton_Raphson(x0,Tol,Nmax) :
    
    x=x0 - f(x0)/f_p(x0)
    e=abs(x-x0)
    n=1
    while n < Nmax and e > Tol :
          x0 = x
          x = x0 - f(x0)/f_p(x0)
          e=abs(x-x0)
          n += 1
          
          
    return x,n,f(x)


#------------ MAIN PROGRAMME -------------#
    
x0=1.5 ;Tol=10**(-8) ;Nmax=100
x,n,fx = Newton_Raphson(x0,Tol,Nmax)

print ('Approximate Solution is ' , x )
print ('number of steps is ' , n)
print ('Value at approximate solution is ' , fx)

t=np.linspace(0,2,100)
y=f(t)

plt.plot(t,y,'grey')
plt.legend(['f(x)'])
plt.ylabel('y')
plt.xlabel('x')
plt.show()

