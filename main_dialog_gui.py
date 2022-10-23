# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MyFrame1
###########################################################################


class MyFrame1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Start Firefox with Proxy",
                          pos=wx.DefaultPosition, size=wx.Size(500, 390), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(137, 207, 240))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText16 = wx.StaticText(
            self, wx.ID_ANY, u"Firefox Program Folder", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)

        self.m_staticText16.SetForegroundColour(wx.Colour(48, 48, 48))

        bSizer16.Add(self.m_staticText16, 1, wx.ALL, 5)

        self.m_dirPicker_exe = wx.DirPickerCtrl(
            self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        bSizer16.Add(self.m_dirPicker_exe, 2, wx.ALL, 5)

        bSizer1.Add(bSizer16, 1, wx.EXPAND, 5)

        bSizer161 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText161 = wx.StaticText(
            self, wx.ID_ANY, u"App Data Folder", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText161.Wrap(-1)

        self.m_staticText161.SetForegroundColour(wx.Colour(48, 48, 48))

        bSizer161.Add(self.m_staticText161, 1, wx.ALL, 5)

        self.m_dirPicker_app_data = wx.DirPickerCtrl(
            self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        bSizer161.Add(self.m_dirPicker_app_data, 2, wx.ALL, 5)

        bSizer1.Add(bSizer161, 1, wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer1.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText15 = wx.StaticText(
            self, wx.ID_ANY, u"Firefox Profile", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)

        self.m_staticText15.SetForegroundColour(wx.Colour(48, 48, 48))

        bSizer1.Add(self.m_staticText15, 0, wx.ALL, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        m_choiceProfilesChoices = []
        self.m_choiceProfiles = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceProfilesChoices, 0)
        self.m_choiceProfiles.SetSelection(0)
        bSizer2.Add(self.m_choiceProfiles, 3, wx.ALL, 5)

        self.m_buttonRefresh = wx.Button(
            self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_buttonRefresh, 0, wx.ALL, 5)

        self.m_buttonNew = wx.Button(
            self, wx.ID_ANY, u"Add Profile", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_buttonNew, 1, wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                 wx.DefaultSize, wx.BORDER_SIMPLE | wx.TAB_TRAVERSAL)
        self.m_panel2.SetBackgroundColour(wx.Colour(137, 207, 240))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10 = wx.StaticText(
            self.m_panel2, wx.ID_ANY, u"Proxy Settings in the Selected Profile", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        bSizer3.Add(self.m_staticText10, 0, wx.ALL, 5)

        self.m_checkBoxEnable = wx.CheckBox(
            self.m_panel2, wx.ID_ANY, u"Manual Proxy is enabled", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBoxEnable.Enable(False)

        bSizer3.Add(self.m_checkBoxEnable, 0, wx.ALL, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(
            self.m_panel2, wx.ID_ANY, u"HTTP Proxy", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetForegroundColour(wx.Colour(48, 48, 48))

        bSizer8.Add(self.m_staticText1, 1, wx.ALL, 5)

        self.m_textCtrlHttpProxyURL = wx.TextCtrl(
            self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer8.Add(self.m_textCtrlHttpProxyURL, 3, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(
            self.m_panel2, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        self.m_staticText2.SetForegroundColour(wx.Colour(48, 48, 48))

        bSizer8.Add(self.m_staticText2, 1, wx.ALL, 5)

        self.m_textCtrlHttpProxyPort = wx.TextCtrl(
            self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer8.Add(self.m_textCtrlHttpProxyPort, 1, wx.ALL, 5)

        bSizer3.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText11 = wx.StaticText(
            self.m_panel2, wx.ID_ANY, u"HTTPS Proxy", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        self.m_staticText11.SetForegroundColour(wx.Colour(48, 48, 48))

        bSizer9.Add(self.m_staticText11, 1, wx.ALL, 5)

        self.m_textCtrlHttpsProxyUrl = wx.TextCtrl(
            self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer9.Add(self.m_textCtrlHttpsProxyUrl, 3, wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(
            self.m_panel2, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)

        self.m_staticText21.SetForegroundColour(wx.Colour(48, 48, 48))

        bSizer9.Add(self.m_staticText21, 1, wx.ALL, 5)

        self.m_textCtrlHttpsProxyPort = wx.TextCtrl(
            self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer9.Add(self.m_textCtrlHttpsProxyPort, 1, wx.ALL, 5)

        bSizer3.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer91 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText111 = wx.StaticText(
            self.m_panel2, wx.ID_ANY, u"Socks Proxy", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)

        self.m_staticText111.SetForegroundColour(wx.Colour(48, 48, 48))

        bSizer91.Add(self.m_staticText111, 1, wx.ALL, 5)

        self.m_textCtrlSocksProxyUrl = wx.TextCtrl(
            self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer91.Add(self.m_textCtrlSocksProxyUrl, 3, wx.ALL, 5)

        self.m_staticText211 = wx.StaticText(
            self.m_panel2, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText211.Wrap(-1)

        self.m_staticText211.SetForegroundColour(wx.Colour(48, 48, 48))

        bSizer91.Add(self.m_staticText211, 1, wx.ALL, 5)

        self.m_textCtrlSocksProxyPort = wx.TextCtrl(
            self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer91.Add(self.m_textCtrlSocksProxyPort, 1, wx.ALL, 5)

        bSizer3.Add(bSizer91, 1, wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_buttonStart = wx.Button(
            self, wx.ID_ANY, u"Start Firefox", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_buttonStart, 0,
                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_dirPicker_exe.Bind(wx.EVT_DIRPICKER_CHANGED, self.pick_exe_dir)
        self.m_dirPicker_app_data.Bind(
            wx.EVT_DIRPICKER_CHANGED, self.pick_app_data_dir)
        self.m_choiceProfiles.Bind(wx.EVT_CHOICE, self.select_profile)
        self.m_buttonRefresh.Bind(wx.EVT_BUTTON, self.refresh_profiles)
        self.m_buttonNew.Bind(wx.EVT_BUTTON, self.add_profiles)
        self.m_buttonStart.Bind(wx.EVT_BUTTON, self.start_firefox)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def pick_exe_dir(self, event):
        event.Skip()

    def pick_app_data_dir(self, event):
        event.Skip()

    def select_profile(self, event):
        event.Skip()

    def refresh_profiles(self, event):
        event.Skip()

    def add_profiles(self, event):
        event.Skip()

    def start_firefox(self, event):
        event.Skip()
