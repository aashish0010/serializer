from django.db import models


# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=111)
    email = models.EmailField()
    roll = models.IntegerField()
    address = models.CharField(max_length=222)

    def __str__(self):
        return self.name