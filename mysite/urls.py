from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.urls import path
from polls import views
from django.urls import path
from polls.views import robots_txt
from django.urls import re_path
from django.contrib import admin

from django.views.static import serve
from django.conf import settings
class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'indo_pak','services', 'projects', 'about', 'contact', 'login', 'signup','python']

    def location(self, item):
        return reverse(item)

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': {'static': StaticViewSitemap}}, name='django.contrib.sitemaps.views.sitemap'),
    
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    re_path(r'^robots\.txt$', serve, {'path': 'robots.txt', 'document_root': settings.STATIC_ROOT, 'content_type': 'text/plain'}),
    path('indo_pak/', views.indo_pak, name='indo_pak'),
    path('python/', views.python, name='python'),
    path('project/', views.project, name='project'),
    path('python_300_project/', views.python_300_project, name='python_300_project'),

]
