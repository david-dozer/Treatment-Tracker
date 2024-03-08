# admin.py
from django.contrib import admin
from .models import Client, Response, Session

admin.site.register(Client)
admin.site.register(Response)
admin.site.register(Session)
