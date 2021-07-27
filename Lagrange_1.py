import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as si
plt.style.use('dark_background')



x_nodes=[0,1,1.5,2,3]
y_val=[5,-6,2,-1,16]
polynomial = si.lagrange(x_nodes, y_val) 
    
x=np.linspace(0,3,1000)
y=polynomial(x)

plt.plot(x,y,'lime')
plt.plot(x_nodes,y_val,'*')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-0.1,3.1)
plt.legend(['Points','Lagrance'])
plt.show()