from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts = [
    {
        'author': 'jack',
        'title': 'post 1',
        'content': 'First post content',
        'date_posted': '06/03/2020'
    },
{
        'author': 'jack',
        'title': 'post 2',
        'content': 'Second post content',
        'date_posted': '07/03/2020'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html')