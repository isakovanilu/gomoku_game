class GomokuModel:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = "X"

    def is_valid_move(self, row, column):
        return 0 <= row < self.size and 0 <= column < self.size and self.board[row][column] == ' '

    def update_board(self, row, column):
        if self.is_valid_move(row, column):
            self.board[row][column] = self.current_player
            return True
        return False

    def check_winner(self, value):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == value:
                    # row-wise/horizontal check
                    if j < self.size - 4 and all([self.board[i][j + k] == value for k in range(5)]):
                        return True
                    # column-wise/vertical check
                    if i < self.size - 4 and all([self.board[i + k][j] == value for k in range(5)]):
                        return True
                    # diagonal check: \
                    if i < self.size - 4 and j < self.size - 4 and all([self.board[i+k][j+k] == value for k in range(5)]):    
                        return True
                    # diagonal check: /
                    if i >= 4 and j < self.size - 4 and all([self.board[i-k][j+k] == value for k in range(5)]):
                        return True
        return False
    
    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def get_current_player(self):
        return self.current_player
