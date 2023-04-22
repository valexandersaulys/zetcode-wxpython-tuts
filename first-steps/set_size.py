#!/usr/bin/env python3.10

import wx

"""
We can pass in a `size` argument. Here we subclass Frame to specify it. 
"""


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(350, 350))


def main():
    app = wx.App()
    ex = Example(None, title="Sizing")
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
