# coding: utf-8

"""
    Solvice API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.tmp_api import TMPApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTMPApi(unittest.TestCase):
    """TMPApi unit test stubs"""

    def setUp(self):
        self.api = api.tmp_api.TMPApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_job(self):
        """Test case for get_job

        gets a job  # noqa: E501
        """
        pass

    def test_get_job_status(self):
        """Test case for get_job_status

        gets a job status  # noqa: E501
        """
        pass

    def test_solve_tmp(self):
        """Test case for solve_tmp

        solve a TMP problem  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()