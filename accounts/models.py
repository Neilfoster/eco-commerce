from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    #profile_pic = models.ImageField(upload_to='images', default=True)

    def __str__(self):
        return self.user.username


def create_or_update_user_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    post_save.connect(create_or_update_user_profile, sender=User)

