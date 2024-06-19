from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    department = models.CharField('отдел', max_length=20)

@receiver(post_save, sender=User)
def create_user_employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
    instance.employee.save()

class order(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)