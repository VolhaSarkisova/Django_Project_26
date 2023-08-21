from django.dispatch import receiver, Signal
from django.db.models.signals import post_save, post_delete
from .models import Projects, Status, Priority, Tasks
from django.contrib.auth.models import User


my_signal = Signal()

@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print(kwargs['msg'])

@receiver(post_save, sender=Projects)
def create_project(sender, instance, created, **kwargs):
    if created:
        print("Project Created")
@receiver(post_delete, sender=Projects)
def delete_project(sender, instance, **kwargs):
    print("Project Deleted")
@receiver(post_save, sender=Status)
def create_status(sender, instance, created, **kwargs):
    if created:
        print("Status Created")
@receiver(post_delete, sender=Status)
def delete_status(sender, instance, **kwargs):
    print("Status Deleted")
@receiver(post_save, sender=Priority)
def create_priority(sender, instance, created, **kwargs):
    if created:
        print("Priority Created")
@receiver(post_delete, sender=Priority)
def delete_priority(sender, instance, **kwargs):
    print("Priority Deleted")
@receiver(post_save, sender=Tasks)
def create_task(sender, instance, created, **kwargs):
    if created:
        print("Task Created")
@receiver(post_delete, sender=Tasks)
def delete_task(sender, instance, **kwargs):
    print("Task Deleted")
@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if instance.is_superuser:
        print("SuperUser Created")
