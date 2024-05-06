def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Updated to match the width of the printed board

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        if check_winner(board):
            break
        if check_draw(board):
            print("It's a draw!")
            break
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                board[row][col] = player
                player = "O" if player == "X" else "X"
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter a valid number.")

    print_board(board)
    winner = check_winner(board)
    if winner:
        print("Player " + winner + " wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
