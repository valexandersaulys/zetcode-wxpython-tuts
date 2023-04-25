#!/usr/bin/env python3.10

import wx


class ChangeDepthDialog(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(ChangeDepthDialog, self).__init__(*args, **kwargs)
        self.InitUI()
        self.SetSize((250, 400))
        self.SetTitle("Change Color Depth")

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sb = wx.StaticBox(panel, label="colors")

        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)
        sbs.Add(wx.RadioButton(panel, label="256 colors", style=wx.RB_GROUP))
        sbs.Add(wx.RadioButton(panel, label="16 colors"))
        sbs.Add(wx.RadioButton(panel, label="2 colors"))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.RadioButton(panel, label="Custom"))
        hbox1.Add(wx.TextCtrl(panel), flag=wx.LEFT, border=5)
        sbs.Add(hbox1)

        panel.SetSizer(sbs)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label="Okay")
        closeButton = wx.Button(self, label="Close")
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        vbox.Add(panel, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

    def OnClose(self, evt):
        self.Destroy()


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        tb = self.CreateToolBar()
        tb.AddTool(
            toolId=wx.ID_ANY, label="", bitmap=wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        )

        tb.Realize()

        tb.Bind(wx.EVT_TOOL, self.OnChangeDepth)

        self.SetSize((350, 350))
        self.SetTitle("Custom Dialog")
        self.Center()

    def OnChangeDepth(self, evt):
        cdDialog = ChangeDepthDialog(None, title="Change color Depth")
        cdDialog.ShowModal()
        cdDialog.Destroy()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
