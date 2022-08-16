# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.reports import ReportsAPI
from tests.api.test_read_endpoint import ReadEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.reports


# TODO: Figure out a way to test creates/updates/deletes without breaking things

# @pytest.fixture(scope="module")
# def api_object_create_body(random_text):
#     return {
#         "name": f"AWS Config Test {random_text}",
#         "type": "AwsCfg",
#         "enabled": 1,
#         "data": {
#             "crossAccountCredentials": {
#                 "externalId": f"{random_text}",
#                 "roleArn": f"arn:aws:iam::434813966438:role/lacework-test-{random_text}"
#             }
#         }
#     }


# @pytest.fixture(scope="module")
# def api_object_update_body(random_text):
#     return {
#         "name": f"AWS Config Test {random_text} Updated",
#         "enabled": 0
#     }


class Reports(ReadEndpoint):

    OBJECT_ID_NAME = "intgGuid"
    OBJECT_TYPE = ReportsAPI

    def test_api_get_by_guid(self, api_object):
        self._get_object_classifier_test(api_object, "guid", self.OBJECT_ID_NAME)

    def test_api_get_by_type(self, api_object):
        self._get_object_classifier_test(api_object, "type")
