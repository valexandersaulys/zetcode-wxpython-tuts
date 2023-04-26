#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)

        wx.StaticBox(panel, label="Personal Info", pos=(5, 5), size=(240, 170))
        wx.CheckBox(panel, label="Male", pos=(15, 30))
        wx.CheckBox(panel, label="Married", pos=(15, 55))

        # this isn't working?
        wx.StaticText(panel, label="Age", pos=(15, 95))
        wx.SpinCtrl(panel, value="1", pos=(55, 90), size=(60, -1), min=-1, max=120)

        btn = wx.Button(panel, label="Ok", pos=(90, 185), size=(60, -1))
        btn.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((270, 250))
        self.SetTitle("Static Box")
        self.Center()

    def OnClose(self, evt):
        self.Close(True)


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
