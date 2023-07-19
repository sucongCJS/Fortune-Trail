import time
import os

from interface.turtleInterface import TurtleInterface
from interface.pygameInterface import PygameInterface

interface_dict = {
    'turtle': TurtleInterface,
    'pygame': PygameInterface,
}

class Screen:
    def __init__(self, tiles, interface_type) -> None:
        Interface = interface_dict.get(interface_type)
        if not Interface:
            raise ValueError('Invalid interface type')
        
        self.interface = Interface(tiles)

    def update_screen(self):
        self.interface.update()