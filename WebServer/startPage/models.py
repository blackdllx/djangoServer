from django.db import models
from django.contrib import auth, admin
from django.conf import settings

from django.utils import timezone


class Forum(models.Model):
    title = models.CharField("Forum titles", max_length=200)
    access = models.IntegerField("Access level")
    date = models.DateTimeField("Creation data", auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Topic(models.Model):
    forum = models.ForeignKey(Forum, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title = models.CharField("Topic titles", max_length=200)
    date = models.DateTimeField("Creation data", auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    topic = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    text = models.CharField("Comment text", max_length=500)
    date = models.DateTimeField("Creation data", auto_now_add=True, null=True)

    def __str__(self):
        return f"Author: {self.author.username} Topic: {self.topic.title}"


class EmailVerify(models.Model):
    master = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    email = models.CharField("email", max_length=500)
    link = models.CharField("token", max_length=500)
    date = models.DateTimeField("request data", auto_now_add=True, null=True)

    def __str__(self):
        return self.email
