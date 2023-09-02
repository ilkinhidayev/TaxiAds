from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='ads/')
    creation_date = models.DateTimeField(auto_now_add=True)