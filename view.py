class GomokuView:
    def display_board(self, board) -> None:
        matrix_length = len(board) * 4 - 3
        for row in board:
            print(" | ".join(row))
            print("-" * matrix_length)

    def display_message(self, msg) -> str:
        print(msg)

    def get_input(self, prompt):
        return input(prompt)
