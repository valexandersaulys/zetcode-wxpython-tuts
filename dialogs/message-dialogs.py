#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)

        hbox = wx.BoxSizer()
        sizer = wx.GridSizer(2, 2, 2, 2)

        btnInfo = wx.Button(panel, label="Info")
        btnError = wx.Button(panel, label="Error")
        btnQuestion = wx.Button(panel, label="Question")
        btnAlert = wx.Button(panel, label="Alert")

        # btnInfo    btnError
        # btnQ       btnA
        sizer.AddMany([btnInfo, btnError, btnQuestion, btnAlert])

        hbox.Add(sizer, 0, wx.ALL, 15)
        panel.SetSizer(hbox)

        btnInfo.Bind(wx.EVT_BUTTON, self.ShowInfoMessage)
        btnError.Bind(wx.EVT_BUTTON, self.ShowErrorMessage)
        btnQuestion.Bind(wx.EVT_BUTTON, self.ShowQuestionMessage)
        btnAlert.Bind(wx.EVT_BUTTON, self.ShowAlertMessage)

    def ShowInfoMessage(self, evt):
        dialog = wx.MessageDialog(None, "Info Message", "Info", wx.OK)
        dialog.ShowModal()

    def ShowErrorMessage(self, evt):
        dialog = wx.MessageDialog(None, "Error Message", "Error", wx.OK | wx.ICON_ERROR)
        dialog.ShowModal()

    def ShowQuestionMessage(self, evt):
        dialog = wx.MessageDialog(
            None,
            "Are you sure you want to quit?",
            "Question",
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION,
        )
        dialog.ShowModal()

    def ShowAlertMessage(self, evt):
        dialog = wx.MessageDialog(
            None, "Unallowed Message", "Exclamation", wx.OK | wx.ICON_EXCLAMATION
        )
        dialog.ShowModal()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
