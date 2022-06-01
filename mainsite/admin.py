from django.contrib import admin
from .models import Teachers, Contact, Register

# Register your models here.
admin.site.register(Register)
admin.site.register(Teachers)
admin.site.register(Contact)
