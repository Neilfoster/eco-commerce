from django.db import models


class Product(models.Model):
    category = models.CharField(max_length=254, default='')
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name

    def format_price_as_euros(self):
        """ Adds Euro Sign to the start of each price """
        return '€'+str(self.price) 