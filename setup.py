import pathlib, setuptools

VERSION = '0.0.4'

pwd = pathlib.Path(__file__).parent
long_description = (pwd / "README.md").read_text()

setuptools.setup(
        name = 'colab_sshfs',
        version = VERSION,
        description = 'Mount sshfs remotes on Google Colaboratory',
        author = 'Paul Nuyujukian',
        url = 'https://github.com/bil/colab_sshfs',
        long_description = long_description,
        long_description_content_type='text/markdown',
        license = 'GPL2',
        packages = setuptools.find_packages() )
