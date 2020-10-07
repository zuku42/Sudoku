import backend.aux_sudoku_funcs as sud

def solve(grid):
	"""
	This function uses a backtracking algorithm to solve
	any solvable sudoku grid. It takes a 9x9 grid with
	zeros representing the empty spots as an argument
	and fills it with numbers using recursion until
	no empty spots are remaining.
	"""
	indices = [0, 0] #a placeholder for the coordinates of the next empty spot

	#find the next empty spot,
	#if no empty spots in a grid, finish the program
	if not(sud.is_empty(grid, indices)):
		return True

	#divide the grid and find the row, column, and box the empty spot is in
	rows, cols, boxes = sud.divide(grid) 
	row_i, col_i, box_i = sud.get_coordinates(indices)

	for number in range(1,10):
		#try putting each number from 1 to 9 in an empty spot
		#if it safe, fill the empty spoty with that number
		if sud.is_safe(number, rows[row_i], cols[col_i], boxes[box_i]):
			grid[row_i][col_i] = number
			#check if the new grid leads to a solution
			if solve(grid):
				return True
			#if it doesn't, erase the number from the spot
			grid[row_i][col_i] = 0
	#trigger backtracking
	return False


if __name__ == "__main__":
	grid_example = [[5,3,0,0,7,0,0,0,0],
					[6,0,0,1,9,5,0,0,0],
					[0,9,8,0,0,0,0,6,0],
					[8,0,0,0,6,0,0,0,3],
					[4,0,0,8,0,3,0,0,1],
					[7,0,0,0,2,0,0,0,6],
					[0,6,0,0,0,0,2,8,0],
					[0,0,0,4,1,9,0,0,5],
					[0,0,0,0,8,0,0,7,9]]

	print("Sudoku puzzle to solve: ")
	sud.print_grid(grid_example)
	print("")
	print("Solution: ")
	if solve(grid_example):
		sud.print_grid(grid_example)
	else:
		print("No solution.")
