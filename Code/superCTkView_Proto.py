# superView.py
# Klasse zum Generieren eines Benutzer-Interfaces
# Programm von Daniel & Yassin

from tkinter import *
import customtkinter as ctk
from functools import partial
# from ResizingCanvas import ResizingCanvas


class View(ctk.CTk):

    # Farbcodes
    # für red und yellow gilt [normal, dunkel, hell]
    red = ['#fc5858', "#d94c4c", "#fda0a0"]
    yellow = ['#ffef00', "#e6d700", "#FFF9A4"]
    blue = "#0d65a8"
    grey = ["#f0f0f0", "#cccccc"]

    def __init__(self, start_callback, game_callback):
        super().__init__()

        self.title("4 Gewinnt")
        self.geometry(f"{720}x{670}")
        # self.overrideredirect(True)
        self.start_callback = start_callback
        self.game_callback = game_callback
        self.game = Game(self)
        self.settings = Settings(self)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        ########################## Fenster zentrieren ###########################

        positionRight = int(self.winfo_screenwidth() / 3 - self.winfo_reqwidth() / 2)
        positionDown = int(self.winfo_screenheight() / 3.2 - self.winfo_reqheight() / 2)

        self.geometry(f"+{positionRight}+{positionDown}")

        ####################################ä####################################

    def changeFrame(self, current_frame: Frame, new_frame: Frame):
        current_frame.grid_remove()
        new_frame.grid(row=0, column=0, sticky="nswe")


class Game(ctk.CTkFrame):

    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)
        self.configure(corner_radius=0, fg_color=("#F2F2F2", "#1F1F1F"))
        self.grid(row=0, column=0, sticky="nswe")

        # Canvas
        self.canvas = ctk.CTkCanvas(self, width=720, height=670, highlightthickness=0)
        self.canvas.grid(row=2, column=0, columnspan=6, sticky="nsew")

        # Switch für White/Dark-Mode
        self.modeSwitch = ctk.CTkSwitch(master=self, text="Dark Mode", command=self.change_mode)
        self.canvas.create_window(60, 24, window=self.modeSwitch)

        # Einstellungen Button
        self.photo = PhotoImage(file="images/settings.png")
        self.settings = ctk.CTkButton(self, width=40, height=40, image=self.photo, text="", command=lambda: parent.changeFrame(self, parent.settings))
        self.canvas.create_window(695, 24, tags="settings", window=self.settings)

        # Start/Neustart Button
        self.restart = ctk.CTkButton(self, width=140, height=35, corner_radius=10, text="START", fg_color=View.red[0],
                                     hover_color=View.red[1], command=parent.start_callback)
        self.canvas.create_window(360, 70, tags="restart", window=self.restart)

        # Chip Einwurf Buttons
        self.buttons = []
        for i, position in zip(range(1, 7+1), range(61, 661+1, 100)):
            self.buttons.append(ctk.CTkButton(self, width=80, height=34, corner_radius=10, border_width=2, border_color=("black", "white"), text="▼", text_color="black", command=partial(parent.game_callback, i)))
            self.canvas.create_window(position, 70, tags="dropButton", state=HIDDEN, window=self.buttons[i-1])

        # Rechteck und Spieler Textfeld
        self.player = self.canvas.create_text(360, 20, text="", tags="fixed_ratio")
        self.canvas.create_rectangle(0, 100, 720, 670, fill=View.blue, tags="fluid_ratio")

        # Slots
        self.slots = {}
        for yOne, yTwo, y in zip(range(120, 570+1, 90), range(200, 750+1, 90), range(1, (6+1))):
            for xOne, xTwo, x in zip(range(20, 620+1, 100), range(100, 700+1, 100), range(1, (7+1))):
                self.slots[x, y] = self.canvas.create_oval(xOne, yOne, xTwo, yTwo, fill=View.grey[0], tags='fixed_ratio')

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
            if button.state == NORMAL:
                button.configure(state=DISABLED)
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
            if button.state == NORMAL:
                button.configure(fg_color=color[0], hover_color=color[1])

    # Deaktiviert einen Button
    def deactivateButton(self, button: int):
        self.buttons[button-1].configure(fg_color=View.grey[1], state=DISABLED)

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
        self.settings.configure(state=NORMAL)

    # Was passiert, wenn das Spiel gestartet wird
    def Start(self):
        self.canvas.itemconfig("restart", state=HIDDEN)
        self.canvas.itemconfig("dropButton", state=NORMAL)
        self.settings.configure(state=DISABLED)
        for button in self.buttons:
            button.configure(state=NORMAL)

    def change_mode(self):
        if self.modeSwitch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")


class Settings(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        # Canvas
        self.canvas = ctk.CTkCanvas(self, width=720, height=670, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Zurück Button
        back = ctk.CTkButton(self, width=40, height=40, text="Back", command=lambda: parent.changeFrame(self, parent.game))
        self.canvas.create_window(660, 5, anchor=NW, window=back)


if __name__ == "__main__":
    print("Funktioniert perfekt ★")
