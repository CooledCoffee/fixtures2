# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='fixtures2',
    version='0.1.3',
    author='Mengchen LEE',
    author_email='CooledCoffee@gmail.com',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
    description='Fixtures2 is an extension of the fixtures test framework.',
    extras_require={
        'mox': ['mox'],
    },
    install_requires=[
        'fixtures',
    ],
    packages=[
        'fixtures2',
    ],
    url='https://github.com/CooledCoffee/fixtures2/',
)
