# 北邮人论坛用户合影

一键合成北邮人论坛十大&主题帖所有回复头像合影～～

现已支持生成合影时的用户头像去重功能。

未对用户去重的合影如下，每行头像代表了帖子的一页：
![此处输入图片的描述][1]
上图源自该贴的所有用户头像：你有一个研一小哥哥，请查收~ https://bbs.byr.cn/#!article/Friends/1858656

对用户去重的合影如下，顺序依然是按照回复帖子的顺序：
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

3. 程序运行后，在headImages目录下生成了合影，命名方式为帖子地址结尾的数字。

注：bbsspider/spiders/const.py中removeDuplicate变量控制是否对用户头像去重，当其为True时去重，为False时不去重。默认不去重。

# 版权声明

1. 本项目为业余开发，代码质量不高。大家随便使用，欢迎交流。

2. 所有代码都在你自己的本地运行，我不会收集论坛密码～

3. 感谢前辈写的论坛爬虫：https://github.com/buptbill220/bbsspider


  [1]: https://raw.githubusercontent.com/fuxuemingzhu/BYR-HeadImgs/master/examples/1858656.png
  [2]: https://github.com/fuxuemingzhu/BYR-HeadImgs/blob/592ae4a7683bbfcc200d5e03410d07c207624795/examples/3208312.png?raw=true