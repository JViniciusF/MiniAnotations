from django.db import models

# Create your models here.
class usuario(models.Model):
    id = models.autoField(primarykey = True)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    first_name = models.CharField(maxlength = 40)
    last_name = models.CharField(maxlength = 50)
