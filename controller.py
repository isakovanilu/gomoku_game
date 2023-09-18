class GomokuController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def play_game(self):
        while True:
            row = int(self.view.get_input(f"Player {self.model.get_current_player()}, enter row: "))
            column = int(self.view.get_input(f"Player {self.model.get_current_player()}, enter column: "))

            if self.model.update_board(row, column):
                self.view.display_board(self.model.board)
                if self.model.check_winner(self.model.get_current_player()):
                    self.view.display_message(f"Player {self.model.get_current_player()} is the winner!")
                    break
                self.model.toggle_player()
            else:
                self.view.display_message('Please enter different coordinates')
