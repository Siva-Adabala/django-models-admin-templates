from django.contrib import admin
from .models import Musician, Album

# Register your models here.
@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'instrument')
    list_editable =('instrument',)
    list_per_page = 2
    list_filter = ('first_name','instrument')
    search_fields = ['first_name','last_name','instrument']
 

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display =('artist', 'name','release_date','num_stars','is_avilable')
    # list_select_related = ('artist','name')
    radio_fields = {"artist":admin.HORIZONTAL}
    ordering = ("num_stars",)
    autocomplete_fields = ["artist"]
    list_per_page = 3

 
# admin.site.register(Album)