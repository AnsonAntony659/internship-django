from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
     path('contact/',views.contact,name='contact'),
]
