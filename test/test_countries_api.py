# coding: utf-8

"""
    CodeChef API

    CodeChef API to support different applications.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import codechef_client
from codechef_client.api.countries_api import CountriesApi  # noqa: E501
from codechef_client.rest import ApiException


class TestCountriesApi(unittest.TestCase):
    """CountriesApi unit test stubs"""

    def setUp(self):
        self.api = codechef_client.api.countries_api.CountriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_country_get(self):
        """Test case for country_get

        Get the list of countries on codechef.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
