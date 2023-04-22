#!/usr/bin/env python3.10

import wx


class MyPopupMenu(wx.Menu):
    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()
        self.parent = parent

        mmi = wx.MenuItem(self, wx.NewId(), "Minimize")
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        # same as for the window menu
        self.Append(wx.ID_ANY, kind=wx.ITEM_SEPARATOR)

        cmi = wx.MenuItem(self, wx.NewId(), "Close")
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)

    def OnMinimize(self, evt):
        self.parent.Iconize()

    def OnClose(self, evt):
        self.parent.Close()


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        self.SetSize((350, 250))
        self.SetTitle("Context Menu")
        self.Center()

    def OnRightDown(self, evt):
        self.PopupMenu(MyPopupMenu(self), evt.GetPosition())


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
