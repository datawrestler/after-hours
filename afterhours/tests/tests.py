#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Jason Lewris"
__license__ = "MIT"
__version__ = "0.2.1"
__maintainer__ = "Jason Lewris"
__email__ = "datawrestler@gmail.com"
__status__ = "Beta"

import glob
import unittest

if __name__ == '__main__':
    # https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory
    test_files = glob.glob('test_*.py')
    module_strings = [test_file[0:len(test_file) - 3] for test_file in test_files]
    suites = [unittest.defaultTestLoader.loadTestsFromName(test_file) for test_file in module_strings]
    test_suite = unittest.TestSuite(suites)
    test_runner = unittest.TextTestRunner().run(test_suite)