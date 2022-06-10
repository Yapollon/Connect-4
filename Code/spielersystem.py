#© Daniel T., Vincent V. 10.11 GHO

from random import randint
from Board import Board
from superView import View


class Main:

    def __init__(self):

        self.View = View(self.start, self.change)
        self.view = self.View.game  # View wird initialisiert
        self.board = Board(7, 6)  # Board wird initialisiert
        self.player = int
        self.color = list
        self.View.mainloop()

    def start(self):
        self.view.gameStart()
        for view_slot, board_slot in zip(self.view.slots, self.board.slots):
            self.view.canvas.itemconfig(self.view.slots[view_slot], fill=View.grey[0])
            self.board.slots[board_slot].status = 0
        self.player = randint(1, 2)
        self.color = self.change_color()
        self.view.changePlayerText(f"Spieler {self.player} ist dran")

    def change(self, x):
        x, y = self.board.getLowestFree(x)
        self.view.chipDropper((x, y), self.color)
        self.board.changeStatus((x, y), self.player)
        wonChips = self.board.checkIfWon((x, y), self.player)

        if wonChips is None:
            print("Noch nicht gewonnen")
            self.player = self.change_player()
            self.view.changePlayerText(f"Spieler {self.player} ist dran")
            self.change_color()
        else:
            print(f"{self.player} hat gewonnen!")
            self.view.gameEnd()
            self.view.changePlayerText(f"Spieler {self.player} hat gewonnen!")
            self.view.flash4([chip.position for chip in wonChips], self.color)

        # Deaktiviert den Button, wenn Reihe 1 erreicht wurde
        if y == 1:
            self.view.deactivateButton(x)
            allColumns = [self.board.getLowestFree(column) for column in range(1, self.board.x_width + 1)]
            if allColumns.count(allColumns[0]) == len(allColumns):
                self.view.gameEnd()
                self.view.changePlayerText("Das Board ist voll!")

    def change_player(self):

        if self.player == 1:
            return 2
        elif self.player == 2:
            return 1

    def change_color(self):

        if self.player == 1:
            self.view.changeButtonColor(View.yellow)
            self.color = View.yellow
        elif self.player == 2:
            self.view.changeButtonColor(View.red)
            self.color = View.red
        return self.color


if __name__ == "__main__":
    Main()
