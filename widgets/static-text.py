#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)

        txt1 = """I'm giving up the ghost of love
in the shadows cast on devotion
She is the one that I adore
creed of my silent suffocation
Break this bittersweet spell on me
lost in the arms of destiny"""

        txt2 = """There is something in the way
You're always somewhere else
Feelings have deserted me
To a point of no return
I don't believe in God
But I pray for you"""

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.DEFAULT)

        st1 = wx.StaticText(panel, label=txt1, style=wx.ALIGN_LEFT)
        st2 = wx.StaticText(panel, label=txt2, style=wx.ALIGN_LEFT)

        st1.SetFont(font)
        st2.SetFont(font)

        vbox.Add(st1, flag=wx.ALL, border=15)
        vbox.Add(st2, flag=wx.ALL, border=15)

        panel.SetSizer(vbox)

        # self.SetSize((350, 350))
        self.SetTitle("Bittersweet")
        self.Center()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
