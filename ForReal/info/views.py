from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'info/info_home.html', {'news':news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'info/details_view.html'
    context_object_name = 'article'

def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_home')
        else:
            error = 'форма заполнена не верно'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'info/create.html', data)