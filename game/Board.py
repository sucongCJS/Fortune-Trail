import interface.cmdInterface, interface.GUIInterface

interface_dict = {
    'cmd': interface.cmdInterface,
    'gui': interface.GUIInterface
}

class Board:
    def __init__(self, row, col, interface_type):
        self.rows = row
        self.col = col
        
        self.interface = interface_dict.get(interface_type)
        if not self.interface:
            raise ValueError('Invalid interface type')
        
        self.interface = self.interface(self.row, self.col)
