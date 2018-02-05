##Read me file for AfterHours package
The goal of AfterHours is to make the process of capturing pre market and after hours trading information 
for various ticker symbols seamless. It has an intuitive, easy to use API that enables capturing of volume, 
high prices, low prices, when the high/low prices occurred, and capturing all relevant trading information simultaneously. 

The main Github repo is located [here](#https://github.com/datawrestler/after-hours)

### Installation
AfterHours is published to Github and pypi. Installation is straightforward with traditional pip installs.

```{python}
    pip install AfterHours
```

### Usage
There are numerous methods available within the AfterHours class. The API is straightforward for 
securing various bits of information related to pre/after hours trading for a particular ticker symbol.

Method Name | Method Usage | Output | Description |
--- | --- | --- | ---
*High* | AH.high() | 100.10 | High price
*Low* | AH.low() | 30.19 | Low price
*Volume* | AH.volume() | 12000 | Total volume
*High Time* | AH.hightime() | 12/15/2017 7:00PM | Time high price occured
*Low Time* | AH.lowtime() | 12/15/2017 6:00PM | Time low price occurred
*Market Close* | AH.mkt_close() | 101.67 | Market close price
*Secure All Pages* | AH.secure_all_pages() | pd.DataFrame() | Dataframe with all after/pre hours trading data
*Run Every* | AH.run_every() | Dataframe run every n seconds | Dataframe with all after/pre hours trading that updates every n seconds

The general framework for using the package can be done in the following format:

```{python}
    AH = AfterHours('appl', typeof = 'pre') # using Apple as the ticker symbol for pre market activity
    
    # capture high price
    AH.high()
    
    # capture low price
    AH.low()
    
    # Capture total volume for pre market activity
    AH.volume()
    
    # Capture datetime of high price
    AH.hightime()
    
    # Capture datetimee of low price
    AH.lowtime()
    
    # Capture market close price
    AH.mkt_close()
    
    # Capture all data points for pre market activity
    AH.secure_all()
    
    # Continuously update data points based on pre market trading activity every n seconds
    AH.run_every(seconds = 1000, num_iter = 2) # run every 1000 seconds 2 times
```
