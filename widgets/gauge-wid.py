#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)

        self.timer = wx.Timer(self, 1)
        self.count = 0
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        self.gauge = wx.Gauge(panel, range=50, size=(250, -1))  # GAUGE
        self.btn1 = wx.Button(panel, wx.ID_OK)
        self.btn2 = wx.Button(panel, wx.ID_STOP)
        self.text = wx.StaticText(panel, label="Task to be done")

        self.Bind(wx.EVT_BUTTON, self.OnOk, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.OnStop, self.btn2)

        hbox1.Add(self.gauge, proportion=1, flag=wx.ALIGN_CENTRE)
        hbox2.Add(self.btn1, proportion=1, flag=wx.RIGHT, border=10)
        hbox2.Add(self.btn2, proportion=1)
        hbox3.Add(self.text, proportion=1)

        vbox.Add((0, 30))
        vbox.Add(hbox1, flag=wx.ALIGN_CENTRE)
        vbox.Add((0, 20))

        vbox.Add(hbox2, proportion=1, flag=wx.ALIGN_CENTRE)
        vbox.Add(hbox3, proportion=1, flag=wx.ALIGN_CENTRE)
        panel.SetSizer(vbox)

        self.SetSize((350, 350))
        self.SetTitle("Toggle Buttons")
        self.Center()

    def OnOk(self, evt):
        if self.count >= 50:
            return
        self.timer.Start(100)
        self.text.SetLabel("<In-Progress>")

    def OnStop(self, evt):
        if self.count == 0 or self.count >= 50 or not self.timer.IsRunning():
            return

        self.timer.Stop()
        self.text.SetLabel("<Interrupted>")

    def OnTimer(self, evt):
        self.count += 1
        self.gauge.SetValue(self.count)  # * * * * *
        if self.count == 50:
            self.timer.Stop()
            self.text.SetLabel("Task Completed")


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
