# -*- coding: utf-8 -*-
import csv
import glob
import os.path
from openpyxl import Workbook

from scrapy.spiders import Spider


class CsgoitemSpider(Spider):
    name = 'csgoItem'
    allowed_domains = ['swap.gg']
    start_urls = ['https://api.swap.gg/inventory/bot/730?sort=CHEAPEST_FIRST']

    def parse(self, response):
        result = response.json()["result"]

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
