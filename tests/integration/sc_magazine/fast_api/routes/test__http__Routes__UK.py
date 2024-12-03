from unittest                                                           import TestCase
from osbot_fast_api.utils.Fast_API_Server                               import Fast_API_Server
from cbr_custom_sc_magazine.sc_magazine.fast_api.SC_Magazine__Fast_API  import SC_Magazine__Fast_API

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

    def test_raw_html_endpoint(self):
        response = self.fast_api_server.requests_get('/uk/raw-html')
        assert response.status_code == 200
        assert response.json()      == 'will be here'

    def test_raw_html_with_custom_path(self):
        response = self.fast_api_server.requests_get('/uk/raw-html', params={'path': '/custom'})
        assert response.status_code == 200
        assert response.json()      == 'will be here'