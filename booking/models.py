from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime


class BookingStatus(models.Model):
    """
    Class for booking status model
    """
    status = models.CharField(max_length=20)
    past = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name = 'Booking status'
        verbose_name_plural = 'Booking statuses'

    def __str__(self):
        """
        Return status name
        """
        return self.status


class Lesson(models.Model):
    """
    Class for lesson name model
    """
    lesson = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        """
        Return lesson name
        """
        return self.lesson


class LessonType(models.Model):
    """
    Return status name
    """
    lesson_type = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Lesson type'
        verbose_name_plural = 'Lesson types'

    def __str__(self):
        """
        Return lesson type
        """
        return self.lesson_type


class Bookings(models.Model):
    """
    Class for Bookings model
    """
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(BookingStatus, on_delete=models.CASCADE, related_name='status1')
    past = models.ForeignKey(BookingStatus, default=False, on_delete=models.CASCADE, related_name='past1')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
        unique_together = ("date", "time")
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'


class About(models.Model):
    """
    Class for about model
    """
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    image = CloudinaryField('image', default='placeholder', blank=True)
    created = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'
        ordering = ('created',)

    def __str__(self):
        """
        Return title
        """
        return self.title
