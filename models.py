from django.db import models
from django.core.mail import send_mail

class Complaint(models.Model):
    ZONE_CHOICES = [(f'Zone {i+1}', f'Zone {i+1}') for i in range(8)]
    
    shop_name = models.CharField(max_length=100)
    shop_zone = models.CharField(max_length=10, choices=ZONE_CHOICES)
    shop_location = models.CharField(max_length=255)
    complaint_type = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    is_resolved = models.BooleanField(default=False)
    
    def _str_(self):
        return f"{self.shop_name} - {self.complaint_type}"

    def save(self, *args, **kwargs):
        if not self.pk:
            send_mail(
                'New AC Repair Complaint',
                f'New complaint from {self.shop_name} in {self.shop_zone}.',
                'aswin21092002@gmail.com',
                ['aswin21092002@gmail.com'],
                fail_silently=False,
            )
        super().save(*args, **kwargs)

    def notify_shop(self):
        send_mail(
            'Complaint Resolved',
            f'Your complaint from {self.shop_name} has been resolved.',
            'aswin21092002@gmail.com',
            [f'{self.phone_number}@smsprovider.com'],
            fail_silently=False,
        )
