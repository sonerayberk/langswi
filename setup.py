#!/usr/bin/env python

import os.path
from setuptools import setup


def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


version = [line for line in read('langswi/__init__.py').split('\n') if '__VERSION__' in line][0]

exec(version)


setupconf = dict(
    name='langswi',
    version='.'.join(str(ver) for ver in __VERSION__),
    license='BSD',
    url='https://github.com/sonerayberk/langswi/',
    author='sonerayberk',
    author_email='soner.ayberk@gmail.com',
    description='Cyrillic-latin and reverse text transformation',
    long_description=read('README.md'),
    packages=['langswi'],
    entry_points={
        'console_scripts': [
            'translator=langswi.main:main'
        ]
    }
)

if __name__ == '__main__':
    setup(**setupconf)
