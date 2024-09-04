import pandas
from cboescraper import scraper


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


def _load_csv(ticker, downloads):
    path = scraper.download_path(ticker, downloads)
    df = pandas.read_csv(path, header=2)
    df = df[CSV_COLS_KEEP.keys()]
    df = df.rename(CSV_COLS_KEEP, axis="columns")
    return df
