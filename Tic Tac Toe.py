# MODS

# Global Variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_running = True
quit_game = True
current_player = "X"
winner = None


# Prints current board to screen
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Taking the users input and displaying it on board
def user_input(board):
    while True:
        spot = int(input(f"Player [{current_player}], pick a spot between 1-9: "))
        if 1 <= spot <= 9 and board[spot - 1] == "-":
            board[spot - 1] = current_player
            break


def check_win(board):
    global game_running, winner

    # Checks horizontal win
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        game_running = False
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        game_running = False
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        game_running = False

    # Checks vertical win
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        game_running = False
    elif board[1] == board[4] == board[7] and board[3] != "-":
        winner = board[3]
        game_running = False
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        game_running = False

    # Checks diagonal win
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        game_running = False
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        game_running = False


def check_tie(board):
    global game_running

    # Check for a tie
    if "-" not in board:
        print("\n\t\t\tThere is a TIE")
        game_running = False


# Switch between player "X" and "O"
def switch_user():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# Print the winner to screen
def display_winner(board):
    if "-" not in board:
        print_board(board)
    else:
        print(f"\n\t\t\tThe winner is [{winner}]!")
        print_board(board)


# Ask the user(s) if they want to play again
def play_again():
    global quit_game, board, game_running, current_player, winner

    response = input("Do you want to play again (Y/N)?: ").upper()
    print()
    if response == "Y" or response == "YES":
        # reset the board
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        game_running = True
        quit_game = True
        current_player = "X"
        winner = None
    else:
        quit_game = False


# main
while quit_game:
    print_board(board)
    while game_running:
        user_input(board)
        print_board(board)
        check_tie(board)
        check_win(board)
        switch_user()
    display_winner(board)
    play_again()
print("Good Game")
