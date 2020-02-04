from django.contrib import admin
from django.urls import path

from myapp.views import homepage_view, contact_view,about_view, social_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage_view, name='homepage'),
    path('contact',contact_view),
    path('about',about_view),
    path('social', social_view)
   
]
