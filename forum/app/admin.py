from django.contrib import admin

# Register your models here.

from .models import User, Theme, Question, Answer

admin.site.register(User)
admin.site.register(Theme)
admin.site.register(Question)
admin.site.register(Answer)