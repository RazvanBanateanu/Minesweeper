from ctypes import util
from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False) 

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)

top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('',48)
)

game_title.place(
    x=utils.width_prct(25),
    y = 0
)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)

left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))


for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c=Cell(x ,y)
        c.create_btn(center_frame)
        c.cell_btn_obj.grid(
            column = y,
            row = x
        )
        
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_obj.place(x=0, y=0)
        
Cell.randomize_mines()

root.mainloop()