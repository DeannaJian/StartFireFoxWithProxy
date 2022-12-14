import os
import configparser
import re


def list_profiles(appdata_path):
    """
        List profiles by reading profiles.ini
        :param appdata_path: the path for firefox app data
        :returns: a list for the profiles
    """
    config_file = os.path.join(appdata_path, "profiles.ini")

    conf = configparser.ConfigParser()
    conf.read(config_file)
    sections = conf.sections()

    profile_list = []
    for ss in sections:
        if 'Profile' in ss:
            dd = {}
            dd['section_name'] = ss
            dd['profile_name'] = conf.get(ss, 'Name')
            dd['IsRelative'] = conf.get(ss, 'IsRelative')
            dd['Path'] = conf.get(ss, 'Path').replace('/', '\\')
            profile_list.append(dd)

    return profile_list


def extract_value(conf_line):
    """
        Extract value from a line of the profile ini file.
        :param conf_line: the line in the profile ini file, which
            should be like 'user_pref("network.proxy.socks", "127.0.0.1");
        :returns: the value. e.g. "127.0.0.1"
    """
    return(re.search('\((.*),(.*?)\)', conf_line).group(2)).strip()


def read_proxy_from_profile_pref(file_path):
    """
        Get proxy setings in the default or user preferences.
        :param file_path: the file path for either prefs.js or user.js
        :returns: the url and port for Socks, HTTP and HTTPS proxies.
    """
    socks_proxy = http_proxy = ssl_proxy = ('', '')
    enable = False
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as ff:
            lines = ff.readlines()

        for ll in lines:
            if 'network.proxy.type' in ll:
                enable = (extract_value(ll) == '1')
            if 'user_pref("network.proxy.socks",' in ll:
                proxy_url = extract_value(ll)
                proxy_url = proxy_url[1:-1]
            if 'user_pref("network.proxy.socks_port"' in ll:
                proxy_port = extract_value(ll)
                socks_proxy = (proxy_url, proxy_port)
            if 'user_pref("network.proxy.http",' in ll:
                proxy_url = extract_value(ll)
                proxy_url = proxy_url[1:-1]
            if 'user_pref("network.proxy.http_port"' in ll:
                proxy_port = extract_value(ll)
                http_proxy = (proxy_url, proxy_port)
            if 'user_pref("network.proxy.ssl",' in ll:
                proxy_url = extract_value(ll)
                proxy_url = proxy_url[1:-1]
            if 'user_pref("network.proxy.ssl_port"' in ll:
                proxy_port = extract_value(ll)
                ssl_proxy = (proxy_url, proxy_port)

    return (enable, socks_proxy, http_proxy, ssl_proxy)


def get_proxy_from_profile(profile, appdata_path=''):
    """
        Get proxy setings in the profile
        :param profile: the profile info, which is a dictionary with
                section_name, profilee_name, IsRelative, Path as the
                keys.
        :param appdata_path: the path for firefox app data
        :returns: the socks5 proxy url and port saved in it.
    """

    # Get storage path of the profile
    if profile['IsRelative'] == '1':
        profile_path = os.path.join(appdata_path, profile['Path'])
    else:
        profile_path = profile['Path']

    # Read from prefs.js
    prefs_js_path = os.path.join(profile_path, 'prefs.js')
    proxy = read_proxy_from_profile_pref(prefs_js_path)

    # Read from user.js. If proxy is found, it will overwrite what
    # is read from prefs.js
    prefs_js_path = os.path.join(profile_path, 'user.js')
    user_proxy = read_proxy_from_profile_pref(prefs_js_path)
    if user_proxy != (False, ('', ''), ('', ''), ('', '')):
        proxy = user_proxy

    return proxy


if __name__ == '__main__':
    appdata_path = 'C:\\Users\\deann\\AppData\\Roaming\\Mozilla\\Firefox'
    profile_list = list_profiles(appdata_path)
    print(get_proxy_from_profile(profile_list[4], appdata_path))
