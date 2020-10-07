import random
import copy

from sudoku_solver import solve
import aux_sudoku_funcs as sud


def init_grid():
	"""
	This function uses a pseudorandom number generator to
	generate unique solved (filled) sudoku grids.
	"""
	new_grid = [[0 for _ in range(9)] for _ in range(9)] #create an empty grid
	initial_nums = [random.randint(1,9) for _ in range(10)] #draw 10 numbers from 1 to 9
	for num in initial_nums:
		not_safe = True
		while not_safe:
			rows, cols, boxes = sud.divide(new_grid)
			#pseudorandomly generate the coordinates, where one of the numbers is to be inserted
			init_row, init_col, init_box = sud.get_coordinates([random.randint(0,8), random.randint(0,8)])
			#check if it is safe to put that number in that spot
			if sud.is_safe(num, rows[init_row], cols[init_col], boxes[init_box]):
				#if it is, fill the space and move on to the next number
				new_grid[init_row][init_col] = num
				not_safe = False
	solve(new_grid) #solve the grid to fill it with numbers
	return new_grid


def generate_puzzle(grid, solution, num_filled):
	"""
	This function uses a backtracking algorithm to generate
	a sudoku puzzle with only one solution. It takes a solved grid
	(solution) as an argument and empties it one spot at a time
	until only a required number of filled spots (num_filled) is remaining.
	"""
	temp_grid = copy.deepcopy(grid) #copy the original (new) grid
	solve(temp_grid) #solve the original (new) grid
	#check if the puzzle still leads to the same solution
	if temp_grid == solution:
		#count non-empty spots in the grid
		non_zeros = 0
		for row in grid:
			for num in row:
				if num is not 0:
					non_zeros += 1
		#if the number of non-empty spots is equal to the required value,
		#finish the program
		if non_zeros <= num_filled:
			return True
		#if it is not, draw the coordinates of the next spot to be emptied
		while True:
			r,c = [random.randint(0,8),random.randint(0,8)]
			#check if the spot not already empty
			if grid[r][c] is not 0:
				val = copy.deepcopy(grid[r][c]) #save the value
				grid[r][c] = 0 #empty the spot
				#check if this new grid leads to the same solution
				if generate_puzzle(grid, solution, num_filled):
					return True
				#if it doesn't, restore the value
				grid[r][c] = val		
	#trigger backtracking
	return False


if __name__ == "__main__":
	new_filled_grid = init_grid()
	new_filled_grid_frozen = copy.deepcopy(new_filled_grid)
	num_of_filled = 35
	empty_grid = generate_puzzle(new_filled_grid, new_filled_grid_frozen, num_of_filled)
	print("PUZZLE: ")
	sud.print_grid(new_filled_grid)
	solve(new_filled_grid)
	print("")
	print("SOLUTION: ")
	sud.print_grid(new_filled_grid)
