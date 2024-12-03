import requests
from unittest                                              import TestCase
from cbr_custom_sc_magazine.utils.Version                  import version__cbr_custom_sc_magazine
from deploy.lambdas.Deploy_Lambda__Cbr_Custom__SC_Magazine import Deploy_Lambda__Cbr_Custom_SC_Magazine


class test__qa__Routes__Info(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.deploy_lambda   = Deploy_Lambda__Cbr_Custom_SC_Magazine()
        cls.lambda_function = cls.deploy_lambda.lambda_function
        cls.lambda_url      = cls.lambda_function.function_url()
        cls.session         = requests.Session()


    def requests_get(self, endpoint, params=None):
        response = self.session.get(f"{self.lambda_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response

    def test_raw_html_live(self):
        response = self.requests_get('info/version')
        assert response.status_code == 200
        assert response.json() == {'version': version__cbr_custom_sc_magazine}