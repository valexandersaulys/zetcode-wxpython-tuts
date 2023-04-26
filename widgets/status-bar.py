#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)

        button = wx.Button(panel, label="Button", pos=(20, 20))
        text = wx.CheckBox(panel, label="CheckBox", pos=(20, 90))
        combo = wx.ComboBox(panel, pos=(120, 22), choices=["Python", "Ruby"])
        slider = wx.Slider(panel, 5, 6, 1, 10, (120, 90), (110, -1))

        panel.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)
        button.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)
        text.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)
        combo.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)
        slider.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)

        self.sb = self.CreateStatusBar()

        self.SetSize((350, 350))
        self.SetTitle("wx.StatusBar")
        self.Center()

    def OnWidgetEnter(self, evt):
        name = evt.GetEventObject().GetClassName()
        self.sb.SetStatusText("%s widget" % name)
        evt.Skip()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
