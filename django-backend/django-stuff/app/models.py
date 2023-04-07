from django.db import models
from django.contrib.auth.models import User


class postEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    description = models.TextField()
    # image = models.ImageField(upload_to='images')

    s_date = models.DateField()
    e_date = models.DateField()
    s_time = models.TimeField()
    e_time = models.TimeField()

    def __str__(self):
        return self.title
