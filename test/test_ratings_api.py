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
from codechef_client.api.ratings_api import RatingsApi  # noqa: E501
from codechef_client.rest import ApiException


class TestRatingsApi(unittest.TestCase):
    """RatingsApi unit test stubs"""

    def setUp(self):
        self.api = codechef_client.api.ratings_api.RatingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ratings_contest_type_get(self):
        """Test case for ratings_contest_type_get

        Return ratinglist for a particular contest type.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
