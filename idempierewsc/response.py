# -*- encoding: utf-8 -*-
"""
Copyright (c) 2016 Saúl Piña <sauljabin@gmail.com>.

This file is part of idempierewsc.

idempierewsc is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

idempierewsc is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with idempierewsc.  If not, see <http://www.gnu.org/licenses/>.
"""

import idempierewsc.base
import idempierewsc.enums


class CompositeResponse(idempierewsc.base.WebServiceResponse):
    def __init__(self):
        super(CompositeResponse, self).__init__()
        self.responses = []

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.CompositeResponse


class RunProcessResponse(idempierewsc.base.WebServiceResponse):
    def __init__(self):
        super(RunProcessResponse, self).__init__()
        self.log_info = ''
        self.summary = ''

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.RunProcessResponse


class StandardResponse(idempierewsc.base.WebServiceResponse):
    def __init__(self):
        super(StandardResponse, self).__init__()
        self.record_id = 0
        self.output_fields = []

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.StandardResponse


class WindowTabDataResponse(idempierewsc.base.WebServiceResponse):
    def __init__(self):
        super(WindowTabDataResponse, self).__init__()
        self.num_rows = 0
        self.total_rows = 0
        self.start_row = 0
        self.data_set = []

    def web_service_response_model(self):
        return idempierewsc.enums.WebServiceResponseModel.WindowTabDataResponse


class ResponseFactory(object):
    """
    ResponseFactory. Class for build reponses
    """

    def create_response(self, response_model, xml_response):
        if not response_model:
            return xml_response

        if response_model == idempierewsc.enums.WebServiceResponseModel.StandardResponse:
            return self.create_standard_response(xml_response)
        elif response_model == idempierewsc.enums.WebServiceResponseModel.CompositeResponse:
            return self.create_composite_response(xml_response)
        elif response_model == idempierewsc.enums.WebServiceResponseModel.RunProcessResponse:
            return self.create_run_process_response(xml_response)
        elif response_model == idempierewsc.enums.WebServiceResponseModel.WindowTabDataResponse:
            return self.create_window_tab_data_response(xml_response)

        return None

    def has_fault_error(self, response, xml_response):
        pass

    def create_composite_response(self, xml_response):
        pass

    def create_run_process_response(self, xml_response):
        pass

    def create_standard_response(self, xml_response):
        pass

    def create_window_tab_data_response(self, xml_response):
        pass