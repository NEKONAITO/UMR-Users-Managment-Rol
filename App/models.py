from django.db import models

# Create your models here.
class Dato(models.Model):
    name = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)

    
    def __str__(self):
        return self.name