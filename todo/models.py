from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    date_create = models.DateTimeField()
    deadline = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.content

