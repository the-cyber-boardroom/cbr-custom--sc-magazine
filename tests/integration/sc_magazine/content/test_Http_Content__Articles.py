from unittest                                                           import TestCase
from cbr_custom_sc_magazine.sc_magazine.content.Http_Content__Articles  import Http_Content__Articles


class test_Http_Content__Articles(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.http_content_articles = Http_Content__Articles()

    def test_requests_get(self):
        with self.http_content_articles as _:
            response = _.requests_get()
            assert response.status_code == 200
            assert response.headers['content-encoding'         ] == 'gzip'
            assert response.headers['content-type'             ] == 'text/html; charset=UTF-8'
            assert response.headers['server'                   ] == 'nginx/1.24.0'
            assert response.headers['strict-transport-security'] == 'max-age=31536000; includeSubDomains;'

            assert response.cookies.keys() == ['XSRF-TOKEN', 'pap_session', 'pap_wcaid_79']

    def test_articles__html(self):
        with self.http_content_articles as _:
            html = _.homepage__html()
            assert " <title>SC Media UK</title>\n" in html

