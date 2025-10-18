import numpy as np

import cpmpy as cp
from cpmpy import cpm_array

cities = 5
distance = np.random.randint(10, 51, size=(cities, cities))
np.fill_diagonal(distance, 0)
distance = cpm_array(distance)

S = cp.intvar(1, cities, shape=cities)
model = cp.Model()

model += cp.Circuit(S)
model.minimize(sum(distance[city, S[city]] for city in range(cities)))

model.solve()

print(distance)

for s in S:
    print(s.value())

print(sum(distance[city, S[city]] for city in range(cities)))