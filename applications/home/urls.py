from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.PruebaCreateView.as_view(), name ='prueba_add'),
    path('prueba/', views.pruebaTemplateView.as_view(), name ='prueba'),
    path('resume-foundation/', views.ResumeFoundationView.as_view(), name ='resume_foundation'),
]