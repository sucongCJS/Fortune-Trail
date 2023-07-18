from interface.CMDInterface import CMDInterface
from interface.GUIInterface import GUIInterface

interface_dict = {
    'cmd': CMDInterface,
    'gui': GUIInterface,
}

class Board:
    def __init__(self, row, col, interface_type) -> None:
        self.row = row
        self.col = col
        
        Interface = interface_dict.get(interface_type)
        if not Interface:
            raise ValueError('Invalid interface type')
        
        self.interface = Interface(self.row, self.col)
        
    def update_board(self):
        self.interface.update()