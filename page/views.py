from .models import *
from .forms import EmailForm
from django.core import mail
from django.views.generic import *
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


context = {
    'projects': Project.objects.only('id', 'title'),
    'keyboards': Keyboard.objects.only('id', 'title')
}


class HomeView(FormView):
    form_class = EmailForm
    template_name = 'page/home.html'
    context.update({'home': Home.objects.first()})
    context.update({'skills': Skill.objects.all()})
    extra_context = context
    context_object_name = 'home'
    success_url = '/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email = form.cleaned_data['email']
        if subject and message and email:
            try:
                send_mail(
                    subject,
                    message,
                    email,
                    ['work@zoed.dev'],
                    fail_silently=False,
                    connection=mail.get_connection(),
                )
                return super().form_valid(form)
            except BadHeaderError:
                form.add_error(None, 'Invalid header found.')
                return self.form_invalid(form)
        else:
            form.add_error(None, 'Invalid input')
            return self.form_invalid(form)


class ProjectsView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'page/projects.html'


class ProjectView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'page/project.html'
    extra_context = context

class KeyboardsView(ListView):
    model = Keyboard
    context_object_name = 'keyboards'
    template_name = 'page/keyboards.html'

class KeyboardView(DetailView):
    model = Keyboard
    context_object_name = 'keyboard'
    template_name = 'page/keyboard.html'
    extra_context = context