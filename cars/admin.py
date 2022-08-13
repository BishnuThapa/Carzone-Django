from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Image'
    list_display = ('thumbnail', 'car_title',
                    'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('car_title',)
    search_fields = ('car_title', 'city', 'model',
                     'body_style', 'fuel_type', 'color', 'year')
    list_filter = ('body_style', 'fuel_type', 'color', 'city',)
    list_editable = ('is_featured',)


admin.site.register(Car, CarAdmin)
