from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

LESSONS = (('lessons_1', 'Piano'),
           ('lessons_2', 'Theory'))

LESSON_TYPE = (('lesson_type1', 'Online'),
               ('lesson_type2', 'Offline'))

BOOKING_STATUS = (('status1', 'Upcoming'),
                  ('status2', 'Completed'))

class BookingStatus(models.Model):
    """
    Class for booking status model
    """
    status = MultiSelectField(choices=BOOKING_STATUS, max_choices=1)

    class Meta:
        verbose_name = 'Booking status'
        verbose_name_plural = 'Booking statuses'

    def __str__(self):
        """
        Return status name
        """
        return self.get_status_display()


class Lesson(models.Model):
    """
    Class for lesson name model
    """
    lesson = MultiSelectField(choices=LESSONS, max_choices=1)

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        """
        Return lesson name
        """
        return self.get_lesson_display()


class LessonType(models.Model):
    """
    Return status name
    """
    lesson_type = MultiSelectField(choices=LESSON_TYPE, max_choices=1)

    class Meta:
        verbose_name = 'Lesson type'
        verbose_name_plural = 'Lesson types'

    def __str__(self):
        """
        Return lesson type
        """
        return self.get_lesson_type_display()


class Bookings(models.Model):
    """
    Class for Bookings model
    """
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(BookingStatus, on_delete=models.CASCADE)
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
    image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        """
        Return title
        """
        return self.title
