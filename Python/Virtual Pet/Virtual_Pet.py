import wx
from wx.adv import Animation, AnimationCtrl
import os

class TestFrame(wx.Frame):
    def __init__(self, parent, id, title):
        file_path = os.path.abspath(__file__)

        # Get the directory containing the file (removes the filename)
        dir_path = os.path.dirname(file_path)

        wx.Frame.__init__(self, parent, -1, title, style=wx.BORDER_NONE | wx.STAY_ON_TOP)
        panel = wx.Panel(self, -1, style=wx.TRANSPARENT_WINDOW)

        animation = Animation(os.path.join(dir_path, "dog.gif"))

        w, h = animation.GetSize()

        width, height = alignment(w, h)

        self.animation = AnimationCtrl(self, anim=animation, name="AnimationCtrl")
        self.animation.Play()

        size = (w, h)
        self.SetSize(size)
        self.Show()

        width, height = alignment(w, h)
        self.SetPosition((width, height))

def alignment(w, h):
    dw, dh = wx.DisplaySize()

    width = dw - w
    height = dh - h

    return width, height

def main():
    app = wx.App(False)
    frame = TestFrame(None, -1, "Test gif")
    app.MainLoop()


if __name__ == '__main__':
    main()