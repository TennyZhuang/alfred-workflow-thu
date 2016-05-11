import sys
from hashlib import md5
from binascii import hexlify
from workflow import Workflow
from workflow.workflow import Settings
from thulib.network import login, logout

log = None

def main(wf):
    args = wf.args
    log.debug(args)

    if args[0] == u'--login':
        username = wf.get_password(u'username')
        password = wf.get_password(u'password')
        login(username, password)
    elif args[0] == u'--logout':
        logout()
    elif args[0] == u'--account':
        username = wf.save_password('username', args[1])
        password = wf.save_password('password',
            hexlify(md5(args[2].encode('latin-1')).digest()))

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
