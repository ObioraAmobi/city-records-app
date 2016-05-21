import urllib
import json
from math import acos, sin, cos, radians

DATA = "https://goo.gl/dE04nJ" # given city records data
DESIRED_CITY = 53.333, -6.267 # (longitude, latitude) coordinates for Dublin, Ireland
MAXIMUM_DISTANCE = 500 # (km) maximum distance away from desired city
EARTH_RADIUS = 6371 # (km) radius of the Earth

# getting data from given URL and outputting in JSON format
def city_records_data_json(url):
    try:
        data = urllib.urlopen(url).read()
        return json.loads(data)
    except ValueError:
        # gracefully failing (just in case)
        return "Error! Issue with data"

# calculating absolute difference of two points
def absolute_difference(x, y):
    return x[0] - y[0], x[1] - y[1]

# calculating central angle of two points
# using acos, sin, cos import and above absolute_difference function
def central_angle(x, y):
    return acos(sin(x[0]) * sin(y[0]) + cos(x[0]) * cos(y[0]) * cos(absolute_difference(x, y)[1]))

# converting degrees to radians in order to calc distance later
# using radians import
def convert_to_radians(point):
    return radians(point[0]), radians(point[1])

# calculating distance of two points with earth radius as radius
# central angle function is used with converted radians function converting the units
def distance(x, y, r=EARTH_RADIUS):
    return r * central_angle(convert_to_radians(x), convert_to_radians(y))

# calculating whether city is within maximum distance limit from desired city
def city_within_limit(desired_city, maximum_distance, city_records):
    if distance((city_records["lat"], city_records["lon"]), desired_city) < maximum_distance:
        return 'Within limit'
    else:
        return False

# filtering out cities not within maximum distance limit
def filter_cities(desired_city, maximum_distance, city_records):
    return filter(lambda city: city_within_limit(desired_city, maximum_distance, city), city_records.values())

# removing unnecessary data
def filter_data(city_records):
    return map(lambda x: x["city"], city_records)

# running whole program
def run():
    return filter_data(sorted(filter_cities(DESIRED_CITY, MAXIMUM_DISTANCE, city_records_data_json(DATA))))

print run()