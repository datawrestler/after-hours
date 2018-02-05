#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Jason Lewris"
__license__ = "MIT"
__version__ = "0.2.1"
__maintainer__ = "Jason Lewris"
__email__ = "datawrestler@gmail.com"
__status__ = "Beta"

import re
from datetime import datetime


class Settings(object):
    """
    Convenience class to store main calibration settings
    """
    # price finder regex
    price_finder = re.compile('[0-9]{1,5}(\.[0-9]{2})?')

    # vol number only
    volnum = re.compile('[0-9]{1,10}')

    # cancelled re
    cancelled = re.compile('cancelled', re.IGNORECASE)

    # main link
    main_link = 'http://www.nasdaq.com/symbol/{}/after-hours'

    # pre market main link
    pre_main_link = 'http://www.nasdaq.com/symbol/{}/premarket'

    # create link dict
    link_dict = {'after': main_link,
                 'pre': pre_main_link}

    # mkt close
    mkt_close_re = re.compile('(?<=\$)[0-9]{1,5}(\.[0-9]{2})?')

    # day regex
    day = re.compile('[1-3][0-9]?')

    # year regex
    year = re.compile('20[0-9]{2}')

    # output formatting
    formatting = {'mktclose': 'price',
                  'highprice': 'price',
                  'lowprice': 'price',
                  'lowtime': 'date',
                  'hightime': 'date',
                  'volume': 'volume'}

    # tag constructs
    settings = {'volume': 'quotes_content_left_lblVolume',
                'highprice': 'quotes_content_left_lblHighprice',
                'lowprice': 'quotes_content_left_lblLowprice',
                'hightime': 'quotes_content_left_lblhightime',
                'lowtime': 'quotes_content_left_lbllowtime',
                'nextpage': 'quotes_content_left_lb_NextPage',
                'pricetable': 'AfterHoursPagingContents_Table',
                'nottrading': 'notTradingIPO',
                'mktclose': re.compile('market', re.IGNORECASE)}

    curdate = datetime.now()


def filter_data(data):
    return ''.join(list(filter(lambda x: ord(x) <= 128, data)))


def formatoutput(output, outtype='date'):
    assert outtype in ['date', 'price', 'volume'], """formatout only supports date, price, volume
                                                        \nUnsupported: {}""".format(outtype)

    if outtype == 'date':
        tme, month, day, year = output
        # if date in defined group indicating no data availalbe, return no data
        if tme in ['', 'N/A', None]:
            return 'DATA NOT AVAILABLE'
        else:
            # filter string for any weird characters
            tme = filter_data(tme)
            # format the date to be returned
            return datetime.strptime('{}-{}-{} {}'.format(month, day, year, tme),
                                     '%m-%d-%Y %H:%M:%S %p')

    else:
        if output in ['', 'N/A', None]:
            return 'DATA NOT AVAILABLE'

        if outtype == 'price':
            price = filter_data(output.replace('$', ''))
            return float(price)

        if outtype == 'volume':
            volume = filter_data(output)
            try:
                # return float of volume for easy manipulation
                return float(volume)
            except ValueError:
                # return cancelled volume info
                return volume

def clean_df(dataframe):
    """
    clean dataframe colummns, pull out cancelled into separate column
    :return: NA
    """
    dataframe['Cancelled'] = dataframe['Volume'].apply(lambda x: True if Settings.cancelled.search(str(x)) else False)
    dataframe['Volume'] = dataframe['Volume'].apply(lambda x: int(Settings.volnum.search(str(x)).group(0)))
    return dataframe
