board = [
    [4, 6, 2, 5, 9, 1, 3, 0, 7],
    [1, 3, 9, 6, 8, 7, 4, 2, 5],
    [7, 5, 8, 3, 4, 2, 1, 9, 6],
    [6, 9, 1, 7, 3, 8, 2, 5, 4],
    [5, 2, 0, 9, 6, 4, 7, 1, 8],
    [8, 7, 4, 2, 1, 5, 9, 6, 3],
    [9, 8, 7, 4, 0, 6, 5, 3, 1],
    [3, 1, 5, 8, 7, 9, 6, 4, 2],
    [2, 4, 6, 1, 5, 3, 8, 7, 0]
]

solvedboard = [
    [4, 6, 2, 5, 9, 1, 3, 8, 7],
    [1, 3, 9, 6, 8, 7, 4, 2, 5],
    [7, 5, 8, 3, 4, 2, 1, 9, 6],
    [6, 9, 1, 7, 3, 8, 2, 5, 4],
    [5, 2, 3, 9, 6, 4, 7, 1, 8],
    [8, 7, 4, 2, 1, 5, 9, 6, 3],
    [9, 8, 7, 4, 2, 6, 5, 3, 1],
    [3, 1, 5, 8, 7, 9, 6, 4, 2],
    [2, 4, 6, 1, 5, 3, 8, 7, 9]
]

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end = " ")
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end= " ")

def get_user_input():
    while True:
        try:
            row = int(input("Enter row (1-9): ")) - 1
            col = int(input("Enter coloumn (1-9): ")) - 1
            value = int(input("Enter value (1-9): "))

            if row not in range(9) or col not in range(9):
                print("Row and coloumn must be between 1-9. Try again u got this")
                continue
            if value not in range(1, 10):
                print("Value must be between 1-9. run it back bro.")
                continue
            return row, col, value
        except ValueError:
            print("stop trying to break my game >:(")

def rules(board,solvedboard, row, col, value):
    if board[row][col] and solvedboard[row][col] == value:
        return True
    else:
        return False

def place_value(board, row, col, value):
    
    if board[row][col] == 0:
        board[row][col] = value
        state = rules(board, solvedboard, row, col, value)
        if not state:
            board[row][col] = 0
            print("WRONG!!!!!!")
        else:
            print("correct!!!") 
    else:
        print("This cell is already filled. Try a different position.")

def winner(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

#MAIN HELL YEAH
print("Solve for '0' on the board")
while True:
    win = winner(board)
    print_board(board)
    if win == True:
        print("you won :)")
        break
    row, col, value = get_user_input()
    place_value(board, row, col, value)