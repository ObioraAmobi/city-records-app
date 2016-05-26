import unittest

from gps import *


class test_gps(unittest.TestCase):

    # checking if unit test is working
    def test_is_this_thing_on(self):
        self.assertEquals(1, 1)

    # testing city records data is valid json
    def test_city_records_data_json(self):
        result = city_records_data_json(DATA)
        self.assertEqual(type(result), dict)

    # testing absolute difference formula
    def test_absolute_difference_positive_numbers(self):
        result = absolute_difference((12, 23), (4, 0))
        self.assertEqual(result[0], 8)
        self.assertEqual(result[1], 23)

    def test_absolute_difference_negative_numbers(self):
        result = absolute_difference((-12, -3), (3, -77))
        self.assertEqual(result[0], -15)
        self.assertEqual(result[1], 74)

    # testing central angle formula
    def test_central_angle(self):
        result = central_angle((23, 134), (23.3, -78))
        self.assertEquals(result, 0.6276256071251978)

    # testing conversion to radians
    def test_convert_to_radians(self):
        result = convert_to_radians((23, 4.5))
        self.assertEquals(result[0], 0.4014257279586958)
        self.assertEquals(result[1], 0.07853981633974483)

    # testing distance formula
    def test_distance(self):
        result = distance((12, 34), (53, -75), EARTH_RADIUS)
        self.assertEquals(result, 10170.68792446244)

    def test_distance_other_radius(self):
        result = distance((12, 34), (53, -75), 5906)
        self.assertEquals(result, 9428.360207483152)

    # testing city within limit function
    def test_city_within_limit(self):
        result = city_within_limit((53.333, -6.267), 500, {"lat": 57.15, "lon": -2.1})
        self.assertTrue(result)

    def test_city_outside_limit(self):
        result = city_within_limit((57.15, -2.1), 500, {'lat': 2.483, "lon": -71.883})
        self.assertFalse(result)

    # testing cities filter function

    # testing that the filter returns no city when all cities in my test city records are outside distant limit
    def test_filter_no_city(self):
        result = filter_cities((12, -3.2), 300, self.test_city_records())
        self.assertEqual(len(list(result)), 0)

    # testing that the filter returns only one city when only one city in my test city records is within distant limit
    def test_filter_one_city(self):
        result = filter_cities((51, -175), 300, self.test_city_records())
        self.assertEqual(len(list(result)), 1)

    # testing that the filter returns all cities when all are within distant limit
    def test_filter_all_cities(self):
        result = filter_cities((51, -175), 99999, self.test_city_records())
        self.assertEqual(len(list(result)), 5)

    # testing re-filtering/cleaning of data to remove
    def test_filter_data(self):
        result = filter_data(self.test_city_records().values())
        self.assertEquals(result, ['Avarua', 'Alofi', 'Adak', 'Pago Pago', 'Apia'])


    # sample data set for testing
    def test_city_records(self):
        return {
            "adak": {
                "lat": 51.883,
                "lon": -176.633,
                "wikipedia": "Adak,_Alaska",
                "city": "Adak"
              },
              "apia": {
                "lat": -13.833,
                "lon": -171.833,
                "wikipedia": "Apia",
                "city": "Apia"
              },
              "pagopago": {
                "lat": -14.267,
                "lon": -170.7,
                "wikipedia": "Pago_Pago",
                "city": "Pago Pago"
              },
              "alofi": {
                "lat": -19.05,
                "lon": -169.917,
                "wikipedia": "Alofi",
                "city": "Alofi"
              },
              "avarua": {
                "lat": -21.2,
                "lon": -159.767,
                "wikipedia": "Avarua",
                "city": "Avarua"
              }
        }