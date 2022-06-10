# superView.py
# Klasse zum Generieren eines Benutzer-Interfaces
# Programm von Daniel & Yassin

from tkinter import *
from functools import partial
from ResizingCanvas import ResizingCanvas


class View(Tk):

    # Farbcodes
    red = '#fc5858'
    darkRed = "#d94c4c"
    disabledRed = "#EB9595"
    yellow = '#ffef00'
    darkYellow = "#e6d700"
    disabledYellow = "#e7e189"
    blue = "#0d65a8"
    grey = "#cccccc"

    # speichert den DISABLED Status für Buttons als klassen eigene Variable um sie übergeben zu können
    disabled = DISABLED

    def __init__(self, callback):
        Tk.__init__(self)
        self.title("4 Gewinnt")
        self.geometry('720x670')
        self.resizable(False, False)
        #self.overrideredirect(True)

        # Canvas
        self.canvas = ResizingCanvas(self, width=720, height=670, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Buttons
        self.buttons = []
        for i, position in zip(range(1, 7+1), range(20, 620+1, 100)):
            self.buttons.append(Button(self, width=10, height=2, text="▼", cursor="hand2", font=self.canvas.buttonSize, command=partial(callback, i)))
            self.canvas.create_window(position, 50, anchor=NW, window=self.buttons[i-1])

        # Rechteck und Spieler Textfeld
        self.player = self.canvas.create_text(360, 20, text="Spieler 1 ist dran", font=self.canvas.textSize)
        self.canvas.create_rectangle(0, 100, 720, 670, fill=View.blue)

        # Slots
        self.slots = {}
        for yOne, yTwo, y in zip(range(120, 570+1, 90), range(200, 750+1, 90), range(1, (6+1))):
            for xOne, xTwo, x in zip(range(20, 620+1, 100), range(100, 700+1, 100), range(1, (7+1))):
                self.slots[x, y] = self.canvas.create_oval(xOne, yOne, xTwo, yTwo, fill=View.grey)

        #######################Fenster zentrieren########################

        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()

        positionRight = int(self.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(self.winfo_screenheight() / 3.2 - windowHeight / 2)

        self.geometry("+{}+{}".format(positionRight, positionDown))

        #################################################################

    def chipDropper(self, coordinate: tuple, color: str):
        column_list = []
        for xOne, xTwo in zip(range(20, 620+1, 100), range(100, 700+1, 100)):
            column_list.append((xOne, 120, xTwo, 200))
        chip_position = column_list[coordinate[0]-1]

        row_list = []
        for yOne, yTwo in zip(range(120, ((coordinate[1]*100)+20)+1, 100), range(200, ((coordinate[1]*100)+100)+1, 100)):
            row_list.append((20, yOne, 100, yTwo))

        chip = self.canvas.create_oval(chip_position, fill=color)

        # Deaktiviert alle Knöpfe, die aktiv sind während der Fall Animation
        normal_buttons = []
        for button in self.buttons:
            if button["state"] == NORMAL:
                button.configure(state=DISABLED, disabledforeground="black")
                normal_buttons.append(button)

        # Fall Animation
        for row in row_list:
            self.after(60)
            self.canvas.update()
            self.canvas.move(chip, 0, 90)
        self.canvas.delete(chip)
        self.canvas.itemconfig(self.slots[coordinate], fill=color)

        # Aktiviert alle Buttons die davor an waren
        for button in normal_buttons:
            button.configure(state=NORMAL)

    # Deaktiviert einen Button
    def deactivateButton(self, button):
        if self.buttons[button-1]["bg"] == View.red:
            self.buttons[button-1].configure(cursor="", bg=View.disabledRed, state=DISABLED, disabledforeground="grey")
        else:
            self.buttons[button-1].configure(cursor="", bg=View.disabledYellow, state=DISABLED, disabledforeground="grey")


# eigener Controller zum Testen
class Controller(object):
    def __init__(self):
        self.view = View(self.caller)
        self.view.mainloop()

    def caller(self, column: int):
        print(column)
        if self.view.buttons[0]["bg"] == View.red:
            for button in self.view.buttons:
                button.configure(bg=View.yellow, activebackground=View.darkYellow)
            self.view.canvas.itemconfig(self.view.player, text="Spieler 1 ist dran")
            self.view.chipDropper((column, 6), View.red)
        else:
            for button in self.view.buttons:
                button.configure(bg=View.red, activebackground=View.darkRed)
            self.view.canvas.itemconfig(self.view.player, text="Spieler 2 ist dran")
            self.view.chipDropper((column, 5), View.yellow)


if __name__ == "__main__":
    Controller()

# Neustart und Beenden Button machen
