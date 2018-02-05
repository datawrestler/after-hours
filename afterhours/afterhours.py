#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Jason Lewris"
__license__ = "MIT"
__version__ = "0.2.1"
__maintainer__ = "Jason Lewris"
__email__ = "datawrestler@gmail.com"
__status__ = "Beta"

import time
import re
import requests
from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup

try:
    from afterhours.utils import Settings, formatoutput, clean_df
except:
    from utils import Settings, formatoutput, clean_df


class AfterHours(object):

    def __init__(self, ticker='appl', typeof='after'):
        # check user inserted correct typeof
        if typeof not in ['after', 'pre']:
            raise ValueError("""Must use `after` or `pre` to define after hours or pre hours trading""")
        self.typeof = typeof

        # init master dataframe for records
        self.df = pd.DataFrame()

        # assign ticker symbol
        if not isinstance(ticker, str):
            raise TypeError("""ticker symbol must be a string containing the trading symbol""")

        self.ticker = ticker

        # assign initial beautiful soup
        self.init = BeautifulSoup(requests.get(Settings.link_dict[self.typeof].format(self.ticker)).content,
                                  'html.parser')

        # check if initial beautiful soup is even available from NASDAQ
        if self.init.find('div', {'class': Settings.settings['nottrading']}):
            raise RuntimeError('NASDAQ NOT TRADING IPO ERROR FOR TICKER: {}'.format(self.ticker))

        # assign to tmp soup
        self.soup = self.init

        # get current day, month, year
        self.get_cur_date()

    def get_cur_date(self):
        """
        Retrieve market close date from Ticker page
        :return: NA
        """
        tmp = self.soup.find('small', text=re.compile('market', re.IGNORECASE)).text.split('Market')[0].strip()

        # assign year
        self.year = Settings.year.search(tmp).group(0)

        # assign day
        self.day = Settings.day.search(tmp).group(0)

        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

        # iterate over months and flag if match found
        for ii, mo in enumerate(months, 1):
            more = re.compile(mo, re.IGNORECASE)
            if more.search(tmp):
                self.month = ii
                break

    def getdata(self, datatype='lowprice'):
        """
        retrieve user defined datatype. Supported datatypes
        includes mktclose, high price, low price, hightime, lowtime, volume
        :param datatype: supported data types [mktclose, highprice, lowprice, hightime,
            lowtime]
        :return: formatted retrieved data type
        """
        datatype = datatype.lower()
        if datatype not in ['mktclose', 'highprice', 'lowprice',
                            'hightime', 'lowtime', 'volume']:
            raise ValueError("""Only supports mktclose, highprice, lowprice, hightime, lowtime
                                \nUnsupported: {}""".format(datatype))

        outputdata = getattr(self.soup.find('span', {'id': Settings.settings[datatype]}), 'text', None)
        # secure appropriate formatting type
        format_out = Settings.formatting[datatype]

        if datatype == 'mktclose':
            if not Settings.mkt_close_re.search(outputdata):
                raise ValueError("""Current market close price unavailable""")
            else:
                return formatoutput(Settings.mkt_close_re.search(outputdata).group(0), format_out)

        elif datatype in ['lowprice', 'highprice']:
            return formatoutput(outputdata, Settings.formatting[datatype])

        elif datatype in ['lowtime', 'hightime']:
            return formatoutput((outputdata, self.month, self.day, self.year), format_out)

        else:
            return formatoutput(outputdata, format_out)

    def secure_all_pages(self):
        """
        iterate over all pages of price information for after hours trading,
            secure data and store in pandas dataframe. Columns incude:
                Time: datetime object of time stamps from trading
                Price: price of trade
                Volume: volume of shares
                Ticker: Ticker symbol of stock

        :return: cleaned dataframe containing
        """
        # check if pricing table is available at all, if not return value error
        if not self.soup.find('table', {'id': Settings.settings['pricetable']}):
            raise ValueError('{} market data not available for {}'.format(self.typeof, self.ticker))

        # format data from table, and convert to pandas dataframe
        table = self.soup.find('table', {'id': Settings.settings['pricetable']}).findAll('td')
        times = [datetime.strptime('{}-{}-{} {}'.format(self.month, self.day, self.year, rec.text),
                                   '%m-%d-%Y %H:%M:%S') for rec in table[::3]]
        prices = [float(Settings.price_finder.search(rec.text).group(0)) for rec in table[1::3]]
        volumes = [rec.text.replace(',', '') for rec in table[2::3]]

        tmpdf = pd.DataFrame({'Time': times,
                              'Price': prices,
                              'Volume': volumes})
        # assign ticker
        tmpdf['Ticker'] = self.ticker

        self.df = self.df.append(tmpdf)

        next_page_tag = self.soup.find('a', {'id': Settings.settings['nextpage']})
        if next_page_tag and next_page_tag.has_attr('href'):
            next_page_link = next_page_tag['href']
            next_soup = BeautifulSoup(requests.get(next_page_link).content, 'html.parser')
            self.soup = next_soup
            self.secure_all_pages()
        else:
            # reset link pointer to main ticker page
            self.soup = self.init
            # drop duplicate rows
            self.df.drop_duplicates(keep = 'first', inplace = True)
            # cleanup dataframe
            self.df = clean_df(self.df)

        return self.df

    def run_every(self, seconds = 10, num_iter = 2):
        """
        secure new runs of data from NASDAQ
        :param seconds: number of seconds between runs
        :param num_iter: number of times to collect data
        :return: NA
        """
        while True:
            if num_iter != 0:
                print(num_iter)
                num_iter -= 1
                self.secure_all_pages()
                time.sleep(seconds)
            else:
                break


if __name__ == '__main__':

    AH = AfterHours('nflx', typeof = 'after')
    AH.getdata(datatype='lowprice')
    AH.getdata(datatype='highprice')
    AH.getdata(datatype='volume')
    AH.getdata(datatype='hightime')
    AH.getdata(datatype='lowtime')
    AH.secure_all_pages()
    AH.run_every(seconds = 5, num_iter = 2)
    AH.df.head(1000)
