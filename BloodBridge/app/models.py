from django.db import models
from django.utils import timezone

class BloodDonor(models.Model):
    donor_id = models.CharField(max_length=255, null=False, unique=True)
    donor_name = models.CharField(max_length=255,null=False,default='None')
    blood_type = models.CharField(max_length=5, null=False)
    lat = models.CharField(max_length=10, null=False)
    lgs = models.CharField(max_length=10, null=False)
    
    def __str__(self):
        return f"Donor ID: {self.donor_id}, Blood Type: {self.blood_type}, Location: ({self.lat}, {self.lgs})"


class Requests(models.Model):
    bank_name = models.CharField(max_length=255)
    message = models.CharField(max_length=500)
    status = models.IntegerField()
    user_id = models.CharField(max_length=255,default="None")
    sent_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.bank_name