import numpy as np

#scalar arithmetic
#array = np.array([1, 2, 3])
#thuc hien phep toan thang vao trong mang

#print(array + 1)
#print(array -2)
#print(array * 3)
#print(array / 4)
#print(array ** 5)

#vectorized math funcs
#array = np.array([1.4, 2.9, 3.6])

#print(np.sqrt(array))
#print(np.round(array))
#print(np.pi)

#ex
#radii = np.array([1, 2, 3])
#print(np.pi * radii ** 2)

#elemet-wise arithmetic
#arr1 = np.array([1, 2, 3])
#arr2 = np.array([4, 5, 6])

#print(arr1 + arr2)
#print(arr1 - arr2)
#print(arr1 * arr2)
#print(arr1 / arr2)
#print(arr1 ** arr2)

#comparison operators
scores = np.array([36, 12, 100, 23, 22, 99])

#print(scores >= 65)
scores[scores< 60] = 0
print(scores)

