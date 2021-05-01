from abc import ABC, abstractmethod

class AbstractPuzzleConstraints(ABC):

    @abstractmethod
    def move_empty_space(self, puzzle_board, empty_coordinates, target_tile_coordinates):
        pass

    def are_constraints_valid(self, x , y):
        pass

    def goal_reached(self, puzzle_board, puzzle_goal):
        pass
