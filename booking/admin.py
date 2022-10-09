from django.contrib import admin
from .models import BookingStatus, LessonType, Lesson, Bookings, About


@admin.register(BookingStatus)
class BookingStatusAdmin(admin.ModelAdmin):
    """
    Class for booking status admin model
    """
    list_display = ('status',)


@admin.register(LessonType)
class LessonTypeAdmin(admin.ModelAdmin):
    """
    Class for lesson type admin model
    """
    list_display = ('lesson_type',)


@admin.register(Lesson)
class LessonTypeAdmin(admin.ModelAdmin):
    """
    Class for lesson name admin model
    """
    list_display = ('lesson',)


@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    """
    Class for bookings admin model
    """
    list_display = ('lesson', 'lesson_type', 'date', 'time', 'user', 'status')
    search_fields = ['date', 'user', 'status']
    list_filter = ('lesson', 'lesson_type', 'date', 'status')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Class for About Admin model
    """
    list_display = ('title', 'text', 'image')
    