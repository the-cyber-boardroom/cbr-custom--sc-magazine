from unittest                                                           import TestCase
from osbot_fast_api.utils.Fast_API_Server                               import Fast_API_Server
from cbr_custom_sc_magazine.sc_magazine.fast_api.SC_Magazine__Fast_API  import SC_Magazine__Fast_API
from tests.integration.sc_magazine__objs_for_tests import HTML_TITLE


class test__http__Routes__UK(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fast_api = SC_Magazine__Fast_API().setup()
        cls.fast_api_server = Fast_API_Server(app=cls.fast_api.app())
        cls.fast_api_server.start()
        assert cls.fast_api_server.is_port_open() is True

    @classmethod
    def tearDownClass(cls):
        cls.fast_api_server.stop()
        assert cls.fast_api_server.is_port_open() is False

    def test_http__uk__articles_html(self):
        response = self.fast_api_server.requests_get('/uk/articles-html')
        assert response.status_code == 200
        assert HTML_TITLE in response.text
