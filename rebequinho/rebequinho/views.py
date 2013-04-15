from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    urls = {'ensaios': 'ensaios/', 
            'revisao': 'revisao/'}
    #return HttpResponse("Hello, world. You're at the poll index.")
    return render(request, 'rebequinho/index.html', urls)