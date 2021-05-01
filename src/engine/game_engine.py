from ia_agents.agent_manager import AgentManager
from data_structures.coordinates import Coordinates
from data_structures.puzzle_board import PuzzleBoard
from rules.puzzle_constraints import AbstractPuzzleConstraints 

class GameEngine(AbstractPuzzleConstraints):
    def __init__(self):
        self.goal = [['1', '2', '3'], ['8', ' ', '4'], ['7', '6', '5']]
        self.puzzle_board = PuzzleBoard()
        self.empty = None
        self.agent_maneger = AgentManager()
        self.initialize_puzzle_board()

    def get_agent_manager(self):
        return self.agent_maneger

    def get_puzzle_board(self):
        return self.puzzle_board    

    def get_empty(self):
        return self.empty

    def initialize_puzzle_board(self):
        self.puzzle_board.set_board_state([['1', '4', '3'], ['7', ' ', '6'], ['5', '8', '2']])
        self.empty = Coordinates(1, 1)

    def move_empty_space(self, puzzle_board, empty_coordinates, target_x, target_y):
        current_tile_value = puzzle_board.get_tile(target_x, target_y)
        empty_value = puzzle_board.get_tile(empty_coordinates.get_x(), empty_coordinates.get_y())
        puzzle_board.set_tile(target_x, target_y, empty_value)
        puzzle_board.set_tile(empty_coordinates.get_x(), empty_coordinates.get_y(), current_tile_value)
        empty_coordinates.update_coordinates(target_x, target_y)
        print(f'moved from [{empty_coordinates.get_x()}, {empty_coordinates.get_y()}] to [{target_x},{target_y}]')

    def are_constraints_valid(self, empty_coordinates, x , y):    
        if empty_coordinates.get_x() != x and empty_coordinates.get_y() != y:
            return False
        elif abs(empty_coordinates.get_x() - x) > 1:
            return False
        elif abs(empty_coordinates.get_y() - y) > 1:
            return False
        else: 
            return True    

    def goal_reached(self, puzzle_board, puzzle_goal):
        return puzzle_board == puzzle_goal