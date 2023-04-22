#!/usr/bin/env python3.10

import wx

app = wx.App()
"""
Frames are container widgets that may or may not have parents. Below
does not have a parent (hence `None` as first argument). 

wx.Frame( parent: wx.Window | None, id: int = -1, title: str = '', 
    pos: wx.Point = wx.DefaultPosition, size: wx.Size = wx.DefaultSize, 
    style=wx.DEFAULT_FRAME_STYLE, name: str = 'frame')

All but the first arg have default values. 

Styles can be combined with pipes (`|`). On Ubuntu for this app, none of
them seem to have any effect whatsoever. 
"""
frame = wx.Frame(
    None,  # parent, cannot be a kwarg
    id=-1,
    pos=wx.DefaultPosition,
    # style=wx.DEFAULT_FRAME_STYLE,
    style=wx.DEFAULT_FRAME_STYLE | wx.SYSTEM_MENU,
    title="Vincent's Simple Application",
)
frame.Show()


"""
Open up a second window -- application will not finish executing until we click "close"
"""
secondFrame = wx.Frame(
    None,  # parent, cannot be a kwarg
    id=-1,
    pos=wx.DefaultPosition,
    # style=wx.DEFAULT_FRAME_STYLE,
    style=wx.DEFAULT_FRAME_STYLE | wx.SYSTEM_MENU,
    title="Vincent's Simple Application Second Window",
)
secondFrame.Show()

app.MainLoop()  # will _not_ execute unless this runs
