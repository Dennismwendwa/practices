board1 = [

        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]

        ]

def solved_board(board):
    backtrack = 0


    def find_empty_cell(board):

        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col

        return -1, -1


    def is_valid(board, row, col, num):

        if num in board[row]:
            return False
        
        if num in [board[i][col] for i in range(9)]:
            return False
        #for i in range(9):
            #if num in board[i][col] == num:
                #return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if board[r][c] == num:

                    return False

        return True

    
    row, col = find_empty_cell(board)

    if row == -1 and col == -1:
        return True, backtrack

    for num in range(1, 10):
        if is_valid(board, row, col, num):

            board[row][col] = num

            solution, backtrack = solved_board(board)

            if solution:
                return True, backtrack

            board[row][col] = 0
            backtrack += 1
    return False, backtrack

def propagate_constraints(board, row, col, num):

    for c in range(9):
        if board[row][c] == 0:
            board[row][c] = -1

    for r in range(9):
        if board[r][col] == 0:
            board[r][col] = -1

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == 0:
                board[r][c] = -1


def print_board(board):
    for row in board:
        print(*row)



"""
sudoku_board = [
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 9, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 6, 0, 0, 0, 0, 0],
    [0, 0, 8, 9, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 0]
]

solution, backtrack_count = solved_board(sudoku_board)

if solution:
    print("Sudoku solved")
    print("Backtrack count:", backtrack_count)
    print_board(sudoku_board)
else:
    print("No solution found")


sudoku_board5 = [
    [5, 0, 1, 0, 6, 0, 0, 2, 4],
    [0, 6, 0, 4, 0, 0, 0, 7, 3],
    [0, 7, 0, 0, 0, 0, 1, 0, 5],
    [0, 0, 0, 0, 0, 7, 2, 0, 8],
    [8, 0, 2, 3, 9, 0, 5, 4, 7],
    [3, 0, 0, 2, 8, 4, 0, 9, 0],
    [0, 0, 5, 6, 0, 0, 4, 0, 0],
    [0, 2, 0, 0, 0, 0, 3, 1, 0],
    [9, 4, 6, 0, 0, 1, 7, 0, 0]
]
print()
print()


#solution, backtrack_count = solved_board(sudoku_board5)
if solution:
    print("Sudoku solved")
    print("Backtrack count:", backtrack_count)
 #   print_board(sudoku_board)
else:
    print("No solution found")


#sudoku_board2 = [
    [5, 6, 0, 0, 4, 0, 3, 0, 9],
    [3, 0, 0, 5, 0, 1, 0, 0, 0],
    [1, 9, 7, 0, 0, 0, 4, 5, 0],
    [0, 0, 1, 9, 0, 0, 0, 2, 7],
    [0, 0, 0, 0, 8, 0, 5, 4, 0],
    [0, 0, 0, 6, 0, 5, 1, 0, 8],
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 2, 0, 1],
    [0, 0, 0, 2, 0, 0, 0, 7, 0]
#]



print()
#solution, backtrack_count = solved_board(sudoku_board2)
if solution:
    print("Sudoku solved")
    print("Backtrack count:", backtrack_count)
 #   print_board(sudoku_board)
else:
    print("No solution found")

#expert
#sudoku_board3 = [
    [0, 8, 0, 1, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 3, 6],
    [0, 0, 1, 0, 0, 0, 5, 2, 0],
    [0, 0, 2, 0, 0, 0, 0, 9, 0],
    [8, 4, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0],
    [1, 0, 0, 0, 0, 8, 7, 0, 0],
    [0, 0, 0, 0, 4, 7, 0, 0, 2]
#]

print()
#solution, backtrack_count = solved_board(sudoku_board3)
if solution:
    print("Sudoku solved")
    print("Backtrack count:", backtrack_count)
#    print_board(sudoku_board)
else:
    print("No solution found")

sudoku_board4 = [
    [1, 0, 3, 0, 0, 4, 0, 8, 7],
    [0, 0, 0, 9, 0, 0, 0, 6, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [5, 0, 7, 0, 0, 3, 0, 0, 1],
    [0, 0, 0, 0, 4, 0, 3, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 8],
    [8, 0, 5, 0, 6, 0, 0, 7, 0],
    [0, 2, 0, 0, 0, 5, 0, 0, 0]
]

print()
solution, backtrack_count = solved_board(sudoku_board4)
if solution:
    print("Sudoku solved")
    print("Backtrack count:", backtrack_count)
    print_board(sudoku_board)
else:
    print("No solution found")
"""
sudoku_board5 = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

print()
solution, backtrack_count = solved_board(sudoku_board5)
if solution:
    print("Sudoku solved")
    print("Backtrack count:", backtrack_count)
    print_board(sudoku_board5)
else:
    print("No solution found")
