#!/usr/bin/env python3.10

import wx


class MyPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(MyPanel, self).__init__(*args, **kwargs)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, evt):
        print("Event Reached Panel Class")
        evt.Skip()


class MyButton(wx.Button):
    def __init__(self, *args, **kwargs):
        super(MyButton, self).__init__(*args, **kwargs)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, evt):
        print("event reached button class")
        evt.Skip()


class Example(wx.Frame):
    """
    => when we click the button, it ripples down
    event reached button class
    Event Reached Panel Class
    event reached frame class
    """

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        main_panel = MyPanel(self)

        MyButton(main_panel, label="okay", pos=(15, 15))

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        self.SetTitle("Propagate Event")
        self.Center()

    def OnButtonClicked(self, evt):
        print("event reached frame class")
        evt.Skip()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
