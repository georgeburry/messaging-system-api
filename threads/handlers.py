from typing import Iterable

from django.contrib.auth.models import User

from .models import Message


def create_message(content: str, author: User, user_ids: Iterable[int]):
    message = Message.objects.create(content=content, author=author)
    if author.id not in user_ids:
        user_ids.append(author.id)

    users = User.objects.filter(id__in=user_ids)

    message.users.add(*users)
