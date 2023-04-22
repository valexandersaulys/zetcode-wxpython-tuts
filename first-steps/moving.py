#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(350, 350))

        """
        Neither of these work on Ubuntu?
        """
        # self.Move((0, 0))
        self.Center()


def main():
    app = wx.App()
    ex = Example(None, title="Moving")
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
