from django.urls import path
from . import views

app_name = 'alchemy'

urlpatterns = [
    path('clap/',views.clap,name='clap'),
    path('throw/',views.throw,name='throw'),
    path('catch/',views.catch,name='catch'),
    ]
    
