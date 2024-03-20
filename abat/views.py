import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Start Screen")

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'abat/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )