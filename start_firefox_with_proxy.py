import wx
import main_dialog_gui
import json
import os
from firefox_utils import *


SETTNGS_FILE = 'settings.json'


class app_dialog(main_dialog_gui.MyFrame1):
    def __init__(self, parent):
        main_dialog_gui.MyFrame1.__init__(self, parent)
        self.settings = {}
        self.profile_dict = {}

        # disable the Add Profile button temporarily
        self.m_buttonNew.Disable()

        # load settings
        if os.path.exists(SETTNGS_FILE):
            with open(SETTNGS_FILE, 'r') as ff:
                self.settings = json.loads(ff.read())
                self.m_dirPicker_exe.SetPath(self.settings['exe_dir'])
                appdata_path = self.settings['app_data_dir']
                self.m_dirPicker_app_data.SetPath(appdata_path)
                self.refresh_choices(appdata_path)

    def refresh_choices(self, path):
        name_list = []

        if os.path.exists(path):
            self.profile_dict = list_profiles(path)
            for pp in self.profile_dict:
                name_list.append(pp['profile_name'])
            self.m_choiceProfiles.SetItems(name_list)
            self.m_choiceProfiles.SetSelection(0)
            self.show_proxy()
        else:
            msg = 'Firefox App Data folder does not exists. '
            msg = msg + 'Please choose a correct one.\n'
            msg = msg + 'It is usally '
            msg = msg + 'C: \\Users\\< username >\\AppData\\'
            msg = msg + 'Roaming\\Mozilla\\Firefox"'
            wx.MessageBox(msg, 'Error', wx.OK)

    def refresh_profiles(self, event):
        appdata_path = self.m_dirPicker_app_data.GetPath()
        self.refresh_choices(appdata_path)

    def save_settings(self):
        # read settings
        exe_dir = self.m_dirPicker_exe.GetPath()
        self.settings['exe_dir'] = exe_dir
        app_data_dir = self.m_dirPicker_app_data.GetPath()
        self.settings['app_data_dir'] = app_data_dir

        # save to file
        with open(SETTNGS_FILE, 'w') as ff:
            ff.write(json.dumps(self.settings))

    def show_proxy(self):
        selection = self.m_choiceProfiles.GetSelection()
        (proxy_enable, socks_proxy, http_proxy, ssl_proxy) = \
            get_proxy_from_profile(
            self.profile_dict[selection], self.m_dirPicker_app_data.GetPath())
        self.m_checkBoxEnable.SetValue(proxy_enable)
        self.m_textCtrlSocksProxyUrl.SetValue(socks_proxy[0])
        self.m_textCtrlSocksProxyPort.SetValue(socks_proxy[1])
        self.m_textCtrlHttpProxyURL.SetValue(http_proxy[0])
        self.m_textCtrlHttpProxyPort.SetValue(http_proxy[1])
        self.m_textCtrlHttpsProxyUrl.SetValue(http_proxy[0])
        self.m_textCtrlHttpsProxyPort.SetValue(http_proxy[1])

    def select_profile(self, event):
        self.show_proxy()

    def start_firefox(self, event):
        self.save_settings()

        if not os.path.exists(self.settings['exe_dir']):
            msg = 'Program folder does not exists. Please choose again.'
            wx.MessageBox(msg, 'Error', wx.OK)
            return

        selection = self.m_choiceProfiles.GetSelection()
        cmd = 'cd /D "' + self.settings['exe_dir'] + '" && firefox -P '
        cmd = cmd + '"' + self.profile_dict[selection]['profile_name'] + '"'
        os.system(cmd)

    def add_profile(self, event):
        if not os.path.exists(self.settings['exe_dir']):
            msg = 'Program folder does not exists. Please choose again.'
            wx.MessageBox(msg, 'Error', wx.OK)
            return

        selection = self.m_choiceProfiles.GetSelection()
        cmd = 'cd /D "' + self.settings['exe_dir'] + '" && firefox -P'
        os.system(cmd)


app = wx.App(False)
dlg = app_dialog(None)
dlg.Show(True)
app.MainLoop()
