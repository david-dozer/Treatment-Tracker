import re
from django.utils.timezone import datetime
from django.http import HttpResponse

# views.py
from django.shortcuts import render, redirect
from .models import Client

def start_screen(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        # Create a new client object or fetch existing if needed
        # Redirect to the next step in treatment
        return redirect('next_step_url_name')
    return render(request, 'start_screen.html')
