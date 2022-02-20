# colab-sshfs

## sshfs mounts for Google Colaboratory

[Google Colaboratory](http://research.google.com/colaboratory) is a free, fully-hosted fork off of a predecessor of [Jupyter](http://jupyter.org) available with a Google account.

While [mounting Google Drive](https://colab.research.google.com/notebooks/io.ipynb#scrollTo=Mounting_Google_Drive_locally) is straightforward, other storage spaces are not.

This package makes mounting [sshfs](https://github.com/libfuse/sshfs)-accessible remote spaces straightforward.

<br>
NOTE: Password-based authentication is not supported.

## Installation

Execute the following in a cell:

    !pip install colab_sshfs

## Usage

    from colab_sshfs import colab_sshfs
    colab_sshfs.mount(remote = '<user>@<host>:[remote path]')

By default, the local path mounted is `/content/sshfs`.

The mount function returns a [CompletedProcess](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess) instance.

Review the docstring for full parameters: `help(colab_sshfs.mount)`.
