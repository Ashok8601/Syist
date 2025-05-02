from django.urls import path
from polls  import views

from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),

]