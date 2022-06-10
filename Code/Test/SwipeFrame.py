import tkinter as tk


# ---- Definition of SwipeFrame ---------------

class SwipeFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        kwargs['width'] = 200
        kwargs['height'] = 150
        tk.Frame.__init__(self, master, **kwargs)
        self.ydown = 300
        self.yup = 150
        self.timestep = 3
        self.place(y=self.ydown, x=0)

    def wish_on(self):
        self.wish(self.ydown, self.yup, -1, self.timestep)

    def wish_off(self):
        self.wish(self.yup, self.ydown, 1, self.timestep)

    def wish(self, y0, yn, step, timestep):
        def do_move(y):
            y += step
            self.place(y=y)
            if y != yn:
                self.after(timestep, do_move, y)

        do_move(y0)


# ---- GUI ---------------------------------------

class Mainframe(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        tk.Label(self, text='Screen', bg=self['bg']).place(y=0, x=0)
        tk.Button(self, text='wish on', command=self.wish_on).place(y=243, x=50)
        self.button_frame = ButtonFrame(self, bg='#d9d93c')

    def wish_on(self):
        self.button_frame.wish_on()


class ButtonFrame(SwipeFrame):
    def __init__(self, master, **kwargs):
        SwipeFrame.__init__(self, master, **kwargs)
        tk.Label(self, text='Swipe Window', bg=self['bg']).place(y=0, x=0)
        tk.Button(self, text='wish off', command=self.wish_off).place(y=93, x=50)


def main():
    app = tk.Tk()
    app.geometry("280x370")
    mainframe = Mainframe(app, width=200, bg='#d949d9', height=300)
    mainframe.place(y=28, x=43)
    app.mainloop()


if __name__ == '__main__':
    main()