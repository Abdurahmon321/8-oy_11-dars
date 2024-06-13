from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Friendship(models.Model):
    from_user = models.ForeignKey(User, related_name='friendship_from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='friendship_to_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['from_user', 'to_user']


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='message_sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='message_recipient', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)