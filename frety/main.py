from tkinter import Tk

from frety.abcplus import AbcPlus
from frety import Controller, Board, Window


def main():
    root = Tk()
    board = Board()
    ui = Window(board, root)

    controller = Controller(ui, board)
    controller.next()

    root.geometry('1020x330')
    root.mainloop()

if __name__ == '__main__':
    main()