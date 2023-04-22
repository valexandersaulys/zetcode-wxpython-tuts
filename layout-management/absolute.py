#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()
        self.Center()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("gray")

        self.LoadImages()

        # here positions are set in absolute terms relative to the container
        self.mincol.SetPosition((20, 20))
        self.baredejov.SetPosition((40, 160))
        self.rotunda.SetPosition((170, 50))

    def LoadImages(self):
        self.mincol = wx.StaticBitmap(
            self.panel, wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_ERROR)
        )
        self.baredejov = wx.StaticBitmap(
            self.panel, wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_QUESTION)
        )
        self.rotunda = wx.StaticBitmap(
            self.panel, wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_WARNING)
        )


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
