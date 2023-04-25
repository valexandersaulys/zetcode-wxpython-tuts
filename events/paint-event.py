#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        self.count = 0

        # Note: every resize is a paint event
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("Paint Events")
        self.SetSize((350, 350))
        self.Center()

    def OnPaint(self, evt):
        self.count += 1
        _dc = wx.PaintDC(self)
        text = "Number of paint events: %d" % self.count
        _dc.DrawText(text, 20, 20)


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
