from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"sample.html",context={'name':'vinod'})

def front(request,name):
    return HttpResponse(f'<h1> my name is {name}</h1>')