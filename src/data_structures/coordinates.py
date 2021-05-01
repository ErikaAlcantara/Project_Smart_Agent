class Coordinates:
    def __init__ (self, init_x, init_y):
        self.x = init_x
        self.y = init_y

    def set_coordinate_x(self, new_x):
        self.x = new_x

    def set_coordinate_y(self, new_y):
        self.y = new_y

    def update_coordinates(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y     

