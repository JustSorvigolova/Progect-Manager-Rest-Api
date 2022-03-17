from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('projects/', views.ProjectListCreate.as_view()),
    path('projects/<int:pk>/', views.ProjectUpdateRetrieveDelete.as_view()),
    path('comment/', views.CommentListCreate.as_view()),
    path('task/', views.TasksListCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
