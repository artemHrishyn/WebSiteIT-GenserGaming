import django.views
from django.shortcuts import render, redirect
from .models import Articls_News
from .forms import Articles_News_Form
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articls_News.objects.order_by('-date')
    return render(request, 'news/news_main.html', {'news': news})


class NewUpdateView(UpdateView):
    model = Articls_News
    template_name = 'News/create.html'
    form_class = Articles_News_Form

class NewDeleteView(DeleteView):
    model = Articls_News
    success_url = '/news/'
    template_name = 'News/news_delete.html'

class NewDatailView(DetailView):
    model = Articls_News
    template_name = 'News/details_view.html'
    context_object_name = 'article'


def create(request):
    error = ''

    if request.method == 'POST':
        form = Articles_News_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверна'

    form = Articles_News_Form

    date = {
        'form': form,
        'error': error
    }

    return render(request, 'News/create.html', date)
