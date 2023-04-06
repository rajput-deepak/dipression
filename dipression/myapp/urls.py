from django.urls import path
from . views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('test', test, name='test'),
    path('decision1', decision1, name='decision1'),
    path('decision2', decision2, name='decision2'),
    path('decision3', decision3, name='decision3'),
    path('decision4', decision4, name='decision4'),
    
]
