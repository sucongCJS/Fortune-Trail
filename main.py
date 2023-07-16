from game.board import Board
from game.screen import Screen

board = Board(row=5, col=5, interface_type='cmd')

screen = Screen(board)
screen.update_screen()