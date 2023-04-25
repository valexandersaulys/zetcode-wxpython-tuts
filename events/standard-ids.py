#!/usr/bin/env python3.10

import wx


# wxPython has some standard ideas, prefixed as wx.ID_*

# You can create your own IDs with wx.NewId()
ID_MENU_NEW = wx.NewId()


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)
        grid = wx.GridSizer(2, 3, 0)  # columns, rows, gap

        # they didn't specify a gap in grid and something below is mucking
        # with the layouts
        grid.AddMany(
            [
                # widget, ?, flag(s), border?
                (wx.Button(panel, wx.ID_CANCEL), 0, wx.TOP | wx.LEFT, 9),
                (wx.Button(panel, wx.ID_DELETE), 0, wx.TOP, 9),
                (wx.Button(panel, wx.ID_SAVE), 0, wx.LEFT, 9),
                (wx.Button(panel, wx.ID_EXIT)),
                (wx.Button(panel, wx.ID_STOP), 0, wx.LEFT, 9),
                # (wx.Button(panel, wx.ID_NEW)),
                (wx.Button(panel, ID_MENU_NEW, "New Menu")),
            ]
        )

        self.Bind(wx.EVT_BUTTON, self.OnQuitApp, id=wx.ID_EXIT)
        self.Bind(wx.EVT_BUTTON, self.DisplayMessage, id=ID_MENU_NEW)
        panel.SetSizer(grid)
        self.SetTitle("Standard IDs")
        self.Center()

    def OnQuitApp(self, evt):
        self.Close()

    def DisplayMessage(self, evt):
        if evt.GetId() == ID_MENU_NEW:
            msg = "New Menu Item Selected"

        _dlg = wx.MessageDialog(self, "New Selection!", "You selected a new menu item!")
        resp = _dlg.ShowModal()
        print(resp)
        if resp == wx.ID_OK:
            print("YEEHAW!")
        _dlg.Destroy()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
