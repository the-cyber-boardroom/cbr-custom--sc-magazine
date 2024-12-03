from unittest                                      import TestCase
from tests.integration.sc_magazine__objs_for_tests import sc_magazine__fast_api__client, HTML_TITLE


class test__client__Routes__UK(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = sc_magazine__fast_api__client

    def test_raw_html_default_path(self):
        response = self.client.get('/uk/articles-html')
        assert response.status_code == 200
        assert HTML_TITLE in response.text
