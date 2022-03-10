# -*- coding: utf-8 -*-

# Copyright (C) 2022 Luis López <luis@cuarentaydos.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
# USA.


import datetime
import enum
import json
from typing import Optional

import requests

API_V1 = "https://services.pepephone.com/v1"
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) "
        "Gecko/20100101 Firefox/97.0"
    ),
}


class PepeAPI:
    def __init__(self, sess: Optional[requests.Session] = None):
        self._sess = sess or requests.Session()
        self._headers = DEFAULT_HEADERS.copy()
        self._token_expiration = datetime.datetime.fromtimestamp(0)

    def _request(self, method, url, **kwargs):
        headers = {}
        headers.update(self._headers)
        headers.update(kwargs.get("headers", {}))
        kwargs["headers"] = headers

        return self._sess.request(method, url, **kwargs)

    def _bytes_request(self, *args, **kwargs):
        # if resp.status_code != 200:
        #     raise RequestError(response=resp)

        return self._request(*args, **kwargs).text

    def _json_request(self, *args, **kwargs):
        data = json.loads(self._bytes_request(*args, **kwargs))
        if "error" in data:
            raise RequestError(json=data)

        return data

    def login(self, username, password):
        data = self._json_request(
            "POST",
            API_V1 + "/auth",
            json={"email": username, "password": password, "source": "ECARE_WEB"},
        )

        auth = f"{data['tokenType']} {data['accessToken']}"
        self._headers["Authorization"] = auth

        self._token_expiration = datetime.datetime.now() + datetime.timedelta(
            seconds=data["expiresIn"]
        )

    @property
    def logged(self):
        return (
            "Authorization" in self._headers
            and self._token_expiration > datetime.datetime.now()
        )

    def get_products(self):
        data = self._json_request("GET", API_V1 + "/all?onlyActive=1")
        products = [(ProductType.MOBILE, x["msisdn"]) for x in data.get("mobile", [])]
        return products

    def get_product_details(self, product_id: str):
        m = [
            # Gasto (€) en datos
            ("data_amount", "dataAmount"),
            # Datos consumidos totales (Mb)
            ("data_consume", "dataConsumeAll"),
            # Datos contratados (Mb)
            ("data_available", "dataFlat"),
            # Llamadas realizadas (seconds)
            ("voice_consume", "voiceConsume"),
            # Gasto (€) en llamadas
            ("voice_amount", "voiceAmount"),
            # Límite (secs) en llamadas
            ("voice_available", "voiceFlat"),
        ]

        data = self._json_request("GET", API_V1 + f"/consumption/{product_id}")
        return {k: data[k2] for (k, k2) in m}


class ProductType(enum.Enum):
    MOBILE = enum.auto()


class BaseError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.args = args
        self.kwargs = kwargs


class RequestError(BaseError):
    pass


class LoginError(RequestError):
    pass
