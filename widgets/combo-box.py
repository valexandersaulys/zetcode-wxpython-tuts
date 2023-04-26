#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)

        distros = ["A", "B", "C", "D"]
        cb = wx.ComboBox(
            panel, pos=(50, 30), choices=distros, style=wx.CB_READONLY  # ?
        )

        self.st = wx.StaticText(panel, label="", pos=(50, 140))
        cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)

        self.SetSize((350, 350))
        self.SetTitle("Toggle Buttons")
        self.Center()

    def OnSelect(self, evt):
        i = evt.GetString()
        self.st.SetLabel(i)


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
