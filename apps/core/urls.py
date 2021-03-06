from django.urls import path
from django.contrib import admin
from django.urls import path, include
from apps.core import views as core_views


urlpatterns = [
    path('admin', core_views.admin , name='admin'),
    path('', core_views.index, name='index'),
    path('receptionFL', core_views.receptionFL, name='receptionFL'),
    path('receptionUL', core_views.receptionUL, name='receptionUL'),
    path('applicant', core_views.applicant, name='applicant'),
    path('cards', core_views.cards, name='cards'),
    path('task_status', core_views.task_status, name='task_status'),
    path('executor', core_views.executor, name='executor'),
    path('report', core_views.report, name='report'),
    path('waiting', core_views.waiting, name='waiting'),
    path('connection', core_views.connection, name='connection'),
    path('addTasks', core_views.addTask, name='addTasks'),
    path('addOperator', core_views.addOperator, name='addOperator')
]