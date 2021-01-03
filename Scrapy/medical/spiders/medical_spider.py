# -*- coding: utf-8 -*-
import scrapy
from medical.items import MedicalItem

class DMedicalSpiderSpider(scrapy.Spider):
	name = 'medical_spider'
	allowed_domains = ['zzk.xywy.com']
	start_urls = ['http://zzk.xywy.com/p/yanke.html']

	def parse(self, response):
		movie_list = response.xpath("//div[@class='fl jblist-con-ill']/div[contains(@class,'ks-ill-txt')]/ul/li")
		for i_item in movie_list:
			medical_item = MedicalItem()
			medical_item['p_classify'] = i_item.xpath(".//a/text()").extract_first()
			#medical_item['p_href1'] = i_item.xpath(".//a/@href").extract()
			if i_item.xpath(".//a/@href").extract():
				next_link0 = "http://zzk.xywy.com"+i_item.xpath(".//a/@href").extract()[0]
				yield scrapy.Request(next_link0,meta={'medical_item':medical_item},callback=self.detail_parse)

	#进入科室，获取问答板块连接
	def detail_parse(self,response):
		medical_item = response.meta['medical_item']
		#medical_item['p_href2'] = response.xpath("//div[@class='wrap mt5']/ul/li[3]/a/@href").extract()
		if response.xpath("//div[@class='wrap mt5']/ul/li[3]/a/@href").extract():
			next_link = "http://zzk.xywy.com/"+response.xpath("//div[@class='wrap mt5']/ul/li[3]/a/@href").extract()[0]
			yield scrapy.Request(next_link,meta={'medical_item':medical_item},callback=self.detail_parse2)

	#进入问答板块，获取每个问答的详情网址
	def detail_parse2(self,response):
		medical_item = response.meta['medical_item']
		new_list = response.xpath("//div[@class='doct-answer-box']/div[contains(@class,'pb10')]")

		for i in new_list:
			#medical_item['p_href3'] = i.xpath(".//div[1]/p/a/@href").extract()
			next_link2 = i.xpath(".//div[1]/p/a/@href").extract()[0]
			if 'http' in next_link2:
				yield scrapy.Request(next_link2,meta={'medical_item':medical_item},callback=self.detail_parse3, dont_filter=True)

	#进入问答详细页面，获取具体问答信息
	def detail_parse3(self,response):
		medical_item = response.meta['medical_item']
		medical_item['p_title'] = response.xpath("//div[@class='club-topbox']/div[1]/div[1]/text()").extract()
		medical_item['p_qdetail1'] = response.xpath("//div[@id='qdetailc']/text()").extract()
		medical_item['p_qdetail2'] = response.xpath("//div[@id='qdetailc']/p[1]/text()").extract_first()
		medical_item['p_qdetail3'] = response.xpath("//div[@id='qdetailc']/p[2]/text()").extract_first()
		medical_item['p_answer1'] = response.xpath("//div[@class='docall clearfix '][1]/div[2]/div[2]/div[1]/text()").extract_first()
		medical_item['p_answer2'] = response.xpath("//div[@class='docall clearfix '][2]/div[2]/div[2]/div[1]/text()").extract_first()

		return medical_item
				
