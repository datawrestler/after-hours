#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Jason Lewris"
__license__ = "MIT"
__version__ = "0.2.1"
__maintainer__ = "Jason Lewris"
__email__ = "datawrestler@gmail.com"
__status__ = "Beta"

import unittest

from afterhours.afterhours import AfterHours


class AfterHoursTestCase(unittest.TestCase):
    # class AfterHoursTestCase tests the method ah_current
    # from after_hours

    def setUp(self):
        """
        only instantiate AfterHours once
        :return:
        """
        ticker = 'aapl'

        self.afterhours = AfterHours(ticker, typeof = 'after')
        self.__class__.afterhours = AfterHours(ticker)

    def tearDown(self):
        """
        kill afterhours instantiation when finished
        :return: NA
        """
        if self.afterhours is not None:
            del self.__class__.afterhours

    def test_high_price(self):
        # method test_pre_latest_price checks if the price being
        # returned from pre_latest is greater than 0
        test = self.afterhours.getdata(datatype='highprice')
        self.assertIn(type(test), [str, float],
                      msg='After tests high price failed with {}'.format(test))

    def test_low_price(self):
        test = self.afterhours.getdata(datatype='lowprice')
        self.assertIn(type(test), [str, float],
                      msg='After tests low price failed with {}'.format(test))

    def test_high_time(self):
        # method test_pre_high_time checks if the time being
        # returned from pre_high is not blank
        test = self.afterhours.getdata(datatype='highprice')
        self.assertNotEqual(test, '',
                            msg='After tests pre_high time failed: {}'.format(test))

    def test_low_time(self):
        test = self.afterhours.getdata(datatype='lowtime')
        self.assertNotEqual(test, '',
                            msg='After tests low time failed: {}'.format(test))

    def test_volume_(self):
        # method test_pre_volume_symbol checks if the symbol
        # being returned from pre_volume is accurate
        test = self.afterhours.getdata(datatype='volume').replace(',', '')
        self.assertIn(type(test), [str, float],
                      msg='Afte tests volume failed with {}'.format(test))

    def test_cur_date_month(self):
        # tests case for get_cur_date method - month
        test = self.afterhours.get_cur_date()
        self.assertIsInstance(self.afterhours.month, int,
                              msg='After tests test_cur_date failed: {}'.format(test))

    def test_cur_date_year(self):
        # tests case for get_cur_date method - year
        test = self.afterhours.get_cur_date()
        y_len = len(self.afterhours.year)
        self.assertEqual(y_len, 4,
                         msg='After tests test_cur_date failed: {}'.format(test))

    def test_cur_date_day(self):
        # tests case for get_cur_date method - day
        test = self.afterhours.get_cur_date()
        day = self.afterhours.day
        self.assertLessEqual(int(day), 31,
                             msg='After tests test_cur_date failed: {}'.format(test))

    def test_all_pages(self):
        # tests secure all pages method
        try:
            output = self.afterhours.secure_all_pages()
            test = self.afterhours.df
            self.assertGreater(test.shape[0], 0,
                               msg='After tests test_mkt_close failed: {}'.format(test))
        except ValueError:
            self.assert_(True)


class PreHoursTestCase(unittest.TestCase):
    # class AfterHoursTestCase tests the method ah_current
    # from after_hours

    def setUp(self):
        """
        only instantiate AfterHours once
        :return:
        """
        ticker = 'aapl'

        self.afterhours = AfterHours(ticker, typeof = 'pre')
        self.__class__.afterhours = AfterHours(ticker)

    def tearDown(self):
        """
        kill afterhours instantiation when finished
        :return: NA
        """
        if self.afterhours is not None:
            del self.__class__.afterhours

    def test_high_price(self):
        # method test_pre_latest_price checks if the price being
        # returned from pre_latest is greater than 0
        test = self.afterhours.getdata(datatype='highprice')
        self.assertIn(type(test), [str, float], msg='Pre tests high price failed with {}'.format(test))

    def test_low_price(self):
        test = self.afterhours.getdata(datatype='lowprice')
        self.assertIn(type(test), [str, float], msg='Pre tests low price failed with {}'.format(test))

    def test_high_time(self):
        # method test_pre_high_time checks if the time being
        # returned from pre_high is not blank
        test = self.afterhours.getdata(datatype='hightime')
        self.assertNotEqual(test, '', msg='Pre tests pre_high time failed: {}'.format(test))

    def test_low_time(self):
        test = self.afterhours.getdata(datatype='lowtime')
        self.assertNotEqual(test, '', msg = 'Pre tests low time failed: {}'.format(test))

    def test_volume_(self):
        # method test_pre_volume_symbol checks if the symbol
        # being returned from pre_volume is accurate
        test = self.afterhours.getdata(datatype='volume').replace(',', '')
        self.assertIsInstance(test, unicode,
                      msg='Pre tests volume failed with {} and type: {}'.format(test, type(test)))

    def test_cur_date_month(self):
        # tests case for get_cur_date method - month
        test = self.afterhours.get_cur_date()
        self.assertIsInstance(self.afterhours.month, int, msg='Pre tests test_cur_date failed: {}'.format(test))

    def test_cur_date_year(self):
        # tests case for get_cur_date method - year
        test = self.afterhours.get_cur_date()
        y_len = len(self.afterhours.year)
        self.assertEqual(y_len, 4, msg='Pre tests test_cur_date failed: {}'.format(test))

    def test_cur_date_day(self):
        # tests case for get_cur_date method - day
        test = self.afterhours.get_cur_date()
        day = self.afterhours.day
        self.assertLessEqual(int(day), 31, msg='Pre tests test_cur_date failed: {}'.format(test))

    def test_all_pages(self):
        # tests secure all pages method
        try:
            output = self.afterhours.secure_all_pages()
            test = self.afterhours.df
            self.assertGreater(test.shape[0], 0, msg = 'Pre tests test_mkt_close failed: {}'.format(test))
        except ValueError:
            self.assert_(True)


if __name__ == '__main__':
    unittest.main()
