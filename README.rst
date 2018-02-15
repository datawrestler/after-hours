.. image:: https://travis-ci.org/datawrestler/after-hours.svg?branch=master
    :target: https://travis-ci.org/datawrestler/after-hours

.. image:: https://badge.fury.io/py/afterhours.svg
    :target: https://badge.fury.io/py/afterhours

.. image:: https://img.shields.io/badge/python-2.7-blue.svg
    :target: https://badge.fury.io/py/afterhours

.. image:: https://img.shields.io/badge/python-3.5-blue.svg
    :target: https://badge.fury.io/py/afterhours

.. image:: https://img.shields.io/badge/python-3.6-blue.svg
    :target: https://badge.fury.io/py/afterhours


********************************
Read me for afterhours package
********************************

Python module afterhours can retrieve pre-market and after-hours trading prices from Nasdaq for a given stock symbol

-Created by Jason Lewris

-License: The MIT License

-Developer Home Page: 'https://github.com/datawrestler'

----


Dependencies
~~~~~~~~~~~~~~~
- Python (>=2.6 or >= 3.5)
- beautifulsoup4 (>= 4.6.0)
- requests (>= 2.18.4)
- pandas (>= 0.20.3)
- lxml (>= 4.1.0)

Valuable Links
~~~~~~~~~~~~~~~~
- Official source code repo: https://github.com/datawrestler/after-hours
- Issue tracking: https://github.com/datawrestler/after-hours/issues
- Download releases: https://pypi.python.org/pypi/afterhours

Method Overview
----------------

                                    +--------------------------------------+--------------------------------------+
                                    |       Method Name                    |          Description                 |
                                    +======================================+======================================+
                                    |       AH.getdata(datatype='highprice)| Returns high market price            |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.getdata(datatype='lowprice')| Returns low market price             |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.getdata(datatype='volume')  | Returns total market volume          |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.getdata(datatype='hightime')| Returns datetime of high price       |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.getdata(datatype='lowtime') | Returns datetime of low price        |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.getdata(datatype='mktclose')| Returns market close price           |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.secure_all()                | Returns dataframe with all activity  |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.run_every()                 | Updates all data points continuosly  |
                                    +--------------------------------------+--------------------------------------+


Installation
**************

Installation is done using pip install:

    .. code-block::

        pip install afterhours

Alternative installation can be done by downloading the source files directly from github, navigating to the directory through terminal and running the following:

    .. code-block:: python

        python setup.py install

    .. note:: The source file can be downloaded here: https://github.com/datawrestler/after-hours/tarball/0.2.1


After installation, the package is ready for use. Simply import it into your python script with the following:

    .. code-block:: python

        from afterhours.afterhours import AfterHours


Source
~~~~~~~~~~~~

The latest source code can be checked out with the following command:

    .. code-block::
    git clone https://github.com/datawrestler/after-hours.git


Examples
~~~~~~~~~~~~

.. code-block:: python

        from afterhours.afterhours import AfterHours

        # AFTER HOURS TRADING DATA
        AH = AfterHours('aapl', typeof = 'after')

        # get the low price from after hours trading
        print(AH.getdata(datatype='lowprice'))
        # 102.18

        # get the high price of after hours trading
        print(AH.getdata(datatype='highprice'))
        # 109.055

        # get the timestamp of after hours high trade
        print(AH.getdata(datatype='hightime'))
        # '12/15/2017 18:58:46 PM'

        print(AH.getdata(datatype='lowtime'))
        # '12/15/2017 19:58:46 PM'

        # get all data points for after hours trading
        print(AH.secure_all())
        # Pandas DataFrame

        # PRE HOURS TRADING DATA
        # get pre hours trading info for apple
        AH = AfterHours('aapl', typeof='pre')

        # get the low price from pre hours trading
        print(AH.getdata(datatype='lowprice'))
        # 102.18

        # get the high price from pre hours trading
        print(AH.getdata(datatype='highprice'))
        # 109.055

        # get the timestamp for lowest trade
        print(AH.getdata(datatype='lowtime'))
        # '12/15/2017 18:58:46 PM'

        # get the timestamp for highest time trade
        print(AH.getdata(datatype='hightime'))
        # '12/15/2017 19:58:46 PM'

        # secure all pre hours trading data
        print(AH.secure_all())
        # Pandas DataFrame

Please add any questions, comments, concerns to the issues tab on Github for the project! I look forward to seeing this package built out further in future releases.

