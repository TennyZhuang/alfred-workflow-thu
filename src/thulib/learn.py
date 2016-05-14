import subprocess
import os
import time
from lib import jinja2 as j2

TEMPLATE_DIR = 'thulib/templates'

def learn(username, password):
    env = j2.Environment(loader=j2.FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)
    html = env.get_template('form.html').render(
        action='https://learn.tsinghua.edu.cn/MultiLanguage/lesson/teacher/loginteacher.jsp',
        inputs=[
            { 'name': 'userid', 'value': username },
            { 'name': 'userpass', 'value': password }
        ])

    with open('html/learn-proxy.html', 'w') as f:
        f.write(html)

    p = subprocess.Popen(['/usr/bin/python', '-m', 'SimpleHTTPServer', '8118'])
    os.system('open http://localhost:8118/html/learn-proxy.html')
    time.sleep(5)
    p.kill()
