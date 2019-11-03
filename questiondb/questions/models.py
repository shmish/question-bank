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
    objectvie_code = models.CharField(max_length=8)
    objective_description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Question(models.Model):
    question_code = models.CharField(max_length=12)
    question_text = models.TextField()
    objectives = models.ManyToManyField(Lobjective)
    answer = models.TextField()

# class Quiz(models.Model):
#     questions = models.ManyToManyField(Question)
#     user_name = models.CharField(max_length=20)
#     attempt_time = models.DateTimeField(auto_now_add=True)
