from thulib import proxy_to_tsinghua

@proxy_to_tsinghua
def learn(username, password):
    return {
        'action': 'https://learn.tsinghua.edu.cn/MultiLanguage/lesson/teacher/loginteacher.jsp',
        'inputs': [
            { 'name': 'userid', 'value': username },
            { 'name': 'userpass', 'value': password }
        ]
    }
