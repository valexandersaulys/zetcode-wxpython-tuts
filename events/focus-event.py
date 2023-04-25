#!/usr/bin/env python3.10

import wx


class MyWindow(wx.Panel):
    """
    Everytime we repaint, we draw the border a different color
    depending on if it has the focus on the mouse cursor
    """

    def __init__(self, parent):
        super(MyWindow, self).__init__(parent)
        self.color = "#b3b3b3"

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen(self.color))

        # draw a border around the space
        x, y = self.GetSize()
        dc.DrawRectangle(0, 0, x, y)

    def OnSize(self, evt):
        self.Refresh()

    def OnSetFocus(self, evt):
        self.color = "#ff0000"
        self.Refresh()

    def OnKillFocus(self, evt):
        self.color = "#b3b3b3"
        self.Refresh()


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        # I'm 99% sure the gap is ~pixels
        grid = wx.GridSizer(2, 2, 20, 20)  # col, row, col gap, row gap
        grid.AddMany(
            [
                (MyWindow(self), 0, wx.EXPAND | wx.TOP | wx.LEFT, 9),
                (MyWindow(self), 0, wx.EXPAND | wx.TOP | wx.RIGHT, 9),
                (MyWindow(self), 0, wx.EXPAND | wx.BOTTOM | wx.LEFT, 9),
                (MyWindow(self), 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT, 9),
            ]
        )
        self.SetSizer(grid)

        self.SetSize((350, 350))
        self.SetTitle("Focus Event")
        self.Center()

    def OnMove(self, evt):
        print(evt.GetEventObject())
        x, y = evt.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
