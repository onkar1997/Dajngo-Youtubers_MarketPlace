from django.contrib import admin
from django.utils.html import format_html
from .models import Youtuber

class YtAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'name', 'myphoto', 'subscriber_count', 'is_featured')
    list_display_links = ('id', 'name', 'myphoto')
    list_filter = ('city', 'camera_type')
    list_editable = ('is_featured',)
    search_fields = ('name', 'camera')


# Register your models here.
admin.site.register(Youtuber, YtAdmin)
