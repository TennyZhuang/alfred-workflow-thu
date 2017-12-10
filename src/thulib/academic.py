from thulib import proxy_to_tsinghua

@proxy_to_tsinghua
def academic(username, password):
    return {
        'action': 'https://academic.tsinghua.edu.cn:80/Login',
        'inputs': [
            { 'name': 'userName', 'value': username },
            { 'name': 'password', 'value': password }
        ]
    }
