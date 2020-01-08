from django.db import models
from datetime import datetime as dt


class UserProfile(models.Model):
    intro = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    date = models.DateTimeField(default=dt.now())

    def __str__(self):
        return self.intro


class WorkPortfolio(models.Model):
    work_title = models.CharField(max_length=255)
    work_details = models.TextField()
    work_link = models.CharField(max_length=255, blank=True)
    work_image = models.ImageField(upload_to='Work/Image/%Y/%m/%d/')
    date = models.DateTimeField(default=dt.now())

    def __str__(self):
        return self.work_title
