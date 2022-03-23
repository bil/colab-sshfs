import subprocess

from . import colab_sshfs

# install system packages needed to mount with sshfs
subprocess.run(['apt-get', '-qq', 'update'])
subprocess.run(['apt-get', 'install', '-qq', 'sshfs', 'krb5-user'])
