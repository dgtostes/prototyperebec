from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    urls = {'ensaios': 'rebequeinho/ensaios/index.html', 'revisao': 'teste'}
    #return HttpResponse("Hello, world. You're at the poll index.")
    return render(request, 'rebequinho/index.html', urls)