from tkinter import *
from ResizingCanvas import ResizingCanvas


# The main class every other view is inheriting from
class View(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("4 Gewinnt")
        self.geometry('720x670')
        self.resizable(False, False)

        # Canvas erstellen
        self.canvas = ResizingCanvas(self, width=720, height=670, highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Rechteck und Spieler Textfeld
        self.player = self.canvas.create_text(360, 20, text="Spieler 1 ist dran", font=self.canvas.textSize)
        self.canvas.create_rectangle(0, 100, 720, 670, fill="#0d65a8")

        for yOne, yTwo in zip(range(120, 571, 90), range(200, 751, 90)):
            for xOne, xTwo in zip(range(20, 621, 100), range(100, 701, 100)):
                self.canvas.create_oval(xOne, yOne, xTwo, yTwo, fill="#cccccc")

        #######################Fenster zentrieren########################

        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()

        positionRight = int(self.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(self.winfo_screenheight() / 3.2 - windowHeight / 2)

        self.geometry("+{}+{}".format(positionRight, positionDown))

        #################################################################

        self.mainloop()


if __name__ == "__main__":
    View()
