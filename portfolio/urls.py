"""URL patterns for the portfolio app."""
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
]
