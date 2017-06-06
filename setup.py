from setuptools import setup
import os

from alpsh import history


def create_config():
    location = os.path.expanduser('~') + "/.alpsh"
    print(location)
    if not os.path.exists(location):
        os.makedirs(location)
        history.create()  # Calls a function inside the actual program to be able to install.


create_config()

setup(
    name='alpsh',
    version='1.0.0',
    packages=['alpsh', 'alpsh.builtins'],
    url='',
    license='MIT',
    author='Mozzo',
    author_email='',
    description='',

    entry_points={
        'console_scripts': [
            'alpsh=source:main',
        ],
    },
)
