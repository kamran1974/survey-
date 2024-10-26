from django.contrib import admin
from .models import Client, Opinion


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenumber', 'createddate')


class OpinionAdmin(admin.ModelAdmin):
    list_display = ('client', 'question1', 'question2', 'idea', 'submitted_date')

admin.site.register(Opinion, OpinionAdmin)