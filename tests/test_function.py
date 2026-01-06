import unittest
import azure.functions as func
from function_app import http_trigger # Adjust this name if your function file is named differently

class TestFunction(unittest.TestCase):
    def test_http_trigger_success(self):
        # Construct a mock HTTP request
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/http_trigger',
            params={'name': 'Azure'}
        )

        # Call the function
        resp = http_trigger(req)

        # Check the output
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Hello, Azure", resp.get_body().decode())