import urllib.request
import urllib.parse
import requests
import json
from pprint import pprint

MAPQUEST_API_KEY = '0asDGT3JfwUTMkxYMNVKAGvUA76AXyvm'

def get_json(url)
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    We did similar thing in the previous assignment.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)

return response_data


def lat_lng(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    place_json = get_json(url)
    find_lat = (place_name['results'][0]['locations'][0]['latLng']['lat'])
    find_lng = (place_name['results'][0]['locations'][0]['latLng']['lng'])
    
return find_lat, find_lng


def build_url(place):
    params = urllib.parse.urlencode({'key': MAPQUEST_API_KEY, 'location': place})
    url = "http://www.mapquestapi.com/geocoding/v1/address?%s" % params
    print(url)

build_url(place)


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    MBTA_BASE_URL = 'https://api-v3.mbta.com/stops'
    MBTA_API_KEY = '7ca835f35d4d4a39a6012d68d8fa20f6'

    mbta_url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    m = urllib.request.urlopen(mbta_url)
    response_text_mbta = m.read().decode('utf-8')
    response_data_mbta = json.loads(response_text_mbta)
    
    print(mbta_url)

    coordinates = lat_lng(data)
    latitude = coordinates[0]
    longitude = coordinates[1]
    
    pprint(response_data_mbta)
    station_name = response_data_mbta[][]
    #mbta_stop = 'Riverside'
    #response = requests.get('https://api-v3.mbta.com/docs/swagger/swagger.json%s' % stop_finder) 
   
    return mbta_stop

get_nearest_station(coordinates)

def check_accessibility(mbta_stop):
    return True


def main():
    """
    You can all the functions here
    """
    get_json(url)
    lat_lng(place_name)
    build_url(place)
    get_nearest_station(latitude, longitude)
    check_accessibility(mbta_stop)

if __name__ == '__main__':
    main()

