import uuid

from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    content = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    users = models.ManyToManyField(
        User,
        through='UserMessage',
        related_name='message_thread'
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Ensure the author is in the users many-to-many field
        if not self.users.filter(id=self.author.id).exists():
            self.users.add(self.author)

    def __str__(self):
        return f'{self.author.username} - {self.timestamp} - {self.content[:50]}'


class UserMessage(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_message',
        null=False
    )
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='message_user',
        null=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'message'],
                name='unique_user_message'
            )
        ]

    def __str__(self):
        return f'{self.user.username} - {self.message.id}'
