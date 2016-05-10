# -*- coding: utf-8 -*-
from distutils.core import setup
import setuptools

setup(
    name='fixtures2',
    version='0.1.7',
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
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    url='https://package-insights.appspot.com/packages/fixtures2'
)
