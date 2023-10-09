def solve_sudoku(board):
    backtrack = 0  # Variable to count backtracking occurrences

    def find_empty_cell(board):
        # Find the next empty cell represented by 0
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return -1, -1

    def is_valid(board, row, col, num):
        # Check if the number is already present in the row
        if num in board[row]:
            return False

        # Check if the number is already present in the column
        if num in [board[i][col] for i in range(9)]:
            return False

        # Check if the number is already present in the 3x3 grid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    # Find the next empty cell
    row, col = find_empty_cell(board)

    # If no empty cell is found, the puzzle is solved
    if row == -1 and col == -1:
        return True, backtrack

    # Try placing numbers from 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number in the empty cell
            board[row][col] = num

            # Recursively solve the rest of the puzzle
            solution, backtrack = solve_sudoku(board)

            if solution:
                return True, backtrack

            # If the solution is not valid, backtrack and try the next number
            board[row][col] = 0
            backtrack += 1

    # If no number can be placed, backtrack to the previous cell
    return False, backtrack


def print_board(board):
    for row in board:
        print(*row)


# Example Sudoku puzzle
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solution, backtrack_count = solve_sudoku(sudoku_board)
if solution:
    print("Sudoku solved!")
    print("Backtrack count:", backtrack_count)
    print_board(sudoku_board)
else:
    print("No solution found.")


print()
print()

sudoku_board1 = [
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


solution, backtrack_count = solve_sudoku(sudoku_board1)
if solution:
    print("Sudoku solved!")
    print("Backtrack count:", backtrack_count)
    print_board(sudoku_board)
else:
    print("No solution found.")

sudoku_board2 = [
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 5, 3, 0, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 3, 2, 0, 0, 0, 8, 0],
    [0, 6, 0, 5, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 9, 7, 0, 0]
]

print()
print()
solution, backtrack_count = solve_sudoku(sudoku_board2)
if solution:
    print("Sudoku solved!")
    print("Backtrack count:", backtrack_count)
    print_board(sudoku_board)
else:
    print("No solution found.")

print()
sudoku_board4 = [
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 5, 3, 0, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 3, 2, 0, 0, 0, 8, 0],
    [0, 6, 0, 5, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 9, 7, 0, 0]
]

print()
print()
solution, backtrack_count = solve_sudoku(sudoku_board4)
if solution:
    print("Sudoku solved!")
    print("Backtrack count:", backtrack_count)
    print_board(sudoku_board)
else:
    print("No solution found.")

sudoku_board5 = [
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 3, 1],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 4],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0]
]

print()
print()
solution, backtrack_count = solve_sudoku(sudoku_board5)
if solution:
    print("Sudoku solved!")
    print("Backtrack count:", backtrack_count)
    print_board(sudoku_board)
else:
    print("No solution found.")

print()
print()

print("allmost over, one to go")
print("\nIts over now")
