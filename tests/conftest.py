# Copyright (C) 2019-2020 HERE Europe B.V.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# License-Filename: LICENSE

import pytest

from here_location_services.geocoding_search_api import GeocodingSearchApi
from here_location_services.isoline_routing_api import IsolineRoutingApi
from here_location_services.utils import get_apikey

LS_API_KEY = get_apikey()


@pytest.fixture()
def geo_search_api():
    """Create shared low level Location services GeocodingSearchApi instance as a pytest fixture.
    :return: :class:`GeocodingSearchApi` object.
    """
    api = GeocodingSearchApi(api_key=LS_API_KEY)
    return api


@pytest.fixture()
def isoline_routing_api():
    """Create shared low level Location services IsolineRoutingApi instance as a pytest fixture."""
    api = IsolineRoutingApi(api_key=LS_API_KEY)
    return api
