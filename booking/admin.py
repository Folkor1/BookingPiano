from django.contrib import admin
from .models import Lesson, About

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Class for Lesson Admin model.
    """

    list_display = ('get_lesson_display', 'get_lesson_type_display', 'date', 'time', 'owner')
    search_fields = ['date', 'owner']
    list_filter = ('lesson', 'lesson_type', 'date')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Class for About Admin model.
    """
    list_display = ('title', 'text', 'image')