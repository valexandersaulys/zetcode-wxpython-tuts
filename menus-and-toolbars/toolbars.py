#!/usr/bin/env python3.10

import wx


"""
Multiple toolbars needs to be enclosed in a BoxSizer element
"""


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        toolbar1 = wx.ToolBar(self)
        toolbar1.AddTool(wx.ID_ANY, "", wx.ArtProvider.GetBitmap(wx.ART_NEW))
        toolbar1.AddTool(wx.ID_ANY, "", wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))
        toolbar1.AddTool(wx.ID_ANY, "", wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE))
        toolbar1.Realize()

        toolbar2 = wx.ToolBar(self)
        qtool = toolbar2.AddTool(wx.ID_EXIT, "", wx.ArtProvider.GetBitmap(wx.ART_QUIT))
        toolbar2.Realize()

        vbox.Add(toolbar1, 0, wx.EXPAND)
        vbox.Add(toolbar2, 0, wx.EXPAND)

        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        self.SetSizer(vbox)

        self.SetSize((350, 350))
        self.SetTitle("Simple toolbar")
        self.Center()

    def OnQuit(self, evt):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
