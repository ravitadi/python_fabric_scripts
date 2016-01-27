from fabric.api import *

"""Using Sudo for starting the node server using port 80"""

SERVER_FILE = 'index.js'

def restart_w_forever():
    """Restart server with forever npm package"""
    sudo('forever start -l forever.log -o out.log -e err.log %s' % SERVER_FILE)

def restart_node():
	"""Restart server with simple node"""
	sudo('killall node')
	sudo('node %s' % SERVER_FILE)

def reinstall_modules():
	run('rm -rf node_modules')
	run('npm install')
