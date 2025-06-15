board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(mark):
    return (
        (board[0] == board[1] == board[2] == mark) or
        (board[3] == board[4] == board[5] == mark) or
        (board[6] == board[7] == board[8] == mark) or
        (board[0] == board[3] == board[6] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[0] == board[4] == board[8] == mark) or
        (board[2] == board[4] == board[6] == mark)
    )

def play():
    turn = "X"
    moves = 0

    while moves < 9:
        show_board()
        choice = input(f"Player {turn}, choose a number (1-9): ")

        if choice not in board:
            print("Invalid or taken. Try again.")
            continue

        board[int(choice) - 1] = turn
        moves += 1

        if check_winner(turn):
            show_board()
            print(f"Player {turn} wins!")
            return

        turn = "O" if turn == "X" else "X"

    show_board()
    print("It's a draw!")

play()
