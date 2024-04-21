import numpy as np

data = np.loadtxt("data/soil_average.csv", delimiter=",")
import matplotlib.pyplot as plt

#colors = ["r","m","y","0.2","g"]
#print(data.shape)
#for i in range (data.shape[0]):
    #plt.plot(data[i,:],colors[i])

#plt.show()

heights = (25,117,535,1070,1700)
import statistics as st

#line1 = data[0,:]
#line2 = data[1,:]
#line_diff = line1-line2
#print(line_diff)

#a = statistics.mean(line_diff)
#print(a/(heights[1]-heights[0]))
labels_a = ("Sam-Zug","Zug-Tqi","Tqi-Pas","Pas-Bak")

for j in range (data.shape[0]-1):
    line1 = data[j,:]
    line2 = data[j+1,:]
    line_diff = line1-line2
    b = line_diff/(heights[1]-heights[0])
    #print(st.mean(b))
    #for k in range (b.shape[0]):
    plt.plot(b,label=labels_a[j])
def months_and_meters():
        plt.ylabel("deg/m")
        plt.legend()
        plt.xticks(np.arange(12))
        plt.grid(axis="x")
        plt.show()
months_and_meters()