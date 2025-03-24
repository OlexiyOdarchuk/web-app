from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'title': 'Головна сторінка',
        'values': ['Some', 'Hello', '12345'],
        'obj':{
            'car': 'BMW',
            'age': '16',
            'hobby': 'dance'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')