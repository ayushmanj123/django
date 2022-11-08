from django.db import models

# Create your models here.

class Aadhar_Front(models.Model):
    aadhar_front = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return str(self.pk)

class Aadhar_Back(models.Model):
    aadhar_back = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return str(self.pk)
