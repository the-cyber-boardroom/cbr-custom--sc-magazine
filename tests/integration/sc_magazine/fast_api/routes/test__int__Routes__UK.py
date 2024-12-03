from unittest                                                      import TestCase
from cbr_custom_sc_magazine.sc_magazine.fast_api.routes.Routes__UK import Routes__UK
from tests.integration.sc_magazine__objs_for_tests import HTML_TITLE


class test__int__Routes__UK(TestCase):

    def setUp(self):
        self.routes_sc_magazine_uk = Routes__UK()

    def test_routes_setup(self):
        with self.routes_sc_magazine_uk as _:
            assert _.tag == 'uk'
            _.setup_routes()
            assert len(_.routes_paths()) > 0

    def test__raw_html(self):
        with self.routes_sc_magazine_uk as _:
            assert HTML_TITLE in _.articles_html()