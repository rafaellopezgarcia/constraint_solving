import cpmpy as cp
import numpy as np
"""
TODO: define the magic sum as a function of n.
Use // operator to get the integer part of a division (div operator).
"""

def magic_square(n: int):
    """
    Solves a magic square.

    Args:
        n (int): Size of the magic square.

    Returns:
        List[List[int]]: Magic square.
    """
    magic_sum = n*(n**2+1)// 2  # sum of each row, column and diagonal

    ## Decision variables
    square = cp.intvar(0, magic_sum,shape=(n,n), name="square")

    ## Model
    model = cp.Model()

    ## Constraints

    # Each cell must have a different value
    model.add(cp.AllDifferent(square))

    for i in range(n):
        # Each row must sum up to magic_sum
        model.add(cp.sum(square[i,:]) == magic_sum)
        # Each column must sum up to magic_sum
        #model.add(cp.sum(square[:,i]) == magic_sum)

    model.add([cp.sum(square[:,i]) == magic_sum for i in range(n)])

    # The diagonal and antidiagonal each have to sum up to magic_sum
    model.add(cp.sum(np.diagonal(square)) == magic_sum)
    model.add(cp.sum(np.diagonal(np.fliplr(square))) == magic_sum)

    ## Solve
    sol =  model.solve()

    if sol:
        for r in range(n):
            for c in range(n):
                print(square[r,c].value(), end=" ")
            print()
        print(f"The magic sum is {magic_sum}")
    else:
        print("The solver did not find any solution")


magic_square(4)

