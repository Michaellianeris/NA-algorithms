import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as si
plt.style.use('dark_background')

def f(x) :
    
    s = 1/(1+25*np.power(x,2))
    
    return s


n=20
x_nodes=[]
for e in range(0,n) :
    s = np.cos(((2*e+1)/(n+1))*(np.pi/2))
    x_nodes.append(s)

y_val=f(x_nodes)
polynomial = si.lagrange(x_nodes, y_val) 



#x=np.linspace(-1,1,1000)
#y=polynomial(x)

x=[]
for e in range(0,n) :
    s = np.cos(((2*e+1)/(n+1))*(np.pi/2))
    x.append(s)



y=polynomial(x)

plt.plot(x,f(x),'blue')
plt.plot(x,y,'cyan')
plt.plot(x_nodes,y_val,'go')

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1.1,1.1)
plt.ylim(-0.3,1.2)
plt.legend(['f(x)','Lagrange/Chebyshev','points'])
plt.show()

