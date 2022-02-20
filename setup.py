import setuptools

VERSION = '0.0.1'

setuptools.setup(
        name = 'colab_sshfs',
        description = 'Mount sshfs remotes on Google Colaboratory',
        author = 'Paul Nuyujukian',
        version = VERSION,
        packages = setuptools.find_packages() )
