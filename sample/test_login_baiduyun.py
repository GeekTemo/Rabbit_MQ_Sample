__author__ = 'GongXingFa'


import requests
import utils

url = 'http://yun.baidu.com/'
x = requests.get(url, cookies = utils.get_chrome_cookies('.baidu.com'))
print x.text
