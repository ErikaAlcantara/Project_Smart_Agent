import tkinter as tk
from tkinter import Frame

class PuzzleWindow:
    def __init__(self):
        self.matrix = [['1', '4', '3'], ['7', ' ', '6'], ['5', '8', '2']]
        self.empty = [1, 1]


    def startRenderLoop(self):
        self.root = tk.Tk()
        
        # self.root.attributes('-toolwindow', True) --> for Windows, enable this.
      
        self.renderButtons()

        self.root.mainloop()

# highlightbackground = '#F24726'
    def renderButtons(self):
        self.button_0_0_color = 'white' if self.matrix[0][0] == ' ' else '#F24726'
        self.button_0_0 = tk.Button(self.root, text=self.matrix[0][0], command=self.buttonClick_0_0, bg=self.button_0_0_color)
        self.button_0_0.grid(row=1, column=0)
        self.button_0_0.config(height=3, width=5)

        self.button_0_1_color = 'white' if self.matrix[0][1] == ' ' else '#F24726'
        self.button_0_1 = tk.Button(self.root, text=self.matrix[0][1], command=self.buttonClick_0_1, bg=self.button_0_1_color)
        self.button_0_1.grid(row=1, column=1)
        self.button_0_1.config(height=3, width=5)

        self.button_0_2_color = 'white' if self.matrix[0][2] == ' ' else '#F24726'
        self.button_0_2 = tk.Button(self.root, text=self.matrix[0][2], command=self.buttonClick_0_2, bg=self.button_0_2_color)
        self.button_0_2.grid(row=1, column=2)
        self.button_0_2.config(height=3, width=5)

        # ---------------------------------------------------------
        self.button_1_0_color = 'white' if self.matrix[1][0] == ' ' else '#F24726'
        self.button_1_0 = tk.Button(self.root, text=self.matrix[1][0], command=self.buttonClick_1_0, bg=self.button_1_0_color)
        self.button_1_0.grid(row=2, column=0)
        self.button_1_0.config(height=3, width=5)

        self.button_1_1_color = 'white' if self.matrix[1][1] == ' ' else '#F24726'
        self.button_1_1 = tk.Button(self.root, text=self.matrix[1][1], command=self.buttonClick_1_1, bg=self.button_1_1_color)
        self.button_1_1.grid(row=2, column=1)
        self.button_1_1.config(height=3, width=5)

        self.button_1_2_color = 'white' if self.matrix[1][2] == ' ' else '#F24726'
        self.button_1_2 = tk.Button(self.root, text=self.matrix[1][2], command=self.buttonClick_1_2, bg=self.button_1_2_color)
        self.button_1_2.grid(row=2, column=2)
        self.button_1_2.config(height=3, width=5)

        # ---------------------------------------------------------
        self.button_2_0_color = 'white' if self.matrix[2][0] == ' ' else '#F24726'
        self.button_2_0 = tk.Button(self.root, text=self.matrix[2][0], command=self.buttonClick_2_0, bg=self.button_2_0_color)
        self.button_2_0.grid(row=3, column=0)
        self.button_2_0.config(height=3, width=5)

        self.button_2_1_color = 'white' if self.matrix[2][1] == ' ' else '#F24726'
        self.button_2_1 = tk.Button(self.root, text=self.matrix[2][1], command=self.buttonClick_2_1, bg=self.button_2_1_color)
        self.button_2_1.grid(row=3, column=1)
        self.button_2_1.config(height=3, width=5)
        
        self.button_2_2_color = 'white' if self.matrix[2][2] == ' ' else '#F24726'
        self.button_2_2 = tk.Button(self.root, text=self.matrix[2][2], command=self.buttonClick_2_2, bg=self.button_2_2_color)
        self.button_2_2.grid(row=3, column=2)
        self.button_2_2.config(height=3, width=5)

        # ---------------------------------------------------------

    def buttonClick_0_0(self, x=0, y=0):
        if self.empty[0] != x and self.empty[1] != y:
            return
        elif abs(self.empty[0] - x) > 1:
            return
        elif abs(self.empty[1] - y) > 1:
            return
        else:
            aux = self.matrix[0][0]     
            self.matrix[0][0] = self.matrix[self.empty[0]][self.empty[1]]
            self.matrix[self.empty[0]][self.empty[1]] = aux
            self.empty = [0, 0]
            self.renderButtons()
            print('0_0')    
        
    
    def buttonClick_0_1(self, x=0, y=1):
        if self.empty[0] != x and self.empty[1] != y:  
            return
        elif abs(self.empty[0] - x) > 1:
            return
        elif abs(self.empty[1] - y) > 1:
            return
        else:
            aux = self.matrix[0][1]     
            self.matrix[0][1] = self.matrix[self.empty[0]][self.empty[1]]
            self.matrix[self.empty[0]][self.empty[1]] = aux
            
            self.empty = [0, 1]
            self.renderButtons()
            print('0_1')     

    def buttonClick_0_2(self, x=0, y=2):
        if self.empty[0] != x and self.empty[1] != y:  
            return
        elif abs(self.empty[0] - x) > 1:
            return
        elif abs(self.empty[1] - y) > 1:
            return
        else:
            aux = self.matrix[0][2]     
            self.matrix[0][2] = self.matrix[self.empty[0]][self.empty[1]]
            self.matrix[self.empty[0]][self.empty[1]] = aux
            
            self.empty = [0, 2]
            self.renderButtons()
            print('0_2')    

    def buttonClick_1_0(self, x=1, y=0):
        if self.empty[0] != x and self.empty[1] != y:  
            return
        elif abs(self.empty[0] - x) > 1:
            return
        elif abs(self.empty[1] - y) > 1:
            return
        else:
            aux = self.matrix[1][0]     
            self.matrix[1][0] = self.matrix[self.empty[0]][self.empty[1]]
            self.matrix[self.empty[0]][self.empty[1]] = aux
            
            self.empty = [1, 0]
            self.renderButtons()
            print('1_0')    

    def buttonClick_1_1(self, x=1, y=1):
        if self.empty[0] != x and self.empty[1] != y:  
            return
        elif abs(self.empty[0] - x) > 1:
            return
        elif abs(self.empty[1] - y) > 1:
            return
        else:
            aux = self.matrix[1][1]     
            self.matrix[1][1] = self.matrix[self.empty[0]][self.empty[1]]
            self.matrix[self.empty[0]][self.empty[1]] = aux
            
            self.empty = [1, 1]
            self.renderButtons()
            print('1_1')     

    def buttonClick_1_2(self, x=1, y=2):
        if self.empty[0] != x and self.empty[1] != y:  
            return
        elif abs(self.empty[0] - x) > 1:
            return
        elif abs(self.empty[1] - y) > 1:
            return
        else:
            aux = self.matrix[1][2]     
            self.matrix[1][2] = self.matrix[self.empty[0]][self.empty[1]]
            self.matrix[self.empty[0]][self.empty[1]] = aux
            
            self.empty = [1, 2]
            self.renderButtons()
            print('1_2')  

    def buttonClick_2_0(self, x=2, y=0):
        if self.empty[0] != x and self.empty[1] != y:  
            return
        elif abs(self.empty[0] - x) > 1:
            return
        elif abs(self.empty[1] - y) > 1:
            return
        else:
            aux = self.matrix[2][0]     
            self.matrix[2][0] = self.matrix[self.empty[0]][self.empty[1]]
            self.matrix[self.empty[0]][self.empty[1]] = aux
            
            self.empty = [2, 0]
            self.renderButtons()
            print('2_0')    

    def buttonClick_2_1(self, x=2, y=1):
        if self.empty[0] != x and self.empty[1] != y:  
            return
        elif abs(self.empty[0] - x) > 1:
            return
        elif abs(self.empty[1] - y) > 1:
            return
        else:
            aux = self.matrix[2][1]     
            self.matrix[2][1] = self.matrix[self.empty[0]][self.empty[1]]
            self.matrix[self.empty[0]][self.empty[1]] = aux
            
            self.empty = [2, 1]
            self.renderButtons()
            print('2_1')      

    def buttonClick_2_2(self, x=2, y=2):
        if self.empty[0] != x and self.empty[1] != y:  
            return
        elif abs(self.empty[0] - x) > 1:
            return
        elif abs(self.empty[1] - y) > 1:
            return
        else:
            aux = self.matrix[2][2]     
            self.matrix[2][2] = self.matrix[self.empty[0]][self.empty[1]]
            self.matrix[self.empty[0]][self.empty[1]] = aux
            
            self.empty = [2, 2]
            self.renderButtons()
            print('2_2') 



        # self.button9 = tk.Button(self.root, text=" ", command=self.buttonClick, bg='blue')
        # self.button9.grid(row=3, column=2)
        # self.button9.config(height=5, width=5)

        # def button_click(self, x, y):
        # if self.empty[0] != x and self.empty[1] != y:
        #     return
        # else:
        #     aux = self.matrix[x][y]     
        #     self.matrix[x][y] = self.matrix[self.empty[0]][self.empty[1]]
        #     self.matrix[self.empty[0]][self.empty[1]] = aux
        #     self.empty = [x, y]
        #     self.renderButtons()
        #     print('0_0') 


# and (abs(self.empty[0] - x > 1) and abs(self.empty[1] - y > 1)
    