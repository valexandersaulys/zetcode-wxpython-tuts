#!/usr/bin/env python3.10

import wx
import wx.html


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        htmlwin = wx.html.HtmlWindow(panel, wx.ID_ANY, style=wx.NO_BORDER)
        htmlwin.SetStandardFonts()
        htmlwin.LoadPage("page.html")

        vbox.Add((-1, 10), 0)
        vbox.Add(htmlwin, 1, wx.EXPAND | wx.ALL, 9)

        bitmap = wx.StaticBitmap(
            panel, wx.ID_ANY, wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_UNDO))
        )
        hbox.Add(bitmap, 0, wx.LEFT | wx.BOTTOM | wx.TOP, 10)
        btnOkay = wx.Button(panel, wx.ID_ANY, "Okay")

        self.Bind(wx.EVT_BUTTON, self.OnClose, id=btnOkay.GetId())

        # hbox.Add((100, -1), 1, wx.EXPAND | wx.ALIGN_RIGHT)
        hbox.Add((100, -1), 1, wx.EXPAND)
        hbox.Add(btnOkay, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        vbox.Add(hbox, 0, wx.EXPAND)

        panel.SetSizer(vbox)

        self.SetTitle("Basic Statistics")
        self.Center()

    def OnClose(self, evt):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
