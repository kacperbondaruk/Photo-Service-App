from django.urls import path
from .views import DashboardView, HomeView, my_custom_login_view

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path('login/', my_custom_login_view, name='login'),
    path('', HomeView.as_view(), name='home'),
]