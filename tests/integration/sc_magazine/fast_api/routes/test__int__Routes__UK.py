from unittest                                                       import TestCase
from osbot_utils.utils.Misc                                         import list_set
from cbr_custom_sc_magazine.sc_magazine.fast_api.routes.Routes__UK  import Routes__UK
from tests.integration.sc_magazine__objs_for_tests                  import HTML_TITLE__ARTICLES_PAGE, HTML_TITLE__HOME_PAGE


class test__int__Routes__UK(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.routes_sc_magazine_uk = Routes__UK()

    def test_routes_setup(self):
        with self.routes_sc_magazine_uk as _:
            assert _.tag == 'uk'
            _.setup_routes()
            assert len(_.routes_paths()) > 0

    def test__articles_data(self):
        with self.routes_sc_magazine_uk as _:
            assert len(_.articles_data()) > 0

    def test__articles_html(self):
        with self.routes_sc_magazine_uk as _:
            assert HTML_TITLE__ARTICLES_PAGE in _.articles_html()

    def test__homepage_data(self):
        with self.routes_sc_magazine_uk as _:
            assert list_set(_.homepage_data()) == [ 'expert_reports'    ,
                                                    'featured_article'  ,
                                                    'latest_articles'   ,
                                                    'news_briefs'       ,
                                                    'upcoming_webinars' ,
                                                    'videos'            ]

    def test__homepage_html(self):
        with self.routes_sc_magazine_uk as _:
            assert HTML_TITLE__HOME_PAGE in _.homepage_html()
