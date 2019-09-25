# coding: utf-8

"""
    Solvice API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class VRPApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_job(self, job_id, **kwargs):  # noqa: E501
        """gets a job  # noqa: E501

        Retrieve a specific job  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The job ID. (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_job_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_job_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def get_job_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """gets a job  # noqa: E501

        Retrieve a specific job  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The job ID. (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/jobs/{jobId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Job',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_job_status(self, job_id, **kwargs):  # noqa: E501
        """gets a job status  # noqa: E501

        Retrieve a specific job status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job_status(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The job ID. (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_job_status_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_job_status_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def get_job_status_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """gets a job status  # noqa: E501

        Retrieve a specific job status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job_status_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The job ID. (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_job_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_job_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/jobs/{jobId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Job',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def solve_vrp(self, **kwargs):  # noqa: E501
        """solve a VRP problem  # noqa: E501

        Adds an item to the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.solve_vrp(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VRP body: VRP problem solve request
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.solve_vrp_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.solve_vrp_with_http_info(**kwargs)  # noqa: E501
            return data

    def solve_vrp_with_http_info(self, **kwargs):  # noqa: E501
        """solve a VRP problem  # noqa: E501

        Adds an item to the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.solve_vrp_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VRP body: VRP problem solve request
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method solve_vrp" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/solve#VRP', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Job',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
