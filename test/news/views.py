from django.shortcuts import render

def news_home(request):
    return render(request, 'news/index.html')
# Create your views here.
