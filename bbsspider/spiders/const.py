#!/usr/bin/env python
# coding=utf-8
URL = 'http://bbs.byr.cn'
ALLOW_DOMAINS = ['bbs.byr.cn']
HEADERS = {'User-Agent': 'Mozilla/5.0', 'Host': 'bbs.byr.cn', 'X-Requested-With': 'XMLHttpRequest',
           'Connection': 'keep-alive'}
# 请修改为你自己的用户名id和密码passwd，其他不用修改，提交代码的时候记得抹掉密码 =. =
LOGIN_DATA = {'id': 'fuxuemingzhu', 'passwd': '*********', 'mode': '0', 'CookieDate': '0'}
DB_CONFIG = {'host': '127.0.0.1', 'user': 'root', 'passwd': '123456', 'db': 'bbs', 'port': 3306, 'charset': 'utf8',
             'timeout': 5}
