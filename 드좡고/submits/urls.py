from django.urls import path
from . import views

app_name='submits'

urlpatterns = [
    path('id/',views.id),
    path('password/',views.password)
]
