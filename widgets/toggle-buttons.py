#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)

        self.col = wx.Colour(0, 0, 0)

        rtb = wx.ToggleButton(panel, label="red", pos=(20, 25))
        gtb = wx.ToggleButton(panel, label="green", pos=(20, 60))
        btb = wx.ToggleButton(panel, label="blue", pos=(20, 100))

        self.cpanel = wx.Panel(panel, pos=(150, 20), size=(110, 110))
        self.cpanel.SetBackgroundColour(self.col)

        rtb.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleRed)
        gtb.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleGreen)
        btb.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleBlue)

        self.SetSize((350, 350))
        self.SetTitle("Toggle Buttons")
        self.Center()

    def ToggleRed(self, evt):
        obj = evt.GetEventObject()
        isPressed = obj.GetValue()
        green = self.col.Green()
        blue = self.col.Blue()
        if isPressed:
            self.col.Set(255, green, blue)
        else:
            self.col.Set(0, green, blue)
        self.cpanel.SetBackgroundColour(self.col)
        self.cpanel.Refresh()

    def ToggleGreen(self, e):

        obj = e.GetEventObject()
        isPressed = obj.GetValue()

        red = self.col.Red()
        blue = self.col.Blue()

        if isPressed:
            self.col.Set(red, 255, blue)
        else:
            self.col.Set(red, 0, blue)

        self.cpanel.SetBackgroundColour(self.col)
        self.cpanel.Refresh()

    def ToggleBlue(self, e):

        obj = e.GetEventObject()
        isPressed = obj.GetValue()

        red = self.col.Red()
        green = self.col.Green()

        if isPressed:
            self.col.Set(red, green, 255)
        else:
            self.col.Set(red, green, 0)

        self.cpanel.SetBackgroundColour(self.col)
        self.cpanel.Refresh()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
