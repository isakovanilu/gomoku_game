
class GomokuModel:
    def __init__(self, board_size):
        if not isinstance(board_size, int):
            raise ValueError('Board size must be an integer.')

        if board_size < 5:
            raise ValueError('board board_size cannot be less than 5')
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)]
                      for _ in range(board_size)]
        self.current_player = "X"

    def is_valid_move(self, row, column):
        """
        Checks if a move is valid with the given row/column index for the move 
        """
        return 0 <= row < self.board_size and 0 <= column < self.board_size and self.board[
            row][column] == ' '

    def update_board(self, row, column):
        """Updates the with the given row/column values."""
        if self.is_valid_move(row, column):
            self.board[row][column] = self.current_player
            return True
        return False

    def check_winner(self, value):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == value:
                    for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                        win = True
                        for k in range(5):
                            r, c = i + k * dx, j + k * dy
                            if not (0 <= r < self.board_size and 0 <= c <
                                    self.board_size and self.board[r][c] == value):
                                win = False
                                break
                        if win:
                            return True
        return False

    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def get_current_player(self):
        return self.current_player
