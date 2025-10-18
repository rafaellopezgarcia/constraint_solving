import cpmpy as cp
import numpy as np
from typing import List, Optional, Tuple

Grid = List[List[int]]

puzzle: Grid = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0],
]
puzzle = np.array(puzzle)
sz = 9 # width and length size
# Constraint variables
# Domain for each variable is [1,sz]
board = cp.intvar(1, sz, (sz, sz), "board")

model = cp.Model()

# All non-zero cells in puzzle should keep the same values
fixed_cells = np.nonzero(puzzle)
for i,j in zip(fixed_cells[0], fixed_cells[1]):
	model.add(board[i,j] == puzzle[i,j])

# All numbers in the same row should be different
# All numbers in the same column should be different
for i in range(sz):
	col_i = board[:,i]
	row_i = board[i,:]
	model.add(cp.AllDifferent(col_i))
	model.add(cp.AllDifferent(row_i))

# All numbers in the same 3x3 block should be different
for row in range(0,sz,3):
	for col in range(0,sz,3):
		block = board[row:row+3, col:col+3]
		model.add(cp.AllDifferent(block))	

model.solve()

for row in board:
	for cell in row:
		print(cell.value(), end=" ")
	print()
	
