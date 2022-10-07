from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)


class Tutor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='tutor')
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=15)
    address = models.CharField(max_length=600, blank=True, null=True)
    image = models.ImageField(upload_to='tutors')
    about = models.TextField()
    intro_video = models.FileField(upload_to='intros', blank=True, null=True)
    academic_qualification = models.CharField(
        max_length=50, blank=True, null=True)
    private_tutoring = models.BooleanField()
    tutoring_experience = models.CharField(
        max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    availability = models.BooleanField(default=True)
    fee_range = models.CharField(max_length=50)
    courses = models.ManyToManyField('tutors.Course', related_name='courses')
    designation = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} profile"


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='student')
    phone_number = models.CharField(
        max_length=20)
    image = models.ImageField(
        upload_to='students', blank=True, null=True)
    location = models.CharField(
        max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} profile"
