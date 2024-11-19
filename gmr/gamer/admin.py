from django.contrib import admin
from .models import Gamerinfo

# Register your models here.

@admin.register(Gamerinfo)
class GamerAdmin(admin.ModelAdmin):
    list_display = ['id' , 'username' , 'state' , 'region']