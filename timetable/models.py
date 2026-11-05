
from django.db import models

class Booking(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    date = models.DateField()

    time_slot = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name