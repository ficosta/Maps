from django.contrib import admin

# Register your models here.
from .models import Status, Occurrence

admin.site.register(Status)
admin.site.register(Occurrence)