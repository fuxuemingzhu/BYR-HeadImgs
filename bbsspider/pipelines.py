import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ImagePipeline(ImagesPipeline):  # 继承ImagesPipeline这个类，实现这个功能

    def get_media_requests(self, item, info):  # 重写ImagesPipeline   get_media_requests方法
        '''
        :param item:
        :param info:
        :return:
        在工作流程中可以看到，
        管道会得到文件的URL并从项目中下载。
        为了这么做，你需要重写 get_media_requests() 方法，
        并对各个图片URL返回一个Request:
        '''
        for i, image_url in enumerate(item['avatarUrls']):
            yield scrapy.Request(image_url)

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return '%s' % (image_guid)
