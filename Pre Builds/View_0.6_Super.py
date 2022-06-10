from tkinter import *
from functools import partial
from ResizingCanvas import ResizingCanvas

# Farbcodes
rot = '#fc5858'
dunkelrot = "#d94c4c"
gelb = '#ffef00'
dunkelgelb = "#e6d700"
blau = "#0d65a8"
grau = "#cccccc"

#Position der Ovale in Reihen und Spalten
spalte1 = (20, 120, 100, 200)
spalte2 = (120, 120, 200, 200)
spalte3 = (220, 120, 300, 200)
spalte4 = (320, 120, 400, 200)
spalte5 = (420, 120, 500, 200)
spalte6 = (520, 120, 600, 200)
spalte7 = (620, 120, 700, 200)
        
reihe6 = (20, 120, 100, 200)
reihe5 = (20, 220, 100, 300)
reihe4 = (20, 320, 100, 400)
reihe3 = (20, 420, 100, 500)
reihe2 = (20, 520, 100, 600)
reihe1 = (20, 620, 100, 700)


class View(Tk):

    def __init__(self, callback):
        Tk.__init__(self)
        self.callback = callback
        self.title("4 Gewinnt")
        self.geometry('720x670')
        self.resizable(False, False)
        #self.overrideredirect(True)

        self.buttons = []
        self.slots = {}

        # Canvas erstellen
        self.canvas = ResizingCanvas(self, width=720, height=670, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Buttons
        for i, position in zip(range(1, 8), range(20, 621, 100)):
            self.buttons.append(Button(self, width=10, height=2, text="▼", bg=rot, activebackground=dunkelrot, cursor="hand2", font=self.canvas.buttonSize, command=partial(callback, i)))
            self.canvas.create_window(position, 50, anchor=NW, window=self.buttons[i-1])

        # Rechteck und Spieler Textfeld
        self.player = self.canvas.create_text(360, 20, text="Spieler 1 ist dran", font=self.canvas.textSize)
        self.canvas.create_rectangle(0, 100, 720, 670, fill=blau)

        # Slot-Generierung
        for yOne, yTwo, y in zip(range(120, 571, 90), range(200, 751, 90), reversed(range(1, (6 + 1)))):
            for xOne, xTwo, x in zip(range(20, 621, 100), range(100, 701, 100), range(1, (7 + 1))):
                self.slots[x, y] = self.canvas.create_oval(xOne, yOne, xTwo, yTwo, fill=grau)

        #######################Fenster zentrieren########################

        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()

        positionRight = int(self.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(self.winfo_screenheight() / 3.2 - windowHeight / 2)

        self.geometry("+{}+{}".format(positionRight, positionDown))

        #################################################################

        #Animation und Slot wird gefärbt
        self.chipDropper(spalte1, reihe1, (1, 1), gelb)
        self.chipDropper(spalte1, reihe2, (1, 2), rot)
        self.chipDropper(spalte1, reihe3, (1, 3), rot)
        self.chipDropper(spalte1, reihe4, (1, 4), rot)
        self.chipDropper(spalte1, reihe5, (1, 5), rot)
        self.chipDropper(spalte1, reihe6, (1, 6), rot)
        
        self.chipDropper(spalte2, reihe1, (2, 1), gelb)

    def chipDropper(self, spalte: tuple, reihe: tuple, coordinate: tuple, color: str):
        first = reihe6
        end = reihe
        diff = (end[0] - first[0], end[1] - first[1], end[2] - first[2], end[3] - first[3])
        chip = self.canvas.create_oval(spalte, fill=color)
        while diff > (0, 0, 0, 0):
            self.after(150)
            self.canvas.update()
            self.canvas.move(chip, 0, 90)
            diff = (diff[0] - 0, diff[1] - 90, diff[2] - 0, diff[3] - 90)
        self.canvas.delete(chip)
        self.canvas.itemconfig(self.slots[coordinate], fill=color)

    def changeSlotColor(self, coordinate: tuple, color: str):
        self.canvas.itemconfig(self.slots[coordinate], fill=color)


class Controller(object):
    def __init__(self):
        self.view = View(self.caller)
        self.view.mainloop()

    def caller(self, column: int):
        print(column)
        if self.view.buttons[0]["bg"] == rot:
            for button in self.view.buttons:
                button.configure(bg=gelb, activebackground=dunkelgelb)
            self.view.canvas.itemconfig(self.view.player, text="Spieler 2 ist dran")
        else:
            for button in self.view.buttons:
                button.configure(bg=rot, activebackground=dunkelrot)
            self.view.canvas.itemconfig(self.view.player, text="Spieler 1 ist dran")


if __name__ == "__main__":
    Controller()

# Neustart und Beenden Button machen
# Button ausgrauen, wenn Spalte voll ist
