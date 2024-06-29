import random

# Define the game board
board = [' ' for _ in range(9)]

# Define the players
HUMAN = 'O'
AI = 'X'

def print_board():
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---+---+---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---+---+---')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def available_moves(board):
    return [i for i in range(9) if board[i] == ' ']

def make_move(board, index, player):
    board[index] = player

def is_winner(board, player):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
           [0, 3, 6], [1, 4, 7], [2, 5, 8],
           [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == player:
            return True
    return False

def is_tie(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if is_winner(board, AI):
        return 1
    elif is_winner(board, HUMAN):
        return -1
    elif is_tie(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(best_score, score)
        return best_score

def get_best_move(board):
    best_score = -float('inf')
    best_move = None
    for move in available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Human's turn
        while True:
            try:
                human_move = int(input("Your move (0-8): "))
                if board[human_move] == ' ':
                    break
                else:
                    print("That spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid move. Try again.")
        make_move(board, human_move, HUMAN)

        if is_winner(board, HUMAN):
            print_board()
            print("You win!")
            return

        if is_tie(board):
            print_board()
            print("It's a tie!")
            return

        # AI's turn
        ai_move = get_best_move(board)
        make_move(board, ai_move, AI)
        print(f"AI moves to position {ai_move}.")

        if is_winner(board, AI):
            print_board()
            print("AI wins!")
            return

        print_board()

play_game()