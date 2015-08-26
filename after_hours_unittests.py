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
# https://github.com/datawrestler/after_hours
#
# THE  SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OF COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE
#

import unittest

import pep8
from testscenarios import TestWithScenarios

import after_hours


class Pep8TestCase(unittest.TestCase):

    def test_pep8(self):
        self.pep8style = pep8.StyleGuide(show_source=True)
        files = ('after_hours.py', 'after_hours_unittests.py')
        self.pep8style.check_files(files)
        self.assertEqual(self.pep8style.options.report.total_errors, 0)


class AfterHoursTestCase(TestWithScenarios):
    # class AfterHoursTestCase tests the method ah_current
    # from after_hours

    def test_web_connect_tree(self):
        # method test_web_connect_tree checks if the type of
        # value being returned is of the class lxml.html.HtmlElement
        stock_symbol = 'ibm'
        market = 'premarket-chart'
        test = after_hours.web_connect(stock_symbol, market)
        self.assertNotEqual(test, '', msg='Test web_connect tree failed')

    def test_pre_latest_symbol(self):
        # method test_pre_latest_symbol checks if the symbol being
        # returned from pre_latest is accurate
        stock_symbol = 'aapl'
        test = after_hours.pre_latest(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'aapl', msg='Test pre_latest symbol failed')

    def test_pre_latest_price(self):
        # method test_pre_latest_price checks if the price being
        # returned from pre_latest is greater than 0
        stock_symbol = 'aapl'
        test = after_hours.pre_latest(stock_symbol)
        test = test[1]
        self.assertGreater(test, 0, msg='Test pre_latest price failed')

    def test_pre_high_symbol(self):
        # method test_pre_high_symbol checks if the symbol being
        # returned from pre_high is accurate
        stock_symbol = 'aapl'
        test = after_hours.pre_high(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'aapl', msg='Test pre_high symbol failed')

    def test_pre_high_price(self):
        # method test_pre_high_price checks if the price being
        # returned from pre_high is greater than 0
        stock_symbol = 'aapl'
        test = after_hours.pre_high(stock_symbol)
        test = test[1]
        self.assertGreater(test, 0, msg='Test pre_high price failed')

    def test_pre_high_time(self):
        # method test_pre_high_time checks if the time being
        # returned from pre_high is not blank
        stock_symbol = 'aapl'
        test = after_hours.pre_high(stock_symbol)
        test = test[2]
        self.assertNotEqual(test, '', msg='Test pre_high time failed')

    def test_pre_low_symbol(self):
        # method test_pre_low_symbol checks if the symbol
        # being returned from pre_low is accurate
        stock_symbol = 'aapl'
        test = after_hours.pre_low(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'aapl', msg='Test pre_low symbol failed')

    def test_pre_low_price(self):
        # method test_pre_low_price checks if the price
        # being returned from pre_low is greater than 0
        stock_symbol = 'aapl'
        test = after_hours.pre_low(stock_symbol)
        test = test[1]
        self.assertGreater(test, 0, msg='Test pre_low price failed')

    def test_pre_low_time(self):
        # method test_pre_low_time checks if the time value
        # being returned from pre_low is not blank
        stock_symbol = 'aapl'
        test = after_hours.pre_low(stock_symbol)
        test = test[2]
        self.assertNotEqual(test, '', msg='Test pre_low time failed')

    def test_pre_volume_symbol(self):
        # method test_pre_volume_symbol checks if the symbol
        # being returned from pre_volume is accurate
        stock_symbol = 'aapl'
        test = after_hours.pre_volume(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'aapl', msg='Test pre_volume symbol failed')

    def test_pre_volume_volume(self):
        # method test_pre_volume_volume checks if the volume
        # value being returned from pre_volume is not blank
        stock_symbol = 'aapl'
        test = after_hours.pre_volume(stock_symbol)
        test = test[1]
        self.assertNotEqual(test, '', msg='Test pre_volume volume failed')

    def test_pre_all_symbol(self):
        # method test_pre_all_symbol checks if the symbol being
        # returned from pre_all is accurate
        stock_symbol = 'aapl'
        test = after_hours.pre_all(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'aapl', msg='Test pre_all symbol failed')

    def test_pre_all_time(self):
        # method test_pre_all_time checks if the time value being
        # returned from pre_all is not blank
        stock_symbol = 'aapl'
        test = after_hours.pre_all(stock_symbol)
        test1 = test[1]
        test2 = test1[0]
        self.assertNotEqual(test2, '', msg='Test pre_all time failed')

    def test_pre_all_price(self):
        # method test_pre_all_time checks if the price value being
        # returned from pre_all is greater than 0
        stock_symbol = 'aapl'
        test = after_hours.pre_all(stock_symbol)
        test = test[2]
        test1 = test[0]
        self.assertGreater(test1, 0, msg='Test pre_all price failed')

    def test_pre_all_volume(self):
        # method test_pre_all_volume checks if the volume being
        # returned from pre_all is not blank
        stock_symbol = 'aapl'
        test = after_hours.pre_all(stock_symbol)
        test1 = test[3]
        test2 = test1[0]
        self.assertNotEqual(test2, '', msg='Test pre_all volume failed')

    def test_pre_market_avg_symbol(self):
        # method test_pre_market_avg_symbol checks if the symbol being returned
        # from pre_market_avg is accurate
        stock_symbol = 'aapl'
        test = after_hours.pre_market_avg(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'aapl', msg='Test pre_market_avg symbol failed')

    def test_pre_market_avg_price(self):
        # method test_pre_market_avg_price checks if the price being returned
        # from pre_market_avg is greater than 0
        stock_symbol = 'aapl'
        test = after_hours.pre_market_avg(stock_symbol)
        test = test[1]
        self.assertGreater(test, 0, msg='Test pre_market_avg price failed')

    def test_pre_market_sse_symbol(self):
        # method test_pre_market_sse_symbol checks if the symbol being returned
        # from pre_market_sse is accurate
        stock_symbol = 'aapl'
        test = after_hours.pre_market_sse(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'aapl', msg='Test pre_market_sse symbol failed')

    def test_pre_market_sse_value(self):
        # method test_pre_market_sse_value checks if the value being returned
        # from pre_market_sse if greater than 0
        stock_symbol = 'aapl'
        test = after_hours.pre_market_sse(stock_symbol)
        test = test[1]
        self.assertGreater(test, 0, msg='Test pre_market_sse value failed')

    def test_pre_market_sd_symbol(self):
        # method test_pre_market_sd_symbol checks if the symbol value being
        # returned from pre_market_sd is accurate
        stock_symbol = 'aapl'
        test = after_hours.pre_market_sd(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'aapl', msg='Test pre_market_sd symbol failed')

    def test_pre_market_sd_value(self):
        # method test_pre_market_sd_value checks if the value being returned
        # for standard deviation in pre_market_sd is greater than 0
        stock_symbol = 'aapl'
        test = after_hours.pre_market_sd(stock_symbol)
        test = test[1]
        self.assertGreater(test, 0, msg='Test pre_market_sd value failed')

    def test_ah_latest_symbol(self):
        # method test_ah_latest_symbol checks if the symbol being
        # returned from ah_latest is accurate
        stock_symbol = 'aapl'
        test = after_hours.ah_latest(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'aapl', msg='Test ah_latest symbol failed')

    def test_ah_latest(self):
        # method test_ah_latest checks if the value being return from
        # ah_latest is greater than 0
        stock_symbol = 'aapl'
        info = after_hours.ah_latest(stock_symbol)
        info = info[1]
        self.assertGreater(float(info), 0)

    def test_ah_high_symbol(self):
        # method test_ah_high_symbol checks if the symbol value
        # being returned from ah_high is equal to test symbol
        # of aapl
        stock_symbol = 'aapl'
        test = after_hours.ah_high(stock_symbol)
        self.assertEquals(test[0], 'aapl', msg='Test ah_high symbol failed')

    def test_ah_high_price(self):
        # method test_ah_high_price checks if value being returned from
        # ah_high is greater than 0 for price
        stock_symbol = 'aapl'
        test = after_hours.ah_high(stock_symbol)
        self.assertGreater(test[1], 0, msg='Test ah_high price failed')

    def test_ah_high_time(self):
        # method test_ah_high_time checks if value returned from
        # ah_high time is not blank
        stock_symbol = 'aapl'
        test = after_hours.ah_high(stock_symbol)
        self.assertNotEquals(test[2], '', msg='Test ah_high time failed')

    def test_ah_low_symbol(self):
        # method test_ah_low_symbol checks if the symbol value
        # being returned from ah_low is equal to test symbol
        # used in unit test, aapl
        stock_symbol = 'aapl'
        test = after_hours.ah_low(stock_symbol)
        self.assertEquals(test[0], 'aapl', msg='Test ah_low symbol failed')

    def test_ah_low_price(self):
        # method test_ah_low_price checks if value being returned
        # from ah_low is greater than 0 for price
        stock_symbol = 'aapl'
        test = after_hours.ah_low(stock_symbol)
        self.assertNotEquals(test[1], '', msg='Test ah_low price failed')

    def test_ah_low_time(self):
        # method test_ah_low_time checks if the value returned
        # from ah_low is not blank
        stock_symbol = 'aapl'
        test = after_hours.ah_low(stock_symbol)
        self.assertNotEquals(test[2], '', msg='Test ah_low time failed')

    def test_ah_volume_symbol(self):
        # method test_ah_volume_symbol checks if the symbol value
        # being returned from ah_volume is equal to the test symbol
        # used in unit test, aapl
        stock_symbol = 'aapl'
        test = after_hours.ah_volume(stock_symbol)
        self.assertEquals(test[0], 'aapl', msg='Test ah_volume symbol failed')

    def test_ah_volume(self):
        # method test_ah_volume checks if the value being returned
        # from ah_volume is not blank
        stock_symbol = 'aapl'
        test = after_hours.ah_volume(stock_symbol)
        self.assertNotEquals(test[1], '', msg='Test ah_volume volume failed')

    def test_ah_all_symbol(self):
        # method test_ah_all_symbol checks if the symbol value
        # being returned from ah_all is equal to the test symbol
        # used in unittest, aapl
        stock_symbol = 'aapl'
        test = after_hours.ah_all(stock_symbol)
        self.assertEquals(test[0], 'aapl', msg='Test ah_all symbol failed')

    def test_ah_all_time(self):
        # method test_ah_all_time checks if the time value
        # being return from ah_all is not empty using symbol
        # yhoo for testing
        stock_symbol = 'yhoo'
        test = after_hours.ah_all(stock_symbol)
        test1 = test[1]
        test2 = test[0]
        test3 = str(test)
        self.assertNotEquals(test3, '', msg='Test ah_all time failed')

    def test_ah_all_price(self):
        # method test_ah_all_price checks if the price value
        # being returned from ah_all is greater than 0
        # using symbol yhoo for testing
        stock_symbol = 'yhoo'
        test = after_hours.ah_all(stock_symbol)
        test1 = test[2][0]
        self.assertGreater(float(test1), 0, msg='Test ah_all price failed')

    def test_ah_all_volume(self):
        # method test_ah_all_volume checks if the volume value
        # being returned from ah_all is not blank using
        # test symbol yhoo
        stock_symbol = 'yhoo'
        test = after_hours.ah_all(stock_symbol)
        test1 = test[3]
        test2 = test1[0]
        test3 = str(test2)
        self.assertNotEquals(test3, '', msg='Test ah_all volume failed')

    def test_ah_avg_symbol(self):
        # method ah_avg_symbol checks if the symbol value
        # from ah_avg is being returned accurately
        stock_symbol = 'yhoo'
        test = after_hours.ah_avg(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'yhoo', msg='Test ah_avg symbol failed')

    def test_ah_avg_price(self):
        # method test_ah_avg_price checks if the average value
        # returned from ah_avg is greater than 0
        stock_symbol = 'yhoo'
        test = after_hours.ah_avg(stock_symbol)
        test = test[1]
        self.assertGreater(test, 0, msg='Test ah_avg price failed')

    def test_ah_sse_symbol(self):
        # method test_ah_sse_symbol checks if the symbol value
        # from ah_sse is being returned accurately
        stock_symbol = 'yhoo'
        test = after_hours.ah_sse(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'yhoo', msg='Test ah_sse symbol failed')

    def test_ah_sse_value(self):
        # method test_ah_sse_value checks if the value being
        # returned for sum of square deviations is greater than 0
        # from method ah_sse
        stock_symbol = 'yhoo'
        test = after_hours.ah_sse(stock_symbol)
        test = test[1]
        self.assertGreater(test, 0, msg='Test ah_sse value failed')

    def test_ah_sd_symbol(self):
        # method test_ah_sd_symbol checks if the symbol value
        # from ah_sd is being returned accurately
        stock_symbol = 'yhoo'
        test = after_hours.ah_sd(stock_symbol)
        test = test[0]
        self.assertEqual(test, 'yhoo', msg='Test ah_sd symbol failed')

    def test_ah_sd_value(self):
        # method test_ah_sd_value checks if the value
        # being returned from ah_sd is greater than 0
        stock_symbol = 'yhoo'
        test = after_hours.ah_sd(stock_symbol)
        test = test[1]
        self.assertGreater(test, 0, msg='Test ah_sd value failed')
if __name__ == '__main__':
    unittest.main()
