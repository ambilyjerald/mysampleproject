from django.db import models

# Create your models here.
class todo(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Place=models.CharField(max_length=20)
    # course=models.CharField(max_length=15)
