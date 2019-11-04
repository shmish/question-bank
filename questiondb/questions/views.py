from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView

from .models import Question, Lobjective, QuestionForm, LobjectiveForm


def index(request):
    return render(request, 'questions/index.html')

class QuestionListView(ListView):
    """Automatically uses question_list for context variable
    and uses <app name>/question_list.html for the template"""
    model = Question

    def get_queryset(self):
        """Return the latest questions created"""
        return Question.objects.order_by('question_code')

class QuestionDetailView(DetailView):
    """Auto template question_detail.html"""
    model = Question

class LobjectiveListView(ListView):
    model = Lobjective

    def get_queryset(self):
        """Return the latest questions created"""
        return Lobjective.objects.order_by('objective_code')

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_item = form.save(commit=False)
            question_item.save()
            return HttpResponseRedirect('/questions/list')
    else:
        form = QuestionForm()
    return render(request, 'questions/question_form.html', {'form': form})

def add_objective(request):
    if request.method == 'POST':
        form = LobjectiveForm(request.POST)
        if form.is_valid():
            objective_item = form.save(commit=False)
            objective_item.save()
            return HttpResponseRedirect('/questions/objectives')
    else:
        form = LobjectiveForm()
    return render(request, 'questions/lobjective_form.html', {'form': form})


