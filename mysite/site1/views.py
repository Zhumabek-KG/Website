from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [ {'title': "About site", 'url_name': 'about'},
    {'title': "Add a statement", 'url_name': 'add_page'},
    {'title': "Contacts", 'url_name': 'contact'},
    {'title': "Login", 'url_name': 'login'},
]
def index(request):
    posts = Boys.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': "Main site"
    }
    return render(request, 'site1/index.html', context=context)

def about(request):
    return render(request, 'site1/about.html', {'menu': menu, 'title': 'About'})


def addpage(request):
    return HttpResponse("Adding a statement")


def contact(request):
    return HttpResponse("Contacts")


def login(request):
    return HttpResponse("Login")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page was not found</h1>')


def show_post(request, post_id):
    return HttpResponse(f"Showing a statement from id = {post_id}")
