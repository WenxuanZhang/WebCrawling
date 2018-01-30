# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AbnbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	room_title = scrapy.Field()
	room_url = scrapy.Field()
	host_id = scrapy.Field()
	host_name = scrapy.Field()
	host_member_since = scrapy.Field()
	# Host_review 
	host_response_rate =scrapy.Field()
	host_response_time = scrapy.Field()
	host_info = scrapy.Field()
	host_super = scrapy.Field()
	# Room Infor
	# price 
	room_price = scrapy.Field()
	# communication & location 
	room_communication = scrapy.Field()
	room_location = scrapy.Field()
	room_lag = scrapy.Field()
	room_lng = scrapy.Field()
	# room
	room_guest_satisfaction_overall = scrapy.Field()
	room_hosting_id =scrapy.Field()
	room_home_tier = scrapy.Field()
	room_saved_to_wishlist_count = scrapy.Field()
	room_amenity_num = scrapy.Field()
	room_value_rating = scrapy.Field()
	# location:lng, lat
	room_bathroom_num = scrapy.Field()
	room_guest_num = scrapy.Field()
	room_bedroom_num = scrapy.Field()
	room_bed_num= scrapy.Field()
	room_score = scrapy.Field()

	# room_score = home_info['star_rating']
