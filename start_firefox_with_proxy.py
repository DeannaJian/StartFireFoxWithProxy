import wx
import main_dialog_gui


app = wx.App(False)
dlg = main_dialog_gui.MyFrame1(None)
dlg.Show(True)
app.MainLoop()
