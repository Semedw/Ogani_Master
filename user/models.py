from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    class Meta:
        verbose_name = 'User'
        verbose_name_plural =  'Users'


    def __str__(self):
        return self.username