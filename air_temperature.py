import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data/air_average.csv", delimiter=",")
print(data)
heights = (25, 117, 535, 1070, 1795)
labels_a = ("Sam-Zug", "Zug-Tqi", "Tqi-Pas", "Pas-Roka")
xpoints = np.linspace(1, 12, num=12)
c = np.zeros(12)
for i in range(data.shape[0] - 1):
    line1 = data[i, :]
    line2 = data[i + 1, :]
    line_diff = line1 - line2
    b = line_diff / (heights[i + 1] - heights[i]) * 100
    plt.plot(xpoints, b, label=labels_a[i])
    c += b
c /= (data.shape[0] - 1)
plt.plot(xpoints, c, "k", label="Average")
plt.ylabel("deg/100m")
plt.xlabel("Months")
plt.legend()
plt.xticks(np.arange(13))
plt.grid(axis="x")
print(np.mean(c))
plt.show()
