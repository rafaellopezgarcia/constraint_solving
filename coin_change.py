import cpmpy as cp
import numpy as np


# Alice needs to give Bob exactly 1.99 euros in change.
# She has six different types of coins with the following values: 1, 2, 5, 10, 25, and 50 cents. 
# However, she only has a limited number of each coin type:
# 20 coins of 1 cent
# 10 coins of 2 cents
# 15 coins of 5 cents
# 8 coins of 10 cents
# 4 coins of 25 cents
# 2 coins of 50 cents.

# How can Alice give Bob the exact change using the **fewest number of coins possible** while respecting the availability of each coin type?

coins = {
            1: 20,
            2: 10,
            5: 15,
            10: 8,
            25: 4,
            50: 2,
        }

values = np.array([key for key in coins.keys()])

# Step 1: Define your variables and their domain
dvars = np.array([cp.intvar(0, i) for i in coins.values()])

# Step 2: Define your constraints
model = cp.Model()
model.add(np.dot(values, dvars) == 199)

# Step 3: Define your function to optimize
model.minimize(cp.sum(dvars))

# Step 4: Solve
sol = model.solve()

# Step 5: Print out results
if sol:
    current_amount = 0
    current_coins = 0
    for key, sel in zip(values, dvars):
        if sel.value() != 0:
            coin_amount = sel.value() * key
            current_amount += coin_amount
            current_coins += sel.value()
            print(f"{sel.value()} coins of value {key} = {coin_amount} \t current amount = {current_amount} \t current number of coins: {current_coins}")

else:
    print("The solver was not able to find a solution to your model")



