#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        viewMenu = wx.Menu()

        # wx.Menu().Append(id, "item name in menu", "help text",
        #     kind=wx.ITEM_SEPARATOR | wx.ITEM_NORMAL | wx.ITEM_CHECK | wx.ITEM_RADIO)
        self.shst = viewMenu.Append(
            wx.ID_ANY, "Show statusbar", "Show Statusbar", kind=wx.ITEM_CHECK
        )
        # No text is needed, but you need an `id`
        viewMenu.Append(wx.ID_ANY, kind=wx.ITEM_SEPARATOR)
        self.shtl = viewMenu.Append(
            wx.ID_ANY, "Show toolbar", "Show Toolbar", kind=wx.ITEM_CHECK
        )

        viewMenu.Check(self.shst.GetId(), True)
        viewMenu.Check(self.shtl.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

        menubar.Append(viewMenu, "&View")
        self.SetMenuBar(menubar)

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddTool(1, "", wx.ArtProvider.GetBitmap(wx.ART_GO_HOME))
        self.toolbar.AddTool(2, "", wx.ArtProvider.GetBitmap(wx.ART_TIP))
        self.toolbar.Realize()

        # this default widget populates from the help text (third arg above)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("Ready")

        self.SetSize((450, 450))
        self.SetTitle("Check Menu Item")
        self.Center()

    def ToggleStatusBar(self, evt):
        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, evt):
        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
