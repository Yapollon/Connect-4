# superView.py
# Klasse zum Generieren eines Benutzer-Interfaces
# Programm von Daniel & Yassin

from tkinter import *
from functools import partial
from ResizingCanvas import ResizingCanvas


# self.withdraw()
# self.deiconify()

class View(Tk):

    # Farbcodes
    # für red und yellow gilt [normal, dunkel, hell]
    red = ['#fc5858', "#d94c4c", "#fda0a0"]
    yellow = ['#ffef00', "#e6d700", "#FFF9A4"]
    blue = "#0d65a8"
    grey = "#cccccc"

    def __init__(self, callback):
        Tk.__init__(self)
        self.title("4 Gewinnt")
        self.geometry('720x670')
        self.resizable(False, False)
        self.callback = callback

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Game, Settings):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

        #######################Fenster zentrieren########################

        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()

        positionRight = int(self.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(self.winfo_screenheight() / 3.2 - windowHeight / 2)

        self.geometry("+{}+{}".format(positionRight, positionDown))

        #################################################################

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

    def chipDropper(self, coordinate: tuple, color: list):
        self.frames["Game"].chipDropper(coordinate, color)

    def changePlayerText(self, player: int):
        self.frames["Game"].changePlayerText(player)

    def changeButtonColor(self, color: list):
        self.frames["Game"].changeButtonColor(color)

    def deactivateButton(self, button: int):
        self.frames["Game"].deactivateButton(button)

    def flash4(self, coordinates: list, color: list):
        self.frames["Game"].flash4(coordinates, color)


class Game(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, controller)
        self.controller = controller
        callback = self.controller.callback.get()

        # Canvas
        self.canvas = ResizingCanvas(self, width=720, height=670, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Einstellungen Button
        self.photo = PhotoImage(file="settings30x30.ppm")
        settings = Button(self, image=self.photo, cursor="hand2", relief="flat", command=lambda: controller.show_frame("Settings"))
        self.canvas.create_window(670, 5, anchor=NW, window=settings)

        # Chip Einwurf Buttons
        self.buttons = []
        for i, position in zip(range(1, 7+1), range(20, 620+1, 100)):
            self.buttons.append(Button(self, width=10, height=2, text="▼", cursor="hand2", font=self.canvas.buttonSize, command=partial(callback, i)))
            self.canvas.create_window(position, 50, anchor=NW, window=self.buttons[i-1])

        # Rechteck und Spieler Textfeld
        self.player = self.canvas.create_text(360, 20, text="Spieler 1 ist dran", font=self.canvas.textSize)
        self.canvas.create_rectangle(0, 100, 720, 670, fill=View.blue)

        # Slots
        self.slots = {}
        for yOne, yTwo, y in zip(range(120, 570+1, 90), range(200, 750+1, 90), reversed(range(1, (6+1)))):
            for xOne, xTwo, x in zip(range(20, 620+1, 100), range(100, 700+1, 100), range(1, (7+1))):
                self.slots[x, y] = self.canvas.create_oval(xOne, yOne, xTwo, yTwo, fill=View.grey)

    # Methode zur Animation des Chip-Einwurfs und der anschließenden Färbung des Slots
    def chipDropper(self, coordinate: tuple, color: list):
        # Ermittelt die Koordinaten an denen der Chip für die Animation erstellt wird
        column_list = []
        for xOne, xTwo in zip(range(20, 620+1, 100), range(100, 700+1, 100)):
            column_list.append((xOne, 120, xTwo, 200))
        chip = self.canvas.create_oval(column_list[coordinate[0]-1], fill=color[0])

        # Deaktiviert alle Knöpfe, die aktiv sind während der Fall Animation
        normal_buttons = []
        for button in self.buttons:
            if button["state"] == NORMAL:
                button.configure(state=DISABLED, disabledforeground="black")
                normal_buttons.append(button)

        # Fall Animation
        for row in range(coordinate[1], 6):
            self.after(60)
            self.canvas.update()
            self.canvas.move(chip, 0, 90)
        self.canvas.delete(chip)
        self.canvas.itemconfig(self.slots[coordinate], fill=color[0])

        # Aktiviert alle Buttons die davor an waren
        for button in normal_buttons:
            button.configure(state=NORMAL)

        # self.flash4([(2, 2), (3, 2), (4, 2), (5, 2)], View.red)

    # Ändert den Spieler-Text
    def changePlayerText(self, player: int):
        self.canvas.itemconfig(self.player, text=f"Spieler {player} ist dran")

    # Ändert die Buttonfarbe
    def changeButtonColor(self, color: list):
        for button in self.buttons:
            if button["state"] == NORMAL:
                button.configure(bg=color[0], activebackground=color[1])

    # Deaktiviert einen Button
    def deactivateButton(self, button: int):
        self.buttons[button-1].configure(cursor="", bg=View.grey, state=DISABLED, disabledforeground="grey")

    # Lässt die 4 Slots bei Gewinn leuchten
    def flash4(self, coordinates: list, color: list):
        x = 0
        for i in range(0, 10):
            x = 2 if x == 0 else 0  # Macht das sich x bei jedem loop zwischen 0 und 3 wechselt
            for coordinate in coordinates:
                self.canvas.itemconfig(self.slots[coordinate], fill=color[x])
            self.canvas.update()
            self.after(200)


class Settings(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, controller)
        self.controller = controller

        # Canvas
        self.canvas = ResizingCanvas(self, width=720, height=670, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Zurück Button
        back = Button(self, text="Back", cursor="hand2", relief="flat", command=lambda: controller.show_frame("Game"))
        self.canvas.create_window(670, 5, anchor=NW, window=back)


if __name__ == "__main__":
    print("Funktioniert perfekt ★")


# Neustart und Beenden Button machen
