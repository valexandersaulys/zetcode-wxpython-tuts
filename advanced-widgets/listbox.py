#!/usr/bin/env python3.10

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Note: order is a queue in a ListBox
        self.listbox = wx.ListBox(panel)
        hbox.Add(self.listbox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        btnPanel = wx.Panel(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        newBtn = wx.Button(btnPanel, wx.ID_ANY, "New", size=(90, 30))
        renBtn = wx.Button(btnPanel, wx.ID_ANY, "Rename", size=(90, 30))
        delBtn = wx.Button(btnPanel, wx.ID_ANY, "Delete", size=(90, 30))
        clrBtn = wx.Button(btnPanel, wx.ID_ANY, "Clear", size=(90, 30))
        self.Bind(wx.EVT_BUTTON, self.NewItem, id=newBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnRename, id=renBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id=delBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnClear, id=clrBtn.GetId())

        # we also want to include a double click event
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnRename)

        vbox.Add((-1, 20))
        vbox.Add(newBtn)
        vbox.Add(renBtn, 0, wx.TOP, 5)
        vbox.Add(delBtn, 0, wx.TOP, 5)
        vbox.Add(clrBtn, 0, wx.TOP, 5)

        btnPanel.SetSizer(vbox)
        # had to cut proportion on second arg?
        hbox.Add(btnPanel, flag=wx.EXPAND | wx.RIGHT, border=20)
        panel.SetSizer(hbox)

        # self.SetSize((350, 350))
        self.SetTitle("wx.ListBox")
        self.Center()

    def NewItem(self, evt):
        # creates a pop-up dialog box with arg1=window caption, arg2=message
        text = wx.GetTextFromUser("Enter a new item", "Insert Dialog")
        if text != "":
            self.listbox.Append(text)

    def OnRename(self, evt):
        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        renamed = wx.GetTextFromUser("Rename item", "Rename dialog", text)

        # delete the old, insert the newly renamed
        # I'm surprised this worked to keep the order correct
        if renamed != "":
            self.listbox.Delete(sel)
            item_id = self.listbox.Insert(renamed, sel)
            self.listbox.SetSelection(item_id)

    def OnDelete(self, evt):
        sel = self.listbox.GetSelection()  # returns index in list
        print(sel)
        if sel != -1:
            self.listbox.Delete(sel)

    def OnClear(self, evt):
        self.listbox.Clear()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
