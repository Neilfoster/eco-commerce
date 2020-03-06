from django.test import TestCase
from .models import Product

# Create your tests here.

class ProductTest(TestCase):
    """
    Define the tests that
    we will run against our
    product models
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')

    def test_format_price_as_euros(self):
        test_product = Product.objects.create(price=10)
        test_formatted_price = test_product.format_price_as_euros()
        self.assertEqual(test_formatted_price, '€10')