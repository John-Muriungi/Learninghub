from django.db import models

# Create your models here.


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    experience = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
