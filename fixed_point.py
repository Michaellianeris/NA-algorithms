import numpy as np 
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')



def f(x) :
    
    
    s = np.power(x,3)  - x - 1
    
    return s

def g(x) :
    
    s = np.sqrt(10/(4+x))
    
    return s



def fixed_point(x0,Tol,Nmax) :
    
    x=g(x0)
    e=np.abs(x-x0)
    n=1
    while n < Nmax and e > Tol :
          x0 = x
          x = g(x0)
          e=np.abs(x-x0)
          n += 1
          
          
    return x,n


#------------ MAIN PROGRAMME -------------#
    
x0=1.5 ;Tol=10**(-8) ;Nmax=100
x,n = fixed_point(x0,Tol,Nmax)

print ('Approximate Solution is ' , '%.6f' %x )
print ('number of steps is ' , n)

t=np.linspace(0,2,100)
y=f(t)

plt.plot(t,y,'cyan')
plt.legend(['f(x)'])
plt.ylabel('y')
plt.xlabel('x')
plt.show()


    