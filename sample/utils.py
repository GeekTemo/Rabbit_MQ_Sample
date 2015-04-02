__author__ = 'GongXingFa'

import sqlite3
import win32crypt


def get_chrome_cookies(url):
    conn = sqlite3.connect("D:\\Cookies.db")
    ret_list = []
    ret_dict = {}
    for row in conn.execute("SELECT host_key, name, path, value, encrypted_value FROM cookies"):
        if row[0] != url:
            continue
        ret = win32crypt.CryptUnprotectData(row[4], None, None, None, 0)
        ret_list.append((row[1], ret[1]))
        ret_dict[row[1]] = ret[1].decode()
    conn.close()
    return ret_dict
