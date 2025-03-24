from django.shortcuts import render
from .models import Articles

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/index.html', {'news': news})