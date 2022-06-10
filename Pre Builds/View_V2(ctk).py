import tkinter
import customtkinter
from ResizingCTkCanvas import ResizingCTkCanvas


class View(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("4 Gewinnt")
        self.geometry('720x670')

        # Canvas erstellen
        feld = ResizingCTkCanvas(self, width=720, height=670, highlightthickness=0)
        feld.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        feld.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        # Drop Buttons

        self.button1 = customtkinter.CTkButton(self, width=10, height=2, text="▼", command=self.chipDropper, bg="#fc5858", highlightbackground="#d94c4c")
        self.button2 = customtkinter.CTkButton(self, width=10, height=2, text="▼", command=self.chipDropper, bg="#fc5858", highlightbackground="#d94c4c")
        self.button3 = customtkinter.CTkButton(self, width=10, height=2, text="▼", command=self.chipDropper, bg="#fc5858", highlightbackground="#d94c4c")
        self.button4 = customtkinter.CTkButton(self, width=10, height=2, text="▼", command=self.chipDropper, bg="#fc5858", highlightbackground="#d94c4c")
        self.button5 = customtkinter.CTkButton(self, width=10, height=2, text="▼", command=self.chipDropper, bg="#fc5858", highlightbackground="#d94c4c")
        self.button6 = customtkinter.CTkButton(self, width=10, height=2, text="▼", command=self.chipDropper, bg="#fc5858", highlightbackground="#d94c4c")
        self.button7 = customtkinter.CTkButton(self, width=10, height=2, text="▼", command=self.chipDropper, bg="#fc5858", highlightbackground="#d94c4c")

        feld.create_window(20, 50, anchor=tkinter.NW, window=self.button1)
        feld.create_window(120, 50, anchor=tkinter.NW, window=self.button2)
        feld.create_window(220, 50, anchor=tkinter.NW, window=self.button3)
        feld.create_window(320, 50, anchor=tkinter.NW, window=self.button4)
        feld.create_window(420, 50, anchor=tkinter.NW, window=self.button5)
        feld.create_window(520, 50, anchor=tkinter.NW, window=self.button6)
        feld.create_window(620, 50, anchor=tkinter.NW, window=self.button7)

        # Rechteck und Spieler Textfeld
        feld.create_text(360, 20, text="Spieler 1 ist dran", font=feld.textSize)
        feld.create_rectangle(0, 100, 720, 670, fill="#0d65a8")

        for yOne, yTwo in zip(range(120, 571, 90), range(200, 651, 90)):
            for xOne, xTwo in zip(range(20, 621, 100), range(100, 701, 100)):
                feld.create_oval(xOne, yOne, xTwo, yTwo, fill="#cccccc")

        #######################Fenster zentrieren########################

        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()

        positionRight = int(self.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(self.winfo_screenheight() / 3.2 - windowHeight / 2)

        self.geometry("+{}+{}".format(positionRight, positionDown))

        #################################################################

        self.mainloop()

    def playerLabel(self, player):
        pass

    def chipDropper(self):
        pass


if __name__ == "__main__":
    View()
