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
    
room_title = home_info['name']
# Host_id 
host_id = home_info['primary_host']['id']
# Host_name
host_name = home_info['primary_host']['host_name']
host_member_since = home_info['primary_host']['member_since']
# Host_review 
host_response_rate =home_info['primary_host']['response_rate_without_na']
host_response_time = home_info['primary_host']['response_time_without_na']
host_info = home_info['primary_host']['about']
host_super = home_info['p3_event_data_logging']['is_superhost']
# Room Infor
# price 
room_price = home_info['p3_event_data_logging']['price']
# communication & location 
room_communication = home_info['p3_event_data_logging']['communication_rating']
room_location = home_info['p3_event_data_logging']['location_rating']
room_lag = home_info['p3_event_data_logging']['listing_lat']
room_lng = home_info['p3_event_data_logging']['listing_lng']
# room
room_guest_satisfaction_overall = home_info['p3_event_data_logging']['guest_satisfaction_overall']
room_hosting_id = home_info['p3_event_data_logging']['hosting_id']
room_home_tier = home_info['p3_event_data_logging']['home_tier']
room_saved_to_wishlist_count = home_info['p3_event_data_logging']['saved_to_wishlist_count']
room_amenity_num = len(home_info['p3_event_data_logging']['amenities'])
room_value_rating = home_info['p3_event_data_logging']['value_rating']
# location:lng, lat
room_bathroom_num = float(home_info['bathroom_label'].split(' ') [0])
room_guest_num = float(home_info['guest_label'].split(' ') [0])
room_bedroom_num = float(home_info['bedroom_label'].split(' ') [0])
room_bed_num= float(home_info['bed_label'].split(' ') [0])
room_score = home_info['star_rating']
