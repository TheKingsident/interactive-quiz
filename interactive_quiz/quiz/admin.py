from django.contrib import admin
from .models import Quiz, Option, User, Score

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Option)
admin.site.register(User)
admin.site.register(Score)
