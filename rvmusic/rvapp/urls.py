
from django.urls import path
from rvapp.views import home,about,service

urlpatterns = [
    path('',home,name='home'),
    path('about',about,name='about'),
    path('service',service,name='service')
]