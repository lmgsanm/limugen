#!/usr/bin/env python3
__Author__ = "limugen"
import wx
app = wx.App()
# win = wx.Frame(None)
# bin = wx.Button(win)
win = wx.Frame(None,title="Sample Editor")
loadButton = wx.Button(win,label='Open')
saveButton = wx.Button(win,label='Save')
win.Show()
app.MainLoop()