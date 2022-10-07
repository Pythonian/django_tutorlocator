from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tutor, Student, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_tutor:
            Tutor.objects.create(user=instance)
        if instance.is_student:
            Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_tutor:
        instance.tutor.save()
    if instance.is_student:
        instance.student.save()
