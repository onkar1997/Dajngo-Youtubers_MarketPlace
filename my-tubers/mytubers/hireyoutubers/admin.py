from django.contrib import admin
from django.utils.html import format_html
from .models import HireYoutuber


class HireYtAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'youtuber_name')
    list_display_links = ('id', 'first_name', 'last_name', 'email')
    list_filter = ('youtuber_name',)
    search_fields = ('youtuber_name',)


admin.site.register(HireYoutuber, HireYtAdmin)
