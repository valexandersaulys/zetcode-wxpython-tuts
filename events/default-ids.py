#!/usr/bin/env python3.10

import wx

"""
> Automatically created id's are always negative, whereas user specified 
> ids must always be positive.

Can pass in either -1 for ID or wx.ID_ANY and wxPython will create the ID
for you. 

wx.ID_ANY is preferred as it may make a difference depending on the host
operating system environment. 
"""


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        pnl = wx.Panel(self)
        exitButton = wx.Button(pnl, wx.ID_ANY, "Exit", (10, 10))
        self.Bind(wx.EVT_BUTTON, self.OnExit, id=exitButton.GetId())
        self.SetTitle("Automatic IDs")
        self.Center()

    def OnExit(self, evt):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
