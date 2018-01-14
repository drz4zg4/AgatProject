from django.shortcuts import render



def index(request):
    return render(request, 'agat/index.html', {})