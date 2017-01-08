import numpy as np

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

a1 = [13,14,15,16]
b1 = [17,18,19,20]
c1 = [21,22,23,24]

cpa = np.array([a, b, c])

print cpa.shape

cpa1 = np.array([[a, b, c], [a1, b1, c1]])

print cpa1.shape

print cpa1[1,1,1]

x = np.array([1, 2, 3, 4, 5])

print np.mean(x)
np.corr
plt.