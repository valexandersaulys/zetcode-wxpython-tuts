#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        wx.CallLater(3000, self.ShowMessage)
        self.SetSize((300, 200))
        self.SetTitle("Message Box")
        self.Center()

    def ShowMessage(self):
        # wx.MessageBox(
        #     "Download Completed",  # text message
        #     "Info",  # title message
        #     wx.OK | wx.ICON_INFORMATION,  # flags
        # )

        # print out the reply below
        response = wx.MessageBox("Thing", "Info", wx.YES_NO)
        print(response, response == wx.YES, response == wx.NO)


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
