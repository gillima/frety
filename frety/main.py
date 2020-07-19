from tkinter import Tk

from frety import Controller, Board, Window


def main():
    root = Tk()
    board = Board()
    ui = Window(board, root)

    controller = Controller(ui, board)
    controller.setup('DFGE')

    root.geometry('1020x330')
    root.mainloop()

if __name__ == '__main__':
    main()