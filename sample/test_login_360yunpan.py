__author__ = 'GongXingFa'

import mechanize
import cookielib


brower = mechanize.Browser()
cookjar = cookielib.LWPCookieJar()
brower.set_cookiejar(cookjar)

brower.set_handle_equiv(True)
brower.set_handle_redirect(True)
brower.set_handle_referer(True)
brower.set_handle_referer(True)
brower.set_handle_robots(True)

brower.set_handle_refresh(mechanize.HTTPRefreshProcessor(), max_time=1)

brower.set_debug_http(True)
brower.addheaders = [
    ('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.11) Gecko/20100701 Firefox/3.5.11')]

login_url = 'http://c4.yunpan.360.cn/'
user = ''
pawd =''

brower.open(login_url)

brower.select_form(nr=1)

brower['username'] = user
brower['password'] = pawd

response = brower.submit()

print '------'*30

print response.read()

