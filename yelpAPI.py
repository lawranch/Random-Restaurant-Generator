import http.client
import json
import urllib
import random

from collections import namedtuple

API_KEY = '-SfYG3s7Zc69CBL0csHMcrnvYTwQFIFWjLO8-rjQvKLx82vSO0PlHcMulBeN_i5ez0fctzzoD4Xun2uwlMDOvk8vYv7v7OFksbjO7lokrUouVt9O9sLqIOS3eYOVW3Yx'
YELP_SEARCH_LINK = '/v3/businesses/search?'
YELP_DETAILS_LINK = '/v3/businesses/'
headers = {'Authorization': 'Bearer {}'.format(API_KEY)}



def build_search_link(parameters: [('name', 'type')]):
    return YELP_SEARCH_LINK + urllib.parse.urlencode(parameters)


def obtain_search_link_info(url: str):
    conn = http.client.HTTPSConnection("api.yelp.com")
    conn.request('GET', url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    response = json.loads(data.decode('utf-8'))
    restaurant_list = []
    for restaurant in response['businesses']:
        restaurant_list.append(restaurant['id'])
    return restaurant_list
    

def select_random_restaurant(restaurant_list: ['id']):
    return restaurant_list[random.randint(0, len(restaurant_list) - 1)]


def build_details_link(id: str):
    return YELP_DETAILS_LINK + id


def obtain_restaurant_details(url: str):
    conn = http.client.HTTPSConnection("api.yelp.com")
    conn.request('GET', url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    response = json.loads(data.decode('utf-8'))
    return response
   
