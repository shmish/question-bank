from django.urls import path

from . import views
from .views import QuestionDetailView, QuestionListView, LobjectiveListView

app_name="questions"
urlpatterns = [
    path('', views.index, name='index'),
    #path('detail/<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('question-detail/<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    #path('list/', views.QuestionListView.as_view(), name='question-list'),
    path('question-list/', views.QuestionListView.as_view(), name='question-list'),
    path('objectives/', views.LobjectiveListView.as_view(), name='lobjective-list'),
    # path('add/', views.add_question, name='add-question'),
    path('lo-add/', views.add_objective, name='add-objective'),
    path('question-add/', views.model_form_upload, name='model_form_upload'),
    path('question-choice/', views.select_course, name='select_course'),
]
