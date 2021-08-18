# SCRAPE SWAP.GG
Get the name and price information of the csgo inventory

## Features

-   Clean
-   Fast (>500 request/sec on a single core)
-   Manages request delays and maximum concurrency per domain
-   Automatic cookie and session handling
-   Sync/async/parallel scraping
-   Caching
-   Automatic encoding of non-unicode responses
-   Robots.txt support
-   Distributed scraping
-   Configuration via environment variables
-   Extensions

## Prerequisites

Before you continue, ensure you meet the following requirements:

* You have installed the latest version of Python.
* You are using a Windows, Linux or Mac OS machine.

## Installation

Add library with `requirements.txt` file:

```cmd
pip install -r requirements.txt
```

## Usage
- 730 is CSOGO id app
- 570 is DOTA2 id app
```cmd
scrapy crawl csgoItem -a app_id=730 -O csgoItem.csv
```

## Donate
Liked some of my work? Buy me a coffee (or more likely a beer)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/toannh8)