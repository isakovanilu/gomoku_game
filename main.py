from view import GomokuView
from model import GomokuModel
from controller import GomokuController, SmartComputerPlayer, DumbComputerPlayer

if __name__ == "__main__":
    board_size = int(input("Enter board size: "))
    while True:
        player_type = input("Choose computer player type (smart/dumb): ").strip().lower()
        if player_type in ["smart", "dumb"]:
            break
        else:
            print("Invalid input. Please choose 'smart' or 'dumb'.")
    
    model = GomokuModel(board_size)
    view = GomokuView()
    
    if player_type == "smart":
        computer_player = SmartComputerPlayer(model.board, board_size)
    else:
        computer_player = DumbComputerPlayer(board_size)
    
    controller = GomokuController(model, view, computer_player)
    controller.play_game()
