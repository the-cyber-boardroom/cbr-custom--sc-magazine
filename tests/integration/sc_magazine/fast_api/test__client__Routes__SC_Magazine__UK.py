from unittest                                      import TestCase
from tests.integration.sc_magazine__objs_for_tests import sc_magazine__fast_api__client

class test__client__Routes__SC_Magazine__UK(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = sc_magazine__fast_api__client

    def test_raw_html_default_path(self):
        response = self.client.get('/uk/raw-html')
        assert response.status_code == 200
        assert 'will be here'       in response.text

    def test_raw_html_custom_path(self):
        response = self.client.get('/uk/raw-html?path=/news')
        assert response.status_code == 200
        assert 'will be here'       in response.text