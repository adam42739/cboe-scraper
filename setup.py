from setuptools import setup

setup(
    name="cboescraper",
    version="0.1.0",
    description="Tool for scraping options data from cboe.com",
    url="https://github.com/adam42739/cboe-scraper",
    author="Adam Lynch",
    author_email="aclynch@umich.edu",
    license="MIT License",
    packages=["cboescraper"],
    install_requires=["pandas>=2.2.2", "selenium>=4.24.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licesnse :: MIT License",
        "Operating System :: OS Independent",
    ],
)
