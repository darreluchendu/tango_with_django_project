from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    contextDict = {
       'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"
    }
    return render(request, 'rango/index.html', context=contextDict)

def about(request):
    return render(request,"rango/about.html")