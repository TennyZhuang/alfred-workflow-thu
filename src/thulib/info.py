import subprocess
import os
import time
from lib import jinja2 as j2

TEMPLATE_DIR = 'thulib/templates'

def info(username, password):
    env = j2.Environment(loader=j2.FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)
    html = env.get_template('form.html').render(
        action='https://info.tsinghua.edu.cn:443/Login',
        inputs=[
            { 'name': 'userName', 'value': username },
            { 'name': 'password', 'value': password }
        ])

    with open('html/info-proxy.html', 'w') as f:
        f.write(html)

    p = subprocess.Popen(['/usr/bin/python', '-m', 'SimpleHTTPServer', '8118'])
    os.system('open http://localhost:8118/html/info-proxy.html')
    time.sleep(5)
    p.kill()
