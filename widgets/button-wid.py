#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)
        closeButton = wx.Button(panel, label="Close", pos=(20, 20))
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
        self.SetSize((350, 250))
        self.SetTitle("It's a wx Button!")
        self.Center()

    def OnClose(self, evt):
        self.Close(True)


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
