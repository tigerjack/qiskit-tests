import numpy as np
from math import sqrt

n = 3
zero = np.array([1, 0])
h = np.array([[1, 1], [1, -1]])
one = np.array([0, 1])

zeroi = zero
hi = h
for i in range(n - 1):
    hi = np.kron(hi, h)
    zeroi = np.kron(zeroi, zero)

print(hi)
print(zeroi)

a = np.kron(zeroi, one)
hi = np.kron(hi, h)

print(a)
print(hi)
