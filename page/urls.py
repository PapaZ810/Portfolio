from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectView.as_view(), name='project'),
    path('keyboards/', KeyboardsView.as_view(), name='keyboards'),
    path('keyboards/<int:pk>/', KeyboardView.as_view(), name='keyboard'),
    ]

