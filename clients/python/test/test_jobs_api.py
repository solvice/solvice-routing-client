# coding: utf-8

"""
    OnRoute API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import SolviceRoutingClient
from api.jobs_api import JobsApi  # noqa: E501
from SolviceRoutingClient.rest import ApiException


class TestJobsApi(unittest.TestCase):
    """JobsApi unit test stubs"""

    def setUp(self):
        self.api = api.jobs_api.JobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_job(self):
        """Test case for get_job

        Job  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
