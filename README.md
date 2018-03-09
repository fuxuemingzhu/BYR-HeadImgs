# 北邮人论坛用户合影

一键合成北邮人论坛十大&主题帖所有回复头像合影

![此处输入图片的描述][1]
上图源自该贴的所有用户头像：你有一个研一小哥哥，请查收~ https://bbs.byr.cn/#!article/Friends/1858656

![此处输入图片的描述][2]
上图来自：十大合影～ https://bbs.byr.cn/#!article/Picture/3208312

# 使用环境

下面的环境请自行安装：

1. python3

2. scrapy

3. PIL

# 使用方法

1. 在bbsspider/spiders/const.py中填写你的byr bbs**用户名密码**。

2. 在本项目根目录（与scrapy.cfg同目录），运行命令：


```bash
scrapy crawl topten
```

自动把十大的十篇文章爬取，并生成用户合影。

或：

修改bbsspider/spiders/bbsarticle.py中的article_urls为要进行操作的文章地址列表，然后运行命令：

```bash
scrapy crawl article
```

生成指定帖子的用户合影。

程序运行后，在headImages目录下生成了合影，命名方式为帖子地址结尾的数字。

# 版权声明

1. 本项目为业余开发，代码质量不高。大家随便使用，欢迎交流。

2. 所有代码都在你自己的本地运行，我不会收集论坛密码～

3. 感谢前辈写的论坛爬虫：https://github.com/buptbill220/bbsspider


  [1]: https://raw.githubusercontent.com/fuxuemingzhu/BYR-HeadImgs/master/headImages/1858656.png
  [2]: https://raw.githubusercontent.com/fuxuemingzhu/BYR-HeadImgs/master/headImages/3208312.png