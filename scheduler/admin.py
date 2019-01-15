from django.contrib import admin
from .models import (Employer, Employee, Event)


# class SchedulerAdmin(admin.ModelAdmin):
#     readonly_fields = ('created_at', 'last_modified')


admin.site.register((Employer, Employee, Event))
