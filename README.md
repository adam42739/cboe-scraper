# cboe-scraper

## Introduction

cboe-scraper uses [Selenium](https://selenium-python.readthedocs.io) to download options data from [cboe.com](https://www.cboe.com). CBOE does not offer free historical options data, but cboe-scraper can be run regularly to get and store current options data in CSV format.

## Requirements

* `Python 3.10.14`

* `pandas: 2.2.2`

* `selenium: 4.24.0`
    
    * A recent version of Google Chrome installed on your system.

## Usage

```python
import cboescraper as options
```

### Saving options data to a directory

```python
options.save_tickers(tickers, downloads, base, date)
```

#### Parameters

> **`tickers`: _list_**

List of tickers to grab data for.

> **`downloads`: _str_**

Path to the directory where Chrome downloads files.

> **`base`: _str_**

Path to the directory where data files will be stored.

> **`date`: _datetime_**

Datetime object for the current date. Not relavent for data collection - only used to label data files stored in `base`.

### Loading data files

```python
options.load_ticker(ticker, base, date)
```

#### Parameters

> **`ticker`: _str_**

The ticker to grab data for.

> **`base`: _str_**

Path to the directory where data files are stored.

> **`date`: _datetime_**

Datetime object for the date to grab the options.
