from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

class Projects(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="Project title",
                            help_text="Enter a project name")
    description = models.TextField(max_length=3000,
                                   verbose_name="Project description",
                                   help_text="Must contain only 3000 characters")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['created_at']
@receiver(post_save, sender=Projects)
def create_project(sender, instance, created, **kwargs):
    if created:
        print("Project Created")
@receiver(post_delete, sender=Projects)
def delete_project(sender, instance, **kwargs):
    print("Project Deleted")

class Status(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="Status title",
                            help_text="Enter a status title"
                            )
    description = models.TextField(max_length=3000,
                                   verbose_name="Status description",
                                   help_text="Must contain only 3000 characters")
    is_active = models.BooleanField(null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
        ordering = ['-is_active', 'name']
@receiver(post_save, sender=Status)
def create_status(sender, instance, created, **kwargs):
    if created:
        print("Status Created")
@receiver(post_delete, sender=Status)
def delete_status(sender, instance, **kwargs):
    print("Status Deleted")
class Priority(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="Priority",
                            help_text="Enter a priority title"
                            )
    description = models.TextField(max_length=3000,
                                   verbose_name="Priority description",
                                   help_text="Must contain only 3000 characters")
    is_active = models.BooleanField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Priority'
        verbose_name_plural = 'Priorities'
        ordering = ['-is_active', 'name']
@receiver(post_save, sender=Priority)
def create_priority(sender, instance, created, **kwargs):
    if created:
        print("Priority Created")
@receiver(post_delete, sender=Priority)
def delete_priority(sender, instance, **kwargs):
    print("Priority Deleted")
class Tasks(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=3000)
    status = models.ForeignKey(Status,  on_delete=models.PROTECT, null=True, limit_choices_to={"is_active": True})
    priority = models.ForeignKey(Priority,
                                 on_delete=models.PROTECT,
                                 limit_choices_to={"is_active": True},
                                 related_name="all_tasks"
                                 )

    def __str__(self):
        return f'{self.project.name}: {self.name}'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['project', 'name']

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