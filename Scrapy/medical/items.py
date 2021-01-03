# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MedicalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    p_classify = scrapy.Field()
    #p_href1 = scrapy.Field()
    #p_href2 = scrapy.Field()
    #p_href3 = scrapy.Field()
    p_title = scrapy.Field()
    p_qdetail1 = scrapy.Field()
    p_qdetail2 = scrapy.Field()
    p_qdetail3 = scrapy.Field()
    p_answer1 = scrapy.Field()
    p_answer2 = scrapy.Field()
