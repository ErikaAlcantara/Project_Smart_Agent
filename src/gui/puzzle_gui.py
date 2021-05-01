import tkinter as tk
import platform
from tkinter import Frame, Label
from data_structures.coordinates import Coordinates
from data_structures.puzzle_board import PuzzleBoard
from engine.game_engine import GameEngine

class PuzzleWindow:
    def __init__(self):
        self.game_engine = None

    def set_engine(self, game_engine):
        self.game_engine = game_engine

    def startRenderLoop(self):
        self.root = tk.Tk()
        self.root.geometry("135x270")
        if platform.system() == "Windows":
            self.root.attributes('-toolwindow', True)
        self.renderButtons()
        self.root.mainloop()

    def renderButtons(self):
        self.button_0_0 = tk.Button(self.root, 
                                    text=self.game_engine.get_puzzle_board().get_tile(0,0), 
                                    command=self.buttonClick_0_0, 
                                    bg=self.game_engine.get_puzzle_board().get_tile_color(0,0))
        self.configure_button_coordinates(self.button_0_0, 1, 0, 3, 5)
        

        self.button_0_1 = tk.Button(self.root, 
                                    text=self.game_engine.get_puzzle_board().get_tile(0,1), 
                                    command=self.buttonClick_0_1, 
                                    bg=self.game_engine.get_puzzle_board().get_tile_color(0,1))
        self.configure_button_coordinates(self.button_0_1, 1, 1, 3, 5)

        self.button_0_2 = tk.Button(self.root, 
                                    text=self.game_engine.get_puzzle_board().get_tile(0,2), 
                                    command=self.buttonClick_0_2, 
                                    bg=self.game_engine.get_puzzle_board().get_tile_color(0,2))
        self.configure_button_coordinates(self.button_0_2, 1, 2, 3, 5)

        # ---------------------------------------------------------
        self.button_1_0 = tk.Button(self.root, 
                                    text=self.game_engine.get_puzzle_board().get_tile(1,0), 
                                    command=self.buttonClick_1_0, 
                                    bg=self.game_engine.get_puzzle_board().get_tile_color(1,0))
        self.configure_button_coordinates(self.button_1_0, 2, 0, 3, 5)

        self.button_1_1 = tk.Button(self.root, 
                                    text=self.game_engine.get_puzzle_board().get_tile(1,1), 
                                    command=self.buttonClick_1_1, 
                                    bg=self.game_engine.get_puzzle_board().get_tile_color(1,1))
        self.configure_button_coordinates(self.button_1_1, 2, 1, 3, 5)

        self.button_1_2 = tk.Button(self.root, 
                                    text=self.game_engine.get_puzzle_board().get_tile(1,2), 
                                    command=self.buttonClick_1_2, 
                                    bg=self.game_engine.get_puzzle_board().get_tile_color(1,2))
        self.configure_button_coordinates(self.button_1_2, 2, 2, 3, 5)

        # ---------------------------------------------------------
        self.button_2_0 = tk.Button(self.root, 
                                    text=self.game_engine.get_puzzle_board().get_tile(2,0), 
                                    command=self.buttonClick_2_0, 
                                    bg=self.game_engine.get_puzzle_board().get_tile_color(2,0))
        self.configure_button_coordinates(self.button_2_0, 3, 0, 3, 5)

        self.button_2_1 = tk.Button(self.root, 
                                    text=self.game_engine.get_puzzle_board().get_tile(2,1), 
                                    command=self.buttonClick_2_1, 
                                    bg=self.game_engine.get_puzzle_board().get_tile_color(2,1))
        self.configure_button_coordinates(self.button_2_1, 3, 1, 3, 5)
        
        self.button_2_2 = tk.Button(self.root, 
                                    text=self.game_engine.get_puzzle_board().get_tile(2,2), 
                                    command=self.buttonClick_2_2, 
                                    bg=self.game_engine.get_puzzle_board().get_tile_color(2,2))
        self.configure_button_coordinates(self.button_2_2, 3, 2, 3, 5)


        self.l = Label(text = "Human Mode Activated")
        self.l.place(x=1, y=170) 
        
        self.human_button = tk.Button(self.root,
                                    text="HUMAN",
                                    command=self.run_human_agent,
                                    bg="white")
        self.configure_button_coordinates(self.human_button, 5, 0, 1, 6)     
        self.human_button.place(x=45, y=195) 

        self.dfs_button = tk.Button(self.root,
                                    text="DFS",
                                    command=self.run_dfs_agent,
                                    bg="white")
        self.configure_button_coordinates(self.dfs_button, 5, 0, 2, 6)     
        self.dfs_button.place(x=5, y=225)        

        self.bfs_button = tk.Button(self.root,
                                    text="BFS",
                                    command=self.run_bfs_agent,
                                    bg="white")
        self.configure_button_coordinates(self.bfs_button, 5, 0, 2, 6)     
        self.bfs_button.place(x=80, y=225)                    

        # ---------------------------------------------------------
    def run_dfs_agent(self):
        agent_manager = self.game_engine.get_agent_manager()
        agent_types = agent_manager.get_agent_enum() 
        agent_manager.create_agent(agent_types.DFS_AGENT)

    def run_bfs_agent(self):
        agent_manager = self.game_engine.get_agent_manager()
        agent_types = agent_manager.get_agent_enum() 
        agent_manager.create_agent(agent_types.BFS_AGENT)  

    def run_human_agent(self):
        agent_manager = self.game_engine.get_agent_manager()
        agent_types = agent_manager.get_agent_enum() 
        agent_manager.create_agent(agent_types.HUMAN_AGENT)        

    def configure_button_coordinates(self, button, x, y, h, w):
        button.grid(row=x, column=y)
        button.config(height=h, width=w)   

    def buttonClick_0_0(self, x=0, y=0):
        if self.game_engine.are_constraints_valid(self.game_engine.get_empty(), x, y):
            self.game_engine.move_empty_space(self.game_engine.get_puzzle_board(), self.game_engine.get_empty(), x, y)
            self.renderButtons()
        
    def buttonClick_0_1(self, x=0, y=1):
        if self.game_engine.are_constraints_valid(self.game_engine.get_empty(), x, y):
            self.game_engine.move_empty_space(self.game_engine.get_puzzle_board(), self.game_engine.get_empty(), x, y)
            self.renderButtons()

    def buttonClick_0_2(self, x=0, y=2):
        if self.game_engine.are_constraints_valid(self.game_engine.get_empty(), x, y):
            self.game_engine.move_empty_space(self.game_engine.get_puzzle_board(), self.game_engine.get_empty(), x, y)
            self.renderButtons()

    def buttonClick_1_0(self, x=1, y=0):
        if self.game_engine.are_constraints_valid(self.game_engine.get_empty(), x, y):
            self.game_engine.move_empty_space(self.game_engine.get_puzzle_board(), self.game_engine.get_empty(), x, y)
            self.renderButtons()

    def buttonClick_1_1(self, x=1, y=1):
        if self.game_engine.are_constraints_valid(self.game_engine.get_empty(), x, y):
            self.game_engine.move_empty_space(self.game_engine.get_puzzle_board(), self.game_engine.get_empty(), x, y)
            self.renderButtons()

    def buttonClick_1_2(self, x=1, y=2):
        if self.game_engine.are_constraints_valid(self.game_engine.get_empty(), x, y):
            self.game_engine.move_empty_space(self.game_engine.get_puzzle_board(), self.game_engine.get_empty(), x, y)
            self.renderButtons()

    def buttonClick_2_0(self, x=2, y=0):
        if self.game_engine.are_constraints_valid(self.game_engine.get_empty(), x, y):
            self.game_engine.move_empty_space(self.game_engine.get_puzzle_board(), self.game_engine.get_empty(), x, y)
            self.renderButtons()

    def buttonClick_2_1(self, x=2, y=1):
        if self.game_engine.are_constraints_valid(self.game_engine.get_empty(), x, y):
            self.game_engine.move_empty_space(self.game_engine.get_puzzle_board(), self.game_engine.get_empty(), x, y)
            self.renderButtons()

    def buttonClick_2_2(self, x=2, y=2):
        if self.game_engine.are_constraints_valid(self.game_engine.get_empty(), x, y):
            self.game_engine.move_empty_space(self.game_engine.get_puzzle_board(), self.game_engine.get_empty(), x, y)
            self.renderButtons()
    