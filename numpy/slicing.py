import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

#lay theo cac hang
# array[start:end:step]
#print(array[0:4:2])
#neu dat step la -1 thi se dao nguoc ma tran, dat theo so nhan cua -1 nhu -2, -3, ... se dao nguoc nhung co step

#lay theo cac cot
#print(array[:, 1::2])

#lay theo ca 2
#print(array[0:2, 0:2])
print(array[0:2, 2:4])