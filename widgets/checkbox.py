#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.HORIZONTAL)

        cb = wx.CheckBox(panel, label="Show title")
        cb.SetValue(True)
        cb.Bind(wx.EVT_CHECKBOX, self.ShowOrHideTitle)

        vbox.Add(cb, flag=wx.TOP | wx.LEFT, border=30)
        panel.SetSizer(vbox)

        self.SetSize((350, 350))
        self.SetTitle("Toggle Buttons")
        self.Center()

    def ShowOrHideTitle(self, evt):
        sender = evt.GetEventObject()
        isChecked = sender.GetValue()

        if isChecked:
            self.SetTitle("wx.CheckBox")
        else:
            self.SetTitle("")


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
