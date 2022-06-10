import tkinter as tk


# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):

        tk.Canvas.__init__(self, parent, **kwargs)
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.bind("<Configure>", self.on_resize)

        self.create_line(0, 0, 350, 200, fill='yellow')
        self.create_rectangle(50, 25, 150, 75, fill="blue")
        self.create_rectangle(100, 80, 250, 130, fill="green")

    def on_resize(self, event):
        x0, y0, x1, y1 = self.bbox('all')
        xratio = float(event.width) / x1
        yratio = float(event.height) / y1

        if xratio < yratio:
            self.scale('all', 0, 0, xratio, xratio)
        else:
            self.scale('all', 0, 0, yratio, yratio)


def main():
    app_win = tk.Tk()
    app_win.geometry('850x400+0+0')
    app_win.title('')

    myframe = tk.Frame(app_win)
    myframe.pack(fill=tk.BOTH, expand=tk.YES)
    mycanvas = ResizingCanvas(myframe, bg="red", highlightthickness=0)
    mycanvas.pack(fill=tk.BOTH, expand=tk.YES)

    app_win.mainloop()


if __name__ == "__main__":
    main()
