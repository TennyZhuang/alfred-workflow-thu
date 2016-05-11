import sys
from hashlib import md5
from binascii import hexlify
from workflow import Workflow
from workflow.notify import notify
from workflow.workflow import PasswordNotFound
from thulib.network import login, logout

log = None

def main(wf):
    args = wf.args
    log.debug(args)

    if args[0] == u'--login':
        try:
            username = wf.get_password(u'username')
            password = wf.get_password(u'password')
        except PasswordNotFound:
            notify(title=u'Account Missing', text=u'set your account by "thu --account [username] [password]" Firstly.')
            return -1
        login(username, password)
    elif args[0] == u'--logout':
        logout()
    elif args[0] == u'--account':
        username = wf.save_password(u'username', args[1])
        password = wf.save_password(u'password',
            hexlify(md5(args[2].encode('latin-1')).digest()))
    elif args[0] == u'--clear':
        wf.delete_password(u'username')
        wf.delete_password(u'password')

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
