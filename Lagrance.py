import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as si
plt.style.use('seaborn-whitegrid')


def f(x) :
    
    s = 1/(1+25*np.power(x,2))
    
    return s



def Lagrance(n) :
    
    
    x_nodes=np.linspace(-1,1,n)
    y_val=f(x_nodes)
    polynomial = si.lagrange(x_nodes, y_val) 
    
    
    
    return polynomial,x_nodes,y_val


#----------- Main Programme --------------------#


n=10
x=np.linspace(-1,1,100)
polynomial,x_nodes,y_val = Lagrance(n)

plt.plot(x,f(x),'lime')
y=polynomial(x)
plt.plot(x_nodes,y_val,'+')
plt.plot(x,y,'green')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1,1)
plt.legend(['f(x)','Points','Lagrance'])
plt.show()