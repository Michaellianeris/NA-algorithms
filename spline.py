import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as si
plt.style.use('seaborn-whitegrid')


def f(x) :
    
    s = 1/(1+25*np.power(x,2))
    
    return s


def spline(n) :
    
    x_nodes=np.linspace(-1,1,n)
    y_val=f(x_nodes)
    x=np.linspace(-1,1,100)
    y = np.interp(x,x_nodes, y_val)
    
    
    return x_nodes,y_val,x,y


#------------------ Main Programme ----------------------#
    
n=10

x_nodes,y_val,x,y = spline(n)

plt.plot(x,f(x),'gold')
plt.plot(x_nodes,y_val,'*')
plt.plot(x,y,'yellow')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1,1)
plt.legend(['f(x)','Points',' spline'])
plt.show()


