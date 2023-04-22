#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        gs = wx.GridSizer(5, 4, 5, 5)

        gs.AddMany(
            [
                (wx.Button(self, label="Cls"), 0, wx.EXPAND),
                (wx.Button(self, label="Bck"), 0, wx.EXPAND),
                (wx.StaticText(self), wx.EXPAND),
                (wx.Button(self, label="Close"), 0, wx.EXPAND),
                (wx.Button(self, label="7"), 0, wx.EXPAND),
                (wx.Button(self, label="8"), 0, wx.EXPAND),
                (wx.Button(self, label="9"), 0, wx.EXPAND),
                (wx.Button(self, label="/"), 0, wx.EXPAND),
                (wx.Button(self, label="4"), 0, wx.EXPAND),
                (wx.Button(self, label="5"), 0, wx.EXPAND),
                (wx.Button(self, label="6"), 0, wx.EXPAND),
                (wx.Button(self, label="*"), 0, wx.EXPAND),
                (wx.Button(self, label="1"), 0, wx.EXPAND),
                (wx.Button(self, label="2"), 0, wx.EXPAND),
                (wx.Button(self, label="3"), 0, wx.EXPAND),
                (wx.Button(self, label="-"), 0, wx.EXPAND),
                (wx.Button(self, label="0"), 0, wx.EXPAND),
                (wx.Button(self, label="."), 0, wx.EXPAND),
                (wx.Button(self, label="="), 0, wx.EXPAND),
                (wx.Button(self, label="+"), 0, wx.EXPAND),
            ]
        )

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
