from django.contrib import admin
from .models import Account, Post, Bulim, Doktor

# Register your models here.
admin.site.register([Account, Post, Bulim, Doktor])