__author__ = 'Jason Lewris'
__version__ = '1.1.0.dev1'

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
# the purpose of this script is to obtain accurate stock data during the
# after hours trading, from 4-8pm and from 4-8am.

try:
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from lxml import html
except ImportError:
    from urllib2 import Request, urlopen
    from lxml import html
    from urllib import urlencode


def web_connect(stock_symbol, market):
    url = 'http://www.nasdaq.com/symbol/%s/%s' % (stock_symbol, market)
    req = Request(url)
    resp = urlopen(req)
    response = resp.read().decode().strip()
    tree = html.fromstring(response)
    return tree


# Pre_current method retrieves the latest pre-market trade price for symbol
def pre_latest(stock_symbol):
    stock_symbol = stock_symbol.lower()
    tree = web_connect(stock_symbol, 'premarket-chart')
    price = tree.xpath('//span[@id="quotes_content_left_lblLastsale"]/text()')
    price = str(price)
    price = price[7:]
    price = price[:-2]
    try:
        price = float(price)
        return stock_symbol, price
    except:
        print("There is currently no pre-market data "
              "available for symbol %s" % stock_symbol)


# pre_high method retrieves the highest pre-market price for given symbol
def pre_high(stock_symbol):
    stock_symbol = stock_symbol.lower()
    tree = web_connect(stock_symbol, 'premarket')
    price = tree.xpath('//span[@id="quotes_content_left_lblHighprice"]'
                       '/text()')
    # slicing the beginning and end of the extracted text which
    # contains un-required information
    price = str(price)
    price = price[7:]
    price = price[:-2]
    try:
        # converting to float
        price = float(price)
        time = tree.xpath('//span[@id="quotes_content_left_lblhightime"]'
                          '/text()')
        time = str(time)
        time = time[2:]
        time = time[:-2]
        return stock_symbol, price, time
    except:
        print("There is currently no pre-market data "
              "available for symbol %s" % stock_symbol)


# This method retrieves the lowest pre-market trade price for given symbol
def pre_low(stock_symbol):
    stock_symbol = stock_symbol.lower()
    tree = web_connect(stock_symbol, 'premarket')
    price = tree.xpath('//span[@id="quotes_content_left_lblLowprice"]'
                       '/text()')
    price = str(price)
    # slicing the beginning and end of the extracted text which contains
    # un-required information
    price = price[7:]
    price = price[:-2]
    # converting to float
    try:
        price = float(price)
        # extracting after hours low time
        time = tree.xpath('//span[@id="quotes_content_left_lbllowtime"]'
                          '/text()')
        time = str(time)
        time = time[2:]
        time = time[:-2]
        return stock_symbol, price, time
    except:
        print("There is currently no pre-market data "
              "available for symbol %s" % stock_symbol)


# Method pre_volume returns the total volume for pre market trading for
# given symbol
def pre_volume(stock_symbol):
    stock_symbol = stock_symbol.lower()
    try:
        tree = web_connect(stock_symbol, 'premarket')
        volume = tree.xpath('//span[@id="quotes_content_left_lblVolume"]'
                            '/text()')
        volume = str(volume)
        volume = volume[+2:]
        volume = volume[:-2]
        return stock_symbol, volume
    except:
        print("There is currently no pre-market data "
              "available for symbol %s" % stock_symbol)


# This method retrieves all after-hours trading prices, times, and
# volume for given symbol
def pre_all(stock_symbol):
    stock_symbol = stock_symbol.lower()
    times = []
    prices = []
    volumes = []
    webconnectdat = ['premarket', 'premarket?page=2']
    try:
        for link in webconnectdat:
            tree = web_connect(stock_symbol, link)
            # extracting time information
            time = tree.xpath('//tr/td[1]/text()')
            for realtime in time:
                ttime = realtime.strip()
                if len(ttime) > 3:
                    times.append(ttime)
            # extracting pricing information
            pricing = tree.xpath('//tr/td[2]/text()')
            for item in pricing:
                price = item.strip()
                if len(price) > 2:
                    price = price[2:]
                    price = float(price)
                    prices.append(price)
            # extracting volume information
            volume = tree.xpath('//tr/td[3]/text()')
            for vol in volume:
                vol = vol.strip()
                if vol != '(' and vol != ')':
                    volumes.append(vol)
        return stock_symbol, times, prices, volumes
    except:
        print("There was an error processing your request which could be due "
              "to no pre-market data being available at this time")


# pre_market_avg return the average pre market trading price
def pre_market_avg(stock_symbol):
    try:
        stock_symbol = stock_symbol.lower()
        test = pre_all(stock_symbol)
        test = test[2]
        n = len(test)
        if n < 1:
            raise ValueError("Calculating the mean requires "
                             "at least one data point")
        return stock_symbol, sum(test) / n
    except:
        print("there was an error processing your request which could be due "
              "to no pre-market data being available at this time")


# pre_market_sse returns the sum of square deviations for symbol
def pre_market_sse(stock_symbol):
    try:
        stock_symbol = stock_symbol.lower()
        test = pre_all(stock_symbol)
        test = test[2]
        mean = pre_market_avg(stock_symbol)
        mean = mean[1]
        ss = sum((x-mean)**2 for x in test)
        return stock_symbol, ss
    except:
        print("there was an error processing your request which could be due "
              "to no pre-market data being available at this time")


