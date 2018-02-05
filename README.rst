

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
        >>> AH = AfterHours('aapl', typeof = 'after')
        >>> print(AH.getdata(datatype='lowprice'))
                102.18

        >>> print(AH.getdata(datatype='highprice'))
            109.055

        >>> print(AH.getdata(datatype='hightime'))
            '12/15/2017 18:58:46 PM'

        >>> print(AH.getdata(datatype='lowtime'))
            '12/15/2017 19:58:46 PM'

        >>> print(AH.secure_all())
            Pandas DataFrame






        >>> AH = AfterHours('aapl', typeof='pre')
        >>> print(AH.getdata(datatype='lowprice'))
                102.18

        >>> print(AH.getdata(datatype='highprice'))
            109.055

        >>> print(AH.getdata(datatype='lowtime'))
            '12/15/2017 18:58:46 PM'

        >>> print(AH.getdata(datatype='hightime'))
            '12/15/2017 19:58:46 PM'

        >>> print(AH.secure_all())
            Pandas DataFrame





