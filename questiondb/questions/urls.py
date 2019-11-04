from django.urls import path

from . import views
from .views import QuestionDetailView, QuestionListView, LobjectiveListView

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('list/', views.QuestionListView.as_view(), name='question-list'),
    path('objectives/', views.LobjectiveListView.as_view(), name='lobjective-list'),
    path('add/', views.add_question, name='add-question'),
    path('loadd/', views.add_objective, name='add-objective'),
]
