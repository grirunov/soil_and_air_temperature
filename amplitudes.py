import numpy as np

data = np.loadtxt("data/soil_average.csv", delimiter=",")
heights = (25, 117, 535, 1070, 1665)
for i in range(data.shape[0]):
    c = np.zeros(4)
    data1 = data[i, :]
    c[0] += heights[i]
    c[1] += np.max(data1)
    c[2] += np.min(data1)
    c[3] = c[1] - c[2]
    print(c)
