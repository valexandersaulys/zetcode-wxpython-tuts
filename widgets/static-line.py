#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)

        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(
            self, label="Central Europe", pos=(25, 15), size=(200, -1)
        )

        heading.SetFont(font)

        wx.StaticLine(self, pos=(25, 50), size=(300, 1))

        wx.StaticText(self, label="Slovakia", pos=(25, 80))
        wx.StaticText(self, label="Hungary", pos=(25, 100))
        wx.StaticText(self, label="Poland", pos=(25, 120))
        wx.StaticText(self, label="Czech Republic", pos=(25, 140))
        wx.StaticText(self, label="Germany", pos=(25, 160))
        wx.StaticText(self, label="Slovenia", pos=(25, 180))
        wx.StaticText(self, label="Austria", pos=(25, 200))
        wx.StaticText(self, label="Switzerland", pos=(25, 220))

        wx.StaticText(self, label="5 445 000", pos=(250, 80))
        wx.StaticText(self, label="10 014 000", pos=(250, 100))
        wx.StaticText(self, label="38 186 000", pos=(250, 120))
        wx.StaticText(self, label="10 562 000", pos=(250, 140))
        wx.StaticText(self, label="81 799 000", pos=(250, 160))
        wx.StaticText(self, label="2 050 000", pos=(250, 180))
        wx.StaticText(self, label="8 414 000", pos=(250, 200))
        wx.StaticText(self, label="7 866 000", pos=(250, 220))

        wx.StaticLine(self, pos=(25, 260), size=(300, 1))

        # the '000' is missing
        tsum = wx.StaticText(self, label="164 336 000", pos=(240, 280))
        sum_font = tsum.GetFont()
        sum_font.SetWeight(wx.BOLD)
        tsum.SetFont(sum_font)

        btn = wx.Button(self, label="Close", pos=(140, 310))

        btn.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((360, 380))
        self.SetTitle("Toggle Buttons")
        self.Center()

    def OnClose(self, evt):
        self.Close(True)


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
