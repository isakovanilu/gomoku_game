from view import GomokuView
from model import GomokuModel
from controller import GomokuController, SmartComputerPlayer

if __name__ == "__main__":
    board_size = int(input("Enter board size: "))
    model = GomokuModel(board_size)
    view = GomokuView()
    computer_player = SmartComputerPlayer(model.board, board_size)
    controller = GomokuController(model, view, computer_player)
    controller.play_game()
