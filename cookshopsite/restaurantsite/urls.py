from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name='home'),
path('contact.html', views.contact, name="contact"),
path('menu.html', views.menu, name='menu'),
path('about.html', views.about, name='about'),
path('service.html', views.service, name='service'),
]