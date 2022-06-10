from tkinter import *
from ResizingCanvas import ResizingCanvas


class View(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("4 Gewinnt")
        self.geometry('720x670')
        self.slots = {}

        # Canvas erstellen
        self.canvas = ResizingCanvas(self, width=720, height=670, highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Drop Buttons
        self.button1 = Button(self, width=10, height=2, text="▼", bg="#fc5858", activebackground="#d94c4c", cursor="hand2", font=self.canvas.buttonSize)
        self.button2 = Button(self, width=10, height=2, text="▼", bg="#fc5858", activebackground="#d94c4c", cursor="hand2", font=self.canvas.buttonSize)
        self.button3 = Button(self, width=10, height=2, text="▼", bg="#fc5858", activebackground="#d94c4c", cursor="hand2", font=self.canvas.buttonSize)
        self.button4 = Button(self, width=10, height=2, text="▼", bg="#fc5858", activebackground="#d94c4c", cursor="hand2", font=self.canvas.buttonSize)
        self.button5 = Button(self, width=10, height=2, text="▼", bg="#fc5858", activebackground="#d94c4c", cursor="hand2", font=self.canvas.buttonSize)
        self.button6 = Button(self, width=10, height=2, text="▼", bg="#fc5858", activebackground="#d94c4c", cursor="hand2", font=self.canvas.buttonSize)
        self.button7 = Button(self, width=10, height=2, text="▼", bg="#fc5858", activebackground="#d94c4c", cursor="hand2", font=self.canvas.buttonSize)

        self.canvas.create_window(20, 50, anchor=NW, window=self.button1)
        self.canvas.create_window(120, 50, anchor=NW, window=self.button2)
        self.canvas.create_window(220, 50, anchor=NW, window=self.button3)
        self.canvas.create_window(320, 50, anchor=NW, window=self.button4)
        self.canvas.create_window(420, 50, anchor=NW, window=self.button5)
        self.canvas.create_window(520, 50, anchor=NW, window=self.button6)
        self.canvas.create_window(620, 50, anchor=NW, window=self.button7)

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

    def changeSlotColor(self, cord: tuple, color: str):
        self.canvas.itemconfig(self.slots[cord], fill=color)


if __name__ == "__main__":
    View()
