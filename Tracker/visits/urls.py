from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('clinics/', views.clinics, name='clinics'),
    path('clinics/<int:clinic_id>/doctors', views.doctors, name='doctors'),
    path('doctors/<int:doctor_id>/visits', views.visits, name='visits'),
    path('new_visit/', views.new_visit, name='new_visit'),
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
