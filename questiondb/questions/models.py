"""models.py for the practice questions app."""
from django.db import models

class Course(models.Model):
    """Model for the base courses"""
    COURSE_CHOICES = [
        ('ph11', 'Physics 11'),
        ('ph12', 'Physics 12'),
    ]
    course_name = models.CharField(
        max_length=20,
        choices=COURSE_CHOICES,
    )

    def __str__(self):
        return self.get_course_name_display()

class Lobjective(models.Model):
    """Model for the learning objectives.  Each LO belongs to only one course"""
    objective_code = models.CharField(max_length=8, unique=True)
    objective_description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.objective_code

class Question(models.Model):
    """Model for the questions. Each question formally belongs to only one LO."""
    question_code = models.CharField(max_length=12)
    question_text = models.TextField()
    lobjective = models.ForeignKey(Lobjective, on_delete=models.CASCADE)
    answer = models.CharField(max_length=40)
    document = models.FileField(upload_to='documents/', blank=True)

class Document(models.Model):
    """Defunct model, no longer used. Used for testing upload of images."""
    question_code = models.CharField(max_length=255, blank=True)
    question_text = models.TextField()
    lobjective = models.ForeignKey(Lobjective, on_delete=models.CASCADE)
    answer = models.CharField(max_length=40)
    document = models.FileField(upload_to='documents/', blank=True)

class Quiz(models.Model):
    """quiz which will have three questions."""
    name = models.CharField(max_length=12)
    questions = models.ManyToManyField(Question)