# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewhouseItem(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 规模
    size = scrapy.Field()
    # 房价
    price = scrapy.Field()
    # 几居
    rooms = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 是否在售
    sale = scrapy.Field()
    # 标签
    tag = scrapy.Field()
    # 页面
    origin_url = scrapy.Field()

class ErshouItem(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 几室几厅
    rooms = scrapy.Field()
    # 几层
    floor = scrapy.Field()
    # 面积
    size = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 年代
    year = scrapy.Field()
    # 全价
    all_price = scrapy.Field()
    # 多少钱一平米
    price = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 标签
    tag = scrapy.Field()
    # 页面
    origin_url = scrapy.Field()
