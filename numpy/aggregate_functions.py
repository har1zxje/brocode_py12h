import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10]])

#print(np.sum(arr))
#print(np.mean(arr))
#print(np.std(arr))
#print(np.var(arr))
#print(np.min(arr))
#print(np.max(arr))
#print(np.argmin(arr))
#print(np.argmax(arr))

#tinh tong theo tung cot
#print(np.sum(arr, axis = 0))

#tinh tong theo tung hang
print(np.sum(arr, axis = 1))