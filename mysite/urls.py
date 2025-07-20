from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.urls import path
from polls import views
from django.urls import path
from django.urls import re_path
from django.contrib import admin

from django.views.static import serve
from django.conf import settings
    
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('indo_pak/', views.indo_pak, name='indo_pak'),
    path('python/', views.python, name='python'),
    path('project/', views.project, name='project'),
    path('python_300_project/', views.python_300_project, name='python_300_project'),
    path('python_learn/', views.python_learn, name='python_learn'),
    path('python_dsa/', views.python_dsa, name='python_dsa'),
    path('web/', views.web, name='web'),
]
