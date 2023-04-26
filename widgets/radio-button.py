#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)

        self.rb1 = wx.RadioButton(
            panel, label="Value A", pos=(10, 10), style=wx.RB_GROUP
        )
        self.rb2 = wx.RadioButton(panel, label="Value B", pos=(10, 30))
        self.rb3 = wx.RadioButton(panel, label="Value C", pos=(10, 50))

        self.rb1.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
        self.rb2.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
        self.rb3.Bind(wx.EVT_RADIOBUTTON, self.SetVal)

        self.sb = self.CreateStatusBar(3)

        # this will set three evenly separate sections, second arg is ID (?)
        self.sb.SetStatusText("True", 0)
        self.sb.SetStatusText("False", 1)
        self.sb.SetStatusText("False", 2)

        self.SetSize((350, 350))
        self.SetTitle("wx.RadioButton")
        self.Center()

    def SetVal(self, evt):

        state1 = str(self.rb1.GetValue())
        state2 = str(self.rb2.GetValue())
        state3 = str(self.rb3.GetValue())

        # Set each of the three sections, second arg is ID
        self.sb.SetStatusText(state1, 0)
        self.sb.SetStatusText(state2, 1)
        self.sb.SetStatusText(state3, 2)


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
