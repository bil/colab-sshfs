import os, subprocess

def mount(remote, local='/content/sshfs', sshopts='StrictHostKeyChecking=no,GSSAPIAuthentication=yes'):
    """
    Mount an sshfs remote on Google Colaboratory

    This function calls sshfs via subprocess.run,
    attempting to mount the remote path on the local
    Google Colaboratory instance.

    Password-based authentication is not supported.

    Parameters
    -----------
    remote  : string
              remote path to mount from
    local   : string
              local path to mount to
              will be created if does not exist
    sshopts : SSH options to pass

    Returns
    -----------
    CompletedProcess
             output of the sshfs subprocess call

    Example
    -----------
    >>> mount(remote = '<user>@<host>:[remote path]')
    """

    assert ('remote' in locals()), 'Argument error: Didn\'t pass in remote path'

    os.makedirs(local, exist_ok=True)

    cp = subprocess.run(['sshfs', '-o', sshopts, remote, local], capture_output=True)

    if cp.returncode:
        print('Mount failed, see returned CompletedProcess instance for details')

    return cp
