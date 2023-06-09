#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)

        self.SetSize((350, 350))
        self.SetTitle("Toggle Buttons")
        self.Center()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
