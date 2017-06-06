from distutils.core import setup
import os

from alpsh import history


    location = os.path.expanduser('~') + "/.alpsh"
    print(location)
    if not os.path.exists(location):
        os.makedirs(location)



setup(
    name='alpsh',
    version='1.0.0',
    packages=['alpsh', 'alpsh.builtins'],
    url='',
    license='MIT',
    author='Mozzo',
    author_email='',
    description=''
)
