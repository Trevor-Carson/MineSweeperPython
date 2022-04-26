# Minesweeper game main method
from tkinter import *
from turtle import color
from cell import Cell
import settings
import utilities


root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.window_width}x{settings.window_height}')
root.title("MineSweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.window_width,
    height=utilities.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=utilities.width_prct(25),
    height=utilities.height_prct(75)
)
left_frame.place(x=0, y=utilities.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=utilities.width_prct(75),
    height=utilities.height_prct(75)
)
center_frame.place(x=utilities.width_prct(25), y=utilities.height_prct(25))

for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell(x, y)
        c.create_btn(center_frame)
        c.cell_btn.grid(column=x, row=y)

Cell.randomize_mines()

# Run the window
root.mainloop()