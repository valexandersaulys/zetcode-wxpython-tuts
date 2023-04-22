#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # first we create our menubar
        menubar = wx.MenuBar()

        # then we create a menu object
        fileMenu = wx.Menu()
        # then we append a Quit action to it -- wx.ID_EXIT will auto add the icon
        # and keyboard shortcut for us
        fileItem = fileMenu.Append(wx.ID_EXIT, "Quit", "Quit Application")

        # append it back to `menubar`, give it a name
        # the '&' is an accelerator key and allows for "Alt-F" to work
        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        # We also need to bind the fileItem to quit when clicked on
        # by itself, wx.ID_EXIT doesn't do anything
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.SetSize((300, 200))
        self.SetTitle("Simple Menu")
        self.Center()

    def OnQuit(self, evt):
        self.Close()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
