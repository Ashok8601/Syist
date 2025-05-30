from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: https://syist-group.onrender.com/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
def indo_pak(request):
    return render(request,'indo_pak.html')
def python(request):
    return render(request,'Python_code.html')    

def project(request):
    return render(request,'project.html')

def python_300_project(request):
    return render(request,'python_300_project.html')
def python_learn(request):
    return render(request,'python_learn.html')
def python_dsa(request):
    return render(request,'python_dsa.html')
def web(request):
    return render(request,'web.html')


