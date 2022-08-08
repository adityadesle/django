from django.db import models

# Create your models here.

class contacts(models.Model):
    email = models.CharField(max_length=122),
    textarea = models.CharField(max_length=122)
    
