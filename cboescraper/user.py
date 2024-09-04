from cboescraper import scraper
from cboescraper import loader
import os
import datetime


def check_save_tickers(tickers, downloads, base, date):
    if not isinstance(tickers, list):
        print("Error: tickers must be a list of strings.")
        return False
    for ticker in tickers:
        if not isinstance(ticker, str):
            print("Error: " + ticker + " in tickers must be a string.")
            return False
    if not os.path.isdir(downloads):
        print("Error: downloads must be a valid directory.")
        return False
    if not os.path.isdir(base):
        print("Error: base must be a valid directory.")
        return False
    if not isinstance(date, datetime.datetime):
        print("Error: date must be a datetime.datetime object.")
        return False
    return True


def save_tickers(tickers, downloads, base, date):
    if not check_save_tickers(tickers, downloads, base, date):
        return
    failed = scraper.download_tickers(tickers, downloads)
    for ticker in tickers:
        if ticker not in failed:
            df = loader.load_csv(ticker, downloads)
            loader.save_df(ticker, df, base, date)
        else:
            print("Failed to get data for " + ticker + ".")


def check_load_ticker(ticker, base, date):
    if not isinstance(ticker, str):
        print("Error: ticker must be a string")
        return False
    if not os.path.isdir(base):
        print("Error: base must be a valid directory.")
        return False
    if not isinstance(date, datetime.datetime):
        print("Error: date must be a datetime.datetime object.")
        return False
    return True


def load_ticker(ticker, base, date):
    if not check_load_ticker(ticker, base, date):
        return
    return loader.read_df(ticker, base, date)
