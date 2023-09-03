from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='ads/')
    creation_date = models.DateTimeField(auto_now_add=True)
    LOCATION_CHOICES = (
        ('yasamal', 'Yasamal'),
        ('nizami', 'Nizami'),
        # Diğer bölgeler buraya eklenebilir...
    )
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    radius = models.FloatField(default=3000)  # varsayılan olarak 3 km
