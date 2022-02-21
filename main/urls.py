from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('projects/', views.ProjectsListView.as_view()),
    path('project/<int:pk>', views.ProjectsDetailtView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)