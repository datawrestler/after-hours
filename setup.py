#
# License: The MIT License (MIT)
#
# Copyright (c) 2015 Jason Lewris
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whome the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# This file is part of after_hours.py
# https://github.com/datawrestler/after-hours
#
# THE  SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OF COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE
#

"""
setup/install script for after_hours
"""

from distutils.core import setup
import os

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.rst')) as f:
    LONG_DESCRIPTION = '\n' + f.read()

setup(
    name='after_hours',
    py_modules =['after_hours'],
    version = '0.1',
    author='Jason Lewris',
    author_email='datawrestler@gmail.com',
    description='retrieve after hours stock information from Nasdaq',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/datawrestler/after-hours',
    download_url='https://github.com/datawrestler/after-hours/tarball/0.1',
    keywords=['stocks', 'stockmarket', 'market', 'finance', 'nasdaq', 'afterhours', 'premarket', 'postmarket'],
    license='GNU LGPLv2+',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Investment'
    ]
)
