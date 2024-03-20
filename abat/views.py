import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from abat.forms import ClientForm

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

def start_screen(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # Concatenate first name and last name
            client_name = f"{first_name} {last_name}"
            # Redirect to hello_there view with the client's name
            return redirect('hello_there', name=client_name)
    else:
        form = ClientForm()
    return render(request, 'abat/start_screen.html', {'form': form})