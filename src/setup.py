# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='fixtures2',
    version='0.1',
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
    install_requires=[
        'fixtures',
        'mox',
    ],
    packages=[
        'fixtures',
    ],
    url='https://github.com/CooledCoffee/fixtures2/',
)
