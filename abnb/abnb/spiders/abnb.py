# -*- coding: utf-8 -*-

import scrapy
import sys
from scrapy.linkextractors import LinkExtractor
from items import AbnbItem
from scrapy.spiders import Rule, CrawlSpider
from scrapy.utils.response import open_in_browser
import json
import re
from bs4 import BeautifulSoup
import time



reload(sys)
sys.setdefaultencoding('utf-8')

QUERY = 'Chengdu--Sichuan--China'


class MySpider(scrapy.Spider):
	name = "abnb"
	allowed_domains = ["airbnb.com/rooms"]
	next_page_domain = ['https://www.airbnb.com/s/Chengdu--Sichuan--China/homes']

	start_urls = ['https://www.airbnb.com/s/Chengdu--Sichuan--China?s_tag=liQkOabl&allow_override%5B%5D=']
	visited = []
	# rules = [Rule(LinkExtractor(canonicalize=True,unique=True),follow=True,callback="parse_items")]
	# start the request
	# def start_requests(self):
	# 	for url in self.start_urls:
	# 		print url
	# 		yield scrapy.Request(url, callback=self.parse, dont_filter=True)
    # visit each page then move to the next page 
	# Get page number 

	def parse(self,response):
		links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
		page_numbers = []
		for link in links:
			if MySpider.next_page_domain[0] in link.url:
				page_numbers.append(link.text)
		print(page_numbers)
		next_page = ['https://www.airbnb.com/s/Chengdu--Sichuan--China/homes?allow_override%5B%5D=&s_tag=R69H-zV3']
		next_page_s = ['https://www.airbnb.com/s/Chengdu--Sichuan--China/homes?allow_override%5B%5D=&ne_lat=30.688247237313426&ne_lng=104.11966288655003&sw_lat=30.603382238805196&sw_lng=104.05185664265355&zoom=13&search_by_map=true&s_tag=Ife483uE&section_offset=']
		max_page_number = page_numbers[-1]
		page_urls = [next_page_s[0]+ str(pageNumber) for pageNumber in range(1, int(max_page_number))]
		next_page = next_page + page_urls
		# for i in range(1,int(max_page_number)):
		# 	next_page.append(next_page[0]+'section_offset=&'+str(i))
		for url in next_page:
			print(url)
			time.sleep(3)
			yield scrapy.Request(url,callback=self.parse_rule,dont_filter=True)
			# rooms = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
			# for room in rooms:
			# # Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
			# 	is_allowed = False
			# 	if MySpider.allowed_domains[0] in room.url:
			# 		is_allowed = True
			# 		if is_allowed:
			# 			yield scrapy.Request(room.url, callback=self.parse_page, dont_filter=True)
#https://www.airbnb.com/s/Chengdu--Sichuan--China/homes?allow_override%5B%5D=&s_tag=R69H-zV3section_offset=&10
# https://www.airbnb.com/s/Chengdu--Sichuan--China/homes?allow_override%5B%5D=&ne_lat=30.688247237313426&ne_lng=104.11966288655003&sw_lat=30.603382238805196&sw_lng=104.05185664265355&zoom=13&search_by_map=true&s_tag=Ife483uE
# https://www.airbnb.com/s/Chengdu--Sichuan--China/homes?allow_override%5B%5D=&ne_lat=30.688247237313426&ne_lng=104.11966288655003&sw_lat=30.603382238805196&sw_lng=104.05185664265355&zoom=13&search_by_map=true&s_tag=Ife483uE&section_offset=1		
# https://www.airbnb.com/s/Chengdu--Sichuan--China/homes?allow_override%5B%5D=&ne_lat=30.688247237313426&ne_lng=104.11966288655003&sw_lat=30.603382238805196&sw_lng=104.05185664265355&zoom=13&search_by_map=true&s_tag=Ife483uE&section_offset=2
	def parse_rule(self,response):
	# 	rooms = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
	# 	for room in rooms:
	# 	# Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domain
	# 		is_allowed = False
	# 		if MySpider.allowed_domains[0] in room.url:
	# 			is_allowed = True
	# 			if is_allowed and room.url not in MySpider.visited:
	# 				print(room.url)
	# 				MySpider.visited.append(room.url)
	# 				yield scrapy.Request(room.url, callback=self.parse_page, dont_filter=True)
		rooms = response.xpath('//div[@class="_v72lrv"]/div/a/@href').extract()
		for room in rooms:
			web_page = 'https://www.airbnb.com'+room
			if 'rooms/' in room and web_page not in MySpider.visited:
				print('seems ok')
				MySpider.visited.append(web_page)
				yield scrapy.Request(web_page, callback=self.parse_page, dont_filter=True)

	# # 	# Return all the found items


	def parse_page(self, response):
		# open_in_browser(response)
		# pass
		item = AbnbItem()
		soup = BeautifulSoup(response.body,"lxml")
		pattern = re.compile(r'bootstrapData')
		a = soup.find_all('script',text=pattern)
		json_data = a[0]
		cleaned=json_data.text.split("!--")[1].replace("-->","")
		data = json.loads('{"data":'+cleaned+'}')
		home_info = data['data']['bootstrapData']['reduxData']['marketplacePdp']['listingInfo']['listing']
		item['room_title'] = home_info['name']
		item['host_id'] = home_info['primary_host']['id']
		item['host_name'] = home_info['primary_host']['host_name']
		item['room_url'] = response.url 
		item['host_member_since'] = home_info['primary_host']['member_since']
		# Host_review 
		item['host_response_rate'] =home_info['primary_host']['response_rate_without_na']
		item['host_response_time'] = home_info['primary_host']['response_time_without_na']
		item['host_info'] = home_info['primary_host']['about']
		item['host_super'] = home_info['p3_event_data_logging']['is_superhost']
		# Room Infor
		# price 
		item['room_price'] = home_info['p3_event_data_logging']['price']
		# communication & location 
		item['room_communication'] = home_info['p3_event_data_logging']['communication_rating']
		item['room_location'] = home_info['p3_event_data_logging']['location_rating']
		item['room_lag'] = home_info['p3_event_data_logging']['listing_lat']
		item['room_lng'] = home_info['p3_event_data_logging']['listing_lng']
		# room
		item['room_guest_satisfaction_overall'] = home_info['p3_event_data_logging']['guest_satisfaction_overall']
		item['room_hosting_id'] = home_info['p3_event_data_logging']['hosting_id']
		item['room_home_tier'] = home_info['p3_event_data_logging']['home_tier']
		item['room_saved_to_wishlist_count'] = home_info['p3_event_data_logging']['saved_to_wishlist_count']
		item['room_amenity_num'] = len(home_info['p3_event_data_logging']['amenities'])
		item['room_value_rating'] = home_info['p3_event_data_logging']['value_rating']
		# location:lng, lat
		item['room_bathroom_num'] = float(home_info['bathroom_label'].split(' ') [0])
		item['room_guest_num'] = float(home_info['guest_label'].split(' ') [0])
		item['room_bedroom_num'] = float(home_info['bedroom_label'].split(' ') [0])
		item['room_bed_num']= float(home_info['bed_label'].split(' ') [0])
		item['room_score'] = home_info['star_rating']

		return item


# # Now I learned to create Item, building pipe line, the next step is to learn with navigation rule

