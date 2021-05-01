from engine.game_engine import GameEngine
from gui.puzzle_gui import PuzzleWindow

if __name__ == '__main__':
    game_engine = GameEngine()
    puzzle_window = PuzzleWindow()
    puzzle_window.set_engine(game_engine)
    puzzle_window.startRenderLoop()



    

    
