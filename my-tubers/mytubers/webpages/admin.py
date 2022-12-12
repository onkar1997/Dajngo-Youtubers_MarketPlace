from django.contrib import admin
from django.utils.html import format_html
from .models import Slider, Team


class SliderAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'myphoto', 'headline', 'button_text')
    list_display_links = ('id', 'myphoto', 'headline')
    search_fields = ('headline',)


class TeamAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date')
    list_display_links = ('id', 'myphoto', 'first_name')
    list_filter = ('role',)
    search_fields = ('first_name', 'role')


admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
