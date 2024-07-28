from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=125)
    email = models.CharField(max_length=125)
    message = models.TextField()

    def __str__(self):
        return self.name
    