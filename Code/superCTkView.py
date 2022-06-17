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

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=2)
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_rowconfigure(2, weight=1000)

        # Switch für White/Dark-Mode
        self.modeSwitch = ctk.CTkSwitch(master=self, width=35, text="Dark Mode", command=self.change_mode)
        self.modeSwitch.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="w")

        # Spieler Textfeld
        self.player = ctk.CTkLabel(self, text="Spieler 1 ist dran", text_font=("", 20))
        self.player.grid(row=0, column=2, columnspan=3, sticky="nswe")

        # Einstellungen Button
        self.photo = PhotoImage(file="images/settings.png")
        self.settings = ctk.CTkButton(self, width=40, height=40, image=self.photo, text="", command=lambda: parent.changeFrame(self, parent.settings))
        self.settings.grid(row=0, column=6, padx=5, pady=5, sticky="e")

        # Start/Neustart Button

        self.restart = ctk.CTkButton(self, width=140, height=35, corner_radius=10, text="START", fg_color=View.red[0],
                                     hover_color=View.red[1], command=parent.start_callback)
        self.restart.grid(row=1, column=0, pady=5, padx=5, sticky="nswe")

        self.restart = ctk.CTkButton(self, width=140, height=35, corner_radius=10, text="START", fg_color=View.red[0],
                                     hover_color=View.red[1], command=parent.start_callback)
        self.restart.grid(row=1, column=1, pady=5, padx=5, sticky="nswe")

        self.restart = ctk.CTkButton(self, width=140, height=35, corner_radius=10, text="START", fg_color=View.red[0],
                                     hover_color=View.red[1], command=parent.start_callback)
        self.restart.grid(row=1, column=2, pady=5, padx=5, sticky="nswe")

        self.restart = ctk.CTkButton(self, width=140, height=35, corner_radius=10, text="START", fg_color=View.red[0],
                                     hover_color=View.red[1], command=parent.start_callback)
        self.restart.grid(row=1, column=3, pady=5, padx=5, sticky="nswe")
        self.restart = ctk.CTkButton(self, width=140, height=35, corner_radius=10, text="START", fg_color=View.red[0],
                                     hover_color=View.red[1], command=parent.start_callback)
        self.restart.grid(row=1, column=4, pady=5, padx=5, sticky="nswe")
        self.restart = ctk.CTkButton(self, width=140, height=35, corner_radius=10, text="START", fg_color=View.red[0],
                                     hover_color=View.red[1], command=parent.start_callback)
        self.restart.grid(row=1, column=5, pady=5, sticky="nswe")

        self.restart = ctk.CTkButton(self, width=140, height=35, corner_radius=10, text="START", fg_color=View.red[0],
                                     hover_color=View.red[1], command=parent.start_callback)
        self.restart.grid(row=1, column=6, pady=5, padx=5, sticky="nswe")

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
