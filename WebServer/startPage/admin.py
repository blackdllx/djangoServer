from django.contrib import admin
from .models import Forum, Topic, Comment, EmailVerify

admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(EmailVerify)
# Register your models here.
