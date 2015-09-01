__author__ = 'Jason Lewris'
__version__ = '0.1.1'

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
# the purpose of this script is to obtain accurate stock data during the
# after hours trading, from 4-8pm and from 4-8am.

try:
    from urllib.request import Request, urlopen
    from lxml import html
except ImportError:
    from urllib2 import Request, urlopen
    from lxml import html


def web_connect(stock_symbol, market):
    """ Opens a web connection to a market with a stock_symbol

        Pfarams:
            stock_symbol: NYSE et. al stock symbol
            market: which market chart should be returned

        Retruns:
            tree: a tree containing the extracted html of the webpage response
    """
    url = 'http://www.nasdaq.com/symbol/%s/%s' % (stock_symbol, market)
    req = Request(url)
    resp = urlopen(req)
    response = resp.read().decode('utf-8').strip()
    tree = html.fromstring(response)
    return tree


# Pre_current method retrieves the latest pre-market trade price for symbol
def pre_latest(stock_symbol):
    """ Get's the latest pre makert trade price

        Params:
            stock_symbol: NYSE et. al stock symbol

        Returns:
            (stock_symbol, price: the stock's price)
    """
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
    """ Returns the highest pre-market price for the given stock

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            price: The premarket high price
            time: The time at which the price occured
    """
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

def pre_low(stock_symbol):
    """ Retrieves the lowest pre-market trade price for given symbol

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            price: The premarket low price
            time: The time at which the price occured
    """
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



def pre_volume(stock_symbol):
    """ Returns the total volume for pre market trading for given symbol

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            volume: the volume of trading for the given stock

    """
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


def pre_all(stock_symbol):
    """ Retrieves all after-hours trading prices, times, and volume data

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            price: The premarket prices
            time: The time at which the price occured
            volume: the volume of trading for the given stock

    """
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


def pre_market_avg(stock_symbol):
    """ Calculates the average pre market trading price

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            average: the average pre market trading price

    """
    try:
        stock_symbol = stock_symbol.lower()
        test = pre_all(stock_symbol)
        test = test[2]
        price_count = len(test)
        if price_count < 1:
            raise ValueError("Calculating the mean requires "
                             "at least one data point")
        return stock_symbol, sum(test) / price_count
    except:
        print("there was an error processing your request which could be due "
              "to no pre-market data being available at this time")


def pre_market_sse(stock_symbol):
    """ Calculates the sum of square deviations for symbol

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            sum_of_squares: sum of square deviations for symbol

    """
    try:
        stock_symbol = stock_symbol.lower()
        premarket_prices = pre_all(stock_symbol)
        premarket_prices = premarket_prices[2]
        mean = pre_market_avg(stock_symbol)
        mean = mean[1]
        sum_of_squares = sum((price-mean)**2 for price in premarket_prices)
        return stock_symbol, sum_of_squares
    except:
        print("there was an error processing your request which could be due "
              "to no pre-market data being available at this time")


def pre_market_sd(stock_symbol):
    """ Calculates the standard deviation for pre-market prices for symbol

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            stdev: the standard deviation of the stock prices

    """
    try:
        stock_symbol = stock_symbol.lower()
        test = pre_all(stock_symbol)
        test = test[2]
        price_count = len(test)
        if price_count < 2:
            raise ValueError("To calculate variance you need at "
                             "least two data points")
        sum_of_squares = pre_market_sse(stock_symbol)
        sum_of_squares = sum_of_squares[1]
        pop_var = sum_of_squares / price_count
        return stock_symbol, pop_var**0.5
    except:
        print("there was an error processing your request which could be due "
              "to no pre-market data being available at this time")


def ah_latest(stock_symbol):
    """ Obtains the current after-hours trade price for given symbol

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            price: the current after-hours price

    """
    stock_symbol = stock_symbol.lower()
    tree = web_connect(stock_symbol, 'after-hours-chart')
    price = tree.xpath('//span[@id="quotes_content_left_lblLastsale"]'
                       '/text()')
    price = str(price)
    price = price[7:]
    price = price[:-2]
    try:
        price = float(price)
        return stock_symbol, price
    except:
        print('There is currently no after-market current price available '
              'for symbol %s' % stock_symbol)


def ah_high(stock_symbol):
    """ Obtains the highest after-hours trade price for given symbol.

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            price: The after-hourse high price
            time: The time at which the high occured

    """
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


def ah_low(stock_symbol):
    """ Retrieves the lowest after-hours trade price for given symbol

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            price: The after-hourse low price
            time: The time at which the low occured

    """
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


def ah_volume(stock_symbol):
    """ Retrieves the total after-hours volume for given symbol.

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            volume: the volume of trading for the given stock

    """
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


def ah_all(stock_symbol):
    """ Retrieves all after-hours trading prices, times, and volume

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            price: The premarket prices
            time: The time at which the price occured
            volume: the volume of trading for the given stock

    """
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


def ah_avg(stock_symbol):
    """ Calculates the average after hours trading price

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            average: the average price after-hours

    """
    stock_symbol = stock_symbol.lower()
    try:
        aftermarket_prices = ah_all(stock_symbol)
        aftermarket_prices = aftermarket_prices[2]
        price_count = len(aftermarket_prices)
        if price_count < 1:
            raise ValueError("Calculating the mean requires "
                             "at least one data point")
        return stock_symbol, sum(aftermarket_prices) / price_count
    except:
        print("there was an error processing your request which could be due "
              "to no after-hours data being available at this time")



def ah_sse(stock_symbol):
    """ Calculates the sum of square deviations for symbol in after-hours trading

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            sum_of_squares: sum of square deviations for symbol

    """
    stock_symbol = stock_symbol.lower()
    try:
        aftermarket_prices = ah_all(stock_symbol)
        aftermarket_prices = aftermarket_prices[2]
        mean = ah_avg(stock_symbol)
        mean = mean[1]
        sum_of_squares = sum((x-mean)**2 for x in aftermarket_prices)
        return stock_symbol, sum_of_squares
    except:
        print("there was an error processing your request which could be due "
              "to no after-hours data being available at this time")


# ah_sd returns the standard deviation for prices in the
# after hours market
def ah_sd(stock_symbol):
    """ Desc.

        Params:
            stock_symbol: NYSE et. al stock symbol

        Retruns:
            stock_symbol: Same as above
            sd: the standard deviation in stock prices

    """
    stock_symbol = stock_symbol.lower()
    try:
        aftermarket_prices = ah_all(stock_symbol)
        aftermarket_prices = aftermarket_prices[2]
        price_count = len(aftermarket_prices)
        if price_count < 2:
            raise ValueError("To calculate variance you need at "
                             "least two data points")
        sum_of_squares = ah_sse(stock_symbol)
        sum_of_squares = sum_of_squares[1]
        pop_var = sum_of_squares / price_count
        return stock_symbol, pop_var**0.5
    except:
        print("there was an error processing your request which could be due "
              "to no after-hours data being available at this time")
