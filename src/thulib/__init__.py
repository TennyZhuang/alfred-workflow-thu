import subprocess
import os
import time
from lib import jinja2 as j2

TEMPLATE_DIR = 'thulib/templates'

def proxy_to_tsinghua(page_func):
    def wrapper(username, password):
        page = page_func.__name__
        form = page_func(username, password)
        env = j2.Environment(loader=j2.FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)
        html = env.get_template('form.html').render(**form)
        proxy_page = 'html/%s-proxy.html' % page

        with open(proxy_page, 'w') as f:
            f.write(html)

        p = subprocess.Popen(['/usr/bin/python', '-m', 'SimpleHTTPServer', '8118'])
        os.system('open http://localhost:8118/%s' % proxy_page)
        time.sleep(5)
        p.kill()

    return wrapper
