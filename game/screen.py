import time
import os

class Screen:
    def __init__(self, board) -> None:
        self.board = board
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def update_screen(self):
        while True:
            self.clear_screen()

            self.board.update_board()

            time.sleep(0.1)