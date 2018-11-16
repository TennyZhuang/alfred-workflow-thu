from thulib import proxy_to_tsinghua

@proxy_to_tsinghua
def mails(username, password):
    return {
        'action': 'https://mails.tsinghua.edu.cn/coremail/login.jsp',
        'inputs': [
            { 'name': 'uid', 'value': username + '@mails.tsinghua.edu.cn' },
            { 'name': 'password', 'value': password }
        ]
    }
