#!/usr/bin/env python3.10

import wx


APP_EXIT = 1


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        # &Entry\tkeyboard-shortcut
        qmi = wx.MenuItem(fileMenu, APP_EXIT, "&Quit\tCtrl+Q")
        qmi.SetBitmap(wx.Bitmap("exit.png"))
        fileMenu.Append(qmi)

        # bind the event corresponding to id=APP_EXIT to quit the application
        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        self.SetSize((300, 200))
        self.SetTitle("Icons and Shortcuts")
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
