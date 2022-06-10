from superView import View


# Controller zum Testen
class Controller(object):
    def __init__(self):
        self.view = View(self.caller)
        self.view.mainloop()

    def caller(self, column: int):
        print(column)
        if self.view.buttons[0]["bg"] == View.red:
            for button in self.view.buttons:
                button.configure(bg=View.yellow[0], activebackground=View.yellow[1])
            self.view.canvas.itemconfig(self.view.player, text="Spieler 1 ist dran")
            self.view.chipDropper((column, 6), View.red[0])
        else:
            for button in self.view.buttons:
                button.configure(bg=View.red[0], activebackground=View.red[1])
            self.view.canvas.itemconfig(self.view.player, text="Spieler 2 ist dran")
            self.view.chipDropper((column, 5), View.yellow[0])
