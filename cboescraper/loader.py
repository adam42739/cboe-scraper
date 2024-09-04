import pandas
from cboescraper import scraper
import datetime
import os


CSV_COLS_KEEP = {
    "Expiration Date": "Expiration",
    "Bid": "Call Bid",
    "Ask": "Call Ask",
    "Volume": "Call Volume",
    "Open Interest": "Open Interest",
    "Strike": "Strike",
    "Bid.1": "Put Bid",
    "Ask.1": "Put Ask",
    "Volume.1": "Put Volume",
    "Open Interest.1": "Put Open Interest",
}


def load_csv(ticker, downloads):
    path = scraper.download_path(ticker, downloads)
    df = pandas.read_csv(path, header=2)
    df = df[CSV_COLS_KEEP.keys()]
    df = df.rename(CSV_COLS_KEEP, axis="columns")
    scraper.rm_downloads(ticker, downloads)
    return df


def save_df(ticker, df, base, date):
    date_string = datetime.datetime.strftime(date, "%Y-%m-%d")
    path = base + ticker + "=" + date_string + ".csv"
    df.to_csv(path)


def read_df(ticker, base, date):
    date_string = datetime.datetime.strftime(date, "%Y-%m-%d")
    path = base + ticker + "=" + date_string + ".csv"
    if not os.path.exists(path):
        print("Error: " + path + " does not exist.")
    return pandas.read_csv(path)
