import requests
from unittest                                              import TestCase
from osbot_aws.AWS_Config                                  import aws_config
from deploy.lambdas.Deploy_Lambda__Cbr_Custom__SC_Magazine import Deploy_Lambda__Cbr_Custom_SC_Magazine


class test__qa__Routes__UK(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.deploy_lambda   = Deploy_Lambda__Cbr_Custom_SC_Magazine()
        cls.lambda_function = cls.deploy_lambda.lambda_function
        cls.lambda_url      = cls.lambda_function.function_url()
        cls.base_url        = f"{cls.lambda_url}/uk"
        cls.session         = requests.Session()


    def requests_get(self, endpoint, params=None):
        response = self.session.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response

    def test__lambda_url(self):
        aws_region = aws_config.region_name()
        response  = requests.get(self.lambda_url, allow_redirects=False)
        assert f'lambda-url.{aws_region}.on.aws' in self.lambda_url
        assert response.status_code              == 307
        assert response.headers['location']      == '/docs'

    def test_raw_html_live(self):
        response = self.requests_get('raw-html')
        assert response.status_code == 200
        assert 'will be here'       in response.text