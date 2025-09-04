from django.contrib import admin
from . import models

@admin.register(models.Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('stuid', 'name_prefix', 'first_name', 'last_name', 'age')
    search_fields = ('first_name', 'last_name')
    fields = ('stuid', 'name_prefix', 'first_name', 'last_name', 'age')