import numpy as np
import pylab

x = np.linspace(0, 20, 1000)  
y1 = np.cos(x)
y2 = np.sin(x)

pylab.plot(x, y1)
pylab.plot(x, y2)
pylab.show()