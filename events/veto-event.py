#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.SetTitle("Event Veto")
        self.Center()

    def OnCloseWindow(self, evt):
        dial = wx.MessageDialog(
            None,
            "Are you sure you want to quit?",
            "Question",
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION,
        )
        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            # we stop the event from proceeding(?)
            evt.Veto()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
