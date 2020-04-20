# -*- coding: utf-8 -*-
import sys
import pytest
from payplug import routes
from payplug.network import HttpClient, UrllibRequest, RequestsRequest
from payplug.test import TestBase


class TestRealHttpQuery(TestBase):
    @pytest.mark.parametrize("api_version", [None, '2019-08-06'])
    def test_http_query_requests(self, api_version):
        http_client = HttpClient(token='a_secret_key', api_version=api_version, request_handler=RequestsRequest)
        _, status = http_client._request('GET', routes.API_BASE_URL + '/test', authenticated=False)
        assert status == 200

    @pytest.mark.xfail(sys.version_info < (2, 7, 9), reason="Can't set ca_file easily with urllib.")
    @pytest.mark.parametrize("api_version", [None, '2019-08-06'])
    def test_http_query_urllib(self, api_version):
        http_client = HttpClient(token='a_secret_key', api_version=api_version, request_handler=UrllibRequest)
        _, status = http_client._request('GET', routes.API_BASE_URL + '/test', authenticated=False)
        assert status == 200
