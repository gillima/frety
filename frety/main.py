from tkinter import Tk

from frety.abcplus import AbcPlus
from frety import Controller, Board, Window


def main():
    root = Tk()
    board = Board()
    ui = Window(root, model=board)

    controller = Controller(ui, board)
    controller.learn_0_5()

    root.geometry('1020x330')
    root.mainloop()


if __name__ == '__main__':
    main()