from thulib import proxy_to_tsinghua

@proxy_to_tsinghua
def info(username, password):
    return {
        'action': 'https://info.tsinghua.edu.cn:443/Login',
        'inputs': [
            { 'name': 'userName', 'value': username },
            { 'name': 'password', 'value': password }
        ]
    }
