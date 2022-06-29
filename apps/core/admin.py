from django.contrib import admin

from apps.core.models import Task   #Research, Customer, Order, Organization, Statement

# @admin.register(Research)
# class ResearchAdmin(admin.ModelAdmin):
#     ...

@admin.register(Task)
class CustomerAdmin(admin.ModelAdmin):
    ...
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     ...
#
# @admin.register(Organization)
# class OrganizationAdmin(admin.ModelAdmin):
#     ...
#
# @admin.register(Statement)
# class StatementAdmin(admin.ModelAdmin):
#     ...