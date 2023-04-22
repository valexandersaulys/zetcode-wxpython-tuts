#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)
        # vgap: int, hgap: int
        sizer = wx.GridBagSizer(4, 4)

        text = wx.StaticText(panel, label="Rename to...")
        sizer.Add(text, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.tc = wx.TextCtrl(panel)
        sizer.Add(
            self.tc,
            pos=(1, 0),  # begin on the second row
            span=(2, 5),  # expand 1 row, 5 columns
            flag=wx.EXPAND | wx.LEFT | wx.RIGHT,
            border=5,  # 5 pixel border of space to the left and right
        )

        buttonOk = wx.Button(panel, label="Ok", size=(90, 28))
        self.Bind(wx.EVT_BUTTON, self.RenameWindow, id=buttonOk.GetId())
        buttonClose = wx.Button(panel, label="Close", size=(90, 28))
        sizer.Add(buttonOk, pos=(3, 3))
        sizer.Add(buttonClose, pos=(3, 4), flag=wx.RIGHT | wx.BOTTOM, border=10)

        # we then keep growing, adding rows and columns here to the sizer
        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(3)
        panel.SetSizer(sizer)

    def RenameWindow(self, evt):
        # print(self.tc.GetValue())
        self.SetTitle(self.tc.GetValue())


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None, title="Rename")
    ex.Show()
    app.MainLoop()
