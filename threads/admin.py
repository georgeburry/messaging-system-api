from django.contrib import admin

from threads.models import UserMessage, Message

# Register your models here.
admin.site.register(Message)
admin.site.register(UserMessage)
