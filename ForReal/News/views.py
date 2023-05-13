from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    data = {
        'title':'Главная страница',
        'values':['Some','Hello','123']
    }
    return render(request, 'News/index.html', data)

def about(request):
    return render(request, 'News/about.html')

def contact(request):
    return render(request, 'News/contact.html')