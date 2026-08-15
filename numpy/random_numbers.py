import numpy as np

#rng = np.random.default_rng()

#print(rng.integers(low = 1, high = 100, size = (3, 2)))

#np.random.seed(seed = 1)
#print(np.random.uniform(low = -1, high = 1, size = (3,2)))

#rng = np.random.default_rng()
#arr = np.array([1, 2, 3, 4, 5])
#rng.shuffle(arr)
#print(arr)

rng = np.random.default_rng()
fruits = np.array(["🍎", "🥥", "🍌", "🍍"])
fruits = rng.choice(fruits, size = (3, 3))
print(fruits)