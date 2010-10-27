from django.db import models

class Truck(models.Model):
    creation_date = models.DateTimeField(blank=True,null=True)
    last_modified = models.DateTimeField(auto_now=True)


# Create your models here.
