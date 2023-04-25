#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        panel.SetFocus()

        self.SetSize((350, 350))
        self.SetTitle("Key Event")
        self.Center()

    def OnKeyDown(self, evt):
        key = evt.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            ret = wx.MessageBox(
                "Are you sure you want to quit?",
                "Question",  # Type of box
                wx.YES_NO | wx.NO_DEFAULT,  # flags to denote type
                self,  # parent?
            )
            if ret == wx.YES:
                self.Close()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
