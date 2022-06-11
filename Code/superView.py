# superView.py
# Klasse zum Generieren eines Benutzer-Interfaces
# Programm von Daniel & Yassin

from tkinter import *
from functools import partial
from ResizingCanvas import ResizingCanvas


class View(Tk):

    # Farbcodes
    # für red und yellow gilt [normal, dunkel, hell]
    red = ['#fc5858', "#d94c4c", "#fda0a0"]
    yellow = ['#ffef00', "#e6d700", "#FFF9A4"]
    blue = "#0d65a8"
    grey = ["#f0f0f0", "#cccccc"]

    def __init__(self, start_callback, game_callback):
        Tk.__init__(self)

        self.title("4 Gewinnt")
        self.geometry('720x670')
        # self.overrideredirect(True)
        self.start_callback = start_callback
        self.game_callback = game_callback
        self.game = Game(self)
        self.settings = Settings(self)

        ########################## Fenster zentrieren ###########################

        positionRight = int(self.winfo_screenwidth() / 3 - self.winfo_reqwidth() / 2)
        positionDown = int(self.winfo_screenheight() / 3.2 - self.winfo_reqheight() / 2)

        self.geometry(f"+{positionRight}+{positionDown}")

        ####################################ä####################################

    def changeFrame(self, current_frame: Frame, new_frame: Frame):
        current_frame.pack_forget()
        new_frame.pack(fill=BOTH, expand=YES)


class Game(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=YES)

        # Canvas
        self.canvas = ResizingCanvas(self, width=720, height=670, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Einstellungen Button
        self.photo = PhotoImage(file="images/settings30x30.ppm")
        self.settings = Button(self, image=self.photo, cursor="hand2", relief="flat", command=lambda: parent.changeFrame(self, parent.settings))
        self.canvas.create_window(695, 24, tags="settings", window=self.settings)

        # Start/Neustart Button
        self.restart = Button(self, width=10, height=1, text="START", font=("", 16), cursor="hand2", bg=View.red[0],
                              activebackground=View.red[1], command=parent.start_callback)
        self.canvas.create_window(360, 70, tags="restart", window=self.restart)

        # Chip Einwurf Buttons
        self.buttons = []
        for i, position in zip(range(1, 7+1), range(61, 661+1, 100)):
            self.buttons.append(Button(self, width=10, height=2, text="▼", cursor="hand2", command=partial(parent.game_callback, i)))
            self.canvas.create_window(position, 70, tags="dropButton", state=HIDDEN, window=self.buttons[i-1])

        # Rechteck und Spieler Textfeld
        self.player = self.canvas.create_text(360, 20, text="", font=self.canvas.textSize)
        self.canvas.create_rectangle(0, 100, 720, 670, fill=View.blue)

        # Slots
        self.slots = {}
        for yOne, yTwo, y in zip(range(120, 570+1, 90), range(200, 750+1, 90), range(1, (6+1))):
            for xOne, xTwo, x in zip(range(20, 620+1, 100), range(100, 700+1, 100), range(1, (7+1))):
                self.slots[x, y] = self.canvas.create_oval(xOne, yOne, xTwo, yTwo, fill=View.grey[0])

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
        for row in range(1, coordinate[1]):
            self.after(60)
            self.canvas.update()
            self.canvas.move(chip, 0, 90)
        self.canvas.delete(chip)
        self.canvas.itemconfig(self.slots[coordinate], fill=color[0])

        # Aktiviert alle Buttons die davor an waren
        for button in normal_buttons:
            button.configure(state=NORMAL)

    # Ändert den Spieler-Text
    def changePlayerText(self, player: str):
        self.canvas.itemconfig(self.player, text=player)

    # Ändert die Buttonfarbe
    def changeButtonColor(self, color: list):
        for button in self.buttons:
            if button["state"] == NORMAL:
                button.configure(bg=color[0], activebackground=color[1])

    # Deaktiviert einen Button
    def deactivateButton(self, button: int):
        self.buttons[button-1].configure(cursor="", bg=View.grey[1], state=DISABLED, disabledforeground="grey")

    # Lässt die 4 Slots bei Gewinn leuchten
    def flash4(self, coordinates: list, color: list):
        x = 0
        while self.canvas.itemcget("restart", "state") == NORMAL:
            x = 2 if x == 0 else 0  # Macht das sich x bei jedem loop zwischen 0 und 3 wechselt
            for coordinate in coordinates:
                self.canvas.itemconfig(self.slots[coordinate], fill=color[x])
            self.canvas.update()
            self.after(200)

    # Was passiert, wenn das Spiel beendet wird
    def End(self):
        self.canvas.itemconfig("dropButton", state=HIDDEN)
        self.canvas.itemconfig("restart", state=NORMAL)
        self.restart.configure(text="Neustart")
        self.settings.configure(state=NORMAL, cursor="hand2")

    # Was passiert, wenn das Spiel gestartet wird
    def Start(self):
        self.canvas.itemconfig("restart", state=HIDDEN)
        self.canvas.itemconfig("dropButton", state=NORMAL)
        self.settings.configure(state=DISABLED, cursor="")
        for button in self.buttons:
            button.configure(state=NORMAL, cursor="hand2")


class Settings(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        # Canvas
        self.canvas = ResizingCanvas(self, width=720, height=670, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Zurück Button
        back = Button(self, text="Back", cursor="hand2", relief="flat", command=lambda: parent.changeFrame(self, parent.game))
        self.canvas.create_window(670, 5, anchor=NW, window=back)


if __name__ == "__main__":
    print("Funktioniert perfekt ★")
