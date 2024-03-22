import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from abat.forms import ClientForm
from abat.models import Client, Response, Session

def home(request):
    return HttpResponse("Start Screen")

def hello_there(request, name='Guest'):
    clients = Client.objects.all()  # Get all clients from the database
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'abat/hello_there.html',
        {
            'name': name,
            'date': datetime.now(),
            'clients': clients  # Pass clients data to the template
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
            client = Client.objects.create(first_name=first_name, last_name=last_name)
            # Redirect to hello_there view with the client's name
            return redirect('hello_there', name=client_name)
    else:
        form = ClientForm()
    return render(request, 'abat/start_screen.html', {'form': form})

def start_treatment(request):
    return render(request, 'abat/session_interface.html')



# def clients_list(request):
#     clients = Client.objects.all()
#     return render(
#         request,
#         'abat/clients_list.html',
#         {
#             'clients': clients,
#         }
#     )