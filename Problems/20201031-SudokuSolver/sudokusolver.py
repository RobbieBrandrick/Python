def print_puzzle(puzzle):            
	for i in range(0,  9):
		print("[", end = '')
		
		for j in range(0, 9):
			print(puzzle[i][j], end = '')
				   
		print("]")

def IsSudokuValid(puzzle):
	
	#horizontal validation
	for y in range(0, 9):
		
		found = []
		
		for x in range(0, 9):
			
			if puzzle[y][x] == 0:
				continue
							
			if found.count(puzzle[y][x]) != 0:
				return False
				
			found.append(puzzle[y][x])
			
	#vertical validation
	for x in range(0, 9):
		
		found = []
		
		for y in range(0, 9):

			if puzzle[y][x] == 0:
				continue

			if found.count(puzzle[y][x]) != 0:	
					 return False
						
			found.append(puzzle[y][x])
			
		#3x3 validation
		for y in range(0, 7, 3):
			for x in range(0, 7, 3):
				
				found = []
				
				for y2 in range(0, 3):
					for x2 in range(0, 3):

						value = puzzle[y + y2][x + x2]

						if value == 0:
							continue

						if found.count(value) != 0:	
							return False	
						 
						found.append(value)
											
								
						
	return True

def increment_yx(y, x):
	if x < 8:
		x += 1
	else:
		y += 1
		x = 0	

	return y, x
			
def sudoku_backtracking(puzzle, y, x):
	
	if y == 9:
		return True
		
	if puzzle[y][x] != 0:
		
		y2, x2 = increment_yx(y, x)
		
		if(sudoku_backtracking(puzzle, y2, x2)):
			return True
		else:
			return False
	
	for i in range(1, 10):
			
			puzzle[y][x] = i
			
			if IsSudokuValid(puzzle):
				
				y2, x2 = increment_yx(y, x)

				if sudoku_backtracking(puzzle, y2, x2):
					return True
				
			puzzle[y][x] = 0

	return False

def solve_puzzle1():
	puzzle = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
			[5, 2, 0, 0, 0, 0, 0, 0, 0], 
			[0, 8, 7, 0, 0, 0, 0, 3, 1], 
			[0, 0, 3, 0, 1, 0, 0, 8, 0], 
			[9, 0, 0, 8, 6, 3, 0, 0, 5], 
			[0, 5, 0, 0, 9, 0, 6, 0, 0], 
			[1, 3, 0, 0, 0, 0, 2, 5, 0], 
			[0, 0, 0, 0, 0, 0, 0, 7, 4], 
			[0, 0, 5, 2, 0, 6, 3, 0, 0] ] 

	print('Input: ')
	print_puzzle(puzzle) 
	print('')

	print('Output: ')
	sudoku_backtracking(puzzle, 0, 0)
	print_puzzle(puzzle)
	print('')

def solve_puzzle2():
	puzzle = [ 
		 [ 3, 1, 6, 5, 7, 8, 4, 9, 2 ],
         [ 5, 2, 9, 1, 3, 4, 7, 6, 8 ],
         [ 4, 8, 7, 6, 2, 9, 5, 3, 1 ],
         [ 2, 6, 3, 0, 1, 5, 9, 8, 7 ],
         [ 9, 7, 4, 8, 6, 0, 1, 2, 5 ],
         [ 8, 5, 1, 7, 9, 2, 6, 4, 3 ],
         [ 1, 3, 8, 0, 4, 7, 2, 0, 6 ],
         [ 6, 9, 2, 3, 5, 1, 8, 7, 4 ],
         [ 7, 4, 5, 0, 8, 6, 3, 1, 0 ] 
		]

	print('Input: ')
	print_puzzle(puzzle) 
	print('')

	print('Output: ')
	sudoku_backtracking(puzzle, 0, 0)
	print_puzzle(puzzle)
	print('')	

solve_puzzle1()
solve_puzzle2()