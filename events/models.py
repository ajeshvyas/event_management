from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# Create your models here.


class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ("online", "Online"),
        ("offline", "Offline"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_seats = models.PositiveIntegerField()
    booking_start_date = models.DateTimeField()
    booking_end_date = models.DateTimeField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        current_datetime = timezone.now()
        if current_datetime < self.event.booking_start_date:
            raise ValidationError("Ticket booking is not yet open.")
        if current_datetime > self.event.booking_end_date:
            raise ValidationError("Ticket booking is closed.")

        super().save(*args, **kwargs)
