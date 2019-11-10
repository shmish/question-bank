from django.db import models

class Course(models.Model):
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
    objective_code = models.CharField(max_length=8, unique=True)
    objective_description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.objective_code

class Question(models.Model):
    question_code = models.CharField(max_length=12)
    question_text = models.TextField()
    lobjective = models.ForeignKey(Lobjective, on_delete=models.CASCADE)
    answer = models.CharField(max_length=40)
    document = models.FileField(upload_to='documents/', blank=True)

class Document(models.Model):
    question_code = models.CharField(max_length=255, blank=True)
    question_text = models.TextField()
    lobjective = models.ForeignKey(Lobjective, on_delete=models.CASCADE)
    answer = models.CharField(max_length=40)
    document = models.FileField(upload_to='documents/', blank=True)

class Practice(models.Model):
    name = models.CharField(max_length=20)
    success = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
