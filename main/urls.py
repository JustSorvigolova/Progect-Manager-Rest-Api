from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectsListView.as_view()),
    path('project/<int:pk>', views.ProjectsDetailtView.as_view())
]