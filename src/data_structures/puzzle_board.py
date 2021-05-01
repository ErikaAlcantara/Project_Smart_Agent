class PuzzleBoard:
    def __init__ (self):
        self.board = None

    def set_board_state(self, configuration):
        self.board = configuration    

    def get_perception(self):
        return self.board

    def get_tile(self, x, y):
        if self.board != None:
            return self.board[x][y]

    def set_tile(self, x, y, value):
        if self.board != None:
            self.board[x][y] = value

    def get_tile_color(self, x, y):
        if self.board != None:
            return 'white' if self.board[x][y] == ' ' else '#F24726'        