import json
import unittest
from typing import Any, Dict
from unittest.mock import patch

from pepephone import API_V1, LoginError, PepeAPI, ProductType, RequestError
from samples import (
    INVALID_LOGIN_RESPONSE,
    INVALID_PRODUCT_RESPONSE,
    PRODUCT_DETAILS,
    PRODUCTS_INFO,
    VALID_LOGIN_RESPONSE,
)


def as_json(buffer) -> Dict[Any, Any]:
    return json.loads(as_utf8(buffer))


def as_utf8(buffer: bytes) -> str:
    return buffer.decode("utf-8")


class TestPepeAPI(unittest.TestCase):
    def test_login(self):
        api = PepeAPI()
        with patch(
            "pepephone.PepeAPI._bytes_request", return_value=VALID_LOGIN_RESPONSE
        ) as mock:
            api.login("a", "b")

        mock.assert_called_with(
            "POST",
            API_V1 + "/auth",
            json={"email": "a", "password": "b", "source": "ECARE_WEB"},
        )

    def test_unsuccessful_login(self):
        api = PepeAPI()
        with patch(
            "pepephone.PepeAPI._bytes_request", return_value=INVALID_LOGIN_RESPONSE
        ):
            with self.assertRaises(RequestError):
                api.login("a", "b")

    def test_get_products(self):
        api = PepeAPI()

        with patch(
            "pepephone.PepeAPI._bytes_request", return_value=PRODUCTS_INFO
        ) as mock:
            products = api.get_products()

        self.assertEqual(products, [(ProductType.MOBILE, "600111222")])
        mock.assert_called_with("GET", API_V1 + "/all?onlyActive=1")

    def test_get_product_details(self):
        api = PepeAPI()
        with patch(
            "pepephone.PepeAPI._bytes_request", return_value=PRODUCT_DETAILS
        ) as mock:
            api.get_product_details("123456789")

        mock.assert_called_with(
            "GET", "https://services.pepephone.com/v1/consumption/123456789"
        )

    def test_get_invalid_product_details(self):
        api = PepeAPI()
        with patch(
            "pepephone.PepeAPI._bytes_request", return_value=INVALID_PRODUCT_RESPONSE
        ):
            with self.assertRaises(RequestError):
                api.get_product_details("123456789")


if __name__ == "__main__":
    unittest.main()
