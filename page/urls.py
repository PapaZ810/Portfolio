from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project'),
    ]
