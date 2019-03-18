from django.contrib import admin
from .models import Location, Image, categories

# Register your models here.
# class ImageAdmin(admin.ModelAdmin):
#     filter_horizontal = ('categories',)

admin.site.register(Location)
admin.site.register(Image)
admin.site.register(categories)