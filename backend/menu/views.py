from django.shortcuts import render
from . models import Page


def main_page(request):
    return render(request, 'base.html',{})

def get_pages(request):
    pages = Page.objects.all()
    return render(request, 'pages.html',{'pages': pages})

def get_page(request, slug):
    page = Page.objects.get(slug=slug)
    return render(request, 'page.html',{'page': page})


