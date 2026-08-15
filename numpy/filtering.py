import numpy as np

ages = np.array([[21, 34, 64, 24, 65, 43, 29],
                 [42, 54, 12, 83, 58, 32, 48]])

#teenagers = ages[ages < 18]
#adults = ages[(18 <= ages) & (ages < 65)]
#seniors = ages[ages >= 65]
#evans = ages[ages % 2 == 0]
#odds = ages[ages % 2 != 0]

#print(teenagers)
#print(adults)
#print(seniors)
#print(evans)
#print(odds)

adults = np.where(ages >= 18, ages, 0)
print(adults)