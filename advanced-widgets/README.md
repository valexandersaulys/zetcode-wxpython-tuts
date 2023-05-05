[Link](https://zetcode.com/wxpython/advanced/)

Can't get `ListCtrl` to work for some reason in [repository example](repository.py).

~~[Supposedly it leverages this
`CheckListCtrlMixin`](https://docs.wxpython.org/wx.lib.mixins.listctrl.CheckListCtrlMixin.html).~~

So apparently this got superseded by `wx.ListCtrl` which now [has an
`wx.EnableCheckBoxes`
function](https://stackoverflow.com/a/73426500). More info [in the
docs](https://docs.wxpython.org/wx.ListCtrl.html?highlight=listctrl#wx.ListCtrl.EnableCheckBoxes). 

In those docs, [it also lists the
`wx.ListEvent`](https://docs.wxpython.org/wx.ListEvent.html) that will
get emitted. There's vague mention of keeping track of you rown
state. [This guy seems to keep track of these sorts of
things](https://stackoverflow.com/a/47283860). 
