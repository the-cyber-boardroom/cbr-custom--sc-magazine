from unittest                                                                   import TestCase
from cbr_custom_sc_magazine.sc_magazine.fast_api.routes.Routes__SC_Magazine__UK import Routes__SC_Magazine__UK, ROUTES_PATHS__SC_MAGAZINE__UK


class test__int__Routes__SC_Magazine__UK(TestCase):

    def setUp(self):
        self.routes_sc_magazine_uk = Routes__SC_Magazine__UK()

    def test_routes_setup(self):
        with self.routes_sc_magazine_uk as _:
            assert _.tag == 'uk'
            _.setup_routes()
            assert _.routes_paths() == ROUTES_PATHS__SC_MAGAZINE__UK

    def test__raw_html(self):
        with self.routes_sc_magazine_uk as _:
            response = _.raw_html()
            assert response == 'will be here'

            response_custom = _.raw_html(path='/custom')
            assert response_custom == 'will be here'