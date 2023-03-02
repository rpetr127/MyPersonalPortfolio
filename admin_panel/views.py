from django.contrib.auth.views import LoginView    

class AdminLogin(LoginView):
    template_name = 'LoginView_form.html'