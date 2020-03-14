from setuptools import setup

setup(
    name='alpsh',
    version='1.0.0',
    packages=['alpsh', 'alpsh.builtins'],
    url='',
    license='MIT',
    author='Mozzo',
    author_email='',
    description='',
    install_requires=['rapidtables'],
    entry_points={
        'console_scripts': [
            'alpsh=alpsh.shell:main',
        ],
    },
)
