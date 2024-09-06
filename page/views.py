from django.views.generic import *
from .models import *


class HomeView(TemplateView):
    template_name = 'page/home.html'


class ProjectsView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'page/projects.html'


