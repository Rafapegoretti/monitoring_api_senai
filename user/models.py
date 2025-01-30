from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
