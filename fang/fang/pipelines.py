# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter
from fang.items import NewhouseItem, ErshouItem

class FangPipeline:
    def __init__(self):
        self.newhouse_fp = open('newhouse.json', 'wb')
        self.ershouhouse_fp = open('ershouhouse.json', 'wb')
        self.newhouse_exporter = JsonLinesItemExporter(self.newhouse_fp, ensure_ascii=False)
        self.ershouhouse_exporter = JsonLinesItemExporter(self.ershouhouse_fp, ensure_ascii=False)


    def process_item(self, item, spider):
        if isinstance(item, NewhouseItem):
            self.newhouse_exporter.export_item(item)
        elif isinstance(item, ErshouItem):
            self.ershouhouse_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.newhouse_fp.close()
        self.ershouhouse_fp.close()
