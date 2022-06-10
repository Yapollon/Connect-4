from tkinter import *
import tkinter.font as tkfont
import customtkinter


# a subclass of Canvas for dealing with resizing of windows
class ResizingCTkCanvas(customtkinter.CTkCanvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()
        self.textSize = tkfont.Font()
        self.buttonSize = tkfont.Font()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        widthScale = float(event.width)/self.width
        heightScale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, widthScale, heightScale)

        width = event.width / 30
        self.textSize.configure(size=int(width))
        if event.width > 1000:
            self.textSize.configure(size=35)
        elif event.width < 250:
            self.textSize.configure(size=8)

        width2 = event.width / 75
        self.buttonSize.configure(size=int(width2))

    def textSize(self):
        return self.textSize

    def buttonSize(self):
        return self.buttonSize
