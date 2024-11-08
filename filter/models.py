from django.db import models
from user.models import CustomUser

class Filter(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    filter_name = models.CharField(max_length=200)
    filter_data = models.CharField(max_length=200)  # Use TextField for potentially large or structured data

    def __str__(self):
        return self.filter_name
