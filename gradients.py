import numpy as np
import matplotlib.pyplot as plt

filename = input("Enter the file name: example (data/soil_average.csv): ")
data = np.loadtxt(filename, delimiter=",")
heights = (25, 117, 535, 1070, 1665)
labels_a = ("Sam-Zug", "Zug-Tqi", "Tqi-Pas", "Pas-Bak")
xpoints = np.linspace(1, 13, num=13)
c = np.zeros(13)
#print("data= ", data)
for i in range(data.shape[0] - 1):
    line1 = data[i, :]
    line2 = data[i + 1, :]
    line_diff = line1 - line2
    b = line_diff / (heights[i + 1] - heights[i]) * 100
    c += b
    b = np.round(b,2)
    plt.plot(xpoints,b, label=labels_a[i])
    print("b= ", b)
c /= (data.shape[0] - 1)
c = np.round(c,2)
print("c= ", c)
plt.plot(xpoints, c, "0.0", label="Average")
plt.ylabel("deg/100m")
plt.xlabel("Months")
plt.legend()
plt.xticks(np.arange(13))
plt.grid(axis="x")
plt.show()
