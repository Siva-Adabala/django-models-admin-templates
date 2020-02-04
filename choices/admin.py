from django.contrib import admin
from .models import Runner, Fruit

@admin.register(Runner)
class RunnerAdmin(admin.ModelAdmin):
    list_display = ['id','name','medal']

# @admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ('name','year_in_school')
    
admin.site.register(Fruit)