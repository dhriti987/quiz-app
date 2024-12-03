from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),
    path('question/', views.question_view, name='question'),
    path('register/', views.register_view, name='register'),
]
