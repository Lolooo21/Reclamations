from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Entreprise)
admin.site.register(Client)
admin.site.register(Reclamation)

