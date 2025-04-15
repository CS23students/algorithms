def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board)
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solve_n_queens(board, row + 1, n) or res
            board[row][col] = 0  # backtrack
    return res

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists.")

# Example: try with N = 4 or N = 8
n = int(input("Enter the value of N for N-Queens: "))
n_queens(n)
