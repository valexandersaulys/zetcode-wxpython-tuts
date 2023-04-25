#!/usr/bin/env python3.10

import wx
import wx.adv  # separate import!


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        menubar = wx.MenuBar()

        _help = wx.Menu()
        _help.Append(wx.ID_ANY, "&About")
        _help.Bind(wx.EVT_MENU, self.OnAboutBox)

        menubar.Append(_help, "&Help")
        self.SetMenuBar(menubar)

        self.SetSize((350, 350))
        self.SetTitle("About Dialog Box")
        self.Center()

    def OnAboutBox(self, evt):
        description = (
            """This is a powerful thing of things, a description if you will"""
        )

        _license = """GNU Public License, version 3 or later"""

        info = wx.adv.AboutDialogInfo()
        info.SetIcon(wx.Icon(wx.ArtProvider.GetBitmap(wx.ART_UNDO)))
        info.SetVersion("1.0")
        info.SetDescription(description)
        info.SetCopyright("(C) 2023 Vincent Saulys")
        info.SetWebSite("https://deferredexception.com/")
        info.SetLicense(_license)
        info.AddDeveloper("Vincent Saulys")
        info.AddDocWriter("Vincent Saulys")
        info.AddArtist("Vincent Saulys")
        info.AddTranslator("Vincent Saulys")

        wx.adv.AboutBox(info)


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
