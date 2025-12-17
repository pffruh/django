from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def news(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})

class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/article_detail.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create_news.html'
    form_class = ArticleForm
    success_url = '/news/'
    # fields = ['title', 'anons', 'full_text', 'date']

class NewsDeleteView(DeleteView):
    model = Article
    template_name = 'news/article_delete.html'
    success_url = '/news/'


def create_news(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверной'
        
    form = ArticleForm()

    data = {
        'form': form,
        'error': error 
        }
    return render(request, 'news/create_news.html', data)