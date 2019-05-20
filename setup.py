from setuptools import setup
import os
import sys


setup(
    name='handlelimiter',
    version=version['__version__'],
    description=('Tools to deal with one or more measurements from single cells'),
    long_description=long_description,
    author='Buys de Barbanson',
    author_email='b.barbanson@hubrecht.eu',
    url='https://github.com/BuysDB/HandleLimiter',
    license='MPL-2.0',
    packages=['handlelimiter'],

  install_requires=[ ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6'],
)
