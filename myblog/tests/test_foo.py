from unittest import TestCase

import requests
import requests_mock


class TestHTTPRequest(TestCase):
    def test_context_manager(self):
        with requests_mock.Mocker() as mock_request:
            mock_request.get("http://123-fake-api.com", text="Hello!")
            response = requests.get("http://123-fake-api.com")

        assert response.text == "Hello!"