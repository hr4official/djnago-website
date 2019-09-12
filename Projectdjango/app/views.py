from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#def index(request):
#   return HttpResponse("hello")

def index_view(request, *args, **kwargs):
  	#return HttpResponse('<h1>Hey!This is Home Page.</h1>')
 	return render(request,"index.html",{})