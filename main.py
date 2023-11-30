from random import randrange

def initialize_board():
    # Ініціалізація пустої дошки 3x3
    return [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

def print_board(board):
    # Вивід дошки в консоль
    for row in board:
        print(" | ".join(row))
        print("---------")

def computer_move(board):
    # Хід комп'ютера - випадковим чином обирається вільне поле
    while True:
        row = randrange(3)
        col = randrange(3)
        if board[row][col] not in ['X', 'O']:
            board[row][col] = 'X'
            break

def check_winner(board):
    # Перевірка виграшу
    for row in board:
        if len(set(row)) == 1 and row[0] in ['X', 'O']:
            return row[0]

    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] in ['X', 'O']:
            return board[0][col]

    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] in ['X', 'O']:
        return board[0][0]

    if len(set([board[i][2 - i] for i in range(3)])) == 1 and board[0][2] in ['X', 'O']:
        return board[0][2]

    return None

def game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!\n")
    print_board(board)

    while True:
        computer_move(board)
        print("Computer's move:")
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Winner: {winner}")
            break

game()