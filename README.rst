

********************************
Read me for after_hours module
********************************

Python module after_hours can retrieve pre-market prices and after-hours trading prices from Nasdaq for a given stock symbol

-Created by Jason Lewris

-License: The MIT License

-Developer Home Page: 'https://github.com/datawrestler'.

----


Requirements
--------------
Python 2.7/3.4+

Method Overview
----------------

                                    +--------------------------------------+--------------------------------------+
                                    |       Method Name                    |          Description                 |
                                    +======================================+======================================+
                                    |       AH.high()                      | Returns high market price            |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.low()                       | Returns low market price             |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.volume()                    | Returns total market volume          |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.hightime()                  | Returns datetime of high price       |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.lowtime()                   | Returns datetime of low price        |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.mkt_close()                 | Returns market close price           |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.secure_all()                | Returns dataframe with all activity  |
                                    +--------------------------------------+--------------------------------------+
                                    |       AH.run_every()                 | Updates all data points continuosly  |
                                    +--------------------------------------+--------------------------------------+


Installation
**************

Installation is done using pip install:

    .. code-block::

        pip install after_hours

Alternative installation can be done by downloading the source files directly from github, navigating to the directory through terminal and running the following:

    .. code-block::

        python setup.py install

    .. note:: The source file can be downloaded here: https://github.com/datawrestler/after-hours/tarball/0.1.1


After installation, the package is ready for use. Simply import it into your python script with the following:

    .. code-block::

        import after_hours


Examples
---------

    .. code-block::


from afterhours import after_hours
        >>> AH = AfterHours('aapl', typeof = 'pre')
        >>> print(AH.high())
                102.18

        >>> print(AH.low())
            109.055

        >>> print(AH.hightime())
            '12/15/2017 18:58:46 PM'

        >>> print(AH.lowtime())
            '12/15/2017 19:58:46 PM'

        >>> print(AH.secure_all())
            Pandas DataFrame






        >>> AH = AfterHours('aapl', typeof = 'pre')
        >>> print(AH.high())
                102.18

        >>> print(AH.low())
            109.055

        >>> print(AH.hightime())
            '12/15/2017 18:58:46 PM'

        >>> print(AH.lowtime())
            '12/15/2017 19:58:46 PM'

        >>> print(AH.secure_all())
            Pandas DataFrame





