from unittest                  import TestCase
from osbot_utils.utils.Objects import dict_to_obj

from deploy.lambdas.Deploy_Lambda__Cbr_Custom__SC_Magazine import Deploy_Lambda__Cbr_Custom_SC_Magazine


class test__live_lambda_function(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.deploy_lambda   = Deploy_Lambda__Cbr_Custom_SC_Magazine()
        cls.lambda_function = cls.deploy_lambda.lambda_function

    def test__check_lambda_deployment(self):
        with self.lambda_function as _:
            assert _.exists             () is True
            assert _.function_url_exists() is True

    def test_invoke(self):
        with self.lambda_function as _:

            result = obj(_.invoke())
            assert result.errorType == 'Runtime.ExitError'                                  # BUG
            assert 'Runtime exited without providing a reason' in result.errorMessage       # BUG


obj = dict_to_obj