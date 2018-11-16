import sys
sys.path.append('./lib')
from workflow import Workflow
from workflow.notify import notify
from workflow.workflow import PasswordNotFound
from thulib.network import login, logout
from thulib.info import info
from thulib.learn import learn
from thulib.academic import academic

log = None

def main(wf):
    args = wf.args
    log.debug(args)

    if args[0] == u'--account':
        username = wf.save_password(u'username', args[1])
        password = wf.save_password(u'password', args[2])
        return 0
    elif args[0] == u'--logout':
        logout()
        return 0

    try:
        username = wf.get_password(u'username')
        password = wf.get_password(u'password')
    except PasswordNotFound:
        notify(title=u'Account Missing', text=u'set your account by "thu account [username] [password]" Firstly.')
        return -1

    if args[0] == u'--login':
        login(username, password)
    elif args[0] == u'--info':
        info(username, password)
    elif args[0] == u'--learn':
        learn(username, password)
    elif args[0] == u'--academic':
        academic(username, password)
    elif args[0] == u'--mail':
        mails(username, password) 
    elif args[0] == u'--clear':
        wf.delete_password(u'username')
        wf.delete_password(u'password')

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
