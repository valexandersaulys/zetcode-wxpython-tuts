# Zetcode Tutorials on wxPython

[Link to Tutorials](https://zetcode.com/wxpython/)


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
