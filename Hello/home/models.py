from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=122,default='000000')
    email = models.CharField(max_length=122,default="ok@")
    password = models.CharField(max_length=122)
    # text = models.CharField(max_length=122)
    
    def __str__(self):
        return self.name    