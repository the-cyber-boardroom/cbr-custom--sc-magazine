from osbot_fast_api.api.Fast_API                                                import Fast_API
from cbr_custom_sc_magazine.sc_magazine.fast_api.routes.Routes__SC_Magazine__UK import Routes__SC_Magazine__UK

class SC_Magazine__Fast_API(Fast_API):
    base_path  : str  = '/sc-magazine'
    enable_cors: bool = True

    def setup_routes(self):
        self.add_routes(Routes__SC_Magazine__UK)
