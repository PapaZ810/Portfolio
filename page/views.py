from django.views.generic import *
from .models import *


context = {
    'projects': Project.objects.only('id', 'title')
}


class HomeView(TemplateView):
    template_name = 'page/home.html'
    extra_context = context


class ProjectsView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'page/projects.html'


class ProjectView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'page/project.html'
    extra_context = context

