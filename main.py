
from view import GomokuView
from model import GomokuModel
from controller import GomokuController

if __name__ == "__main__":
    size = int(input("Enter board size: "))
    model = GomokuModel(size)
    view = GomokuView()
    controller = GomokuController(model, view)
    controller.play_game()
