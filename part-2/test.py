import checker
import aggregator
import unittest
import httpretty
import json
import requests
import requests_mock

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

class RequestChecker(unittest.TestCase):
    """
    Test the checker package
    """
    @requests_mock.Mocker(kw='mock')
    def test_image_exists(self, **kwargs):
        """
        Test that the output format is valid
        """
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/1.png', status_code=200)
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/2.png', status_code=200)

        product_mock = {
            'productId': '123',
            'images': ['http://localhost:4567/images/1.png','http://localhost:4567/images/2.png']
        }
        checker_return = checker.image_exists(json.dumps(product_mock))
        
        self.assertEqual(checker_return, product_mock)
    
    @requests_mock.Mocker(kw='mock')
    def test_missing_one_image(self, **kwargs):
        """
        Test that the output with one missing image
        """
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/1.png', status_code=200)
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/2.png', status_code=500)

        product_mock = {
            'productId': '123',
            'images': ['http://localhost:4567/images/1.png','http://localhost:4567/images/2.png']
        }

        expected_product = {
            'productId': '123',
            'images': ['http://localhost:4567/images/1.png']
        }

        checker_return = checker.image_exists(json.dumps(product_mock))
        self.assertEqual(checker_return, expected_product)

    @requests_mock.Mocker(kw='mock')
    def test_four_existing_images(self, **kwargs):
        """
        Test that the output with one missing image
        """
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/1.png', status_code=200)
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/2.png', status_code=200)
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/3.png', status_code=200)
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/4.png', status_code=200)

        product_mock = {
            'productId': '123',
            'images': [
                'http://localhost:4567/images/1.png',
                'http://localhost:4567/images/2.png',
                'http://localhost:4567/images/3.png',
                'http://localhost:4567/images/4.png'
            ]
        }

        expected_product = {
            'productId': '123',
            'images': [
                'http://localhost:4567/images/1.png',
                'http://localhost:4567/images/2.png',
                'http://localhost:4567/images/3.png'
            ]
        }

        checker_return = checker.image_exists(json.dumps(product_mock))
        self.assertEqual(checker_return, expected_product)

    @requests_mock.Mocker(kw='mock')
    def test_four_existing_images_with_one_missing_in_the_middle(self, **kwargs):
        """
        Test that the output with one missing image
        """
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/1.png', status_code=200)
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/2.png', status_code=200)
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/3.png', status_code=500)
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/4.png', status_code=200)
        kwargs['mock'].register_uri('GET', 'http://localhost:4567/images/5.png', status_code=200)

        product_mock = {
            'productId': '123',
            'images': [
                'http://localhost:4567/images/1.png',
                'http://localhost:4567/images/2.png',
                'http://localhost:4567/images/3.png',
                'http://localhost:4567/images/4.png',
                'http://localhost:4567/images/5.png'
            ]
        }

        expected_product = {
            'productId': '123',
            'images': [
                'http://localhost:4567/images/1.png',
                'http://localhost:4567/images/2.png',
                'http://localhost:4567/images/4.png'
            ]
        }

        checker_return = checker.image_exists(json.dumps(product_mock))
        self.assertEqual(checker_return, expected_product)

if __name__ == '__main__':
    unittest.main()
