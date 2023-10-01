
from view import GomokuView
from model import GomokuModel
from controller import GomokuController, DumbComputerPlayer

if __name__ == "__main__":
    board_size = int(input("Enter board size: "))
    model = GomokuModel(board_size)
    view = GomokuView()
    dumbcomputer = DumbComputerPlayer(board_size)
    controller = GomokuController(model, view, dumbcomputer)
    controller.play_game()
