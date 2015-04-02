__author__ = 'GongXingFa'

user = ''
pawd = ''

import mechanize
import cookielib
url = 'http://www.douban.com/'

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

brower.open(url)

form_name = 'lzform'

brower.select_form(name=form_name)

brower.form['form_email'] = user
brower.form['form_password'] = pawd

response = brower.submit()

print '----'*30

print response.read()

response = brower.open('http://www.douban.com/doumail/')

print '------'*30

print response.read()



