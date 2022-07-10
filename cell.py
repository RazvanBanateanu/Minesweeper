from tkinter import Button, Label
import random
from winreg import CloseKey
import settings
import ctypes
import sys

class Cell:
    all =[]  #class atribute
    cell_count = settings.GRID_SIZE**2
    cell_count_label_obj = None
    
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_obj = None
        self.x = x
        self.y = y
        Cell.all.append(self)
        
    def create_btn(self, location):
        btn=Button(
            location,
            width=12,
            height=4
        )
        btn.bind('<Button-1>', self.left_click_action) # Left Click
        btn.bind('<Button-3>', self.right_click_action) # Right Click
        self.cell_btn_obj = btn
    
    @staticmethod    
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{Cell.cell_count}",
            width=12,
            height=4,
            font=("New Times Roman", 30)
        )
        Cell.cell_count_label_obj=lbl
        
    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'You won', 'Game Over' , 0)
                sys.exit()
            
        self.cell_btn_obj.unbind('<Button-1>')
        self.cell_btn_obj.unbind('<Button-3>')
            
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
            
    def show_mine(self):
        self.cell_btn_obj.configure(bg='red')
        result = ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine!', 'Game Over', 6)
        sys.exit()
    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_obj.configure(text=self.surrounded_cells_mines)
            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.configure(text=f"Cells Left: {Cell.cell_count}")
            self.cell_btn_obj.configure(bg='SystemButtonFace')
        self.is_opened = True

    @property
    def surrounded_cells_mines(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter+=1
        return counter         
        
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1)
        ]
        
        cells = [cell for cell in cells if cell is not None]
        
        return cells
        
        
    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_obj.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_obj.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False
        
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        
        
    def __repr__(self): 
        return f"Cell({self.x},{self.y})"
    