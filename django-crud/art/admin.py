from django.contrib import admin
from art.models import Art


class ArtAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']


admin.site.register(Art, ArtAdmin)
