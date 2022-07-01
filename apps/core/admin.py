from django.contrib import admin

from apps.core.models import Task, Authentication


@admin.register(Authentication)
class CustomerAdmin(admin.ModelAdmin):
    ...


@admin.register(Task)
class CustomerAdmin(admin.ModelAdmin):
    ...
