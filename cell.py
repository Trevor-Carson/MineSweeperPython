# Cell object to be used in each button on the grid
from msilib.schema import Property
from tkinter import Button
import settings
import random

# Class to hold grid cell type
class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn = None
        self.x = x
        self.y = y
        # Append the object ot the Cell.all list
        Cell.all.append(self)

    # Function to create button for grid cell and assign click events
    def create_btn(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            #text=f"{self.x}, {self.y}" # TODO remove cell coord text 
        )
        btn.bind('<Button-1>', self.btn_left_click)
        btn.bind('<Button-2>', self.btn_right_click)
        btn.bind('<Button-3>', self.btn_right_click)
        self.cell_btn = btn

    # Function/event for left mouse click
    def btn_left_click(self, event):
        if self.is_mine:
             self.show_mine()
        else:
            self.show_mines_number()

    # Function to trigger if button clicked on is a mine
    def show_mine(self):
        self.cell_btn.configure(bg = 'red')

    # Function to return a cell value based on the x,y axis
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell # Return the cells x,y coordinate

    # Attrubute/function to get the x,y value of surrounding cells excluding cells that equal None
    @property
    def surrounded_cells(self):
        cell_radius = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y    ),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x    , self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y    ),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x    , self.y + 1),
        ]
        cell_radius = [cell for cell in cell_radius if cell is not None]
        return cell_radius  # Returns the x,y value of surrounding cells

    # Attribute/function to check if surrounding cells are mines
    @property
    def count_surrounding_mines(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter  # Returns the number of mines
    
    # Function to show the number of mines around the cell button
    def show_mines_number(self):
        self.cell_btn.configure(text=self.count_surrounding_mines)

    # Function/event for right mouse click
    def btn_right_click(self, event):
        print("Right Click")

    # Static function to generate randomized mines
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.mine_count)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    # Overridden print function
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"