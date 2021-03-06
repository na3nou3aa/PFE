from django.db import models
from django.contrib.auth.models import User


class Scan (models.Model):

    name = models.CharField(max_length=255, null=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, blank=True)
    Target = models.FileField(upload_to='uploads/')
    Client = models.TextField(blank=True)


def __str__(self):
    return self.name + ": " + str(self.filepath)


class Documents (models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=255, blank=True)
    filepath = models.FileField(upload_to='files/', null=True, verbose_name="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
