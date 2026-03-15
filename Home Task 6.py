print("Welcome to Tic-Tac-Toe! You are X and the AI is O.")

import math

# create board
def initial_state():
    return [" " for _ in range(9)]

# print board
def print_board(board):
    print()
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()

# check winner
def check_winner(board):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    
    if " " not in board:
        return "draw"
    
    return None

# possible moves
def possible_moves(board):
    return [i for i,v in enumerate(board) if v == " "]

# minimax algorithm
def minimax(board, is_maximizing):
    result = check_winner(board)

    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "draw":
        return 0

    if is_maximizing:
        best = -math.inf
        for move in possible_moves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            best = max(score, best)
        return best
    else:
        best = math.inf
        for move in possible_moves(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "
            best = min(score, best)
        return best

# best AI move
def best_move(board):
    best_score = -math.inf
    move = None

    for i in possible_moves(board):
        board[i] = "O"
        score = minimax(board, False)
        board[i] = " "
        
        if score > best_score:
            best_score = score
            move = i

    return move

# play game
def play_game():
    board = initial_state()

    while True:
        print_board(board)

        # player move
        move = int(input("Enter position (0-8): "))
        if board[move] != " ":
            print("Invalid move!")
            continue

        board[move] = "X"

        result = check_winner(board)
        if result:
            print_board(board)
            if result == "X":
                print("You win!")
            elif result == "O":
                print("AI wins!")
            else:
                print("It's a draw!")
            break

        # AI move
        ai = best_move(board)
        board[ai] = "O"
        print(f"AI plays at position {ai}")

        result = check_winner(board)
        if result:
            print_board(board)
            if result == "X":
                print("You win!")
            elif result == "O":
                print("AI wins!")
            else:
                print("It's a draw!")
            break

play_game()