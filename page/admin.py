from django.contrib import admin
from .models import *


admin.site.site_header = 'Portfolio Admin Panel'
admin.site.site_title = 'Portfolio Admin Panel'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description']
    search_fields = ['title', 'short_description']
    list_filter = ['title', 'short_description']
    ordering = ['title', 'short_description']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Home)
admin.site.register(Skill)
admin.site.register(Keyboard)
