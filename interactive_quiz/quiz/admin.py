from django.contrib import admin
from .models import Quiz, Option, User, Score

# Register your models here.
# admin.site.register(Quiz)
admin.site.register(Option)
# admin.site.register(User)
admin.site.register(Score)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'topic', 'difficulty')
    search_fields = ('question', 'answer', 'topic', 'difficulty')
    list_filter = ('topic', 'difficulty')
    ordering = ('difficulty',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('first_name', 'last_name')