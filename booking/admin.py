from django.contrib import admin
from .models import BookingStatus, Bookings, About


@admin.register(BookingStatus)
class BookingStatusAdmin(admin.ModelAdmin):
    """
    Class for booking status admin model
    """
    list_display = ('status',)
    list_filter = ('status',)


@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    """
    Class for bookings admin model
    """
    list_display = ('lesson', 'lesson_type', 'time', 'date', 'status')
    search_fields = ['lesson', 'lesson_type', 'date', 'status']
    list_filter = ('lesson', 'lesson_type', 'date', 'status')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Class for About Admin model
    """
    list_display = ('title', 'text', 'image')
    