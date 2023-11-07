from django.shortcuts import render
from django.http import HttpResponse
from .models import Record

def index(request):
    record = Record.objects.all()
    context = {
        'records': record,
        'title': 'records',
    }
    return render(request, 'daybook/index.html', context)


