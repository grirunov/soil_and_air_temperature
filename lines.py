import numpy as np

data = np.loadtxt("data/soil_average.csv", delimiter=",")
import matplotlib.pyplot as plt

plt.plot(data[0,:],"b*-")
#plt.plot(data[1,:])
#plt.plot(data[2,:])
#plt.plot(data[3,:])
#plt.plot(data[4,:])

plt.show()

