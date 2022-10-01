from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

LESSONS = (('lessons_1', 'Piano'),
           ('lessons_2', 'Theory'))

LESSON_TYPE = (('lesson_type1', 'Online'),
               ('lesson_type2', 'Offline'))

class Lesson(models.Model):
    """
    Class for lessons model.
    """
    lesson = MultiSelectField(choices=LESSONS, max_choices=1)
    lesson_type = MultiSelectField(choices=LESSON_TYPE, max_choices=1)
    date = models.DateField()
    time = models.TimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lessons")

    class Meta:
        ordering = ['-date']
        unique_together = ("date", "time")

    def __str__(self):
        return self.get_lesson_display()
