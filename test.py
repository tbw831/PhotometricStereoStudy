import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])

A = np.vstack([x,np.ones(len(x))]).T

print(A)

print(np.linalg.lstsq(A, y, rcond=None)[0])