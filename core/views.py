from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm

class DashboardView(View):
    def get(self, request):
        return render(request, "core/dashboard.html")

class HomeView(TemplateView):
    template_name = 'home.html'

def my_custom_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("You're logged in.")
            else:
                return HttpResponse("Your username and password didn't match.")
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {'form': form})