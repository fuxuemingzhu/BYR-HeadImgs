#!/usr/bin/env python
# coding=utf-8

from bbsspider.items import ArtItem
import bbsspider.spiders.const as const
from collections import defaultdict
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import scrapy
import PIL.Image as Image
import math
import os


class Article(scrapy.Spider):
    name = 'article'
    start_urls = const.ALLOW_DOMAINS
    article_urls = ['https://bbs.byr.cn/#!article/Picture/3208312']
    headers = const.HEADERS
    all_articles = defaultdict(list)

    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        print(self.all_articles)
        with open('all_articles_users.txt', 'w') as f:
            f.write(str(dict(self.all_articles)))
        if not os.path.exists('./headImages'):
            os.mkdir('./headImages')
        for art, users in self.all_articles.items():
            users_len = len(users)
            per = 133
            rows = 133  # 图片大小+图片间隔
            toImage = Image.new('RGBA', (133 * 10, 133 * math.ceil(users_len / 10)), (255, 255, 255))
            ys = int(math.ceil(users_len / 10))
            for y in range(0, ys):
                for x in range(0, 10):
                    if 10 * y + x >= users_len:
                        break
                    fname = "images/%s" % users[10 * y + x].split('/')[-1]
                    img = Image.open(fname)
                    img.thumbnail((125, 125))
                    toImage.paste(img, (x * rows, y * rows))
            toImage.save('./headImages/%s.png' % art.split('/')[-1])
            print(art + '\tsave image success!')

    def parse(self, response):
        cur_page_url = response._get_url()
        avatarUrls = response.css('div.b-content table.article div.a-u-img ::attr(src)').extract()
        motherurl = cur_page_url.split('?')[0]
        if const.removeDuplicate:
            for avatarUrl in avatarUrls:
                if avatarUrl not in self.all_articles[motherurl]:
                    self.all_articles[motherurl].append(avatarUrl)
        else:
            self.all_articles[motherurl].extend(avatarUrls)
        item = ArtItem()
        item['url'] = motherurl
        item['avatarUrls'] = avatarUrls
        print(item)
        yield item
        sel_page = response.css('div.t-pre ul.pagination li ol')
        cur_page_num = sel_page.css('li.page-select > a::text').extract()
        page_list_num = sel_page.css('li.page-normal > a::text').extract()
        page_list_url = sel_page.css('li.page-normal > a::attr(href)').extract()
        print('cur page is %s' % cur_page_num[0])
        if len(page_list_url) > len(page_list_num):
            pre_page_num = '%d' % (int(cur_page_num[0]) - 1)
            page_list_num.insert(0, pre_page_num)
        for idx, num in enumerate(page_list_num):
            print('%d,%s,%s' % (idx, page_list_num[idx], page_list_url[idx]))
            if page_list_num[idx] == '>>':
                next_url = response.urljoin(page_list_url[idx])
                print('crawl next article page [%s]' % next_url)
                yield scrapy.Request(next_url, meta={'cookiejar': response.meta['cookiejar']}, headers=self.headers,
                                     callback=self.parse)

    def start_requests(self):
        return [scrapy.FormRequest("http://bbs.byr.cn/user/ajax_login.json",
                                   formdata=const.LOGIN_DATA,
                                   meta={'cookiejar': 1},
                                   headers=self.headers,
                                   callback=self.get_articles)]

    def get_articles(self, response):
        self.article_urls = map(lambda x: x.replace('#!', ''), self.article_urls)
        for url in self.article_urls:
            yield scrapy.Request(url, meta={'cookiejar': response.meta['cookiejar']}, headers=self.headers,
                                 callback=self.parse)
