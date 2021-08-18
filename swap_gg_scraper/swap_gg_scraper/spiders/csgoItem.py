# -*- coding: utf-8 -*-
import csv
import glob
import os.path
from openpyxl import Workbook
import operator

from scrapy.spiders import Spider
from scrapy.http import Request


class CsgoitemSpider(Spider):
    name = 'csgoItem'
    allowed_domains = ['swap.gg']
    start_urls = ['https://api.swap.gg/inventory/bot/730?sort=CHEAPEST_FIRST']

    def __init__(self, app_id=None):
        self.app_id = app_id

    def parse(self, response):
        yield Request('https://api.swap.gg/inventory/bot/' + self.app_id + '?sort=CHEAPEST_FIRST',
                      callback=self.parse_item)

    def parse_item(self, response):
        result = response.json()["result"]

        result.sort(key=operator.itemgetter('p'))

        newArr = []
        for i in result:
            if i["n"] not in [item["n"] for item in newArr]:
                newArr.append(i)

        for item in newArr:
            yield {
                "name": item["n"],
                "price": item["p"] / 100,
            }

    def close(spider, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)

        wb = Workbook()
        ws = wb.active

        with open(csv_file, 'r', encoding="utf8") as f:
            for row in csv.reader(f):
                ws.append(row)

        wb.save(csv_file.replace('.csv', '') + '.xlsx')
