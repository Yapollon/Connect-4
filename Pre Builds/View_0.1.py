from tkinter import *
from tkinter import ttk


# The main class every other view is inheriting from
class View(Tk):
    def __init__(self, *callbacks):
        Tk.__init__(self)
        self.title("4 Gewinnt")
        self.geometry('720x670')
        self.resizable(None, None)

        # Canvas erstellen
        feld = Canvas(self, width=720, height=670)
        feld.pack()

        # Rechteck und Spieler Textfeld
        feld.create_rectangle(0, 100, 1000, 670, fill="#0d65a8")
        feld.create_text(360, 20, text="Spieler 1 ist dran")

        # Reihe 1
        feld.create_oval(20, 120, 100, 200, fill="#cccccc")
        feld.create_oval(120, 120, 200, 200, fill="#cccccc")
        feld.create_oval(220, 120, 300, 200, fill="#cccccc")
        feld.create_oval(320, 120, 400, 200, fill="#cccccc")
        feld.create_oval(420, 120, 500, 200, fill="#cccccc")
        feld.create_oval(520, 120, 600, 200, fill="#cccccc")
        feld.create_oval(620, 120, 700, 200, fill="#cccccc")

        # Reihe 2
        feld.create_oval(20, 210, 100, 290, fill="#cccccc")
        feld.create_oval(120, 210, 200, 290, fill="#cccccc")
        feld.create_oval(220, 210, 300, 290, fill="#cccccc")
        feld.create_oval(320, 210, 400, 290, fill="#cccccc")
        feld.create_oval(420, 210, 500, 290, fill="#cccccc")
        feld.create_oval(520, 210, 600, 290, fill="#cccccc")
        feld.create_oval(620, 210, 700, 290, fill="#cccccc")

        # Reihe 3
        feld.create_oval(20, 300, 100, 380, fill="#cccccc")
        feld.create_oval(120, 300, 200, 380, fill="#cccccc")
        feld.create_oval(220, 300, 300, 380, fill="#cccccc")
        feld.create_oval(320, 300, 400, 380, fill="#cccccc")
        feld.create_oval(420, 300, 500, 380, fill="#cccccc")
        feld.create_oval(520, 300, 600, 380, fill="#cccccc")
        feld.create_oval(620, 300, 700, 380, fill="#cccccc")

        # Reihe 4
        feld.create_oval(20, 390, 100, 470, fill="#cccccc")
        feld.create_oval(120, 390, 200, 470, fill="#cccccc")
        feld.create_oval(220, 390, 300, 470, fill="#cccccc")
        feld.create_oval(320, 390, 400, 470, fill="#cccccc")
        feld.create_oval(420, 390, 500, 470, fill="#cccccc")
        feld.create_oval(520, 390, 600, 470, fill="#cccccc")
        feld.create_oval(620, 390, 700, 470, fill="#cccccc")

        # Reihe 5
        feld.create_oval(20, 480, 100, 560, fill="#cccccc")
        feld.create_oval(120, 480, 200, 560, fill="#cccccc")
        feld.create_oval(220, 480, 300, 560, fill="#cccccc")
        feld.create_oval(320, 480, 400, 560, fill="#cccccc")
        feld.create_oval(420, 480, 500, 560, fill="#cccccc")
        feld.create_oval(520, 480, 600, 560, fill="#cccccc")
        feld.create_oval(620, 480, 700, 560, fill="#cccccc")

        # Reihe 6
        feld.create_oval(20, 570, 100, 650, fill="#cccccc")
        feld.create_oval(120, 570, 200, 650, fill="#cccccc")
        feld.create_oval(220, 570, 300, 650, fill="#cccccc")
        feld.create_oval(320, 570, 400, 650, fill="#cccccc")
        feld.create_oval(420, 570, 500, 650, fill="#cccccc")
        feld.create_oval(520, 570, 600, 650, fill="#cccccc")
        feld.create_oval(620, 570, 700, 650, fill="#cccccc")

        #######################Fenster zentrieren########################

        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        positionRight = int(self.winfo_screenwidth() / 3.8 - windowWidth / 2)
        positionDown = int(self.winfo_screenheight() / 3.2 - windowHeight / 2)

        self.geometry("+{}+{}".format(positionRight, positionDown))

        #################################################################

        self.mainloop()

    def playerLabel(self, player):
        pass

    def killView(self):
        self.destroy()


if __name__ == "__main__":
    View()
