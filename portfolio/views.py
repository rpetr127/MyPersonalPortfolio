from django.shortcuts import render
from .models import Project
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
