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

    def test_index_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html') 
    
    def test_all_household_template(self):
        response = self.client.get("/products/all_household", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('all_household.html')

    def test_all_selfcare_template(self):
        response = self.client.get("/products/all_selfcare", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('all_selfcare.html')

    def test_all_products_template(self):
        response = self.client.get("/products/all_products", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('all_products.html')