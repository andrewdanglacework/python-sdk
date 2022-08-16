# -*- coding: utf-8 -*-
"""
Lacework Reports API wrapper.
"""

from laceworksdk.api.base_endpoint import BaseEndpoint


class ReportsAPI(BaseEndpoint):

    def __init__(self, session):
        """
        Initializes the ReportsAPI object.
        :param session: An instance of the HttpSession class
        :return ReportsAPI object.
        """

        super().__init__(session, "Reports")

    def get(self,
            primaryQueryId=None,
            secondaryQueryId=None,
            format=None,
            type=None,
            reportType=None
            templateName=None,
            latest=None,
            **request_params):
        """
        A method to get Reports objects.
        :param primaryQueryId: The primary ID that is used to fetch the report; for example, AWS Account ID or Azure Tenant ID.
            Note: For GCP, use the secondaryQueryId attribute to provide your GCP Project ID.
        :param secondaryQueryId: The secondary ID that is used to fetch the report; for example, GCP Project ID or Azure Subscription ID.
            Note: For AWS, this parameter is not required.
        :param format: The report's format
        :param type: The report's type
        :param reportType: The report's notification type; for example, AZURE_NIST_CSF.
        :param templateName: The template's name that is used for the report; for example, Default.
        :param latest: To receive the latest report, set this attribute to True

        :return response json
        """

        params = self.build_dict_from_items(
            request_params,
            primaryQueryId=primaryQueryId,
            secondaryQueryId=secondaryQueryId,
            format=format,
            type=type,
            reportType=reportType,
            templateName=templateName,
            latest=latest
        )

        response = self._session.get(self.build_url(), params=params)

        return response.json()
