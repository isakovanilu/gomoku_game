import random
class SmartComputerPlayer:
    def __init__(self, board, board_size):
        self.board = board
        self.board_size = board_size
        
    def make_smart_move(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == '-':
                    pass
                    # TODO check the moves
        

    def check_winning_move(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        count = 0
        for i in range(-4, 5):
            r, c = row + i * directions[0], col + i * directions[1]
            pass
            
class DumbComputerPlayer:
    def __init__(self, board_size):
        self.board_size = board_size

    def make_random_move(self):
        return random.randint(0, self.board_size-1), random.randint(0, self.board_size-1)

class GomokuController:
    def __init__(self, model, view, dumb_computer=None):
        self.model = model
        self.view = view
        self.dumb_computer = dumb_computer

    def play_game(self):
        while True:
            if self.dumb_computer and self.model.get_current_player() == "O":  
                row, column = self.dumb_computer.make_random_move()
                self.view.display_message(f"Dumb Computer Player chose ({row}, {column})")
            else:
                row = int(self.view.get_input(f"Player {self.model.get_current_player()}, enter row: "))
                column = int(self.view.get_input(f"Player {self.model.get_current_player()}, enter column: "))

            if self.model.update_board(row, column):
                self.view.display_board(self.model.board)
                if self.model.check_winner(self.model.get_current_player()):
                    self.view.display_message(f"Player {self.model.get_current_player()} is the winner!")
                    break
                self.model.toggle_player()
            else:
                self.view.display_message('Please enter different coordinates or position already occupied')