from django.contrib import admin
from .models import Person
from django.contrib.auth.models import User,Group
from django.contrib.admin import DateFieldListFilter



@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')
    fields = ('first_name', 'last_name')
    search_fields = ('first_name','last_name')
    list_filter = (('first_name',admin.DateFieldListFilter),)


admin.site.unregister(User)
admin.site.unregister(Group)