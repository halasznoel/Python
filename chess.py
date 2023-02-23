# Define the chess board as a 2D list
board = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
]

# Define a function to print the board
def print_board(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=' ')
        print()

# Define a function to move a piece
def move_piece(board, start, end):
    piece = board[start[0]][start[1]]
    board[start[0]][start[1]] = ' '
    board[end[0]][end[1]] = piece

# Define the main function to play chess
def play_chess():
    print_board(board)
    while True:
        start = input("Enter the starting position of the piece (e.g. 'e2'): ")
        start_row = int(start[1]) - 1
        start_col = ord(start[0]) - 97
        end = input("Enter the ending position of the piece (e.g. 'e4'): ")
        end_row = int(end[1]) - 1
        end_col = ord(end[0]) - 97
        move_piece(board, (start_row, start_col), (end_row, end_col))
        print_board(board)

# Call the main function to play chess
play_chess()
