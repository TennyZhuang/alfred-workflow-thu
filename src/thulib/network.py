from workflow.web import request

def login(username, md5pwd):
    data = {
        'action': 'login',
        'username': username,
        'password': u'{MD5_HEX}' + md5pwd,
        'ac_id': 1
    }

    res = request('POST', 'http://net.tsinghua.edu.cn/do_login.php', data=data)

def logout():
    pass
