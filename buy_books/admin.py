from django.contrib import admin
from .models import Author,Publisher,Book,Store
from django.contrib.admin import DateFieldListFilter, RelatedOnlyFieldListFilter
from django.utils.translation import ugettext_lazy

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name','age']
    list_display = ['name','age']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','pages','price','pubdate','rating')
    list_editable = ['price']
    list_per_page = 5
    list_filter = ["name",("price"), ("pubdate",DateFieldListFilter),"rating",('authors', admin.RelatedOnlyFieldListFilter)]
    search_fields = ('name', )


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name',)


# admin.site.register(Publisher)
# admin.site.register(Book)
# admin.site.register(Store)
