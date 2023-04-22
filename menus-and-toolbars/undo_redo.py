#!/usr/bin/env python3

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.count = 5

        self.toolbar = self.CreateToolBar()
        tundo = self.toolbar.AddTool(
            wx.ID_UNDO, "", wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        )
        tredo = self.toolbar.AddTool(
            wx.ID_REDO, "", wx.ArtProvider.GetBitmap(wx.ART_REDO)
        )
        # we disable redo in the beginning
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.AddSeparator()  # new shortcut!
        texit = self.toolbar.AddTool(
            wx.ID_EXIT, "", wx.ArtProvider.GetBitmap(wx.ART_QUIT)
        )
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, texit)
        self.Bind(wx.EVT_TOOL, self.OnUndo, tundo)
        self.Bind(wx.EVT_TOOL, self.OnRedo, tredo)

        self.SetSize((350, 350))
        self.SetTitle("Undo Reod")
        self.Center()

    def OnUndo(self, evt):
        if self.count > 1 and self.count <= 5:
            self.count -= 1
        if self.count <= 1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)
        if self.count >= 4:
            self.toolbar.EnableTool(wx.ID_REDO, True)

    def OnRedo(self, evt):
        if self.count < 5 and self.count >= 1:
            self.count += 1
        if self.count >= 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)
        if self.count <= 2:
            self.toolbar.EnableTool(wx.ID_UNDO, True)

    def OnQuit(self, evt):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
