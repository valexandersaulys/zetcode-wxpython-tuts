#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()
        self.Center()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#4f5049")

        vbox = wx.BoxSizer(wx.VERTICAL)

        midPan = wx.Panel(panel)
        midPan.SetBackgroundColour("#ededed")

        # I still don't quite follow how the ID and other keywords get passed here
        # 20 is supposed to be the margin or padding I think
        vbox.Add(midPan, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        panel.SetSizer(vbox)


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
