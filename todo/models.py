from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False, blank=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ("status", "-date_create")

    def __str__(self):
        return self.content
