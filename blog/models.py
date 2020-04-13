from django.db import models


class Blog(models.Model):
    image = models.ImageField(upload_to='images')
    headline = models.CharField(max_length=50, default='')
    author = models.CharField(max_length=50, default='')
    blog_text = models.TextField()

    def __str__(self):
        return self.headline
