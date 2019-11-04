from django.db import models
from django.forms import ModelForm

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

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_code', 'question_text', 'lobjective', 'answer']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['lobjective'].label = "Learning Objective"

class LobjectiveForm(ModelForm):
    class Meta:
        model = Lobjective
        fields = ['course', 'objective_code', 'objective_description']