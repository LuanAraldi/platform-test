import checker
import aggregator
import unittest
import httpretty
import json

class TestAggregator(unittest.TestCase):
    """
    Test the aggregator package
    """

    def test_format_document(self):
        """
        Test that the output format is valid
        """
        expected_format = {
            'productId': '123',
            'images': ['a','b','c']
        }
        aggregator_format = aggregator.format_product('123', ['a', 'b', 'c'])
        self.assertEqual(expected_format, aggregator_format)

class TestChecker(unittest.TestCase):
    """
    Test the checker package
    """

    def test_image_exists(self):
        """
        Test that the output format is valid
        """
        httpretty.enable()
        httpretty.register_uri(httpretty.GET, 'http://localhost:4567/', status=200)
        product_mock = {
            'productId': '123',
            'images': ['http://localhost:4567/images/1.png','http://localhost:4567/images/2.png']
        }
        checker_return = checker.image_exists(json.dumps(product_mock))
        self.assertEqual(product_mock, checker_return)

if __name__ == '__main__':
    unittest.main()
