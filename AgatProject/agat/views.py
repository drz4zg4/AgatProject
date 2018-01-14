from django.shortcuts import render
from django.utils import timezone
from .models import FlatPanelDispla

def index(request):
    posts = FlatPanelDispla.objects.filter(data_testu__lte=timezone.now()).order_by('published_date')
    return render(request, 'agat/index.html', {'posts': posts})