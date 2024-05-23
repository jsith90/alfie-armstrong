from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')


def gallery(request):
    return render(request, 'portfolio/gallery.html')