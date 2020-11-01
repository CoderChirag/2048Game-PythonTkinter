from tkinter import Tk, CENTER, Frame, Label

import LogicsFinal
import constants as c

class Game2048(Frame):
    def __init__(self, root):
        root.minsize(840, 625)
        root.maxsize(850,620)
        root.wm_iconbitmap('2048-icon.ico')
        Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.master.bind('<Key>', self.key_down)
        self.commands = {c.KEY_UP: LogicsFinal.move_up, c.KEY_DOWN: LogicsFinal.move_down, 
                         c.KEY_RIGHT: LogicsFinal.move_right, c.KEY_LEFT: LogicsFinal.move_left
                        }
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE)
        background.grid()
        for i in range(c.GRID_LEN):
            self.grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, width=c.SIZE/c.GRID_LEN, height=c.SIZE/c.GRID_LEN, bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING, pady=c.GRID_PADDING)

                t = Label(master=cell, text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY, width=5, height=2, justify=CENTER, font=c.FONT)
                t.grid()
                self.grid_row.append(t)
            self.grid_cells.append(self.grid_row)

    def init_matrix(self):
        self.matrix = LogicsFinal.start_game()
        LogicsFinal.add_new_2(self.matrix)
        LogicsFinal.add_new_2(self.matrix)
        print(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].config(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].config(text=str(new_number), bg=c.BACKGROUND_COLOR_DICT[new_number], fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()

    def key_down(self, event):
        print('Key pressed', event)
        # print(event.keycode)
        key = repr(event.keycode)
        print(key)
        if key in self.commands:
            self.matrix, changed = self.commands[key](self.matrix)
            if changed:
                LogicsFinal.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False
                print(LogicsFinal.get_current_state(self.matrix))
                if LogicsFinal.get_current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(text='You', bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text='Win!', bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.master.unbind('<Key>')
                    
                if LogicsFinal.get_current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(text='You', bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text='Lose!', bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        print(self.matrix)


if __name__ == '__main__':
    Game2048(Tk())

