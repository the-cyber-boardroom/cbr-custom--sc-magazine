from unittest                                                           import TestCase
from cbr_custom_sc_magazine.sc_magazine.fast_api.SC_Magazine__Fast_API  import SC_Magazine__Fast_API
from cbr_custom_sc_magazine.sc_magazine.fast_api.routes.Routes__Info    import ROUTES_PATHS__INFO
from cbr_custom_sc_magazine.sc_magazine.fast_api.routes.Routes__UK      import ROUTES_PATHS__UK


class test_SC_Magazine__Fast_API(TestCase):

    def setUp(self):
        self.fast_api = SC_Magazine__Fast_API()

    def test_base_path(self):
        assert self.fast_api.base_path == '/sc-magazine'
        assert self.fast_api.enable_cors is True

    def test_setup_routes(self):
        self.fast_api.setup()
        routes = self.fast_api.routes_paths()

        assert routes == sorted(['/', '/config/info', '/config/status', '/config/version'] \
                                 + ROUTES_PATHS__UK                                        \
                                 + ROUTES_PATHS__INFO                                      )



