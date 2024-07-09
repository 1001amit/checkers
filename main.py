class Piece:
    def __init__(self, color, is_king=False):
        self.color = color
        self.is_king = is_king

    def make_king(self):
        self.is_king = True

    def __repr__(self):
        return f"{'W' if self.color == 'white' else 'R'}{'K' if self.is_king else ''}"

class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = []
        for row in range(8):
            board.append([])
            for col in range(8):
                if (row % 2 == 0 and col % 2 == 1) or (row % 2 == 1 and col % 2 == 0):
                    if row < 3:
                        board[row].append(Piece('white'))
                    elif row > 4:
                        board[row].append(Piece('red'))
                    else:
                        board[row].append(None)
                else:
                    board[row].append(None)
        return board

    def draw_board(self):
        for row in self.board:
            print(" | ".join([str(piece) if piece else "  " for piece in row]))
            print("-" * 32)

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = None
        self.board[end_row][end_col] = piece

        if (piece.color == 'white' and end_row == 7) or (piece.color == 'red' and end_row == 0):
            piece.make_king()

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        # Implement the logic for checking if a move is valid
        return True

def main():
    board = Board()
    board.draw_board()

    while True:
        start_row = int(input("Enter the starting row: "))
        start_col = int(input("Enter the starting column: "))
        end_row = int(input("Enter the ending row: "))
        end_col = int(input("Enter the ending column: "))

        if board.is_valid_move(start_row, start_col, end_row, end_col):
            board.move_piece(start_row, start_col, end_row, end_col)
        else:
            print("Invalid move! Try again.")

        board.draw_board()

if __name__ == "__main__":
    main()
