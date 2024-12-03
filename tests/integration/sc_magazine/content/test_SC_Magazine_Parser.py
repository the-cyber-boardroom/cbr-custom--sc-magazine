import pytest
from bs4                                                            import BeautifulSoup
from cbr_custom_sc_magazine.sc_magazine.content.SC_Magazine_Parser  import SC_Magazine_Parser
from cbr_custom_sc_magazine.sc_magazine.schema.Article              import Article
from cbr_custom_sc_magazine.sc_magazine.schema.Home_Page            import Home_Page
from cbr_custom_sc_magazine.sc_magazine.schema.Webinar              import Webinar

# Test cases
class Test_SC_Magazine_Parser:

    def test_init(self, parser):                                        # Test parser initialization
        assert isinstance(parser.soup, BeautifulSoup)
        assert parser.base_url == "https://insight.scmagazineuk.com"

    def test_parse_metadata(self, parser):                              # Test metadata parsing
        metadata = parser.parse_metadata()
        assert metadata.title == "SC Media UK - Test"
        assert metadata.og_description == "Test description"

    def test_parse_featured_article(self, parser):                      # Test featured article parsing
        article = parser._parse_featured_article()
        assert isinstance(article, Article)
        assert article.title == "Featured Article Title"
        assert article.url == "https://insight.scmagazineuk.com/article/1"
        assert article.description == "Article description"
        assert article.tags == ["Security"]

    def test_parse_latest_articles(self, parser):                       # Test latest articles parsing
        articles = parser._parse_latest_articles()
        assert len(articles) > 0
        assert all(isinstance(a, Article) for a in articles)
        assert articles[0].title == "Regular Article Title"

    def test_parse_webinars(self, parser):                              # Test webinars parsing
        webinars = parser._parse_webinars()
        assert len(webinars) > 0
        webinar = webinars[0]
        assert isinstance(webinar, Webinar)
        assert webinar.title == "Test Webinar"
        assert len(webinar.speakers) == 1
        assert webinar.speakers[0].name == "John Doe"

    def test_parse_expert_reports(self, parser):                        # Test expert reports parsing
        reports = parser._parse_expert_reports()
        assert isinstance(reports, list)

    def test_parse_videos(self, parser):                                # Test videos parsing
        videos = parser._parse_videos()
        assert isinstance(videos, list)


    def test_full_homepage_parsing(self, parser):                       # Integration test for full homepage parsing
        homepage = parser.parse_homepage()
        assert homepage.featured_article is not None
        assert isinstance(homepage                   , Home_Page)
        assert isinstance(homepage.latest_articles   , list     )
        assert isinstance(homepage.upcoming_webinars , list     )
        assert isinstance(homepage.expert_reports    , list     )
        assert isinstance(homepage.news_briefs       , list     )
        assert isinstance(homepage.videos            , list     )

# Test fixtures
@pytest.fixture
def sample_html():
    """Load sample HTML from file"""
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>SC Media UK</title>
            <meta property="og:title" content="SC Media UK - Test" />
            <meta property="og:description" content="Test description" />
        </head>
        <body>
            <!-- Featured Article -->
            <article class="card-highlighted">
                <h3>Featured Article Title</h3>
                <a class="block-link" href="/article/1">Read more</a>
                <time datetime="2024-03-01T10:00:00">March 1, 2024</time>
                <div class="card-excerpt">Article description</div>
                <img src="https://example.com/image.jpg" />
                <a class="term-badge" href="/tag/security">Security</a>
            </article>

            <!-- Regular Article -->
            <article class="card-list--article">
                <h3>Regular Article Title</h3>
                <a class="block-link" href="/article/2">Read more</a>
                <time datetime="2024-03-02T10:00:00">March 2, 2024</time>
                <div class="card-excerpt">Another description</div>
            </article>

            <!-- Webinar -->
            <div class="event-horizontal-card">
                <h3 class="event-horizontal-card__title">Test Webinar</h3>
                <a class="event-horizontal-card__more-btn" href="/webinar/1">Details</a>
                <time datetime="2024-03-15T14:00:00">March 15, 2024</time>
                <span class="card-live-session__speaker" data-tooltip="<strong>John Doe</strong><br />CTO<br />TechCorp">
                    <img src="https://example.com/speaker.jpg" />
                </span>
            </div>
        </body>
    </html>
    """


@pytest.fixture
def parser(sample_html):
    return SC_Magazine_Parser(sample_html)