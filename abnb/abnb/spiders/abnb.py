# -*- coding: utf-8 -*-

import scrapy
import sys
from scrapy.linkextractors import LinkExtractor
from items import AbnbItem
from scrapy.spiders import Rule, CrawlSpider


reload(sys)
sys.setdefaultencoding('utf-8')

QUERY = 'Chengdu--Sichuan--China'


class MySpider(scrapy.Spider):
	name = "abnb"
	allowed_domains = ["airbnb.com/rooms"]
	next_page_domain = ['https://www.airbnb.com/s/Chengdu--Sichuan--China/homes']

	start_urls = ['https://www.airbnb.com/s/'+QUERY]
	print start_urls
	next_page = 'https://www.airbnb.com/s/Chengdu--Sichuan--China/homes?allow_override%5B%5D=&place_id=ChIJIXdEACPF7zYRAg4kLs5Shrk&refinement_paths%5B%5D=%2Ffor_you&s_tag=MH0aE2dZ&section_offset='
	# rules = [Rule(LinkExtractor(canonicalize=True,unique=True),follow=True,callback="parse_items")]
	# start the request
	# def start_requests(self):
	# 	for url in self.start_urls:
	# 		print url
	# 		yield scrapy.Request(url, callback=self.parse, dont_filter=True)
    # visit each page then move to the next page 
	# Get page number 
	def last_page(self,response):
		page_number = 0
		links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
		for link in links:
		# Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
			print link
			is_allowed = False
			for allowed_domain in self.allowed_domains:
				if allowed_domain in link.url:
					is_allowed = True
					if is_allowed:
						page_number +=1
		return page_number


	def parse_rule(self,response):
		pn = last_page(response)
			items = []
			links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
			for link in links:
			# Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
				print link
				is_allowed = False
				for allowed_domain in self.allowed_domains:
					if allowed_domain in link.url:
						is_allowed = True
						if is_allowed:
							yield scrapy.Request(link.url, callback=self.parse, dont_filter=True)
		# Return all the found items
	def parse(self, response):
		item = AbnbItem()
		title = response.css('title::text')[0].extract()
		print title
		item['title'] = title.encode('utf-8')
		item['url'] = response.url 
		yield item

# # Now I learned to create Item, building pipe line, the next step is to learn with navigation rule

