import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as si
plt.style.use('dark_background')


def f(x) :
    
    s = 1/(1+25*np.power(x,2))
    
    return s


def natural_spline(n) :
    
    x_nodes=np.linspace(-1,1,n)
    y_val=f(x_nodes)
    c_spline = si.CubicSpline(x_nodes, y_val, bc_type=((1, 0), (1, 0)))
    x=np.linspace(-1,1,100)
    y=c_spline(x)
    c_spline_natural = si.CubicSpline(x_nodes, y_val, bc_type=((2, 0), (2, 0))) 
    y_natural=c_spline_natural(x)
    
    
    return x_nodes,y_val,x,y,y_natural


#------------------ Main Programme ----------------------#
    
n=20

x_nodes,y_val,x,y,y_natural = natural_spline(n)

plt.plot(x,f(x),'orchid')
plt.plot(x_nodes,y_val,'*')
plt.plot(x,y_natural,'purple')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1,1)
plt.legend(['f(x)','Points','natural spline'])
plt.show()


    
    
    

