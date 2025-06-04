import wx
import wx.lib.agw.advancedsplash as AS

app = wx.App()

frame = wx.Frame(None, -1, "AdvancedSplash Test")

imagePath = "test.png"
bitmap = wx.Bitmap(imagePath)

splash = AS.AdvancedSplash(frame, bitmap=bitmap)

app.MainLoop()