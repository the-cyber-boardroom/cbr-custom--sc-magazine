from cbr_custom_sc_magazine.sc_magazine.fast_api.SC_Magazine__Fast_API import SC_Magazine__Fast_API

HTML_TITLE__HOME_PAGE     = '<title>SC Media UK</title>'
HTML_TITLE__ARTICLES_PAGE = '<title>Articles | SC Media UK</title>'

sc_magazine__fast_api         = SC_Magazine__Fast_API().setup()
sc_magazine__fast_api__app    = SC_Magazine__Fast_API().app()
sc_magazine__fast_api__client = sc_magazine__fast_api.client()