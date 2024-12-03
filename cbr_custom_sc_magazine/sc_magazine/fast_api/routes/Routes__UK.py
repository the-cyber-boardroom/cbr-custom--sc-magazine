from osbot_fast_api.api.Fast_API_Routes import Fast_API_Routes

from cbr_custom_sc_magazine.sc_magazine.content.Http_Content__Articles import Http_Content__Articles

ROUTES_PATHS__UK = ['/uk/articles-html']

class Routes__UK(Fast_API_Routes):
    tag                  : str = 'uk'
    http_content_articles: Http_Content__Articles

    def articles_html(self):
        return self.http_content_articles.articles__html()

    def setup_routes(self):
        self.add_route_get(self.articles_html)

