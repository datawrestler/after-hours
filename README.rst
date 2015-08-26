

********************************
Read me for after_hours module
********************************

Python module after_hours can retrieve pre-market prices and after-hours trading prices from Nasdaq for a given stock symbol

-Created by Jason Lewris

-License: GNU LGPLv2+

-Developer Home Page: 'https://github.com/datawrestler <https://github.com/datawrestler>'_

----


Requirements
--------------
Python 2.7/3.4

Method Overview
----------------

                                    +--------------------------------------+--------------------------------------+
                                    |       Method Name                    |          Description                 |
                                    +======================================+======================================+
                                    |       pre_latest                     | Returns latest pre market price      |
                                    +--------------------------------------+--------------------------------------+
                                    |       pre_high                       | Returns high pre market price        |
                                    +--------------------------------------+--------------------------------------+
                                    |       pre_low                        | Returns low pre market price         |
                                    +--------------------------------------+--------------------------------------+
                                    |       pre_volume                     | Returns volume pre market price      |
                                    +--------------------------------------+--------------------------------------+
                                    |       pre_market_avg                 | Returns avg pre market prices        |
                                    +--------------------------------------+--------------------------------------+
                                    |       pre_market_sse                 | pre market standard sqaure error     |
                                    +--------------------------------------+--------------------------------------+
                                    |       pre_market_sd                  | pre market standard deviation        |
                                    +--------------------------------------+--------------------------------------+
                                    |       ah_latest                      | Returns latest after hours price     |
                                    +--------------------------------------+--------------------------------------+
                                    |       ah_high                        | Returns high after hours price       |
                                    +--------------------------------------+--------------------------------------+
                                    |       ah_low                         | Returns low after hours price        |
                                    +--------------------------------------+--------------------------------------+
                                    |       ah_volume                      | Returns after hours volume           |
                                    +--------------------------------------+--------------------------------------+
                                    |       ah_all                         | Returns all after hours prices       |
                                    +--------------------------------------+--------------------------------------+
                                    |       ah_avg                         | Returns after hours average price    |
                                    +--------------------------------------+--------------------------------------+
                                    |       ah_sse                         | After hours standard sqaure error    |
                                    +--------------------------------------+--------------------------------------+
                                    |       ah_sd                          | After hours standard deviation       |
                                    +--------------------------------------+--------------------------------------+

Installation
**************

Installation is done using pip install:

    .. code-block::

        pip install after_hours

Alternative installation can be done by downloading the source files directly from github, navigating to the directory through terminal and running the following:

    .. code-block::

        python setup.py


After installation, the package is ready for use. Simply import it into your python script with the following:

    .. code-block::

        import after_hours


Examples
---------

    .. code-block::

        >>> import after_hours
        >>> print(after_hours.ah_latest('aapl'))
            ('aapl', 102.18)

        >>> print(after_hours.ah_high('aapl'))
            ('aapl', 109.055, '16:09:59 PM')

        >>> print(after_hours.ah_low('aapl'))
            ('aapl', 102.1, '19:58:46 PM')

        >>> print(after_hours.ah_volume('aapl'))
            ('aapl', '2,140,117')

        >>> print(after_hours.ah_all('aapl'))
            ('aapl', ['19:59', '19:57', '19:53'], [102.18, 102.16, 102.11], ['100', '10', '10']

        >>> print(after_hours.ah_avg('aapl'))
            ('aapl', 102.22793048

        >>> print(after_hours.ah_sse('aapl'))
            ('aapl', 0.572312)

        >>> print(after_hours.ah_sd('aapl'))
            ('aapl', 0.0835429)





