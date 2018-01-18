from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'boldmessage': 'I leik Trains'
    }
    return render(request, 'rango/index.html', context)
