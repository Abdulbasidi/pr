from django.db import models
from django.conf import settings
# Create your models here.


class Booking(models.Model):
    SERVICE_CHOICES = [
        ('diagnostics', 'Диагностика'),
        ('repair', 'Ремонт'),
        ('ecu', 'ECU прошивка'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    service = models.CharField(
        max_length=30,
        choices=SERVICE_CHOICES
    )

    date = models.DateField()
    time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} | {self.service} | {self.date} {self.time}'
