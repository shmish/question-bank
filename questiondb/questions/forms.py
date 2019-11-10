from django.forms import ModelForm
from .models import Document, Question, Lobjective

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['lobjective', 'question_code', 'question_text', 'document', 'answer']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['lobjective'].label = "Learning Objective"

class LobjectiveForm(ModelForm):
    class Meta:
        model = Lobjective
        fields = ['course', 'objective_code', 'objective_description']

# class DocumentForm(ModelForm):
#     class Meta:
#         model = Document
#         fields = ('lobjective', 'question_code', 'question_text', 'document', 'answer')