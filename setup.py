from __future__ import absolute_import, division, print_function

import os
import re
import sys

from setuptools import setup, find_packages


prefix = os.path.abspath(os.path.dirname(__file__))
version = re.search(r'^__version__\s*=\s*([\'"].+[\'"]).*',
                    open(os.path.join(prefix,
                                      'pymo',
                                      '_version.py')).read()).group(1)


setup(
    name='pymo',
    version=version,
    description='MongoClient instrumentation and factory',
    url='https://github.com/mlab/pymo',
    author='Greg Banks',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: pymongo',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='pymongo mongodb driver',
    packages=find_packages(exclude=['tests']),
    install_requires=['pymongo>=2,<4'],
    extras_require={
        'test': ['nose2'],
    }
)