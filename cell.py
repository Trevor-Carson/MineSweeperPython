from tkinter import Button

class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn = None

    def create_btn(self, location):
        btn = Button(
            location,
            text='Text'
        )
        self.cell_btn = btn