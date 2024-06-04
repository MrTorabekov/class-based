from django.db import models

class People(models.Model):
    full_name = models.CharField(max_length=225)
    jobs = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    images = models.ImageField(upload_to='images')


    def __str__(self):
        return self.full_name