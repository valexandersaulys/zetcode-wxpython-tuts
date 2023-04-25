#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        wx.StaticText(self, label="x", pos=(10, 10))
        wx.StaticText(self, label="y", pos=(10, 30))

        self.st1 = wx.StaticText(self, label="", pos=(30, 10))
        self.st2 = wx.StaticText(self, label="", pos=(30, 30))

        # bind a window move event(?) -- not sure if this is working
        # on Wayland
        self.Bind(wx.EVT_MOVE, self.onMove)

        self.SetSize((350, 250))
        self.SetTitle("Mouse Event")
        self.Center()

    def onMove(self, evt):
        # get the position of the mouse
        x, y = evt.GetPosition()

        # apply to labels
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
