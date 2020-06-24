from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'title' : "Oscars delayed",
        'author': "aadi",
        'text'  : "Oscars have been delayed"
    },
    {
        'title' : "tenet huly 31st",
        'author': "aadi",
        'text'  : "Nolan's new film"
    }
]

contexts = {
    'posts' : posts
}
def home(request):
   
    return render(request, 'blog/home.html', contexts)

def about(request):
    return render(request, 'blog/about.html')