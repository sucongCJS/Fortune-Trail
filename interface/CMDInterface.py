
class Block:
    def __init__(self, mode, size=2) -> None:
        """
        basic element of the board of the game, which is a little square
        """
        self.id
        self.x
        self.y


class CMDInterface:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def _make_block(self, mode, width=4, height=1):
        """
        width and height for the display section, excluding borders
        """
        if mode == 'solid':
            horizontal_line = '─' * (width - 2)
            top_bottom_line = '┌' + horizontal_line + '┐'
            middle_line     = '│' + ' ' * (width - 2) + '│'
            bottom_line     = '└' + horizontal_line + '┘'

            print(top_bottom_line)
            for _ in range(height - 2):
                print(middle_line)
            print(bottom_line)
        elif mode == 'hollow':
            horizontal_line = ' ' * (width + 2)
            for _ in range(height + 2):
                print(horizontal_line)

    def update(self):
        
        

    
    