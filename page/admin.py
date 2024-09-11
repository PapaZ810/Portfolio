from django.contrib import admin
from .models import *


admin.site.site_header = 'Portfolio Admin Panel'
admin.site.site_title = 'Portfolio Admin Panel'

admin.site.register(Project)
admin.site.register(Home)
