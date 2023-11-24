import numpy as np
class GomokuModel:
    def __init__(self, size):
        if size < 5:
            raise ValueError('board size cannot be less than 5')
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
                    for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                        win = True
                        for k in range(5):
                            r, c = i + k * dx, j + k * dy
                            if not (0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == value):
                                win = False
                                break
                        if win:
                            return True
        return False
    
    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def get_current_player(self):
        return self.current_player
