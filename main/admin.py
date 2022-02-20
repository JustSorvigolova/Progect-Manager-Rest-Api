from django.contrib import admin

from .models import Projects, Workers, Administrator, Supervisor, Tasks


admin.site.register(Projects)
admin.site.register(Workers)
admin.site.register(Administrator)
admin.site.register(Supervisor)
admin.site.register(Tasks)
