from django.contrib import admin
from django.utils.html import format_html
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'company_name')
    list_display_links = ('id', 'full_name')

admin.site.register(Contact, ContactAdmin)