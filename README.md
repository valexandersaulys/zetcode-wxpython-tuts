# Zetcode Tutorials on wxPython

[Link to Tutorials](https://zetcode.com/wxpython/)

**Progress**

+ [X] First steps in wxPython
+ [X] Menus and toolbars
+ [X] Layout management
+ [X] wxPython events
+ [X] wxPython dialogs
+ [ ] wxPython widgets
+ [ ] Advanced widgets
+ [ ] Drag and drop
+ [ ] Graphics
+ [ ] Custom widgets
+ [ ] Skeletons
+ [ ] The Tetris game


## Corrections

`wx.ArtProvider.GetBitmap(wx.ART_GO_HOME)` => Set the bitmap, the
previous defaults don't work anymore. [More info here](https://docs.wxpython.org/wx.ArtProvider.html)



## Conventions

Functions that draw things are capitalized in `wxPython`. This means
`MyFrame(None).InitUI(...)` _not_ `MyFrame(None.initUI(...)`. 


## Common Errors


### `failed at ... in DoSetSize(): invalid frame`

You probably forgot to set the parent to `None` for the top level frame
```
wx._core.wxAssertionError: C++ assertion ""m_widget"" failed at ... in DoSetSize(): invalid frame
```

### My Columns/Rows aren't expanding as expected

Did you make sure its `AddGrowableRow` or `AddGrowableCol` as you
required? These are easy to mix up.


# Documentation on Some Odd Bits

[`wx.Sizer`
Flags](https://docs.wxpython.org/sizers_overview.html#the-flags-and-border-parameters)

[Flags for `wx.TextCtrl`](https://docs.wxpython.org/wx.TextCtrl.html#styles-window-styles)
