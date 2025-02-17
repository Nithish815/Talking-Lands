from django.db import models
from location_field.models.plain import PlainLocationField

class Point(models.Model):
    name = models.CharField(max_length=100)
    location = PlainLocationField(based_fields=['name'], zoom=7)

    def __str__(self):
        return self.name
