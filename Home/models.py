from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=12, default='SOME STRING')
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    