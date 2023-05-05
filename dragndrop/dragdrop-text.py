#!/usr/bin/env python3.10

from pathlib import Path
import os
import wx


class MyTextDropTarget(wx.TextDropTarget):
    def __init__(self, object):
        wx.TextDropTarget.__init__(self)
        self.object = object

    def OnDropText(self, x, y, data):
        self.object.InsertItem(0, data)
        return True


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # wx.ArtProvider.GetBitmap(wx.ART_UNDO)
        # panel = wx.Panel(self)
        splitter1 = wx.SplitterWindow(self, style=wx.SP_3D)
        splitter2 = wx.SplitterWindow(splitter1, style=wx.SP_3D)

        home_dir = str(Path.home())

        # Directory selector widget
        self.dirWid = wx.GenericDirCtrl(
            splitter1, dir=home_dir, style=wx.DIRCTRL_DIR_ONLY
        )
        self.lc1 = wx.ListCtrl(splitter2, style=wx.LC_LIST)
        self.lc2 = wx.ListCtrl(splitter2, style=wx.LC_LIST)

        dt = MyTextDropTarget(self.lc2)
        self.lc2.SetDropTarget(dt)

        self.Bind(wx.EVT_LIST_BEGIN_DRAG, self.OnDragInit, id=self.lc1.GetId())

        tree = self.dirWid.GetTreeCtrl()
        splitter2.SplitHorizontally(self.lc1, self.lc2, 150)
        splitter1.SplitVertically(self.dirWid, splitter2, 200)

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelect, id=tree.GetId())

        self.OnSelect(0)

        # self.SetSize((350, 350))
        self.SetTitle("Toggle Buttons")
        self.Center()

    def OnDragInit(self, evt):
        text = self.lc1.GetItemText(evt.GetIndex())
        tdo = wx.TextDataObject(text)
        tds = wx.DropSource(self.lc1)
        tds.SetData(tdo)
        tds.DoDragDrop(True)

    def OnSelect(self, evt):
        _list = os.listdir(self.dirWid.GetPath())
        self.lc1.ClearAll()
        self.lc2.ClearAll()
        for i in range(len(_list)):
            if _list[i][0] != ".":
                self.lc1.InsertItem(0, _list[i])


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
