from workflow.web import post
from workflow.notify import notify
from urllib2 import URLError
from hashlib import md5
from binascii import hexlify

LOGIN_URL = 'http://net.tsinghua.edu.cn/do_login.php'

def login(username, password):
    md5pwd = hexlify(md5(password.encode('latin-1')).digest())
    data = {
        'action': 'login',
        'username': username,
        'password': u'{MD5_HEX}' + md5pwd,
        'ac_id': 1
    }

    try:
        res = post(LOGIN_URL, data=data, timeout=1)
        notify(title=str(res.status_code), text=res.text)
    except URLError as e:
        notify(title=str(e.errno), text=str(e.reason))

def logout():
    data = { 'action': 'logout' }
    try:
        res = post(LOGIN_URL, data=data, timeout=1)
        notify(title=str(res.status_code), text=res.text)
    except URLError as e:
        notify(title=str(e.errno), text=str(e.reason))
