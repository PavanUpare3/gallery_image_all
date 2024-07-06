from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('singlegallery/', views.singleGallery, name='gallery'),
    path('contact/', views.contact, name= 'contact'),
    path('services/', views.services, name= 'services'),
    path('about/', views.about, name='about'),
    path('gallery/', views.galler, name='gallery2'),
    path('gallerydemo/', views.galldemo, name='gallerydemo'),
    
]
