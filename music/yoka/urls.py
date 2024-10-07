from django.urls import path
from .views import *

urlpatterns = [
    path('',home ,name='home'),
    path('home',home ,name='home'),
    path('albums',albums ,name='albums'),
    path('events',events ,name='events'),
    path('blog',blog ,name='blog'),
    path('contact',contact ,name='contact'),
    path('elements',elements ,name='elements'),
    path('login',login ,name='login'),
    path('register',register ,name='register'),        
    path('music',music ,name='music'),  
    path('formulaire',formulaire ,name='formulaire'),
]
