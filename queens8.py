# Check if queen can be placed
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


# Solve 8 queens
def solve_queens(board, row):
    if row == 8:
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
            board[row] = -1

    return False


# Main
board = [-1] * 8
solve_queens(board, 0)

# Print 8x8 board
print("8 Queens Solution (8x8 Board):\n")
for row in range(8):
    for col in range(8):
        if board[row] == col:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()
