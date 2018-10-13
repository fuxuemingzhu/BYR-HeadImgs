# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArtItem(scrapy.Item):
    url = scrapy.Field()
    avatarUrls = scrapy.Field()
    userName = scrapy.Field()
