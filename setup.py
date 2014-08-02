try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'birds',
    'author': 'Victor A. Hernandez',
    'url': 'birds.victorhernandez.me.',
    'download_url': 'birds.victorhernandez.me/download',
    'author_email': 'mail@victorhernandez.me.',
    'version': '0.1',
    'install_requires': ['nose', 'sqlalchemy'],
    'packages': ['birds'],
    'scripts': [],
    'name': 'birds'
}

setup(**config)
