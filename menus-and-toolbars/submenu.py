#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()

        # .Append(id, "name")
        # .AppendMenu(id, "name", menuItem)
        # .AppendItem(wx.MenuItem(wx.Menu, id, "name"))

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, "&New")
        fileMenu.Append(wx.ID_OPEN, "&Open")
        fileMenu.Append(wx.ID_SAVE, "&Save")
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, "Import Newsfeed List...")
        imp.Append(wx.ID_ANY, "Import Bookmarks...")
        imp.Append(wx.ID_ANY, "Import mail...")

        # apparently '&' get cut altogether
        fileMenu.AppendMenu(wx.ID_ANY, "I&mport", imp)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, "&Quit\tCtrl+W")
        fileMenu.AppendItem(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        self.SetSize((350, 350))
        self.SetTitle("Submenu")
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
