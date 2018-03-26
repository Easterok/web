from django.contrib import admin
from .models import Board


@admin.register(Board)
class PersonAdmin(admin.ModelAdmin):
    pass
