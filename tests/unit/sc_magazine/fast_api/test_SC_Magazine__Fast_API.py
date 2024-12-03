from unittest import TestCase

from osbot_utils.utils.Dev import pprint

from cbr_custom_sc_magazine.sc_magazine.fast_api.SC_Magazine__Fast_API import SC_Magazine__Fast_API


class test_SC_Magazine__Fast_API(TestCase):

    def setUp(self):
        self.fast_api = SC_Magazine__Fast_API()

    def test_base_path(self):
        assert self.fast_api.base_path == '/sc-magazine'
        assert self.fast_api.enable_cors is True

    def test_setup_routes(self):
        self.fast_api.setup()
        routes = self.fast_api.routes_paths()

        assert routes == ['/', '/config/info', '/config/status', '/config/version', '/uk/raw-html']
