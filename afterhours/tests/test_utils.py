#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Jason Lewris"
__license__ = "MIT"
__version__ = "0.2.1"
__maintainer__ = "Jason Lewris"
__email__ = "datawrestler@gmail.com"
__status__ = "Beta"

import unittest
import datetime

import afterhours.utils as utils


class AfterHoursTestCase(unittest.TestCase):
    # class AfterHoursTestCase tests the method ah_current
    # from after_hours

    def test_cancelled(self):
        # test cancelled regex
        canc = 'this trade was cancelled'
        canc_re = utils.Settings.cancelled.search(canc).group(0)
        self.assertEqual(canc_re,
                         'cancelled',
                         """Cancelled regex did not equal cancelled
                         \nRegex: {}""".format(canc_re))

    def test_formatting(self):
        # test formatting dictionary
        self.assertEqual(utils.Settings.formatting['mktclose'],
                         'price',
                         """formatting output unexpected output
                         \nMktclose Output: {}""".format(utils.Settings.formatting['mktclose']))

        self.assertEqual(utils.Settings.formatting['highprice'],
                         'price',
                         """formatting output unexpected output
                         \nhighprice Output: {}""".format(utils.Settings.formatting['highprice']))

        self.assertEqual(utils.Settings.formatting['lowprice'],
                         'price',
                         """formatting output unexpected output
                         \nlowprice Output: {}""".format(utils.Settings.formatting['lowprice']))

        self.assertEqual(utils.Settings.formatting['volume'],
                         'volume',
                         """formatting output unexpected output
                         \nvolume Output: {}""".format(utils.Settings.formatting['volume']))

        self.assertEqual(utils.Settings.formatting['lowtime'],
                         'date',
                         """formatting output unexpected output
                         \nlowtime Output: {}""".format(utils.Settings.formatting['lowtime']))

        self.assertEqual(utils.Settings.formatting['hightime'],
                         'date',
                         """formatting output unexpected output
                         \nhightime Output: {}""".format(utils.Settings.formatting['hightime']))

    def test_filter(self):
        # test filtering function stripping of large ordinals
        test_str = '\xa0this is a freaking test'

        filtered = utils.filter_data(test_str)

        self.assertNotIn('\xa0', filtered,
                         """Filtered function not stripping ordinals above 128""")

    def format_price(self):
        # check price formatting output
        res = utils.formatoutput('$128.9', outtype='price')
        self.assertIsInstance(res, float,
                              """formatoutput unexpected return type for price""")
        self.assertEqual(res, 128.9,
                         """formatoutput unexecpted conversion for price""")

    def format_date(self):
        import datetime
        res = utils.formatoutput(('12:07:03 PM', '12', '2', '2018'), outtype='date')
        self.assertIsInstance(res,
                              datetime.datetime,
                              """formatoutput unexecpted formatting did not return datetime
                              \nreturned: {}""".format(type(res)))


if __name__ == '__main__':
    unittest.main()