# pre_market_sd returns the standard deviation for pre-market
# prices for symbol
def pre_market_sd(stock_symbol):
    try:
        stock_symbol = stock_symbol.lower()
        test = pre_all(stock_symbol)
        test = test[2]
        n = len(test)
        if n < 2:
            raise ValueError("To calculate variance you need at "
                             "least two data points")
        ss = pre_market_sse(stock_symbol)
        ss = ss[1]
        pop_var = ss / n
        return stock_symbol, pop_var**0.5
    except:
        print("there was an error processing your request which could be due "
              "to no pre-market data being available at this time")


# This method obtains the current after-hours trade price for given symbol
def ah_latest(stock_symbol):
    stock_symbol = stock_symbol.lower()
    tree = web_connect(stock_symbol, 'after-hours-chart')
    price = tree.xpath('//span[@id="quotes_content_left_lblLastsale"]'
                       '/text()')
    price = str(price)
    price = price[7:]
    price = price[:-2]
    print(price)
    try:
        price = float(price)
        return stock_symbol, price
    except:
        print('There is currently no after-market current price available '
              'for symbol %s' % stock_symbol)


# This method obtains the highest after-hours trade price for given symbol
def ah_high(stock_symbol):
    stock_symbol = stock_symbol.lower()
    tree = web_connect(stock_symbol, 'after-hours')
    price = tree.xpath('//span[@id="quotes_content_left_lblHighprice"]'
                       '/text()')
    # slicing the beginning and end of the extracted text which
    # contains un-required information
    price = str(price)
    price = price[7:]
    price = price[:-2]
    # converting to float
    try:
        price = float(price)
        # extracting after hours high time
        time = tree.xpath('//span[@id="quotes_content_left_lblhightime"]'
                          '/text()')
        time = str(time)
        time = time[2:]
        time = time[:-2]
        return stock_symbol, price, time
    except:
        print("there was an error processing your request which could be due "
              "to no after-hours data being available at this time")


# This method retrieves the lowest after-hours trade price for given symbol
def ah_low(stock_symbol):
    stock_symbol = stock_symbol.lower()
    tree = web_connect(stock_symbol, 'after-hours')
    price = tree.xpath('//span[@id="quotes_content_left_lblLowprice"]'
                       '/text()')
    price = str(price)
    price = price[7:]
    price = price[:-2]
    try:
        # converting to float
        price = float(price)
        # extracting after hours low time
        time = tree.xpath('//span[@id="quotes_content_left_lbllowtime"]'
                          '/text()')
        time = str(time)
        time = time[2:]
        time = time[:-2]
        return stock_symbol, price, time
    except:
        print("there was an error processing your request which could be due "
              "to no after-hours data being available at this time")


# This method retrieves the total after-hours volume for given symbol
def ah_volume(stock_symbol):
    stock_symbol = stock_symbol.lower()
    tree = web_connect(stock_symbol, 'after-hours')
    try:
        volume = tree.xpath('//span[@id="quotes_content_left_lblVolume"]'
                            '/text()')
        volume = str(volume)
        volume = volume[+2:]
        volume = volume[:-2]
        return stock_symbol, volume
    except:
        print("there was an error processing your request which could be due "
              "to no after-hours data being available at this time")


# This method retrieves all after-hours trading prices, times, and
# volume for given symbol
def ah_all(stock_symbol):
    stock_symbol = stock_symbol.lower()
    times = []
    prices = []
    volumes = []
    webconnectdat = ['after-hours', 'after-hours?page=2']
    try:
        for link in webconnectdat:
            tree = web_connect(stock_symbol, link)
            # extracting time information
            time = tree.xpath('//tr/td[1]/text()')
            for realtime in time:
                ttime = realtime.strip()
                if len(ttime) > 3:
                    times.append(ttime)
            # extracting pricing information
            pricing = tree.xpath('//tr/td[2]/text()')
            for item in pricing:
                price = item.strip()
                if len(price) > 2:
                    price = price[2:]
                    price = float(price)
                    prices.append(price)
            # extracting volume information
            volume = tree.xpath('//tr/td[3]/text()')
            for vol in volume:
                vol = vol.strip()
                if vol != '(' and vol != ')':
                    volumes.append(vol)
        return stock_symbol, times, prices, volumes
    except:
        print("There was an error processing your request which could be due "
              "to no after-hours data being available at this time")


# ah_avg returns the average after hours trading price
def ah_avg(stock_symbol):
    stock_symbol = stock_symbol.lower()
    try:
        test = ah_all(stock_symbol)
        test = test[2]
        n = len(test)
        if n < 1:
            raise ValueError("Calculating the mean requires "
                             "at least one data point")
        return stock_symbol, sum(test) / n
    except:
        print("there was an error processing your request which could be due "
              "to no after-hours data being available at this time")


# ah_sse returns the sum of square deviations for symbol in after
# hours trading
def ah_sse(stock_symbol):
    stock_symbol = stock_symbol.lower()
    try:
        test = ah_all(stock_symbol)
        test = test[2]
        mean = ah_avg(stock_symbol)
        mean = mean[1]
        ss = sum((x-mean)**2 for x in test)
        return stock_symbol, ss
    except:
        print("there was an error processing your request which could be due "
              "to no after-hours data being available at this time")


# ah_sd returns the standard deviation for prices in the
# after hours market
def ah_sd(stock_symbol):
    stock_symbol = stock_symbol.lower()
    try:
        test = ah_all(stock_symbol)
        test = test[2]
        n = len(test)
        if n < 2:
            raise ValueError("To calculate variance you need at "
                             "least two data points")
        ss = ah_sse(stock_symbol)
        ss = ss[1]
        pop_var = ss / n
        return stock_symbol, pop_var**0.5
    except:
        print("there was an error processing your request which could be due "
              "to no after-hours data being available at this time")
