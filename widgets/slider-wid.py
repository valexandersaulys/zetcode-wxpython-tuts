#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)
        slider = wx.Slider(
            panel, value=200, minValue=150, maxValue=500, style=wx.SL_HORIZONTAL
        )
        slider.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        sizer.Add(slider, pos=(0, 0), flag=wx.ALL | wx.EXPAND, border=25)

        self.txt = wx.StaticText(panel, label="200")
        sizer.Add(self.txt, pos=(0, 1), flag=wx.TOP | wx.RIGHT, border=25)

        sizer.AddGrowableCol(0)
        panel.SetSizer(sizer)

        self.SetSize((350, 350))
        self.SetTitle("Toggle Buttons")
        self.Center()

    def OnSliderScroll(self, evt):
        obj = evt.GetEventObject()
        val = obj.GetValue()
        self.txt.SetLabel(str(val))


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
