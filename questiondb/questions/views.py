from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import DetailView, ListView

from .models import Question, Lobjective, Document, Course
from .forms import QuestionForm, LobjectiveForm

def index(request):
    return render(request, 'questions/index.html')

class QuestionListView(ListView):
    """Automatically uses question_list for context variable
    and uses <app name>/question_list.html for the template"""
    model = Question

    def get_queryset(self):
        """Return the latest questions created"""
        return Question.objects.order_by('lobjective', 'question_code')

# class DocumentListView(ListView):
#     """Automatically uses question_list for context variable
#     and uses <app name>/question_list.html for the template"""
#     model = Document

#     def get_queryset(self):
#         """Return the latest questions created"""
#         return Document.objects.order_by('lobjective', 'question_code')

class QuestionDetailView(DetailView):
    """Auto template question_detail.html"""
    model = Question

# class DocumentDetailView(DetailView):
#     """Auto template question_detail.html"""
#     model = Document

class LobjectiveListView(ListView):
    model = Lobjective

    def get_queryset(self):
        """Return the latest questions created"""
        return Lobjective.objects.order_by('objective_code')

# def add_question(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question_item = form.save(commit=False)
#             question_item.save()
#             return HttpResponseRedirect('/questions/list')
#     else:
#         form = QuestionForm()
#     return render(request, 'questions/question_form.html', {'form': form})

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

def model_form_upload(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question_item = form.save(commit=False)
            question_item.save()
            return redirect('index')
    else:
        form = QuestionForm()
    return render(request, 'questions/model_form_upload.html', {
        'form': form
    })

def select_course(request):
    courses = Course.objects.all().order_by('course_name')
    course_choice = request.GET.get('course_choice')
    objectives = Lobjective.objects.all().filter(course__course_name=course_choice)
    context = {'courses': courses}
    context['objectives'] = objectives
    return render(request, 'questions/coursechoice.html', context)
