# -*- coding: utf-8 -*-
import scrapy
import re
from fang.items import NewhouseItem, ErshouItem

class SoufangwangSpider(scrapy.Spider):
    name = 'soufangwang'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        province = None
        trs = response.xpath("//div[@class='outCont']/table//tr")
        for tr in trs:
            province_text = tr.xpath("./td[2]//text()").get()
            province_text = re.sub(r'\s', '', province_text)
            cities = tr.xpath("./td[3]/a/text()").getall()
            url = tr.xpath("./td[3]/a/@href").getall()
            if province_text == '':
                province_text = province
            else:
                province = province_text
            if province_text == '其它':
                continue
            else:
                for i in range(len(cities)):
                    if cities[i] == '北京':
                        newhouse_url = 'https://newhouse.fang.com/house/s/'
                        ershou_url = 'https://esf.fang.com/'
                    else:
                        newhouse_url = ('//newhouse.'.join(url[i].split('//'))) + 'house/s'
                        ershou_url = 'esf.fang'.join(url[i].split('fang'))
                    yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={'info': (province, cities[i])})
                    yield scrapy.Request(url=ershou_url, callback=self.parse_ershou, meta={'info': (province, cities[i])})

    def parse_newhouse(self, response):
        province, city = response.meta.get('info')
        lis = response.xpath("//div[contains(@class, 'nl_con')]/ul/li[@id]")
        for li in lis:
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get().strip()
            rooms = '/'.join(li.xpath(".//div[@class='house_type clearfix']/a/text()").getall())
            size = li.xpath(".//div[@class='house_type clearfix']//text()").getall()[-1].strip('\t')\
                .strip('－').strip()
            price = ''.join(li.xpath(".//div[@class='nhouse_price']//text()").getall()).strip()
            address = li.xpath(".//div[@class='address']/a/@title").get()
            sale = li.xpath(".//div[contains(@class, 'fangyuan')]/span/text()").get()
            tag = '/'.join(li.xpath(".//div[contains(@class, 'fangyuan')]/a/text()").getall())
            origin_url = 'https:'+li.xpath(".//div[@class='nlcd_name']/a/@href").get().split('?')[0]
            item = NewhouseItem(province=province, city=city, name=name, rooms=rooms, size=size,
                                price=price, address=address, sale=sale, tag=tag, origin_url=origin_url)
            yield item

        next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse,
                                 meta={'info': (province, city)})

    def parse_ershou(self, response):
        province, city = response.meta.get('info')
        dls = response.xpath("//div[@class='shop_list shop_list_4']/dl[@id]")
        for dl in dls:
            name = dl.xpath(".//p[@class='add_shop']/a/@title").get()
            content = dl.xpath(".//p[@class='tel_shop']/text()").getall()
            rooms = content[0].strip()
            size = content[1].strip()
            floor = content[2].strip()
            toward = content[3].strip()
            year = content[4].strip()
            all_price = ''.join(dl.xpath(".//dd[@class='price_right']/span[1]//text()").getall())
            price = dl.xpath(".//dd[@class='price_right']/span[2]/text()").get()
            address = dl.xpath(".//p[@class='add_shop']/span/text()").get()
            tag = ' '.join(dl.xpath(".//p[@class='clearfix label']/span/text()").getall())
            origin_url = response.urljoin(dl.xpath(".//h4[@class='clearfix']/a/@href").get())
            item = ErshouItem(province=province, city=city, name=name, rooms=rooms, floor=floor,
                              size=size, toward=toward, year=year, all_price=all_price, price=price,
                              address=address, tag=tag, origin_url=origin_url)

            yield item

        next_url = response.xpath("//div[@class='page_al']/p/a/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_ershou,
                                 meta={'info': (province, city)})