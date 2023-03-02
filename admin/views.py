from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def admin_view(request):
    return render(request, 'admin/base_site.html')