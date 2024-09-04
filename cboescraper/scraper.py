from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from cboescraper import elements
import os


CBOE_FILE_ENDING = "_quotedata"


def _ticker_format(ticker):
    return ticker.lower().replace("-", ".")


def _tickers_format(tickers):
    tickers_new = []
    for i in range(0, len(tickers)):
        tickers_new.append(_ticker_format(tickers[i]))
    return tickers_new


class Driver:
    def __init__(self):
        self.driver = Chrome()
        self.driver.maximize_window()

    def __del__(self):
        self.driver.quit()

    def _get_ticker(self, ticker):
        LINK1 = "https://www.cboe.com/delayed_quotes/"
        LINK2 = "/quote_table"
        url = LINK1 + ticker + LINK2
        self.driver.get(url)

    def _find_selectors(self):
        self.selectors = self.driver.find_elements(
            By.CLASS_NAME, elements.SELECTOR_CLASS
        )

    def _scroll_element_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("window.scrollBy(0,-100)")

    def _set_selectors(self):
        for selector in self.selectors:
            input = selector.find_element(By.CLASS_NAME, elements.INPUT_CONTAINER)
            self._scroll_element_into_view(input)
            input.send_keys("All")
            input.send_keys(Keys.ENTER)

    def _view_chain(self, wait_time=0.3):
        button = self.driver.find_element(By.CLASS_NAME, elements.VIEW_CHAIN_BUTTON)
        self._scroll_element_into_view(button)
        button.click()
        time.sleep(wait_time)

    def _download(self):
        link = self.driver.find_element(By.CLASS_NAME, elements.DOWNLOAD_LINK)
        self._scroll_element_into_view(link)
        link.click()

    def download_ticker(self, ticker, load_time):
        print("Downloading " + ticker + " ...")
        self._get_ticker(ticker)
        self._find_selectors()
        self._set_selectors()
        self._view_chain(load_time)
        self._download()


def download_path(ticker, downloads):
    return downloads + ticker + CBOE_FILE_ENDING + ".csv"


def _exists(ticker, downloads):
    path = download_path(ticker, downloads)
    return os.path.exists(path)


def _apt_size(ticker, downloads, size):
    path = download_path(ticker, downloads)
    return os.path.getsize(path) > size


def rm_downloads(ticker, downloads):
    path = download_path(ticker, downloads)
    os.remove(path)


def _download_tickers(driver, tickers, load_time):
    for ticker in tickers:
        try:
            driver.download_ticker(ticker, load_time)
        except:
            pass


KB = 1024
MB = 1024 * KB
APT_SIZE = 10 * KB


def _failed(tickers, downloads):
    failed = []
    for ticker in tickers:
        if not _exists(ticker, downloads):
            failed.append(ticker)
            print("Failed to download " + ticker + ".")
        elif not _apt_size(ticker, downloads, APT_SIZE):
            rm_downloads(ticker, downloads)
            failed.append(ticker)
            print("Failed to download " + ticker + ".")
    return failed


LOAD_FAST = 0.5
LOAD_SLOW = 3

DOWNLOAD_WAIT_TIME = 5


def download_tickers(tickers, downloads):
    tickers = _tickers_format(tickers.copy())
    driver = Driver()
    _download_tickers(driver, tickers, LOAD_FAST)
    time.sleep(DOWNLOAD_WAIT_TIME)
    failed = _failed(tickers, downloads)
    _download_tickers(driver, failed, LOAD_SLOW)
    time.sleep(DOWNLOAD_WAIT_TIME)
    failed = _failed(failed, downloads)
    return failed
