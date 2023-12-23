from django.db import models

class Data(models.Model):
    ID_number = models.CharField(max_length=32)
    Name = models.CharField(max_length=256)
    Last_Name = models.CharField(max_length=256)
    DOB = models.DateField()
    Date_of_Issue = models.DateField()
    Date_of_Expiry = models.DateField()
