
class Block:
    def __init__(self, mode, size=2) -> None:
        """
        basic element of the board of the game, which is a little square
        """
        self.id
        self.x
        self.y


class CmdInterface:
    def __init__(self, row, col):
        for r in range(row):
            if r == 0:
                self._make_block()

    def _make_block(self, mode, width=4, height=1):
        if mode == 'solid':
            horizontal_line = '─' * (width - 2)
            top_bottom_line = '┌' + horizontal_line + '┐'
            middle_line     = '│' + ' ' * (width - 2) + '│'
            bottom_line     = '└' + horizontal_line + '┘'

            print(top_bottom_line)
            for _ in range(height - 2):
                print(middle_line)
            print(bottom_line)
        # elif mode == ''
    
    