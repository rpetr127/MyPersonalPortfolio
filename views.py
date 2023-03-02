from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


@method_decorator(staff_member_required, name='dispatch')
class AdminLoginView(LoginView):
    template_name = 'admin/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('admin:index')