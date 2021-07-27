import numpy as np 
import matplotlib.pyplot as plt





def f(x) :
   
    s = np.power(x,3) + 4*np.power(x,2) - 10
    
    return s



def Bisection(a,b,Tol,Nmax) :
    
    Fa = f(a);Fb = f(b)
    d = b - a
    c = a + d/2
    Fc = f(c)
    n = 1
    d = d/2
    while n < Nmax and Fc != 0 and d > Tol :
          if np.sign(Fa) == np.sign(Fc) :
             a = c
             Fa = Fc
          else :
             b = c
             Fb = Fc
             
             
          c = a + d/2
          Fc = f(c)
          d = d/2
          n += 1
             
    
    return c,n,d,Fc


#------------ MAIN PROGRAMME -------------#
a=1;b=2 ;Tol=10**(-8) ;Nmax=100
c,n,d,Fc = Bisection(a,b,Tol,Nmax)

print ('Number of steps is ' , n )
print ('Approximation is' , c )
print ('The value of function is' , Fc )
print ('Distance from root less than ' , d)


t=np.linspace(1,2,100)
y=f(t)

plt.plot(t,y,'orange')
plt.legend(['f(x)'])
plt.ylabel('y')
plt.xlabel('x')
plt.show()











