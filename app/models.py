from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='myimages')

    def __str__(self):
        return self.title 

