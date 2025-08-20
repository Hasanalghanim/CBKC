from django.contrib import admin
from .models import TryoutEvent,TryoutRegistrant

admin.site.register(TryoutEvent)
admin.site.register(TryoutRegistrant)