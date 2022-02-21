from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Theme(models.Model):
    title = models.CharField(max_length=200, null=False)
    body = models.CharField(max_length=500, null=True)
    color = models.CharField(max_length=7, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=True)

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    favorite = models.IntegerField(default=0)
    like = models.ManyToManyField(User, related_name='like', blank=True)
    dislike = models.ManyToManyField(User, related_name='dislike', blank=True)
    view = models.IntegerField( null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title


class Answer(models.Model):
    body = models.TextField(null=False)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='answer')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    favorite = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user')

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body
