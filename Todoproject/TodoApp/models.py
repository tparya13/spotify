from django.db import models


# Create your models here.
class Music(models.Model):
    name=models.CharField(max_length=30)
    language=models.CharField(max_length=30)
    duration=models.CharField(max_length=10)
    image=models.ImageField(upload_to='todoimage')
    description=models.CharField(max_length=200)
    def __str__(self):
        return self.name