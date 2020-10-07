import numpy as np


def divide(grid):
	"""
	This function divides a 9x9 sudoku grid represented by
	a list of 9 lists (of 9 elements each) into three lists
	each representing either rows, columns or 3x3 subgrids
	(boxes) of the original grid.
	"""
	rows = grid
	grid_arr = np.asarray(grid)
	grid_arr_t = grid_arr.T
	columns = grid_arr_t.tolist()
	boxes = [[] for _ in range(9)]
	j = 0
	i = 1
	for row in grid:
		for k in range(3):
			boxes[j].append(row[k])
			boxes[j+1].append(row[k+3])
			boxes[j+2].append(row[k+6])
		if i%3 == 0:
			j += 3
		i += 1
	return rows, columns, boxes


def get_coordinates(ind):
	"""
	This function takes a pair of numbers representing
	the coordinates of a single space in a sudoku grid
	and returns the indices of the row, column and box
	the space belongs to.
	"""
	row_num = ind[0]
	col_num = ind[1]
	if row_num <= 2 and col_num <= 2:
		box_num = 0
	elif row_num <= 2 and 3 <= col_num <=5:
		box_num = 1
	elif row_num <= 2 and 6 <= col_num <= 8:
		box_num = 2
	elif 3 <= row_num <= 5 and col_num <=2:
		box_num = 3
	elif 3 <= row_num <= 5 and 3 <= col_num <= 5:
		box_num = 4
	elif 3 <= row_num <= 5 and 6 <= col_num <=8:
		box_num = 5
	elif 6 <= row_num <= 8 and col_num <= 2:
		box_num = 6
	elif 6 <= row_num <= 8 and 3 <= col_num <=5:
		box_num = 7
	elif 6 <= row_num <= 8 and 6 <= col_num <= 8:
		box_num = 8
	return row_num, col_num, box_num


def is_safe(num, row, col, box):
	"""
	This function checks whether it is safe to put
	a given number (num) in a space given by its
	row, column, and box indices.
	"""
	#if number already in the same row, column, or box - not safe
	if any([num in row, num in col, num in box]):
		return False
	#safe otherwise
	return True


def is_empty(grid, coordinates):
	"""
	This function checks if there are any empty
	spots in a given sudoku grid.
	"""
	for row in range(9):
		for column in range(9):
			#if an empty spot encountered, get its coordinates
			#and break the loop by returning True
			if grid[row][column] == 0:
				coordinates[0] = row
				coordinates[1] = column
				return True
	#no empty spots otherwise
	return False


def print_grid(grid):
	"""
	This function prints out the sudoku grid
	in a readible manner.
	"""
	for row in grid:
		for item in row:
			if item == 0:
				print("_", end=" ")
			else:
				print(item, end=" ")
		print("")

