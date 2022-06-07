from django.http import HttpRequest, JsonResponse
from django.shortcuts import render


# def main(request: HttpRequest) -> JsonResponse:
#     return JsonResponse(data={
#         "error": False,
#         "status": "Hello from Ramil Django",
#         "details": None
#     }, status=200)


def admin(request):
    return render(request, 'admin')


def index(request):
    return render(request, 'core/index.html')


def reception(request):
    return render(request, 'core/reception.html')


def applicant(request):
    return render(request, 'core/applicant.html')


def cards(request):
    return render(request, 'core/cards.html')


def task_status(request):
    return render(request, 'core/task_status.html')


def executor(request):
    return render(request, 'core/executor.html')


def report(request):
    return render(request, 'core/report.html')


def waiting(request):
    return render(request, 'core/waiting.html')


def connection(request):
    return render(request, 'core/connection.html')

