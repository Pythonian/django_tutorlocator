from django.conf import settings
from django.db import models
from django.urls import reverse

from accounts.models import User


class Course(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse("course", kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Request(models.Model):
    TUTORIAL_TYPE_CHOICES = (
        ('PERSONAL', 'Personal'),
        ('GROUP', 'Group'),
    )
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    description = models.TextField()
    type_of_tutorial = models.CharField(max_length=15, choices=TUTORIAL_TYPE_CHOICES)
    scheduled_date =  models.DateField()
    location = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Request by {self.user}"


class Schedule(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.name} by {self.user}"


class Testimonial(models.Model):
    fullname = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Testimonial by {self.fullname}"
