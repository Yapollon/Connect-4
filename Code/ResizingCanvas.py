from tkinter import *
import tkinter.font as tkfont


# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()
        self.textSize = tkfont.Font()

    def on_resize(self, event):

        x0, y0, x1, y1 = self.bbox('all')
        xratio = float(event.width) / x1
        yratio = float(event.height) / y1

        if xratio < yratio:
            self.scale('all', 0, 0, xratio, xratio)
        else:
            self.scale('all', 0, 0, yratio, yratio)

        width = event.width / 30
        self.textSize.configure(size=int(width))
        if event.width > 1000:
            self.textSize.configure(size=35)
        elif event.width < 250:
            self.textSize.configure(size=8)

    def textSize(self):
        return self.textSize
