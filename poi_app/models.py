from django.db import models

# Create your models here.
class PointOfInterest(models.Model):
    CATEGORY_CHOICES = [
        ('restaurant', 'Restaurant'),
        ('mosque', 'Mosque'),
        ('fitness club', 'Fitness club'),
        ('cafe', 'Cafe'),
        ('hotel', 'Hotel'),
        ('medical', 'Medical'),
        ('hijama center', 'Hijama center'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name