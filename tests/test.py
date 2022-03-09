import unittest
from unittest.mock import patch
from pepephone import PepeAPI, LoginError, RequestError, ProductType, API_V1

from samples import (
    VALID_LOGIN_RESPONSE,
    INVALID_LOGIN_RESPONSE,
    PRODUCTS_INFO,
    PRODUCT_DETAILS,
    INVALID_PRODUCT_RESPONSE,
)
import json
from typing import Dict, Any


def as_json(buffer) -> Dict[Any, Any]:
    return json.loads(as_utf8(buffer))


def as_utf8(buffer: bytes) -> str:
    return buffer.decode("utf-8")


class TestPepeAPI(unittest.TestCase):
    @patch("pepephone.PepeAPI._bytes_request")
    def test_login(self, _bytes_request):
        _bytes_request.return_value = VALID_LOGIN_RESPONSE
        api = PepeAPI()
        api.login("a", "b")

        # mock.assert_called_with("GET", API_V1 + "/auth")

    @patch("pepephone.PepeAPI._bytes_request")
    def test_unsuccessful_login(self, _bytes_request):
        _bytes_request.return_value = INVALID_LOGIN_RESPONSE

        api = PepeAPI()
        with self.assertRaises(RequestError):
            api.login("a", "b")

    @patch("pepephone.PepeAPI._bytes_request")
    def test_get_products(self, _bytes_request):
        api = PepeAPI()

        # mock.return_value = VALID_LOGIN_RESPONSE
        # self.api.login("a", "b")

        _bytes_request.return_value = PRODUCTS_INFO
        products = api.get_products()

        self.assertEqual(products, [(ProductType.MOBILE, "600111222")])

    @patch("pepephone.PepeAPI._bytes_request")
    def test_get_product_details(self, _bytes_request):
        _bytes_request.return_value = PRODUCT_DETAILS

        api = PepeAPI()
        details = api.get_product_details("123456789")

        _bytes_request.assert_called_with(
            "GET", "https://services.pepephone.com/v1//consumption/123456789"
        )


if __name__ == "__main__":
    unittest.main()
