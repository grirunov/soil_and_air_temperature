import numpy as np

data = np.loadtxt("data/soil_average.csv", delimiter=",")
import matplotlib.pyplot as plt

#for x in data:
    #print("x = ", x)
    #plt.plot(x)
#plt.plot(data[1,:])
#plt.plot(data[2,:])
#plt.plot(data[3,:])
#plt.plot(data[4,:])

#plt.show()
colors = ["r","m","y","0.2","g"]
print(data.shape)
for i in range (data.shape[0]):
    plt.plot(data[i,:],colors[i])

plt.show()