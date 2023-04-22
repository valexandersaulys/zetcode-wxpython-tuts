#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):

        # Create tool bar -- default is horizontal, no borders, displays icons
        toolbar = self.CreateToolBar()

        # add an icon to our toolbar:  arg1=id, arg2=label, arg3=image
        qtool = toolbar.AddTool(
            wx.ID_ANY, "Quit", wx.ArtProvider.GetBitmap(wx.ART_QUIT)
        )

        # not obligatory on linux but required on Windows
        toolbar.Realize()

        # bind any necesary events
        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

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
